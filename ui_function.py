import os
import multiprocessing
from datetime import datetime
import GPUtil
import docker
import traceback
import requests
from typing import (
    List,
)

from PySide6.QtWidgets import QStyle, QLabel, QFrame, QHBoxLayout, QSpacerItem, QSizePolicy, QVBoxLayout
from PySide6.QtCore import QSize, QThread
from PySide6.QtGui import (
    QFont,
    QIcon,
    QPixmap,
    QStandardItem,
    QStandardItemModel,
)

from main import MainWindow
from run_functions import run_worker
from ui_utils import (
    get_text,
    resource_path,
    load_yaml_config,
    change_wizard_page,    
    set_text,
    is_path_exists_or_creatable,
    check_supported_container_versions,
)


class UIFunction:
    def __init__(self, main_window: MainWindow):
        self.main_window = main_window

    def initStackTab(self):
        """
        Initialize GUI.
        """
        if not self.main_window.cfg.settings["init"]:
            self.main_window.ui.stackedWidget.setCurrentWidget(self.main_window.ui.page_home)
            self.main_window.ui.frame_home.setStyleSheet("background:rgb(255,255,255)")

            self.main_window.ui.biapy_logo_label.setPixmap(
                QPixmap(resource_path(os.path.join("images", "biapy_logo.png")))
            )
            self.main_window.ui.bn_close.setIcon(
                self.main_window.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarCloseButton)
            )
            self.main_window.ui.bn_min.setIcon(
                self.main_window.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarMinButton)
            )

            style_bns = """
            QPushButton {
                border: none;
                background-color: rgba(0,0,0,0);
            }
            QPushButton:hover {
                background-color: rgb(255,255,255);
            }
            QPushButton:pressed {	
                background-color: rgb(255,255,255);
            }
            """
            self.main_window.ui.bn_home.setIcon(QPixmap(resource_path(os.path.join("images", "bn_images", "home.png"))))
            self.main_window.ui.bn_home.setStyleSheet(style_bns)
            self.main_window.ui.bn_wizard.setIcon(
                QPixmap(resource_path(os.path.join("images", "bn_images", "wizard.png")))
            )
            self.main_window.ui.bn_wizard.setStyleSheet(style_bns)
            self.main_window.ui.bn_run_biapy.setIcon(
                QPixmap(resource_path(os.path.join("images", "bn_images", "run.png")))
            )
            self.main_window.ui.bn_run_biapy.setStyleSheet(style_bns)

            self.init_main_page()
            self.oninit_checks()
            self.init_wizard_page()
            self.init_run()

            self.main_window.cfg.settings["init"] = True
            self.main_window.last_selected_workflow = -1

    def oninit_checks(self):
        """
        Initial checks of the GUI. Specifically, Docker installation and GPU are checked.
        """
        # Docker check
        try:
            self.main_window.docker_client = docker.from_env()
            self.main_window.cfg.settings["docker_found"] = True
        except:
            self.main_window.cfg.settings["docker_found"] = False
            self.main_window.logger.info("The following error is expected as Docker has not been found in the system:")
            self.main_window.logger.warning(traceback.format_exc())
            self.main_window.logger.info("Below this point the we expect no more errors!")
        if self.main_window.cfg.settings["docker_found"]:
            self.main_window.ui.docker_status_label.setText("<br>Docker installation found")
            self.main_window.cfg.settings["biapy_container_ready"] = True
            self.main_window.ui.docker_head_label.setText("Docker dependency")

            self.main_window.ui.docker_frame.setStyleSheet(
                "#docker_frame { border: 3px solid green; border-radius: 25px;}\n#docker_frame:disabled {border: 3px solid rgb(169,169,169);}"
            )
        else:
            self.main_window.ui.docker_status_label.setText(
                'Docker installation not found. Follow the \
                    <a href="https://biapy.readthedocs.io/en/latest/get_started/installation.html#docker-installation/">documentation</a> to install it.'
            )
            self.main_window.ui.docker_head_label.setText("Docker dependency error")
            self.main_window.ui.docker_frame.setStyleSheet(
                "#docker_frame { border: 3px solid red; border-radius: 25px;}\n#docker_frame:disabled {border: 3px solid rgb(169,169,169);}"
            )

        # GPU check
        self.main_window.cfg.settings["GPUs"] = []
        try:
            self.main_window.cfg.settings["GPUs"] = GPUtil.getGPUs()

            # Always select the last docker container for now
            pos = -1
            if len(self.main_window.cfg.settings["GPUs"]) > 0:
                driver_version = float(".".join(self.main_window.cfg.settings["GPUs"][0].driver.split(".")[:2]))
                print(f"Driver_version found: {driver_version}")
                # for i in range(len(main_window.cfg.settings["NVIDIA_driver_list"])):
                #     pos = i
                #     if driver_version < main_window.cfg.settings["NVIDIA_driver_list"][i]:
                #         break

            pos = -1
            self.main_window.cfg.settings["CUDA_selected"] = str(self.main_window.cfg.settings["CUDA_version"][pos])
            self.main_window.cfg.settings["biapy_container_size"] = self.main_window.cfg.settings["biapy_container_sizes"][pos]

        except Exception as gpu_check_error:
            self.main_window.cfg.settings["GPUs"] = []
            self.main_window.logger.warning(f"ERROR during driver check: {gpu_check_error}")

        if len(self.main_window.cfg.settings["GPUs"]) > 0:
            if len(self.main_window.cfg.settings["GPUs"]) == 1:
                self.main_window.ui.gpu_status_label.setText("1 NVIDIA GPU card found")
            else:
                self.main_window.ui.gpu_status_label.setText(
                    "{} NVIDIA GPU cards found".format(len(self.main_window.cfg.settings["GPUs"]))
                )
            self.main_window.ui.gpu_head_label.setText("GPU dependency")
            self.main_window.ui.gpu_frame.setStyleSheet(
                "#gpu_frame { border: 3px solid green; border-radius: 25px;}\n#gpu_frame:disabled {border: 3px solid rgb(169,169,169);}"
            )
        else:
            self.main_window.ui.gpu_status_label.setText(
                "No NVIDIA GPU card was found. BiaPy will run on the CPU, which is much slower!"
            )
            self.main_window.ui.gpu_head_label.setText("GPU dependency error")
            self.main_window.ui.gpu_frame.setStyleSheet(
                "#gpu_frame { border: 3px solid red; border-radius: 25px;}\n#gpu_frame:disabled {border: 3px solid rgb(169,169,169);}"
            )


    ###########
    # Home page
    ###########
    def init_main_page(self):
        """
        Initialize main page.
        """
        font = QFont()
        font.setFamily("DejaVu Math TeX Gyre")
        font.setPointSize(12)

        self.main_window.ui.biapy_github_bn.setIcon(
            QPixmap(resource_path(os.path.join("images", "bn_images", "github_icon.svg")))
        )
        self.main_window.ui.biapy_github_bn.setIconSize(QSize(40, 40))
        self.main_window.ui.biapy_forum_bn.setIcon(
            QPixmap(resource_path(os.path.join("images", "bn_images", "forum_icon.svg")))
        )
        self.main_window.ui.biapy_forum_bn.setIconSize(QSize(40, 40))
        self.main_window.ui.biapy_templates_bn.setIcon(
            QPixmap(resource_path(os.path.join("images", "bn_images", "template_icon.svg")))
        )
        self.main_window.ui.biapy_templates_bn.setIconSize(QSize(40, 40))
        self.main_window.ui.biapy_doc_bn.setIcon(
            QPixmap(resource_path(os.path.join("images", "bn_images", "doc_icon.svg")))
        )
        self.main_window.ui.biapy_doc_bn.setIconSize(QSize(40, 40))
        self.main_window.ui.biapy_notebooks_bn.setIcon(
            QPixmap(resource_path(os.path.join("images", "bn_images", "notebook_icon.svg")))
        )
        self.main_window.ui.biapy_notebooks_bn.setIconSize(QSize(40, 40))
        self.main_window.ui.biapy_citation_bn.setIcon(
            QPixmap(resource_path(os.path.join("images", "bn_images", "citation_icon.svg")))
        )
        self.main_window.ui.biapy_citation_bn.setIconSize(QSize(31, 31))
        self.main_window.ui.docker_logo.setPixmap(QPixmap(resource_path(os.path.join("images", "docker_logo.svg"))))
        self.main_window.ui.gpu_icon_label.setPixmap(QPixmap(resource_path(os.path.join("images", "gpu_icon.svg"))))
        self.main_window.ui.biapy_version.setText(
            f"Version {self.main_window.cfg.settings['biapy_code_version']} - GUI: {self.main_window.cfg.settings['biapy_gui_version']}"
        )

    ###############
    # Wizard page
    ###############
    def init_wizard_page(self):
        """
        Initialize wizard page.
        """
        self.main_window.ui.wizard_start_wizard_icon.setPixmap(self.main_window.cfg.settings["wizard_img"])
        # self.main_window.cfg.settings["wizard_animation_img"].setScaledSize(QSize(self.main_window.ui.wizard_question_wizard_icon.width(), self.main_window.ui.wizard_question_wizard_icon.height()))

        def update_ani():
            self.main_window.ui.wizard_question_wizard_icon.setIcon(
                QIcon(self.main_window.cfg.settings["wizard_animation_img"].currentPixmap())
            )
            self.main_window.ui.main_window_wizard_question_wizard_icon.setIcon(
                QIcon(self.main_window.cfg.settings["wizard_animation_img"].currentPixmap())
            )

        self.main_window.cfg.settings["wizard_animation_img"].start()
        self.main_window.cfg.settings["wizard_animation_img"].frameChanged.connect(update_ani)
        self.main_window.ui.wizard_question_wizard_icon.setIcon(
            self.main_window.cfg.settings["wizard_animation_img"].currentPixmap()
        )
        self.main_window.ui.main_window_wizard_question_wizard_icon.setIcon(
            self.main_window.cfg.settings["wizard_animation_img"].currentPixmap()
        )

        self.main_window.wizard_toc_model = QStandardItemModel()
        self.configure_from_list(self.main_window.wizard_toc_model, self.main_window.cfg.settings["wizard_sections"])
        self.main_window.ui.wizard_treeView.setModel(self.main_window.wizard_toc_model)
        self.main_window.ui.wizard_treeView.expandAll()
        self.main_window.ui.wizard_treeView.selectionModel()
        self.main_window.ui.wizard_treeView.setCurrentIndex(self.main_window.wizard_toc_model.item(0).child(0).index())
        self.main_window.ui.wizard_treeView.selectionModel().selectionChanged.connect(
            lambda: change_wizard_page(
                self.main_window, self.main_window.cfg.settings["wizard_question_index"], based_on_toc=True
            )
        )

        # Set TOC item visibility
        for i, vis in enumerate(self.main_window.cfg.settings["wizard_question_visible"]):
            vis = self.main_window.cfg.settings["wizard_question_visible"][i]
            index_in_toc = self.main_window.cfg.settings["wizard_from_question_index_to_toc"][i]
            self.main_window.ui.wizard_treeView.setRowHidden(
                index_in_toc[1], self.main_window.wizard_toc_model.index(index_in_toc[0], 0), not vis
            )

        self.main_window.ui.wizard_path_input_frame.setVisible(False)
        self.main_window.ui.wizard_question_answer.setVisible(True)
        self.main_window.ui.wizard_model_input_frame.setVisible(False)

        set_text(
            self.main_window.ui.wizard_data_checked_label,
            "<span style='color:#ff3300'><span style='font-size:16pt;'>&larr;</span> Data not checked yet!</span>",
        )

        # Create summary page
        self.main_window.question_cards = []
        font7 = QFont()
        font7.setFamily("DejaVu Math TeX Gyre")
        font7.setBold(False)
        font7.setItalic(True)
        font8 = QFont()
        font8.setFamily("DejaVu Math TeX Gyre")
        font8.setPointSize(11)

        for i in range(len(self.main_window.cfg.settings["wizard_questions"])):
            self.main_window.question_cards.append({})

            self.main_window.question_cards[i][f"summary_question_frame_{i}"] = QFrame(
                self.main_window.ui.scrollAreaWidgetContents_23
            )
            self.main_window.question_cards[i][f"summary_question_frame_{i}"].setObjectName(
                f"summary_question_frame_{i}"
            )
            self.main_window.question_cards[i][f"summary_question_frame_{i}"].setMinimumSize(QSize(700, 100))
            self.main_window.question_cards[i][f"summary_question_frame_{i}"].setMaximumSize(QSize(700, 9999))
            self.main_window.question_cards[i][f"verticalLayout_61{i}"] = QVBoxLayout(
                self.main_window.question_cards[i][f"summary_question_frame_{i}"]
            )
            self.main_window.question_cards[i][f"verticalLayout_61{i}"].setObjectName(f"verticalLayout_61{i}")
            self.main_window.question_cards[i][f"summary_question_text_frame{i}"] = QFrame(
                self.main_window.question_cards[i][f"summary_question_frame_{i}"]
            )
            self.main_window.question_cards[i][f"summary_question_text_frame{i}"].setObjectName(
                f"summary_question_text_frame{i}"
            )
            self.main_window.question_cards[i][f"summary_question_text_frame{i}"].setFrameShape(QFrame.NoFrame)
            self.main_window.question_cards[i][f"summary_question_text_frame{i}"].setFrameShadow(QFrame.Raised)
            self.main_window.question_cards[i][f"horizontalLayout_45{i}"] = QHBoxLayout(
                self.main_window.question_cards[i][f"summary_question_text_frame{i}"]
            )
            self.main_window.question_cards[i][f"horizontalLayout_45{i}"].setObjectName(f"horizontalLayout_45{i}")
            self.main_window.question_cards[i][f"summary_question_text_bullet{i}"] = QLabel(
                self.main_window.question_cards[i][f"summary_question_text_frame{i}"]
            )
            self.main_window.question_cards[i][f"summary_question_text_bullet{i}"].setObjectName(
                f"summary_question_text_bullet{i}"
            )
            self.main_window.question_cards[i][f"summary_question_text_bullet{i}"].setMinimumSize(QSize(20, 20))
            self.main_window.question_cards[i][f"summary_question_text_bullet{i}"].setMaximumSize(QSize(20, 20))
            self.main_window.question_cards[i][f"summary_question_text_bullet{i}"].setStyleSheet(
                "background-color: rgb(64,144,253);\n"
            )
            self.main_window.question_cards[i][f"horizontalLayout_45{i}"].addWidget(
                self.main_window.question_cards[i][f"summary_question_text_bullet{i}"]
            )
            self.main_window.question_cards[i][f"summary_question_text{i}"] = QLabel(
                self.main_window.question_cards[i][f"summary_question_text_frame{i}"]
            )
            self.main_window.question_cards[i][f"summary_question_text{i}"].setObjectName(f"summary_question_text{i}")
            self.main_window.question_cards[i][f"summary_question_text{i}"].setFont(font7)
            self.main_window.question_cards[i][f"summary_question_text{i}"].setStyleSheet(
                "color: rgb(120,120,120);\nfont: italic;"
            )
            self.main_window.question_cards[i][f"summary_question_text{i}"].setWordWrap(True)
            self.main_window.question_cards[i][f"horizontalLayout_45{i}"].addWidget(
                self.main_window.question_cards[i][f"summary_question_text{i}"]
            )
            self.main_window.question_cards[i][f"verticalLayout_61{i}"].addWidget(
                self.main_window.question_cards[i][f"summary_question_text_frame{i}"]
            )
            self.main_window.question_cards[i][f"summary_question_text_answer_{i}"] = QLabel(
                self.main_window.question_cards[i][f"summary_question_frame_{i}"]
            )
            self.main_window.question_cards[i][f"summary_question_text_answer_{i}"].setObjectName(
                f"summary_question_text_answer_{i}"
            )
            self.main_window.question_cards[i][f"summary_question_text_answer_{i}"].setFont(font8)
            self.main_window.question_cards[i][f"summary_question_text_answer_{i}"].setWordWrap(True)
            self.main_window.question_cards[i][f"summary_question_text_answer_{i}"].setIndent(45)
            self.main_window.question_cards[i][f"verticalLayout_61{i}"].addWidget(
                self.main_window.question_cards[i][f"summary_question_text_answer_{i}"]
            )
            self.main_window.ui.verticalLayout_62.addWidget(
                self.main_window.question_cards[i][f"summary_question_frame_{i}"]
            )

        self.main_window.ui.verticalSpacer_60 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.main_window.ui.verticalLayout_62.addItem(self.main_window.ui.verticalSpacer_60)

    def configure_from_list(self, model: QStandardItemModel, _list: List):
        """
        Initialize QStandardItemModel ``model`` with ``_list`` list items. This function is not recursive and only
        can handle depth 1 lists.

        Parameters
        ----------
        model : QStandardItemModel
            Model to be filled with items from ``_list``.

        _list : list of list of list
            List of objects to fill the model with.
        """
        parent_item = model.invisibleRootItem()
        for line in _list:
            item = QStandardItem()
            item.setText(line[0])
            item.setEditable(False)
            item.setSelectable(False)
            parent_item.appendRow(item)

            # Add subchilds if any
            if len(line) > 1 and isinstance(line[1], list) and len(line[1]) > 0:
                for x in line[1]:
                    subitem = QStandardItem()
                    subitem.setText(x)
                    subitem.setEditable(False)
                    item.appendRow(subitem)

    def display_wizard_help_window(self):
        """
        Starts workflow description page.
        """
        # Load first time
        self.main_window.basic_dialog_exec(
            self.main_window.cfg.settings["wizard_question_additional_info"][
                self.main_window.cfg.settings["wizard_question_index"]
            ]
        )

    def init_run(self):
        """
        Initialize run page.
        """
        # Fill device input field
        self.main_window.ui.device_input.addItem("CPU")
        if len(self.main_window.cfg.settings["GPUs"]) > 0:
            for i, gpu in enumerate(self.main_window.cfg.settings["GPUs"]):
                self.main_window.ui.device_input.addItem("GPU {} : {} ".format(i, gpu.name))

        supported_versions = check_supported_container_versions(
            self.main_window.cfg.settings["biapy_gui_version"], self.main_window.logger
        )

        # Set at least the base version that this GUI supports
        if len(supported_versions) == 0:
            self.main_window.logger.info(
                "No BiaPy compatible containers found in the landing page. Setting the default one {}".format(
                    self.main_window.cfg.settings["biapy_code_version"]
                )
            )
            supported_versions = [self.main_window.cfg.settings["biapy_code_version"]]
        else:
            found_ge_version = False
            for ver in supported_versions:
                if ver >= self.main_window.cfg.settings["biapy_code_version"]:
                    found_ge_version = True
            if found_ge_version:
                self.main_window.logger.info("Compatible containers found: {}".format(supported_versions))
            else:
                supported_versions = [self.main_window.cfg.settings["biapy_code_version"]]
                self.main_window.logger.info(
                    "Containers in the landing page seem to be older than the default (contact BiaPy team so the can fix that in the website). Using the default container version: {}".format(
                        supported_versions
                    )
                )

        self.main_window.ui.container_input.addItem(f"{supported_versions[0]}")
        if len(supported_versions) > 1:
            for cont_version in range(1, len(supported_versions)):
                self.main_window.ui.container_input.addItem("{}".format(supported_versions[cont_version]))

        self.main_window.ui.SYSTEM__NUM_CPUS__INPUT.addItem("All")
        cpu_count = multiprocessing.cpu_count()
        for i in range(cpu_count):
            self.main_window.ui.SYSTEM__NUM_CPUS__INPUT.addItem(str(i + 1))
            
        self.main_window.ui.SYSTEM__NUM_WORKERS__INPUT.addItem("0")
        for i in range(min(cpu_count, 10)):
            self.main_window.ui.SYSTEM__NUM_WORKERS__INPUT.addItem(str(i + 1))
        self.main_window.ui.SYSTEM__NUM_WORKERS__INPUT.setCurrentText("2")

    def update_container_status_in_build(self, signal: int):
        """
        Updates container status during its building process.

        Parameters
        ----------
        signal : int
            Signal from the bulding process thread.
        """
        # If the container was built correctly
        if signal == 0:
            self.main_window.cfg.settings["biapy_container_ready"] = True
            self.main_window.ui.docker_head_label.setText("Dependencies")
            self.main_window.ui.docker_frame.setStyleSheet("")

    def run_biapy(self):
        """
        Run BiaPy container in a different thread.
        """
        # Load the YAML file selected
        r = load_yaml_config(self.main_window)
        if not r:
            return

        # Job name check
        jobname = get_text(self.main_window.ui.job_name_input)
        if jobname == "":
            self.main_window.dialog_exec("Job name can not be empty", "jobname")
            return

        # Output folder check
        if self.main_window.cfg.settings["output_folder"] == "":
            self.main_window.dialog_exec("Output folder must be defined", "output_folder")
            return
        if not is_path_exists_or_creatable(self.main_window.cfg.settings["job_real_output_path"]):
            self.main_window.dialog_exec(
                "Job results folder is invalid. Please set a valid path within your system.", "output_folder"
            )
            return
        if os.path.exists(self.main_window.cfg.settings["job_real_output_path"]):
            new_jobname = jobname + "_" + datetime.now().strftime("%Y%m%d_%H_%M_%S")
            self.main_window.yes_no_exec(
                "Job results folder already exists. Do you want to change it to '{}' to avoid overwriting?".format(
                    new_jobname
                )
            )
            assert self.main_window.yes_no
            if self.main_window.yes_no.answer:
                self.main_window.ui.job_name_input.setPlainText(new_jobname)

        # Docker installation check
        if not self.main_window.cfg.settings["docker_found"]:
            self.main_window.dialog_exec(
                'Docker installation not found. Please, install it before running BiaPy in its\
                    <a href="https://docs.docker.com/get-docker/">official documentation</a>. Once you have \
                    done that please restart this application.',
                "docker_installation",
            )
            return
        if not self.main_window.cfg.settings["biapy_container_ready"]:
            self.main_window.dialog_exec(
                "You need to build BiaPy's container first. You will be redirected yo the main page "
                "so you can do it.",
                "docker_installation",
            )
            return

        # Device selection
        device = get_text(self.main_window.ui.device_input)
        use_gpu = True if "GPU" in device else False

        # Set the container name
        container_version_selected = get_text(self.main_window.ui.container_input)
        self.main_window.cfg.settings["biapy_container_name"] = (
            self.main_window.cfg.settings["biapy_container_basename"]
            + ":"
            + container_version_selected
            + "-"
            + str(self.main_window.cfg.settings["CUDA_selected"])
        )

        # Check if a pull is necessary
        local_images = self.main_window.docker_client.images.list()
        local_biapy_image_tag = ""
        local_biapy_container_found = False
        if len(local_images) > 0:
            # Capture local BiaPy image
            for i in range(len(local_images)):
                if len(local_images[i].attrs.get("RepoTags")) > 0:
                    if (
                        local_images[i].attrs.get("RepoTags")[0]
                        == self.main_window.cfg.settings["biapy_container_name"]
                    ):
                        # local_biapy_container_found = True # Activate this when locally want to try new BiaPy code
                        if len(local_images[i].attrs.get("RepoDigests")) > 0:
                            local_biapy_image_tag = (
                                local_images[i].attrs.get("RepoDigests")[0].replace("biapyx/biapy@", "")
                            )

            res = requests.get("https://registry.hub.docker.com/v2/repositories/biapyx/biapy/tags/")
            res = res.json()
            dockerhub_image_tag = ""
            for i in range(len(res["results"])):
                if res["results"][i]["name"] == self.main_window.cfg.settings["biapy_container_name"].split(":")[-1]:
                    dockerhub_image_tag = res["results"][i]["images"][0]["digest"]

            # Replace BiaPy container
            if dockerhub_image_tag != "" and local_biapy_image_tag != "":
                if dockerhub_image_tag != local_biapy_image_tag:
                    self.main_window.yes_no_exec(
                        "There is another BiaPy container ('{}'). Do yo want to remove the current one to "
                        "save disk space?".format(self.main_window.cfg.settings["biapy_container_name"])
                    )
                    assert self.main_window.yes_no
                    if self.main_window.yes_no.answer:
                        self.main_window.logger.info("Removing last valid container")
                        self.main_window.docker_client.images.remove(
                            self.main_window.cfg.settings["biapy_container_name"], force=True
                        )

        # First time
        run_biapy_cond = True
        if local_biapy_image_tag == "":
            if not local_biapy_container_found:
                self.main_window.yes_no_exec(
                    f"Container version '{container_version_selected}' not found. You will need to download "
                    + "it (in the future, if you reuse it, downloading won't be required). This will require approximately 12GB ".format(
                        self.main_window.cfg.settings["biapy_container_size"]
                    )
                    + "of disk space. Would you like to proceed?"
                )
            else:
                self.main_window.yes_no_exec(
                    "Seems that there is an existing BiaPy container locally built ({}). Do you want to continue?".format(
                        self.main_window.cfg.settings["biapy_container_name"]
                    )
                )
            assert self.main_window.yes_no
            run_biapy_cond = self.main_window.yes_no.answer

        if run_biapy_cond:
            # Initialize thread/worker
            self.main_window.cfg.settings["running_threads"].append(QThread())
            worker_id = len(self.main_window.cfg.settings["running_workers"])
            self.main_window.cfg.settings["running_workers"].append(
                run_worker(
                    self.main_window,
                    self.main_window.cfg.settings["biapy_cfg"],
                    self.main_window.cfg.settings["biapy_container_name"],
                    worker_id,
                    self.main_window.cfg.settings["output_folder"],
                    self.main_window.cfg.settings["user_host"],
                    use_gpu,
                    use_local_biapy_image=local_biapy_container_found,
                )
            )

            # Set up signals so the mainn thread, in charge of updating the GUI, can do it
            self.main_window.cfg.settings["running_workers"][worker_id].moveToThread(
                self.main_window.cfg.settings["running_threads"][worker_id]
            )
            self.main_window.cfg.settings["running_threads"][worker_id].started.connect(
                self.main_window.cfg.settings["running_workers"][worker_id].run
            )
            self.main_window.cfg.settings["running_workers"][worker_id].finished_signal.connect(
                self.main_window.cfg.settings["running_threads"][worker_id].quit
            )
            self.main_window.cfg.settings["running_workers"][worker_id].finished_signal.connect(
                self.main_window.cfg.settings["running_workers"][worker_id].deleteLater
            )
            self.main_window.cfg.settings["running_threads"][worker_id].finished.connect(
                self.main_window.cfg.settings["running_threads"][worker_id].deleteLater
            )
            self.main_window.cfg.settings["running_workers"][worker_id].update_log_signal.connect(
                self.main_window.cfg.settings["running_workers"][worker_id].gui.update_gui
            )
            self.main_window.cfg.settings["running_workers"][worker_id].update_cont_state_signal.connect(
                self.main_window.cfg.settings["running_workers"][worker_id].gui.update_cont_state
            )
            self.main_window.cfg.settings["running_workers"][worker_id].update_train_progress_signal.connect(
                self.main_window.cfg.settings["running_workers"][worker_id].gui.update_train_progress
            )
            self.main_window.cfg.settings["running_workers"][worker_id].update_test_progress_signal.connect(
                self.main_window.cfg.settings["running_workers"][worker_id].gui.update_test_progress
            )
            self.main_window.cfg.settings["running_workers"][worker_id].update_pulling_progress_signal.connect(
                self.main_window.cfg.settings["running_workers"][worker_id].gui.update_pulling_progress
            )
            self.main_window.cfg.settings["running_workers"][worker_id].update_pulling_signal.connect(
                self.main_window.cfg.settings["running_workers"][worker_id].gui.pulling_progress
            )

            # Start thread
            self.main_window.cfg.settings["running_threads"][worker_id].start()
