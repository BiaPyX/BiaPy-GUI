import os
import traceback
import docker
import yaml
import numpy as np
from datetime import datetime, timedelta

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt, QObject, QUrl
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import *

from ui_utils import get_text, resource_path, path_in_list, path_to_linux
from ui.ui_run import Ui_RunBiaPy 
from ui.aux_windows import yes_no_Ui

class runBiaPy_Ui(QDialog):
    def __init__(self, parent_worker):
        super(runBiaPy_Ui, self).__init__()
        self.run_window = Ui_RunBiaPy()
        self.parent_worker = parent_worker
        self.run_window.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.run_window.bn_min.clicked.connect(self.showMinimized)
        self.run_window.bn_close.clicked.connect(self.close)
        self.run_window.bn_close.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","close_icon.png"))))
        self.run_window.bn_min.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","hide_icon.png"))))
        self.run_window.icon_label.setPixmap(QPixmap(resource_path(os.path.join("images","bn_images","info.png"))))
        self.run_window.return_icon_label.setPixmap(QPixmap(resource_path(os.path.join("images","bn_images","return_icon.png"))))
        self.run_window.window_des_label.setText("  Running information")
        self.run_window.stop_container_bn.clicked.connect(lambda: self.parent_worker.stop_worker())
        self.run_window.container_state_label.setText("BiaPy state [ Initializing ]")
        self.run_window.train_progress_bar.setValue(0)
        self.run_window.test_progress_bar.setValue(0)
        self.setStyleSheet("#centralwidget{ border: 1px solid black;} QWidget{ font-size:16px;}")
        self.dragPos = self.pos()  
        def movedialogWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
        self.run_window.frame_top.mouseMoveEvent = movedialogWindow  
        self.yes_no = yes_no_Ui()
        self.forcing_close = False
        self.progress_pulling_time = True

    def center_window(self, widget, geometry):
        window = widget.window()
        window.setGeometry(
            QtWidgets.QStyle.alignedRect(
                QtCore.Qt.LeftToRight,
                QtCore.Qt.AlignCenter,
                window.size(),
                geometry,
            ),
        )

    def closeEvent(self, event):
        if self.forcing_close:
            self.kill_all_processes()
        else:
            if "run" in self.parent_worker.process_steps:
                m = "Are you sure that you want to exit? Running container will be stopped"
            elif "pull" in self.parent_worker.process_steps:
                m = "Are you sure that you want to exit? Container's pulling process will be stopped"
            else:
                m = "Are you sure that you want to exit?"
            self.yes_no.create_question(m)
            self.center_window(self.yes_no, self.geometry())
            self.yes_no.exec_()
            if self.yes_no.answer:
                self.kill_all_processes()
            else:
                event.ignore()

    def kill_all_processes(self):
        self.parent_worker.stop_worker()
        try:
            self.parent_worker.finished_signal.emit()
        except Exception as e:
            print(f"Possible expected error during BiaPy's running thread deletion: {e}")
        self.close()
        
    def init_log(self, container_info):
        self.run_window.biapy_container_info_label.setText(container_info)
        self.run_window.run_biapy_log.setText(' ')

    def update_gui(self, signal):
        # Initialize the GUI
        if signal == 0:
            self.parent_worker.init_gui()
        elif signal == 1:
            self.update_log()
        else:
            print("Nothing")
            
    def update_log(self):
        finished_good = False
        with open(self.parent_worker.container_stdout_file, 'r') as f:
            last_lines = f.readlines()[-20:]
            last_lines = ''.join(last_lines).replace("\x08", "").replace("[A", "").replace("", "")           
            self.run_window.run_biapy_log.setText(str(last_lines))
            if "FINISHED JOB" in last_lines:
                finished_good = True 
        
        if finished_good:
            self.update_cont_state(0)
        else:
            self.update_cont_state(1)

    def update_cont_state(self, svalue):
        st = "unknown"
        if svalue == 1:
            if self.parent_worker.biapy_container is not None:
                self.parent_worker.biapy_container.reload()
                st = self.parent_worker.biapy_container.status
                if st == "running":
                    st = "<span style=\"color:green;\">R"+st[1:]+"</span>"
                elif st == "exited":
                    st = "<span style=\"color:red;\">E"+st[1:]+"</span>"
                    self.run_window.stop_container_bn.setEnabled(False)
                elif st == "created":
                    st = "<span style=\"color:orange;\">C"+st[1:]+"</span>"
        # When the signal is 0 the container has finished good
        else:
            st = "finished"
        self.run_window.container_state_label.setText("Container state [ {} ]".format(st))

    def update_train_progress(self, value):
        self.run_window.train_progress_bar.setValue(value)
        self.run_window.train_epochs_label.setText("<html><head/><body><p align=\"center\"><span \
            style=\"font-size:12pt;\">Epochs</span></p><p align=\"center\"><span \
            style=\"font-size:12pt;\">"+"{}/{}".format(self.parent_worker.epoch_count, \
            self.parent_worker.total_epochs)+"</span></p></body></html>")

    def update_test_progress(self, value):
        self.run_window.test_progress_bar.setValue(value)
        self.run_window.test_files_label.setText("<html><head/><body><p align=\"center\"><span \
            style=\"font-size:12pt;\">Files</span></p><p align=\"center\"><span \
            style=\"font-size:12pt;\">"+"{}/{}".format(self.parent_worker.test_image_count, \
            self.parent_worker.test_files)+"</span></p></body></html>") 
        
    def update_pulling_progress(self, value):
        if self.progress_pulling_time:
            self.run_window.biapy_image_pulling_progress_bar.setMaximum(len(self.parent_worker.total_layers)*10)
        self.run_window.biapy_image_pulling_progress_bar.setValue(value)

    def pulling_progress(self, value):
        if value == 0: # Start of the pulling process 
            self.run_window.biapy_image_status.setText("BiaPy image [ <span style=\"color:orange;\"> Pulling </span> ]")
            self.run_window.pulling_label.setText("Downloading BiaPy image (only done once) - Total size: {}"
                .format(self.parent_worker.main_gui.cfg.settings['biapy_container_size']))
            self.run_window.container_pulling_frame.setVisible(True)
            self.run_window.biapy_container_info_label.setText("Wait for the image to download completely.")
        else:
            self.run_window.container_pulling_frame.setVisible(False)
            self.run_window.biapy_image_status.setText("BiaPy image [ <span style=\"color:green;\">Downloaded</span> ]")
            self.run_window.biapy_container_info_label.setText("INITIALIZING . . . (this may take a while)")

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

class run_worker(QObject):
    # Signal to indicate the main thread that the worker has finished 
    finished_signal = QtCore.Signal()

    # Signal to indicate the main thread to update the log frame (1) or init the GUI (0, this last is done just one time)
    update_log_signal = QtCore.Signal(int)

    # Signal to indicate the main thread to update the GUI with a finish message according to the container state. If
    # the log file contains a last message of BiaPy such as "FINISHED JOB" the execution finished without errors and 
    # the state will be "finished" (0). Otherwise, a 1 is sent and "running", "created" or "exited" will be displayed.
    update_cont_state_signal = QtCore.Signal(int)

    # Signal to indicate the main thread to update the GUI with the new progress of the training phase
    update_train_progress_signal = QtCore.Signal(int)

    # Signal to indicate the main thread to update the GUI with the new progress of the test phase
    update_test_progress_signal = QtCore.Signal(int)

    # Signal to indicate the main thread to update the GUI to advice user in the pulling process steps
    update_pulling_signal = QtCore.Signal(int)

    # Signal to indicate the main thread to update the GUI with the pulling progress
    update_pulling_progress_signal = QtCore.Signal(int)

    def __init__(self, main_gui, config, container_name, worker_id, output_folder, user_host, use_gpu):
        super(run_worker, self).__init__()
        self.main_gui = main_gui
        self.config = config
        self.container_name = container_name
        self.worker_id = worker_id
        self.output_folder_in_host = output_folder
        self.windows_os = True if "win" in self.main_gui.cfg.settings['os_host'].lower() else False
        self.user_host = user_host
        self.use_gpu = use_gpu
        self.gui = runBiaPy_Ui(self)
        self.gui.open()
        self.docker_client = docker.from_env()
        self.biapy_container = None
        self.container_info = 'NONE'
        self.process_steps = "NONE"
        self.break_pulling = False

    def stop_worker(self):
        print("Stopping the container . . . ")
        if self.biapy_container is not None:
            self.biapy_container.stop(timeout=1)
            try:
                self.update_cont_state_signal.emit(1)
            except Exception as e:
                print(f"Possible expected error during BiaPy's running thread deletion: {e}")
            self.gui.run_window.stop_container_bn.setEnabled(False)
            self.gui.run_window.test_progress_label.setEnabled(False)
            self.gui.run_window.test_progress_bar.setEnabled(False)
            self.gui.run_window.test_files_label.setEnabled(False)
            self.gui.run_window.train_progress_label.setEnabled(False)
            self.gui.run_window.train_progress_bar.setEnabled(False)
            self.gui.run_window.train_epochs_label.setEnabled(False)
        else:
            print("Container not running yet")      
            # To kill pulling process if it is running 
            self.break_pulling = True
            
    def init_gui(self):
        self.gui.init_log(self.container_info)
        if self.config['TRAIN']['ENABLE']:
            self.gui.run_window.train_epochs_label.setText("<html><head/><body><p align=\"center\"><span \
                style=\"font-size:12pt;\">Epochs</span></p><p align=\"center\"><span \
                style=\"font-size:12pt;\">"+"-/{}".format(self.total_epochs)+\
                "</span></p></body></html>")
        if self.config['TEST']['ENABLE']:
            self.gui.run_window.test_files_label.setText("<html><head/><body><p align=\"center\"><span \
                style=\"font-size:12pt;\">Files</span></p><p align=\"center\"><span \
                style=\"font-size:12pt;\">"+"-/{}".format(self.test_files)+\
                "</span></p></body></html>")

    def run(self): 
        f = None
        try:       
            ###########
            # PULLING #
            ###########
            self.update_pulling_signal.emit(0)
            self.process_steps = "pulling"
            # Collect the output of the container and update the GUI
            self.total_layers = {}
            for item in self.docker_client.api.pull(self.main_gui.cfg.settings['biapy_container_name'], stream=True, decode=True):
                print(item)
                if item["status"] == 'Pulling fs layer':
                    self.total_layers[item["id"]+"_download"] = 0
                    self.total_layers[item["id"]+"_extract"] = 0
                elif item["status"] == "Downloading":
                    self.total_layers[item["id"]+"_download"] = item["progressDetail"]['current']/item["progressDetail"]['total']
                elif item["status"] == "Extracting": 
                    self.total_layers[item["id"]+"_extract"] = item["progressDetail"]['current']/item["progressDetail"]['total'] 
                elif item["status"] == "Pull complete": 
                    self.total_layers[item["id"]+"_download"] = 1
                    self.total_layers[item["id"]+"_extract"] = 1

                if self.break_pulling:
                    print("Stopping pulling process . . .")
                    return 
                # Update GUI 
                steps = np.sum([int(float(x)*10) for x in self.total_layers.values()])
                self.update_pulling_progress_signal.emit(steps)

            self.update_pulling_signal.emit(1)     

            #################
            # RUN CONTAINER #
            #################
            now = datetime.now()
            dt_string = now.strftime("%Y%m%d_%H%M%S")
            jobname = get_text(self.main_gui.ui.job_name_input)
            self.process_steps = "pre-running"

            # Paths definition
            # Need to create a new copy of the input config file to adapt Windows paths to linux (container's OS)
            cfg_file = get_text(self.main_gui.ui.select_yaml_name_label).replace('\\','/')
            container_out_dir_in_host = os.path.normpath(os.path.join(self.output_folder_in_host, jobname))
            self.container_stdout_file = os.path.normpath(os.path.join(container_out_dir_in_host, jobname+"_out_"+dt_string))
            self.container_stderr_file = os.path.normpath(os.path.join(container_out_dir_in_host, jobname+"_err_"+dt_string))
            self.output_folder_in_container = path_to_linux(self.output_folder_in_host, self.main_gui.cfg.settings['os_host']) 
            cfg_input = os.path.join(container_out_dir_in_host, "input_config")
            real_cfg_input = os.path.join(cfg_input, "input"+dt_string+".yaml")
            os.makedirs(cfg_input, exist_ok=True)

            # Read the configuration file
            with open(cfg_file, "r") as stream:
                try:
                    temp_cfg = yaml.safe_load(stream)
                except yaml.YAMLError as exc:
                    print(exc)

            command = ["--config", "/BiaPy_files/input.yaml", "--result_dir", "{}".format(self.output_folder_in_container),
                "--name", "{}".format(jobname), "--run_id", "1"]   
            gpus = " "
            if self.use_gpu:
                gpus = self.main_gui.ui.gpu_input.currentData()
                gpus = [int(x[0]) for x in gpus]
                gpus = ','.join(str(x) for x in gpus)
                command += ["--gpu", gpus]

            # Docker mount points 
            volumes = {}
            volumes[real_cfg_input] = {"bind": "/BiaPy_files/input.yaml", "mode": "ro"}
            volumes[self.output_folder_in_host] = {"bind": self.output_folder_in_container, "mode": "rw"}
            paths = []
            paths.append(self.output_folder_in_container)
            
            if self.config['TRAIN']['ENABLE']: # mirar los paths que se repiten y bindear solo uan vez, si no error
                self.total_epochs = int(self.config['TRAIN']['EPOCHS'])
                self.gui.run_window.train_progress_bar.setMaximum(self.total_epochs)

                # Train path
                p = os.path.realpath(os.path.join(self.config['DATA']['TRAIN']['PATH'], '..')) 
                p = path_to_linux(p, self.main_gui.cfg.settings['os_host'])
                if not path_in_list(paths,p):
                    paths.append(p)
                    volumes[p] = {"bind": p, "mode": "ro"}
                p = path_to_linux(self.config['DATA']['TRAIN']['PATH'], self.main_gui.cfg.settings['os_host'])
                temp_cfg['DATA']['TRAIN']['PATH'] = p

                # Train GT path
                p = os.path.realpath(os.path.join(self.config['DATA']['TRAIN']['GT_PATH'], '..'))
                p = path_to_linux(p, self.main_gui.cfg.settings['os_host'])
                if not path_in_list(paths,p):
                    paths.append(p)    
                    volumes[p] = {"bind": p, "mode": "ro"}
                p = path_to_linux(self.config['DATA']['TRAIN']['GT_PATH'], self.main_gui.cfg.settings['os_host'])
                temp_cfg['DATA']['TRAIN']['GT_PATH'] = p

                if not self.config['DATA']['VAL']['FROM_TRAIN']:
                    # Val path
                    p = os.path.realpath(os.path.join(self.config['DATA']['VAL']['PATH'], '..'))
                    p = path_to_linux(p, self.main_gui.cfg.settings['os_host'])
                    if not path_in_list(paths,p):
                        paths.append(p)
                        volumes[p] = {"bind": p, "mode": "ro"}
                    p = path_to_linux(self.config['DATA']['VAL']['PATH'], self.main_gui.cfg.settings['os_host'])
                    temp_cfg['DATA']['VAL']['PATH'] = p

                    # Val GT path
                    p = os.path.realpath(os.path.join(self.config['DATA']['VAL']['GT_PATH'], '..'))
                    p = path_to_linux(p, self.main_gui.cfg.settings['os_host'])
                    if not path_in_list(paths,p):
                        paths.append(p)
                        volumes[p] = {"bind": p, "mode": "ro"}
                    p = path_to_linux(self.config['DATA']['VAL']['GT_PATH'], self.main_gui.cfg.settings['os_host'])
                    temp_cfg['DATA']['VAL']['GT_PATH'] = p
            else:
                self.gui.run_window.train_progress_label.setVisible(False)
                self.gui.run_window.train_progress_bar.setVisible(False)
                self.gui.run_window.train_epochs_label.setVisible(False)
            if self.config['TEST']['ENABLE'] and not self.config['DATA']['TEST']['USE_VAL_AS_TEST']:
                # Test path
                p = os.path.realpath(os.path.join(self.config['DATA']['TEST']['PATH'], '..'))
                p = path_to_linux(p, self.main_gui.cfg.settings['os_host'])
                if not path_in_list(paths,p):
                    paths.append(p)
                    volumes[p] = {"bind": p, "mode": "ro"}
                p = path_to_linux(self.config['DATA']['TEST']['PATH'], self.main_gui.cfg.settings['os_host'])
                temp_cfg['DATA']['TEST']['PATH'] = p

                if self.config['DATA']['TEST']['LOAD_GT']:
                    # Test GT path
                    p = os.path.realpath(os.path.join(self.config['DATA']['TEST']['GT_PATH'], '..'))   
                    p = path_to_linux(p, self.main_gui.cfg.settings['os_host'])
                    if not path_in_list(paths,p):
                        paths.append(p)
                        volumes[p] = {"bind": p, "mode": "ro"} 
                    p = path_to_linux(self.config['DATA']['TEST']['GT_PATH'], self.main_gui.cfg.settings['os_host'])
                    temp_cfg['DATA']['TEST']['GT_PATH'] = p   

            if self.config['MODEL']['LOAD_CHECKPOINT']: 
                p = os.path.realpath(os.path.join(self.config['PATHS']['CHECKPOINT_FILE'], '..'))
                p = path_to_linux(p, self.main_gui.cfg.settings['os_host'])
                if not path_in_list(paths,p):
                    paths.append(p)
                    volumes[p] = {"bind": p, "mode": "ro"} 
                p = path_to_linux(self.config['PATHS']['CHECKPOINT_FILE'], self.main_gui.cfg.settings['os_host'])
                temp_cfg['PATHS']['CHECKPOINT_FILE'] = p

            if not self.config['TEST']['ENABLE']:
                self.gui.run_window.test_progress_label.setVisible(False)
                self.gui.run_window.test_progress_bar.setVisible(False)
                self.gui.run_window.test_files_label.setVisible(False)
            else:
                self.test_filenames = sorted(next(os.walk(self.config['DATA']['TEST']['PATH']))[2])
                self.test_files = len(sorted(next(os.walk(self.config['DATA']['TEST']['PATH']))[2]))
                self.gui.run_window.test_progress_bar.setMaximum(self.test_files)

            if self.config['TEST']['ENABLE'] and self.config['TEST']['ENABLE']:
                self.gui.run_window.test_progress_label.setEnabled(False)
                self.gui.run_window.test_progress_bar.setEnabled(False)
                self.gui.run_window.test_files_label.setEnabled(False)
            
            print("Creating temporal input YAML file") 
            with open(real_cfg_input, 'w') as outfile:
                yaml.dump(temp_cfg, outfile, default_flow_style=False)

            if self.use_gpu and not self.windows_os:
                device_requests = [ docker.types.DeviceRequest(count=-1, capabilities=[['gpu']]) ]
            else:
                device_requests = None

            # Run container
            # check_command = [ "python3", "-u", "-c", "'import torch; print(torch.cuda.is_available())'"]
            print(f"Command: {command}")
            print(f"Volumes:  {volumes}")
            self.biapy_container = self.docker_client.containers.run(
                self.container_name, 
                # entrypoint=[ "/bin/bash", "-l", "-c" ],
                command=command,
                detach=True,
                volumes=volumes,
                user=self.user_host if not self.windows_os else None,
                device_requests=device_requests,
                shm_size="512m", 
            )
            self.process_steps = "running"
            print("Container created!")

            # Set the window header 
            self.container_info = \
            "<b>BiaPy container ({} - ID: {})</b><br>\
            <table>\
                <tr><td>Start date</td><td>{}</td></tr>\
                <tr><td>Jobname</td><td>{}</td></tr>\
                <tr><td>YAML</td><td><a href={}>{}</a></td></tr>\
                <tr><td>Output folder  </td><td><a href={}>{}</a></td></tr>\
                <tr><td>Output log</td><td><a href={}>{}</a></td></tr>\
                <tr><td>Error log</td><td><a href={}>{}</a></td></tr>\
            </table>"\
            .format(str(self.biapy_container.image).replace('<','').replace('>',''), self.biapy_container.short_id,
                now.strftime("%Y/%m/%d %H:%M:%S"), jobname,
                bytearray(QUrl.fromLocalFile(get_text(self.main_gui.ui.select_yaml_name_label)).toEncoded()).decode(), get_text(self.main_gui.ui.select_yaml_name_label),
                bytearray(QUrl.fromLocalFile(container_out_dir_in_host).toEncoded()).decode(), container_out_dir_in_host,
                bytearray(QUrl.fromLocalFile(self.container_stdout_file).toEncoded()).decode(), self.container_stdout_file,
                bytearray(QUrl.fromLocalFile(self.container_stderr_file).toEncoded()).decode(), self.container_stderr_file)
            
            self.update_log_signal.emit(0)

            # Log the output in a file     
            f = open(self.container_stderr_file, "x")
            f.close()       
            f = open(self.container_stdout_file, "w")
            f.write("#########################################################\n")
            f.write(self.container_info.replace("<tr><td>", "").replace("</td><td>", ": ").replace("</td></tr>", "")\
                .replace("<table>", "\n").replace("</table>", "\n").replace('<b>','').replace('</b>','').replace('<br>','').strip())
            f.write("#########################################################\n")

            # Collect the output of the container and update the GUI
            last_write = datetime.now()
            self.epoch_count = 0
            self.test_image_count = 0
            start_test = False
            for log in self.biapy_container.logs(stream=True):
                l = log.decode("utf-8")
                try:
                    print(l.encode("utf-8") if self.windows_os else l, end="")
                except: 
                    pass 
                try:
                    f.write(l)
                    f.flush()
                except: 
                    pass 

                # Update training progress bar
                if self.config['TRAIN']['ENABLE'] and "Epoch {}/{}".format(self.epoch_count+1,self.total_epochs) in l:
                    self.epoch_count += 1 
                    self.update_train_progress_signal.emit(self.epoch_count)
                
                # Activate test phase. This is used to not let the test if below check if "Processing .." string is in the log output 
                # continuously and reduce the computation. 
                if "#  INFERENCE  #" in l:
                    start_test = True
                    self.gui.run_window.test_progress_label.setEnabled(True)
                    self.gui.run_window.test_progress_bar.setEnabled(True)
                    self.gui.run_window.test_files_label.setEnabled(True)
                    if self.config['TRAIN']['ENABLE']:
                        self.gui.run_window.train_progress_label.setEnabled(False)
                        self.gui.run_window.train_progress_bar.setEnabled(False)
                        self.gui.run_window.train_epochs_label.setEnabled(False)
                    
                # Update test progress bar
                if self.config['TEST']['ENABLE'] and start_test and self.test_image_count < self.test_files and \
                    "Processing image(s): ['{}']".format(self.test_filenames[self.test_image_count]) in l: 
                    self.test_image_count += 1
                    self.update_test_progress_signal.emit(self.test_image_count)

                if datetime.now() - last_write > timedelta(seconds=3):
                    self.update_log_signal.emit(1)
                    last_write = datetime.now()
                    
            self.update_log_signal.emit(1)

            if self.config['TEST']['ENABLE']:
                self.gui.run_window.test_progress_label.setEnabled(False)
                self.gui.run_window.test_progress_bar.setEnabled(False)
                self.gui.run_window.test_files_label.setEnabled(False)
            self.process_steps = "finished"
            f.close()
        except:
            # Print first the traceback (only visible through terminal)
            print(traceback.format_exc())

            # Try to log the error in the error file
            ferr = open(self.container_stderr_file, "w")
            ferr.write("#########################################################\n")
            ferr.write(self.container_info+"\n")
            ferr.write("#########################################################\n")
            ferr.write(traceback.format_exc())
            ferr.close()
            if f is not None: f.close()
            self.finished_signal.emit()
