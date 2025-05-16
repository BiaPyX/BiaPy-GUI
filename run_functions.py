from __future__ import annotations
import os
import traceback
import docker
import yaml
import numpy as np
from datetime import datetime, timedelta
import multiprocessing
import json
from pathlib import Path
from typing import Dict, List, Optional

from PySide6 import QtCore
from PySide6.QtCore import Qt, QObject, QUrl
from PySide6.QtGui import QPixmap, QMovie, QCloseEvent
from PySide6.QtWidgets import QDialog, QStyle

from ui_utils import get_text, resource_path, path_in_list, path_to_linux, center_window
from biapy.biapy_check_configuration import convert_old_model_cfg_to_current_version
from ui.ui_run import Ui_RunBiaPy
from ui.aux_windows import yes_no_Ui
import main


class runBiaPy_Ui(QDialog):
    def __init__(self, parent_worker: run_worker):
        """
        Creates the UI in charge of running BiaPy.

        Parameters
        ----------
        parent_ui : MainWindow
            Main window.
        """
        super(runBiaPy_Ui, self).__init__()
        self.run_window = Ui_RunBiaPy()
        self.parent_worker = parent_worker
        self.run_window.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | Qt.WindowMinimizeButtonHint)
        self.run_window.bn_min.clicked.connect(self.showMinimized)
        self.run_window.bn_close.clicked.connect(self.close)
        self.run_window.bn_close.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarCloseButton))
        self.run_window.bn_min.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarMinButton))
        self.run_window.icon_label.setPixmap(QPixmap(resource_path(os.path.join("images", "bn_images", "info.png"))))
        self.run_window.return_icon_label.setPixmap(
            QPixmap(resource_path(os.path.join("images", "bn_images", "return_icon.png")))
        )
        self.run_window.return_icon_label_2.setPixmap(
            QPixmap(resource_path(os.path.join("images", "bn_images", "return_icon.png")))
        )
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
        self.pulling_terminal_buffer = []
        self.run_window.biapy_image_downloading_progress_bar.setMaximum(100)
        self.run_window.biapy_image_extracting_progress_bar.setMaximum(100)
        self.run_window.container_pulling_extract_frame.setVisible(False)
        self.log_lines = 23

        # Initializing spin
        self.run_window.spin_label.setVisible(False)
        self.loading_spin = QMovie(resource_path(os.path.join("images", "circle_loader.gif")))
        self.run_window.spin_label.setPixmap(self.loading_spin.currentPixmap())

        def update_spin(j):
            self.run_window.spin_label.setPixmap(self.loading_spin.currentPixmap())

        self.loading_spin.start()
        self.loading_spin.frameChanged.connect(update_spin)

    def closeEvent(self, event: QCloseEvent):
        """
        Close event handler.

        Parameters
        ----------
        event: QCloseEvent
            Event that called this function.
        """
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
            center_window(self.yes_no, self.geometry())
            self.yes_no.exec_()
            if self.yes_no.answer:
                self.kill_all_processes()
            else:
                event.ignore()

    def kill_all_processes(self):
        """
        Kill all the processes running.
        """
        self.parent_worker.stop_worker()
        self.run_window.spin_label.setVisible(False)
        try:
            self.parent_worker.finished_signal.emit()
        except Exception as e:
            self.parent_worker.main_gui.logger.error(
                f"Possible expected error during BiaPy's running thread deletion: {e}"
            )
        self.close()

    def init_log(self, container_info: str):
        """
        Initializes the log setting container information for the user.

        Parameters
        ----------
        container_info: str
            Information of the container to be set.
        """
        self.run_window.biapy_container_info_label.setText(container_info)
        self.run_window.run_biapy_log.setText(" ")

    def update_gui(self, signal: int):
        """
        Close event handler.

        Parameters
        ----------
        signal : int
            Signal emited by a thread. Possibilities:
            * 0 tells the main GUI to initialize the window.
            * 1 tells the main GUI that the log needs to be updated. This is going to be called multiple times.
            otherwise.
        """
        # Initialize the GUI
        if signal == 0:
            self.parent_worker.init_gui()
        elif signal == 1:
            self.update_log()
        else:
            self.parent_worker.main_gui.logger.info("Nothing")

    def update_log(self):
        """
        Read the last lines of the output to decide if the job has finished or not.
        """
        finished_good = False
        with open(self.parent_worker.container_stdout_file, "r", encoding="utf8") as f:
            last_lines = f.readlines()[-self.log_lines :]
            last_lines = "".join(last_lines).replace("\x08", "").replace("[A", "").replace("", "")
            self.run_window.run_biapy_log.setText(str(last_lines))
            if "FINISHED JOB" in last_lines:
                finished_good = True

        if finished_good:
            self.update_cont_state(0)
        else:
            self.update_cont_state(1)

    def update_cont_state(self, svalue: int):
        """
        Updates the container state.

        Parameters
        ----------
        svalue : int
            Signal to update the state accordingly. The possible cases are:
            * If 1 is received means that the container status will be evaluated and will set in the GUI
              the corresponding information so the user knows it.
            * If 0 is received means that the container has finished good
        """
        st = "unknown"
        if svalue == 1:
            if self.parent_worker.biapy_container is not None:
                try:
                    self.parent_worker.biapy_container.reload()
                except Exception as e:
                    self.parent_worker.main_gui.logger.error(
                        f"Possible expected error during container status reload(): {e}"
                    )

                st = self.parent_worker.biapy_container.status
                if st == "running":
                    st = '<span style="color:green;">R' + st[1:] + "</span>"
                elif st == "exited":
                    st = '<span style="color:red;">E' + st[1:] + "</span>"
                    self.run_window.stop_container_bn.setEnabled(False)
                elif st == "created":
                    st = '<span style="color:orange;">C' + st[1:] + "</span>"
        # When the signal is 0 the container has finished good
        else:
            st = "finished"
            self.run_window.stop_container_bn.setEnabled(False)
        self.run_window.container_state_label.setText("Container state [ {} ]".format(st))

    def update_train_progress(self, value: int):
        """
        Updates training progress.

        Parameters
        ----------
        value : int
            Value to set the training bar with.
        """
        self.run_window.train_progress_bar.setValue(value)
        self.run_window.train_epochs_label.setText(
            '<html><head/><body><p align="center"><span \
            style="font-size:12pt;">Epochs</span></p><p align="center"><span \
            style="font-size:12pt;">'
            + "{}/{}".format(self.parent_worker.epoch_count, self.parent_worker.total_epochs)
            + "</span></p></body></html>"
        )

    def update_test_progress(self, value: int):
        """
        Updates test progress.

        Parameters
        ----------
        value : int
            Value to set the test bar with.
        """
        self.run_window.test_progress_bar.setValue(value)
        self.run_window.test_files_label.setText(
            '<html><head/><body><p align="center"><span \
            style="font-size:12pt;">Files</span></p><p align="center"><span \
            style="font-size:12pt;">'
            + "{}/{}".format(self.parent_worker.test_image_count, self.parent_worker.test_files)
            + "</span></p></body></html>"
        )

    def update_pulling_progress(self, d_value: int, e_value: int, item: str):
        """
        Updates the pulling process progress.

        Parameters
        ----------
        d_value : int
            Value to set the download process bar with.

        e_value : int
            Value to set the download process bar with.

        item : str
            Message of the download/extraction process to be stored.
        """
        dmax = max(10, len(self.parent_worker.download_total_layers) * 10)
        emax = max(10, len(self.parent_worker.extract_total_layers) * 10)

        # Download process
        self.run_window.biapy_image_downloading_progress_bar.setMaximum(dmax)
        self.run_window.biapy_image_downloading_progress_bar.setValue(d_value)
        # Extracting process
        self.run_window.biapy_image_extracting_progress_bar.setMaximum(emax)
        self.run_window.biapy_image_extracting_progress_bar.setValue(e_value)

        if d_value / dmax > 0.99 and e_value / emax > 0.99:
            self.run_window.spin_label.setVisible(True)

        # Update terminal-like label
        self.pulling_terminal_buffer.append(item)
        if len(self.pulling_terminal_buffer) > self.log_lines:
            self.pulling_terminal_buffer.pop(0)
        self.run_window.run_biapy_log.setText("\n".join(self.pulling_terminal_buffer))

    def pulling_progress(self, value: int):
        """
        Updates the container state.

        Parameters
        ----------
        value : int
            Signal to update the pulling progress accordingly. The possible cases are:
            * If 0 is received means that the download process has been started.
            * If 1 is received means that the extraction process has been started and is present.
              In new macOS this process may be hidden.
            * In other cases means that the pulling process has finished.
        """
        if value == 0:  # Start download process
            self.run_window.image_prep_title_label.setVisible(True)
            self.run_window.image_prep_title_label.setText(
                "Preparing BiaPy image (only done once) - Total approx. size: {}".format(
                    self.parent_worker.main_gui.cfg.settings["biapy_container_size"]
                )
            )
            self.run_window.biapy_image_status.setText('BiaPy image [ <span style="color:orange;"> Pulling </span> ]')
            self.run_window.container_pulling_frame.setVisible(True)
            self.run_window.biapy_container_info_label.setText(
                "Please wait for the image to download fully. Occasionally, parts of the container may be downloaded twice,\ncausing the progress bar to move backward slightly."
            )
            self.run_window.terminal_upper_label.setText("Downloading and unpacking log")
        elif value == 1:  # Start extracting process
            self.run_window.container_pulling_extract_frame.setVisible(True)
        else:  # end
            self.run_window.container_pulling_frame.setVisible(False)
            self.run_window.image_prep_title_label.setVisible(False)
            self.run_window.biapy_image_status.setText('BiaPy image [ <span style="color:green;">Downloaded</span> ]')
            self.run_window.biapy_container_info_label.setText("INITIALIZING . . . (this may take a while)")
            self.run_window.run_biapy_log.setText(
                "Please wait, the first screen update may take a while depending on your OS"
            )
            self.run_window.terminal_upper_label.setText("Last lines of the log (updating every 3 seconds):")
            self.run_window.spin_label.setVisible(True)

    def mousePressEvent(self, event: QCloseEvent):
        """
        Mouse press event handler.

        Parameters
        ----------
        event: QCloseEvent
            Event that called this function.
        """
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
    update_pulling_progress_signal = QtCore.Signal(int, int, str)

    def __init__(
        self,
        main_gui: main.MainWindow,
        config: Dict,
        container_name: str,
        worker_id: int,
        output_folder: str,
        user_host: str,
        use_gpu: bool,
        use_local_biapy_image: bool,
    ):
        """
        Initialized the worker in charge of running BiaPy container.

        Parameters
        ----------
        main_gui : MainWindow
            Main window.

        config : dict
            Running donfiguration.

        container_name : str
            Name of the container to download and run.

        worker_id : int
            Id of the worker as more than one running window can be launched at the same time.

        output_folder : str
            Output folder.

        user_host : str
            User that is going to run the container. Only used id the OS is windows.

        use_gpu : bool
            Whether to use GPU or not.

        use_local_biapy_image : bool
            Whether to use a local BiaPy image or download it. This is mainly used for debugging.
        """
        super(run_worker, self).__init__()
        self.main_gui = main_gui
        self.config = config
        self.container_name = container_name
        self.worker_id = worker_id
        self.output_folder_in_host = output_folder
        self.windows_os = True if "win" in self.main_gui.cfg.settings["os_host"].lower() else False
        self.user_host = user_host
        self.use_gpu = use_gpu
        self.gui = runBiaPy_Ui(self)
        self.gui.open()
        self.docker_client = docker.from_env()
        self.biapy_container = None
        self.container_info = "NONE"
        self.process_steps = "NONE"
        self.break_pulling = False
        self.use_local_biapy_image = use_local_biapy_image

    def stop_worker(self):
        """
        Stops the worker.
        """
        self.main_gui.logger.info("Stopping the container . . . ")
        if self.biapy_container is not None:
            self.biapy_container.stop(timeout=1)
            try:
                self.update_cont_state_signal.emit(1)
            except Exception as e:
                self.main_gui.logger.error(f"Possible expected error during BiaPy's running thread deletion: {e}")
            self.gui.run_window.stop_container_bn.setEnabled(False)
            self.gui.run_window.test_progress_label.setEnabled(False)
            self.gui.run_window.test_progress_bar.setEnabled(False)
            self.gui.run_window.test_files_label.setEnabled(False)
            self.gui.run_window.train_progress_label.setEnabled(False)
            self.gui.run_window.train_progress_bar.setEnabled(False)
            self.gui.run_window.train_epochs_label.setEnabled(False)
        else:
            self.main_gui.logger.info("Container not running yet")
            # To kill pulling process if it is running
            self.break_pulling = True

    def init_gui(self):
        """
        Initializes the GUI.
        """
        self.gui.init_log(self.container_info)
        self.gui.run_window.spin_label.setVisible(False)
        if self.config["TRAIN"]["ENABLE"]:
            self.gui.run_window.train_epochs_label.setText(
                '<html><head/><body><p align="center"><span \
                style="font-size:12pt;">Epochs</span></p><p align="center"><span \
                style="font-size:12pt;">'
                + "-/{}".format(self.total_epochs)
                + "</span></p></body></html>"
            )
        if self.config["TEST"]["ENABLE"]:
            self.gui.run_window.test_files_label.setText(
                '<html><head/><body><p align="center"><span \
                style="font-size:12pt;">Files</span></p><p align="center"><span \
                style="font-size:12pt;">'
                + "-/{}".format(self.test_files)
                + "</span></p></body></html>"
            )

    def run(self):
        """
        Run the container.
        """
        f = None
        try:
            ###########
            # PULLING #
            ###########
            self.update_pulling_signal.emit(0)
            self.process_steps = "pulling"
            # Collect the output of the container and update the GUI
            self.download_total_layers = {}
            self.extract_total_layers = {}
            problem_attempts = 0
            json_orig_data = None
            extracting_bar_activated = False
            if self.use_local_biapy_image:
                self.main_gui.logger.info("Using local BiaPy image")
                self.docker_client = docker.from_env()  # Necessary
            else:
                while problem_attempts < 4:
                    try:
                        self.main_gui.logger.info("Pulling container . . .")
                        self.docker_client = docker.from_env()  # Necessary
                        for item in self.docker_client.api.pull(
                            self.main_gui.cfg.settings["biapy_container_name"], stream=True, decode=True
                        ):
                            self.main_gui.logger.info(item)
                            if item["status"] == "Pulling fs layer":
                                self.download_total_layers[item["id"] + "_download"] = 0
                                self.extract_total_layers[item["id"] + "_extract"] = 0
                            elif item["status"] == "Downloading":
                                total = item["progressDetail"]["total"] if "total" in item["progressDetail"] else 1
                                self.download_total_layers[item["id"] + "_download"] = (
                                    item["progressDetail"]["current"] / total
                                )
                            elif item["status"] == "Extracting":
                                if not extracting_bar_activated:
                                    extracting_bar_activated = True
                                    self.update_pulling_signal.emit(1)
                                total = item["progressDetail"]["total"] if "total" in item["progressDetail"] else 1
                                self.extract_total_layers[item["id"] + "_extract"] = (
                                    item["progressDetail"]["current"] / total
                                )
                            elif item["status"] == "Download complete":
                                self.download_total_layers[item["id"] + "_download"] = 1
                            elif item["status"] == "Pull complete":
                                self.extract_total_layers[item["id"] + "_extract"] = 1

                            if self.break_pulling:
                                self.main_gui.logger.info("Stopping pulling process . . .")
                                return

                            # Update GUI
                            d_steps = np.sum([int(float(x) * 10) for x in self.download_total_layers.values()])
                            if extracting_bar_activated:
                                e_steps = np.sum([int(float(x) * 10) for x in self.extract_total_layers.values()])
                            else:
                                e_steps = max(10, len(self.extract_total_layers) * 10)
                            self.update_pulling_progress_signal.emit(d_steps, e_steps, str(item))
                    except Exception as e:
                        problem_attempts += 1
                        self.main_gui.logger.error(f"Error pulling the container: {e}")
                        self.main_gui.logger.info(
                            f"Trying to modify ~/.docker/config.json - (attempt {problem_attempts})"
                        )

                        # Attempt 1: trying to change the values of "credsStore" and some possible typos as documented in
                        # the issue: https://github.com/docker/for-mac/issues/3785#issuecomment-518328553
                        if problem_attempts == 1:
                            try:
                                with open(Path.home() / ".docker" / "config.json", "r", encoding="utf8") as jsonFile:
                                    data = json.load(jsonFile)
                                    json_orig_data = data.copy()

                                # Possible typo
                                if "credSstore" in data:
                                    val = data["credSstore"]
                                    del data["credSstore"]
                                    data["credsStore"] = val

                                # Change credsStore value
                                if "credsStore" in data:
                                    val = data["credsStore"]
                                    data["credsStore"] = "osxkeychain" if "desktop" in val else "desktop"

                                with open(Path.home() / ".docker" / "config.json", "w", encoding="utf8") as jsonFile:
                                    json.dump(data, jsonFile, indent=4)
                            except Exception as e:
                                self.main_gui.logger.error(
                                    f"Error modifying ~/.docker/config.json file (attempt 1): {e}"
                                )

                        # Attempt 2: remove "credsStore" key
                        elif problem_attempts == 2:
                            try:
                                with open(Path.home() / ".docker" / "config.json", "r", encoding="utf8") as jsonFile:
                                    data = json.load(jsonFile)

                                # Delete credsStore directly
                                if "credsStore" in data:
                                    del data["credsStore"]

                                with open(Path.home() / ".docker" / "config.json", "w", encoding="utf8") as jsonFile:
                                    json.dump(data, jsonFile, indent=4)

                            except Exception as e:
                                self.main_gui.logger.error(
                                    f"Error modifying ~/.docker/config.json file (attempt 2): {e}"
                                )

                        # Attempt 3: rename the file
                        else:
                            try:
                                os.rename(
                                    Path.home() / ".docker" / "config.json",
                                    Path.home() / ".docker" / "config.json.backup",
                                )
                            except Exception as e:
                                self.main_gui.logger.error(
                                    f"Error modifying ~/.docker/config.json file (attempt 3): {e}"
                                )
                    else:
                        self.main_gui.logger.info(f"No errors pulling, continuing . . .")
                        problem_attempts = 10  # break the loop

                # Revert configuration ~/.docker/config.json configuration
                if json_orig_data is not None:
                    if os.path.exists(Path.home() / ".docker" / "config.json.backup"):
                        os.rename(
                            Path.home() / ".docker" / "config.json.backup", Path.home() / ".docker" / "config.json"
                        )
                    with open(Path.home() / ".docker" / "config.json", "w", encoding="utf8") as jsonFile:
                        json.dump(json_orig_data, jsonFile, indent=4)

            self.update_pulling_signal.emit(2)

            #################
            # RUN CONTAINER #
            #################
            now = datetime.now()
            dt_string = now.strftime("%Y%m%d_%H%M%S")
            jobname = get_text(self.main_gui.ui.job_name_input)
            self.process_steps = "pre-running"

            # Paths definition
            # Need to create a new copy of the input config file to adapt Windows paths to linux (container's OS)
            cfg_file = get_text(self.main_gui.ui.select_yaml_name_label).replace("\\", "/")
            container_out_dir_in_host = os.path.normpath(os.path.join(self.output_folder_in_host, jobname))
            cfg_input = os.path.join(container_out_dir_in_host, "input_config")
            real_cfg_input = os.path.join(cfg_input, "input" + dt_string + ".yaml")
            os.makedirs(cfg_input, exist_ok=True)
            self.container_stdout_file = os.path.normpath(
                os.path.join(container_out_dir_in_host, jobname + "_out_" + dt_string)
            )
            self.container_stderr_file = os.path.normpath(
                os.path.join(container_out_dir_in_host, jobname + "_err_" + dt_string)
            )
            self.container_plots_folder = os.path.normpath(
                os.path.join(container_out_dir_in_host, "results", jobname + "_1", "charts")
            )
            self.container_bmz_folder = os.path.normpath(
                os.path.join(container_out_dir_in_host, "results", jobname + "_1", "BMZ_files")
            )
            self.output_folder_in_container = path_to_linux(
                self.output_folder_in_host, self.main_gui.cfg.settings["os_host"]
            )

            # Read the configuration file
            with open(cfg_file, "r", encoding="utf8") as stream:
                try:
                    temp_cfg = yaml.safe_load(stream)
                except yaml.YAMLError as exc:
                    self.main_gui.logger.error(exc)

            dist_backend = "gloo" if self.windows_os else "nccl"
            command = [
                "--config",
                "/BiaPy_files/input.yaml",
                "--result_dir",
                "{}".format(self.output_folder_in_container),
                "--name",
                "{}".format(jobname),
                "--run_id",
                "1",
                "--dist_backend",
                f"{dist_backend}",
            ]
            gpus = " "
            device = get_text(self.main_gui.ui.device_input)
            if self.use_gpu:
                gpus = device.split()[1]  # As the format is "GPU 0 : NVIDIA RTX ..."
                command += ["--gpu", gpus]

            # Limit a bit the proccesses used in Docker if it's using a GPU, as multiGPU is not supported yet through the GUI
            cpu_count = get_text(self.main_gui.ui.SYSTEM__NUM_CPUS__INPUT)
            cpu_count = multiprocessing.cpu_count() if cpu_count == "All" else int(cpu_count)
            shm_size = f"{128*cpu_count}m"

            # dist_backend = "gloo" if self.windows_os else "nccl"
            # command = ["-c", f"from biapy import BiaPy; BiaPy( '/BiaPy_files/input.yaml', result_dir='{self.output_folder_in_container}', name='{jobname}', run_id=1, dist_backend='{dist_backend}'"]
            # gpus = " "
            # if self.use_gpu:
            #     gpus = self.main_gui.ui.device_input.currentData()
            #     gpus = [int(x[0]) for x in gpus]
            #     gpus = ','.join(str(x) for x in gpus)
            #     command[-1] += f", gpu='{gpus}'"
            # command[-1] += ")"

            # Docker mount points
            volumes = {}
            volumes[real_cfg_input] = {"bind": "/BiaPy_files/input.yaml", "mode": "ro"}
            # To debug with local BiaPy copy
            # volumes["/data/dfranco/BiaPy"] = {"bind": "/installations/BiaPy", "mode": "ro"}
            volumes[str(Path.home())] = {"bind": "/home/user", "mode": "rw"}  # Bind user's home into /home/user
            volumes[self.output_folder_in_host] = {"bind": self.output_folder_in_container, "mode": "rw"}
            paths = []
            paths.append(self.output_folder_in_container)

            mode = "rw" if self.config["PROBLEM"]["TYPE"] in ["INSTANCE_SEG", "DETECTION", "SELF_SUPERVISED"] else "ro"
            paths_message = ""
            if self.config["TRAIN"]["ENABLE"]:  # mirar los paths que se repiten y bindear solo uan vez, si no error
                self.total_epochs = int(self.config["TRAIN"]["EPOCHS"])
                self.gui.run_window.train_progress_bar.setMaximum(self.total_epochs)

                # Train path
                p = os.path.realpath(os.path.join(self.config["DATA"]["TRAIN"]["PATH"], ".."))
                p = path_to_linux(p, self.main_gui.cfg.settings["os_host"])
                if not path_in_list(paths, p):
                    paths.append(p)
                    volumes[p] = {"bind": p, "mode": mode}
                p = path_to_linux(self.config["DATA"]["TRAIN"]["PATH"], self.main_gui.cfg.settings["os_host"])
                temp_cfg["DATA"]["TRAIN"]["PATH"] = p
                paths_message += "<tr><td>Train raw image path  </td><td>{}</td></tr>".format(
                    self.config["DATA"]["TRAIN"]["PATH"]
                )

                # Train GT path
                if self.config["PROBLEM"]["TYPE"] not in ["DENOISING", "CLASSIFICATION", "SELF_SUPERVISED"]:
                    p = os.path.realpath(os.path.join(self.config["DATA"]["TRAIN"]["GT_PATH"], ".."))
                    p = path_to_linux(p, self.main_gui.cfg.settings["os_host"])
                    if not path_in_list(paths, p):
                        paths.append(p)
                        volumes[p] = {"bind": p, "mode": mode}
                    p = path_to_linux(self.config["DATA"]["TRAIN"]["GT_PATH"], self.main_gui.cfg.settings["os_host"])
                    temp_cfg["DATA"]["TRAIN"]["GT_PATH"] = p
                    paths_message += "<tr><td>Train target path  </td><td>{}</td></tr>".format(
                        self.config["DATA"]["TRAIN"]["GT_PATH"]
                    )

                if not self.config["DATA"]["VAL"]["FROM_TRAIN"]:
                    # Val path
                    p = os.path.realpath(os.path.join(self.config["DATA"]["VAL"]["PATH"], ".."))
                    p = path_to_linux(p, self.main_gui.cfg.settings["os_host"])
                    if not path_in_list(paths, p):
                        paths.append(p)
                        volumes[p] = {"bind": p, "mode": mode}
                    p = path_to_linux(self.config["DATA"]["VAL"]["PATH"], self.main_gui.cfg.settings["os_host"])
                    temp_cfg["DATA"]["VAL"]["PATH"] = p
                    paths_message += "<tr><td>Validation raw image path  </td><td>{}</td></tr>".format(
                        self.config["DATA"]["VAL"]["PATH"]
                    )

                    # Val GT path
                    if self.config["PROBLEM"]["TYPE"] not in ["DENOISING", "CLASSIFICATION", "SELF_SUPERVISED"]:
                        p = os.path.realpath(os.path.join(self.config["DATA"]["VAL"]["GT_PATH"], ".."))
                        p = path_to_linux(p, self.main_gui.cfg.settings["os_host"])
                        if not path_in_list(paths, p):
                            paths.append(p)
                            volumes[p] = {"bind": p, "mode": mode}
                        p = path_to_linux(self.config["DATA"]["VAL"]["GT_PATH"], self.main_gui.cfg.settings["os_host"])
                        temp_cfg["DATA"]["VAL"]["GT_PATH"] = p
                        paths_message += "<tr><td>Validation target path  </td><td>{}</td></tr>".format(
                            self.config["DATA"]["VAL"]["GT_PATH"]
                        )
            else:
                self.gui.run_window.train_progress_label.setVisible(False)
                self.gui.run_window.train_progress_bar.setVisible(False)
                self.gui.run_window.train_epochs_label.setVisible(False)
            if self.config["TEST"]["ENABLE"] and not self.config["DATA"]["TEST"]["USE_VAL_AS_TEST"]:
                # Test path
                p = os.path.realpath(os.path.join(self.config["DATA"]["TEST"]["PATH"], ".."))
                p = path_to_linux(p, self.main_gui.cfg.settings["os_host"])
                if not path_in_list(paths, p):
                    paths.append(p)
                    volumes[p] = {"bind": p, "mode": mode}
                p = path_to_linux(self.config["DATA"]["TEST"]["PATH"], self.main_gui.cfg.settings["os_host"])
                temp_cfg["DATA"]["TEST"]["PATH"] = p
                paths_message += "<tr><td>Test raw image path  </td><td>{}</td></tr>".format(
                    self.config["DATA"]["TEST"]["PATH"]
                )

                if self.config["DATA"]["TEST"]["LOAD_GT"] and self.config["PROBLEM"]["TYPE"] not in [
                    "DENOISING",
                    "CLASSIFICATION",
                    "SELF_SUPERVISED",
                ]:
                    # Test GT path
                    p = os.path.realpath(os.path.join(self.config["DATA"]["TEST"]["GT_PATH"], ".."))
                    p = path_to_linux(p, self.main_gui.cfg.settings["os_host"])
                    if not path_in_list(paths, p):
                        paths.append(p)
                        volumes[p] = {"bind": p, "mode": mode}
                    p = path_to_linux(self.config["DATA"]["TEST"]["GT_PATH"], self.main_gui.cfg.settings["os_host"])
                    temp_cfg["DATA"]["TEST"]["GT_PATH"] = p
                    paths_message += "<tr><td>Test target path  </td><td>{}</td></tr>".format(
                        self.config["DATA"]["TEST"]["GT_PATH"]
                    )

            if self.config["MODEL"]["LOAD_CHECKPOINT"]:
                p = os.path.realpath(os.path.join(self.config["PATHS"]["CHECKPOINT_FILE"], ".."))
                p = path_to_linux(p, self.main_gui.cfg.settings["os_host"])
                if not path_in_list(paths, p):
                    paths.append(p)
                    volumes[p] = {"bind": p, "mode": "ro"}
                p = path_to_linux(self.config["PATHS"]["CHECKPOINT_FILE"], self.main_gui.cfg.settings["os_host"])
                if "PATHS" not in temp_cfg:
                    temp_cfg["PATHS"] = {}
                temp_cfg["PATHS"]["CHECKPOINT_FILE"] = p

            if not self.config["TEST"]["ENABLE"]:
                self.gui.run_window.test_progress_label.setVisible(False)
                self.gui.run_window.test_progress_bar.setVisible(False)
                self.gui.run_window.test_files_label.setVisible(False)
            else:
                self.test_files = len(sorted(next(os.walk(self.config["DATA"]["TEST"]["PATH"]))[2]))
                self.gui.run_window.test_progress_bar.setMaximum(self.test_files)

            self.main_gui.logger.info("Creating temporal input YAML file")
            temp_cfg = convert_old_model_cfg_to_current_version(temp_cfg)
            with open(real_cfg_input, "w", encoding="utf8") as outfile:
                yaml.dump(temp_cfg, outfile, default_flow_style=False)

            if self.use_gpu:
                device_requests = [docker.types.DeviceRequest(count=-1, capabilities=[["gpu"]])]
            else:
                device_requests = None

            # Run container
            # check_command = [ "python3", "-u", "-c", "'import torch; print(torch.cuda.is_available())'"]
            self.main_gui.logger.info(f"Command: {command}")
            self.main_gui.logger.info(f"Volumes:  {volumes}")
            self.main_gui.logger.info(f"GPU (IDs): {gpus}")
            self.main_gui.logger.info(f"CPUs: {cpu_count}")
            self.main_gui.logger.info(f"GUI version: {self.main_gui.cfg.settings['biapy_gui_version']}")
            nofile_limit = docker.types.Ulimit(name="nofile", soft=10000, hard=10000)

            self.biapy_container = self.docker_client.containers.run(
                self.container_name,
                # entrypoint=[ "/bin/bash", "-l", "-c" ],
                command=command,
                detach=True,
                volumes=volumes,
                user=self.user_host if not self.windows_os else None,
                device_requests=device_requests,
                shm_size=shm_size,
                ulimits=[nofile_limit],
                nano_cpus=1000000000 * cpu_count,
                cpu_count=cpu_count,
            )

            self.process_steps = "running"
            self.main_gui.logger.info("Container created!")

            workflow_name = self.main_gui.cfg.settings["workflow_names"][
                self.main_gui.cfg.settings["workflow_key_names"].index(self.config["PROBLEM"]["TYPE"])
            ]
            workflow_name = workflow_name.replace("\n", " ")
            # Set the window header
            try:
                bmz_export_enabled = self.config["MODEL"]["BMZ"]["EXPORT"]["ENABLE"]
            except:
                bmz_export_enabled = False

            if bmz_export_enabled:
                bmz_message = "<tr><td>BioImage Model Zoo file folder</td><td><a href={}>{}</a></td></tr>".format(
                    bytearray(QUrl.fromLocalFile(self.container_bmz_folder).toEncoded()).decode(), # type: ignore
                    self.container_bmz_folder,
                )
            else:
                bmz_message = ""

            self.container_info = "<b>BiaPy container ({} - ID: {})</b><br>\
            <table>\
                <tr><td>Start date</td><td>{}</td></tr>\
                <tr><td>Jobname</td><td>{}</td></tr>\
                <tr><td>YAML</td><td><a href={}>{}</a></td></tr>\
                <tr><td>Device</td><td>{}</td></tr>\
                <tr><td>Output folder</td><td><a href={}>{}</a></td></tr>\
                <tr><td>Training plots folder</td><td><a href={}>{}</a></td></tr>\
                {}\
                <tr><td>Output log</td><td><a href={}>{}</a></td></tr>\
                <tr><td>Error log</td><td><a href={}>{}</a></td></tr>\
                {}\
            </table>".format(
                str(self.biapy_container.image).replace("<", "").replace(">", ""),
                self.biapy_container.short_id,
                now.strftime("%Y/%m/%d %H:%M:%S"),
                jobname + " (" + self.config["PROBLEM"]["NDIM"] + " " + workflow_name + ")",
                bytearray(QUrl.fromLocalFile(get_text(self.main_gui.ui.select_yaml_name_label)).toEncoded()).decode(), # type: ignore
                get_text(self.main_gui.ui.select_yaml_name_label),
                device,
                bytearray(QUrl.fromLocalFile(container_out_dir_in_host).toEncoded()).decode(), # type: ignore
                container_out_dir_in_host,
                bytearray(QUrl.fromLocalFile(self.container_plots_folder).toEncoded()).decode(), # type: ignore
                self.container_plots_folder,
                bmz_message,
                bytearray(QUrl.fromLocalFile(self.container_stdout_file).toEncoded()).decode(), # type: ignore
                self.container_stdout_file,
                bytearray(QUrl.fromLocalFile(self.container_stderr_file).toEncoded()).decode(), # type: ignore
                self.container_stderr_file,
                paths_message,
            )
            self.update_log_signal.emit(0)

            # Log the output in a file
            f = open(self.container_stderr_file, "x", encoding="utf8")
            f.close()
            f = open(self.container_stdout_file, "w", encoding="utf8")
            f.write("#########################################################\n")
            f.write(
                self.container_info.replace("<tr><td>", "")
                .replace("</td><td>", ": ")
                .replace("</td></tr>", "")
                .replace("<table>", "\n")
                .replace("</table>", "\n")
                .replace("<b>", "")
                .replace("</b>", "")
                .replace("<br>", "")
                .strip()
            )
            f.write("#########################################################\n")
            f.write(f"Command: {command}")
            f.write("#########################################################\n")
            f.write(f"Volumes: {volumes}")
            f.write("#########################################################\n")
            f.write(f"GUI version: {self.main_gui.cfg.settings['biapy_gui_version']}")
            if self.use_gpu:
                f.write(f"GPU: {gpus}")
            f.write(f"CPUs: {cpu_count}")
            f.write("#########################################################\n")

            # Collect the output of the container and update the GUI
            last_write = datetime.now()
            self.epoch_count = 0
            self.test_image_count = 0
            start_test = False
            for log in self.biapy_container.logs(stream=True):
                l = log.decode("utf-8")
                try:
                    self.main_gui.logger.info(l.encode("utf-8") if self.windows_os else l)
                except:
                    pass
                try:
                    f.write(l)
                    f.flush()
                except:
                    pass

                # Update training progress bar
                if (
                    self.config["TRAIN"]["ENABLE"]
                    and "Epoch {}/{}".format(self.epoch_count + 1, self.total_epochs) in l
                ):
                    self.epoch_count += 1
                    self.update_train_progress_signal.emit(self.epoch_count)

                # Activate test phase. This is used to not let the test if below check if "Processing .." string is in the log output
                # continuously and reduce the computation.
                if "#  INFERENCE  #" in l:
                    start_test = True
                    self.gui.run_window.test_progress_label.setEnabled(True)
                    self.gui.run_window.test_progress_bar.setEnabled(True)
                    self.gui.run_window.test_files_label.setEnabled(True)
                    if self.config["TRAIN"]["ENABLE"]:
                        self.gui.run_window.train_progress_label.setEnabled(False)
                        self.gui.run_window.train_progress_bar.setEnabled(False)
                        self.gui.run_window.train_epochs_label.setEnabled(False)

                # Update test progress bar
                if (
                    self.config["TEST"]["ENABLE"]
                    and start_test
                    and self.test_image_count < self.test_files
                    and "Processing image: " in l
                ):
                    self.test_image_count += 1
                    self.update_test_progress_signal.emit(self.test_image_count)

                if datetime.now() - last_write > timedelta(seconds=3):
                    self.update_log_signal.emit(1)
                    last_write = datetime.now()

            self.update_log_signal.emit(1)

            if self.config["TEST"]["ENABLE"]:
                self.gui.run_window.test_progress_label.setEnabled(False)
                self.gui.run_window.test_progress_bar.setEnabled(False)
                self.gui.run_window.test_files_label.setEnabled(False)
            self.process_steps = "finished"
            f.close()
            self.finished_signal.emit()
        except:
            # Print first the traceback (only visible through terminal)
            self.main_gui.logger.error(traceback.format_exc())
            # Try to log the error in the error file
            ferr = open(self.container_stderr_file, "w", encoding="utf8")
            ferr.write("#########################################################\n")
            ferr.write(self.container_info + "\n")
            ferr.write("#########################################################\n")
            ferr.write(traceback.format_exc())
            ferr.close()
            if f is not None:
                f.close()
            self.finished_signal.emit()
