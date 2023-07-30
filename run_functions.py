import os
import traceback
import docker
from datetime import datetime, timedelta

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt, QObject, QUrl
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import *

from ui_utils import get_text, resource_path
from ui_run import Ui_RunBiaPy 

class runBiaPy_Ui(QDialog):
    def __init__(self, parent_worker):
        super(runBiaPy_Ui, self).__init__()
        self.run_window = Ui_RunBiaPy()
        self.parent_worker = parent_worker
        self.run_window.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.run_window.bn_min.clicked.connect(self.showMinimized)
        self.run_window.bn_close.clicked.connect(self.close_all)
        self.run_window.bn_close.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","closeAsset 43.png"))))
        self.run_window.bn_min.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","hideAsset 53.png"))))
        self.run_window.icon_label.setPixmap(QPixmap(resource_path(os.path.join("images","bn_images","info.png"))))
        self.run_window.stop_container_bn.clicked.connect(self.parent_worker.stop_worker)
        self.run_window.container_state_label.setText("BiaPy state [ Initializing ]")
        self.run_window.train_progress_bar.setValue(0)
        self.run_window.test_progress_bar.setValue(0)
        self.dragPos = self.pos()  
        def movedialogWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
        self.run_window.frame_top.mouseMoveEvent = movedialogWindow  

    def close_all(self):
        self.parent_worker.stop_worker()
        self.parent_worker.finished_signal.emit()
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
            last_lines = f.readlines()[-11:]
            last_lines = ''.join(last_lines).replace("\x08", "").replace("[A", "").replace("", "")           
            self.run_window.run_biapy_log.setText(str(last_lines))
            if "FINISHED JOB" in last_lines:
                finished_good = True 
        
        if finished_good:
            self.update_cont_state(0)
        else:
            self.update_cont_state(1)

    def update_cont_state(self, svalue):
        if svalue == 1:
            self.parent_worker.biapy_container.reload()
            st = self.parent_worker.biapy_container.status
            if st == "running":
                st = "<span style=\"color:green;\">"+st+"</span>"
            elif st == "exited":
                st = "<span style=\"color:red;\">"+st+"</span>"
                self.run_window.stop_container_bn.setEnabled(False)
            elif st == "created":
                st = "<span style=\"color:yellow;\">"+st+"</span>"
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

    def __init__(self, main_gui, config, container_name, worker_id, output_folder, user_host):
        super(run_worker, self).__init__()
        self.main_gui = main_gui
        self.config = config
        self.container_name = container_name
        self.worker_id = worker_id
        self.output_folder = output_folder
        self.user_host = user_host
        self.gui = runBiaPy_Ui(self)
        self.gui.open()
        self.docker_client = docker.from_env()
        self.biapy_container = None
        self.container_info = 'NONE'

    def stop_worker(self):
        if self.biapy_container is not None:
            self.biapy_container.stop(timeout=1)
        self.update_cont_state_signal.emit(1)
        self.gui.run_window.stop_container_bn.setEnabled(False)
        self.gui.run_window.test_progress_label.setEnabled(False)
        self.gui.run_window.test_progress_bar.setEnabled(False)
        self.gui.run_window.test_files_label.setEnabled(False)
        self.gui.run_window.train_progress_label.setEnabled(False)
        self.gui.run_window.train_progress_bar.setEnabled(False)
        self.gui.run_window.train_epochs_label.setEnabled(False)

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
            # BiaPy call construction
            now = datetime.now()
            dt_string = now.strftime("%Y%m%d_%H%M%S")
            jobname = get_text(self.main_gui.ui.job_name_input)
            cfg_file = get_text(self.main_gui.ui.select_yaml_name_label)
            gpus = self.main_gui.ui.gpu_input.currentData()
            gpus = sorted([int(x[0]) for x in gpus])
            gpus = list(dict.fromkeys(gpus))
            gpus = ','.join(str(x) for x in gpus)
            command=["-cfg", "{}".format(cfg_file), "-rdir", "{}".format(self.output_folder),
                "-name", "{}".format(jobname), "-rid", "0", "-gpu", gpus]
            
            # Create the result dir
            container_out_dir = os.path.join(self.output_folder, jobname)
            self.container_stdout_file = os.path.join(container_out_dir, jobname+"_out_"+dt_string)
            self.container_stderr_file = os.path.join(container_out_dir, jobname+"_err_"+dt_string)
            os.makedirs(container_out_dir, exist_ok=True)
            
            # Docker mount points 
            volumes = {}
            volumes[cfg_file] = {"bind": cfg_file, "mode": "ro"}
            volumes[self.output_folder] = {"bind": self.output_folder, "mode": "rw"}
            if self.config['TRAIN']['ENABLE']:
                self.total_epochs = int(self.config['TRAIN']['EPOCHS'])
                self.gui.run_window.train_progress_bar.setMaximum(self.total_epochs)
                volumes[self.config['DATA']['TRAIN']['PATH']] = {"bind": self.config['DATA']['TRAIN']['PATH'], "mode": "ro"}
                volumes[self.config['DATA']['TRAIN']['GT_PATH']] = {"bind": self.config['DATA']['TRAIN']['GT_PATH'], "mode": "ro"}
                if not self.config['DATA']['VAL']['FROM_TRAIN']:
                    volumes[self.config['DATA']['VAL']['PATH']] = {"bind": self.config['DATA']['VAL']['PATH'], "mode": "ro"}
                    volumes[self.config['DATA']['VAL']['GT_PATH']] = {"bind": self.config['DATA']['VAL']['GT_PATH'], "mode": "ro"}
            else:
                self.gui.run_window.train_progress_label.setVisible(False)
                self.gui.run_window.train_progress_bar.setVisible(False)
                self.gui.run_window.train_epochs_label.setVisible(False)
            if self.config['TEST']['ENABLE'] and not self.config['DATA']['TEST']['USE_VAL_AS_TEST']:
                volumes[self.config['DATA']['TEST']['PATH']] = {"bind": self.config['DATA']['TEST']['PATH'], "mode": "ro"}
                if self.config['DATA']['TEST']['LOAD_GT']:
                    volumes[self.config['DATA']['TEST']['GT_PATH']] = {"bind": self.config['DATA']['TEST']['GT_PATH'], "mode": "ro"}    
            if self.config['MODEL']['LOAD_CHECKPOINT']:
                volumes[self.config['PATHS']['CHECKPOINT_FILE']] = {"bind": self.config['PATHS']['CHECKPOINT_FILE'], "mode": "ro"} 

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

            # Run container
            self.biapy_container = self.docker_client.containers.run(
                self.container_name, 
                command=command,
                detach=True,
                volumes=volumes,
                user=self.user_host,
                device_requests=[ docker.types.DeviceRequest(count=-1, capabilities=[['gpu']]) ]
            )

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
                bytearray(QUrl.fromLocalFile(cfg_file).toEncoded()).decode(), cfg_file,
                bytearray(QUrl.fromLocalFile(container_out_dir).toEncoded()).decode(), container_out_dir,
                bytearray(QUrl.fromLocalFile(self.container_stdout_file).toEncoded()).decode(), self.container_stdout_file,
                bytearray(QUrl.fromLocalFile(self.container_stderr_file).toEncoded()).decode(), self.container_stderr_file)
            
            self.update_log_signal.emit(0)

            # Log the output in a file             
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
                print(l)
                f.write(l)

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

                # Update GUI after a few seconds
                if datetime.now() - last_write > timedelta(seconds=3):
                    self.update_log_signal.emit(1)
                    last_write = datetime.now()

            self.update_log_signal.emit(1)

            if self.config['TEST']['ENABLE']:
                self.gui.run_window.test_progress_label.setEnabled(False)
                self.gui.run_window.test_progress_bar.setEnabled(False)
                self.gui.run_window.test_files_label.setEnabled(False)

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
