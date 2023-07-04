import os
import traceback
import docker
import urllib.request
from datetime import datetime, timedelta
from pathlib import Path

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt, QObject, QUrl
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import *

from ui_utils import resource_path, get_text
from ui_build import Ui_BuildBiaPy 

class buildBiapy_Ui(QDialog):
    def __init__(self, parent_worker):
        super(buildBiapy_Ui, self).__init__()
        self.run_window = Ui_BuildBiaPy()
        self.parent_worker = parent_worker
        self.run_window.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.run_window.bn_min.clicked.connect(self.showMinimized)
        self.run_window.bn_close.clicked.connect(self.close_all)
        self.run_window.bn_close.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","closeAsset 43.png"))))
        self.run_window.bn_min.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","hideAsset 53.png"))))
        self.run_window.build_progress_bar.setValue(0)
        self.progress_first_time = True

        self.dragPos = self.pos()  
        def movedialogWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
        self.run_window.frame_top.mouseMoveEvent = movedialogWindow  

    def close_all(self):
        self.parent_worker.finished_signal.emit(self.parent_worker.finished_good)
        self.parent_worker.close_signal.emit()
        self.close()
        
    def init_log(self, container_info):
        self.run_window.biapy_container_info_label.setText(container_info)
        self.run_window.build_biapy_log.setText(' ')

    def update_gui(self, signal):
        # Initialize the GUI
        if signal == 0:
            self.parent_worker.init_gui()
        elif signal == 1:
            self.update_log()
        else:
            print("Nothing")

    def update_log(self):
        with open(self.parent_worker.container_stdout_file, 'r') as f:
            last_lines = f.readlines()[-11:]
            last_lines = ' '.join(last_lines)
            self.run_window.build_biapy_log.setText(last_lines)
            if "Successfully built " in last_lines:
                self.parent_worker.finished_good = 0 

    def update_building_progress(self, value):
        if self.progress_first_time:
            self.run_window.build_progress_bar.setMaximum(self.parent_worker.total_steps)
        self.run_window.build_progress_bar.setValue(value)
        
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

class build_worker(QObject):
    # Signal to indicate the main thread that the worker has finished 
    finished_signal = QtCore.Signal(int)

    # Signal to indicate the main thread that the worker has finished 
    close_signal = QtCore.Signal()

    # Signal to indicate the main thread to update the log frame (1) or init the GUI (0, this last is done just one time)
    update_log_signal = QtCore.Signal(int)

    # Signal to indicate the main thread to update the GUI with the new progress of the building
    update_build_progress_signal = QtCore.Signal(int)

    def __init__(self, main_gui, biapy_container_dockerfile, container_name, output_folder):
        super(build_worker, self).__init__()
        self.main_gui = main_gui
        self.biapy_container_dockerfile = biapy_container_dockerfile
        self.container_name = container_name
        self.output_folder = output_folder
        self.gui = buildBiapy_Ui(self)
        self.gui.open()
        self.docker_client = docker.from_env()
        self.container_info = 'NONE'
        self.finished_good = 1
        self.container_stdout_file = "None"

    def init_gui(self):
        self.gui.init_log(self.container_info)

    def run(self): 
        f = None
        try:       
            now = datetime.now()
            dt_string = now.strftime("%Y%m%d_%H%M%S")
            jobname = get_text(self.main_gui.ui.job_name_input)
            # dockerfile = os.path.join(self.log_dir, "Dockerfile")
            dockerfile = os.path.join(str(Path.home()), "Dockerfile")
            container_out_dir = os.path.join(self.output_folder, jobname)
            if jobname == '': jobname = "BiaPy"
            self.container_stdout_file = os.path.join(container_out_dir, jobname+"_container_build_"+dt_string)

            # Log the output in a file             
            f = open(self.container_stdout_file, "w")
            f.write("#########################################################\n")
            f.write("Building BiaPy container\nStart date: {}\nDockerfile: {}\n".format(now.strftime("%Y/%m/%d %H:%M:%S"), dockerfile))
            f.write("#########################################################\n")

            if os.path.exists(dockerfile):
                self.main_gui.yes_no_exec("{} file exists. Do you want to overwrite it?".format(dockerfile))
            
            if self.main_gui.yes_no.answer:
                print("Fetching file {}".format(self.biapy_container_dockerfile))
                f.write("Fetching file {}".format(self.biapy_container_dockerfile))
                urllib.request.urlretrieve(self.biapy_container_dockerfile, dockerfile)
            
            # Set the window header 
            self.container_info = \
            "<b>Building BiaPy container</b><br>\
                <table>\
                <tr><td>Start date</td><td>{}</td>\
                </tr><tr><td>Dockerfile</td><td><a href={}>{}</a></td></tr>\
                </tr><tr><td>Build log</td><td><a href={}>{}</a></td></tr>\
                </table>"\
                .format(now.strftime("%Y/%m/%d %H:%M:%S"), 
                        bytearray(QUrl.fromLocalFile(dockerfile).toEncoded()).decode(), dockerfile,
                        bytearray(QUrl.fromLocalFile(self.container_stdout_file).toEncoded()).decode(), self.container_stdout_file)
            
            self.update_log_signal.emit(0)

            # Build container
            result = self.docker_client.images.build(path="/data/dfranco/ficheros_BiaPy_GUI", rm=True, forcerm=True)

            # Collect the output of the container and update the GUI
            last_write = datetime.now()
            self.steps = 0
            first_time = True
            for item in result[1]:
                for key, value in item.items():
                    if key == 'stream':
                        text = value.strip()
                        if text:
                            print(text)
                            f.write(text+'\n')     
                            if 'Step' in text:
                                if first_time:
                                    self.total_steps = int(text.split(' ')[1].split('/')[1])
                                    first_time = False 
                                self.steps += 1 
                                self.update_build_progress_signal.emit(self.steps)
                
                    # Update GUI after a few seconds
                    if datetime.now() - last_write > timedelta(seconds=3):
                        self.update_log_signal.emit(1)            
                        last_write = datetime.now()

            self.update_log_signal.emit(1)
            self.finished_signal.emit(self.finished_good)
            f.close()
        except:
            # Print first the traceback (only visible through terminal)
            print(traceback.format_exc())

            # Try to log the error in the error file
            ferr = open(container_stderr_file, "w")
            ferr.write("#########################################################\n")
            ferr.write(self.container_info+"\n")
            ferr.write("#########################################################\n")
            ferr.write(traceback.format_exc())
            ferr.close()
            if f is not None: f.close()
            self.finished_signal.emit(2)
