import os
import multiprocessing
from datetime import datetime
import ast 
from collections import deque
import requests

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtSvg import QSvgWidget

from main import MainWindow
from run_functions import run_worker
from build_functions import build_worker
from ui_utils import get_text, resource_path, oninit_checks, load_yaml_config, change_wizard_page, set_text, is_path_exists_or_creatable
from aux_classes.checkableComboBox import CheckableComboBox

class UIFunction(MainWindow):

    def initStackTab(main_window):
        """
        Initialize GUI. 
        
        Parameters
        ----------
        main_window : QMainWindow
            Main window of the application.
        """
        if not main_window.cfg.settings['init']:
            main_window.ui.stackedWidget.setCurrentWidget(main_window.ui.page_home)
            main_window.ui.frame_home.setStyleSheet("background:rgb(255,255,255)") 
            
            main_window.ui.biapy_logo_label.setPixmap(QPixmap(resource_path(os.path.join("images","biapy_logo.png"))))
            main_window.ui.bn_close.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","close_icon.png"))))
            main_window.ui.bn_min.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","hide_icon.png"))))

            main_window.ui.bn_home.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","home.png"))))
            main_window.ui.bn_wizard.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","wizard.png"))))
            main_window.ui.bn_workflow.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","workflow.png"))))
            main_window.ui.bn_goptions.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","goptions.png"))))
            main_window.ui.bn_train.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","train.png"))))
            main_window.ui.bn_test.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","test.png"))))
            main_window.ui.bn_run_biapy.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","run.png"))))

            main_window.ui.left_arrow_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","left_arrow.svg"))))
            main_window.ui.right_arrow_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","right_arrow.svg"))))
            main_window.ui.goptions_advanced_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","down_arrow.svg"))))
            main_window.ui.train_advanced_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","down_arrow.svg"))))
            main_window.ui.test_advanced_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","down_arrow.svg"))))

            UIFunction.init_main_page(main_window)
            oninit_checks(main_window)
            UIFunction.init_workflow_page(main_window)
            UIFunction.init_wizard_page(main_window)
            UIFunction.init_goptions_page(main_window)
            UIFunction.init_train_page(main_window)
            UIFunction.init_test_page(main_window)
            UIFunction.init_run(main_window)

            main_window.cfg.settings['init'] = True
            main_window.last_selected_workflow = -1

    def obtain_workflow_description(main_window, s_workflow):
        """
        Starts workflow description page. 
                
        Parameters
        ----------
        main_window : QMainWindow
            Main window of the application.
        """
        # Load first time
        if not 'workflow_description_images' in main_window.cfg.settings:
            main_window.cfg.load_workflow_detail_page()

        workflow_name = main_window.cfg.settings['workflow_names'][s_workflow].replace("\n"," ") 
        workflow_images = main_window.cfg.settings['workflow_description_images'][s_workflow]
        workflow_description = main_window.cfg.settings['workflow_descriptions'][s_workflow]
        workflow_ready_examples = main_window.cfg.settings['ready_to_use_workflows'][s_workflow]
        workflow_doc = main_window.cfg.settings['workflow_description_doc'][s_workflow]
        main_window.workflow_info_exec(workflow_name, workflow_images, workflow_description, workflow_doc,
            workflow_ready_examples)

    ###########
    # Home page 
    ###########
    def init_main_page(main_window):
        """
        Initialize main page.
                
        Parameters
        ----------
        main_window : QMainWindow
            Main window of the application.
        """
        font = QFont()
        font.setFamily(u"DejaVu Math TeX Gyre")
        font.setPointSize(12)

        main_window.ui.biapy_github_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","github_icon.svg"))))
        main_window.ui.biapy_github_bn.setIconSize(QSize(40, 40))
        main_window.ui.biapy_forum_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","forum_icon.svg"))))
        main_window.ui.biapy_forum_bn.setIconSize(QSize(40, 40))
        main_window.ui.biapy_templates_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","template_icon.svg"))))
        main_window.ui.biapy_templates_bn.setIconSize(QSize(40, 40))
        main_window.ui.biapy_doc_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","doc_icon.svg"))))
        main_window.ui.biapy_doc_bn.setIconSize(QSize(40, 40))
        main_window.ui.biapy_notebooks_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","notebook_icon.svg"))))
        main_window.ui.biapy_notebooks_bn.setIconSize(QSize(40, 40))
        main_window.ui.biapy_citation_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","citation_icon.svg"))))
        main_window.ui.biapy_citation_bn.setIconSize(QSize(31, 31))

        # Create docker logo and text here. This last is necessary to do it here and not in ui_main.py
        # because they are inserted in order 
        dockerlogo = QFile(resource_path(os.path.join("images","docker_logo.svg")))
        dockerlogo.open(QIODevice.ReadWrite)
        main_window.docker_logo_bytearray_str = dockerlogo.readAll()
        dockerlogo.close()
        main_window.ui.docker_logo = QSvgWidget()
        main_window.ui.docker_logo.setObjectName(u"docker_logo")
        main_window.ui.docker_logo.setMinimumSize(QSize(220, 56))
        main_window.ui.docker_logo.setMaximumSize(QSize(220, 56))
        main_window.ui.docker_logo.load(main_window.docker_logo_bytearray_str)
        main_window.ui.verticalLayout_28.addWidget(main_window.ui.docker_logo, alignment=Qt.AlignCenter)

        main_window.ui.docker_status_label = QLabel(main_window.ui.docker_frame)
        main_window.ui.docker_status_label.setObjectName(u"docker_status_label")
        main_window.ui.docker_status_label.setMinimumSize(QSize(0, 0))
        main_window.ui.docker_status_label.setMaximumSize(QSize(16777215, 16777215))
        main_window.ui.docker_status_label.setFont(font)
        main_window.ui.docker_status_label.setAlignment(Qt.AlignCenter)
        main_window.ui.docker_status_label.setWordWrap(True)
        main_window.ui.docker_status_label.setOpenExternalLinks(True)
        main_window.ui.verticalLayout_28.addWidget(main_window.ui.docker_status_label)

        # GPU logo and text
        gpu_icon = QFile(resource_path(os.path.join("images","gpu_icon.svg")))
        gpu_icon.open(QIODevice.ReadWrite)
        main_window.gpu_icon_bytearray_str = gpu_icon.readAll()
        gpu_icon.close()
        main_window.ui.gpu_icon_label = QSvgWidget()
        main_window.ui.gpu_icon_label.setObjectName(u"gpu_icon_label")
        main_window.ui.gpu_icon_label.setMinimumSize(QSize(122, 80))
        main_window.ui.gpu_icon_label.setMaximumSize(QSize(122, 80))
        main_window.ui.gpu_icon_label.load(main_window.gpu_icon_bytearray_str)
        main_window.ui.verticalLayout_33.addWidget(main_window.ui.gpu_icon_label, alignment=Qt.AlignCenter)

        main_window.ui.gpu_status_label = QLabel(main_window.ui.gpu_frame)
        main_window.ui.gpu_status_label.setObjectName(u"gpu_status_label")
        main_window.ui.gpu_status_label.setMinimumSize(QSize(0, 0))
        main_window.ui.gpu_status_label.setFont(font)
        main_window.ui.gpu_status_label.setAlignment(Qt.AlignCenter)
        main_window.ui.gpu_status_label.setWordWrap(True)
        main_window.ui.gpu_status_label.setOpenExternalLinks(True)
        main_window.ui.verticalLayout_33.addWidget(main_window.ui.gpu_status_label)
        
        main_window.ui.biapy_version.setText(f"Version {main_window.cfg.settings['biapy_code_version']} - GUI: {main_window.cfg.settings['biapy_gui_version']}")

    ###############
    # Wizard page 
    ###############
    def init_wizard_page(main_window):
        """
        Initialize wizard page.
                
        Parameters
        ----------
        main_window : QMainWindow
            Main window of the application.
        """
        main_window.ui.wizard_start_wizard_icon.setPixmap(main_window.cfg.settings['wizard_img'])
        # main_window.cfg.settings["wizard_animation_img"].setScaledSize(QSize(main_window.ui.wizard_question_wizard_icon.width(), main_window.ui.wizard_question_wizard_icon.height()))
        
        def update_ani(self):
            main_window.ui.wizard_question_wizard_icon.setIcon(QIcon(main_window.cfg.settings["wizard_animation_img"].currentPixmap()))
            main_window.ui.main_window_wizard_question_wizard_icon.setIcon(QIcon(main_window.cfg.settings["wizard_animation_img"].currentPixmap()))
            
        main_window.cfg.settings['wizard_animation_img'].start()
        main_window.cfg.settings["wizard_animation_img"].frameChanged.connect(update_ani)
        main_window.ui.wizard_question_wizard_icon.setIcon(main_window.cfg.settings["wizard_animation_img"].currentPixmap())
        main_window.ui.main_window_wizard_question_wizard_icon.setIcon(main_window.cfg.settings["wizard_animation_img"].currentPixmap())

        main_window.wizard_toc_model = QStandardItemModel()
        UIFunction.configure_from_list(main_window.wizard_toc_model, main_window.cfg.settings["wizard_sections"])     
        main_window.ui.wizard_treeView.setModel(main_window.wizard_toc_model)
        main_window.ui.wizard_treeView.expandAll()
        main_window.ui.wizard_treeView.selectionModel()
        main_window.ui.wizard_treeView.setCurrentIndex(main_window.wizard_toc_model.item(0).child(0).index())
        main_window.ui.wizard_treeView.selectionModel().selectionChanged.connect(
            lambda: change_wizard_page(main_window, main_window.cfg.settings['wizard_question_index'], based_on_toc=True))
        
        # Set TOC item visibility 
        for i, vis in enumerate(main_window.cfg.settings['wizard_question_visible']):
            vis = main_window.cfg.settings['wizard_question_visible'][i]
            index_in_toc = main_window.cfg.settings['wizard_from_question_index_to_toc'][i]
            main_window.ui.wizard_treeView.setRowHidden(index_in_toc[1], main_window.wizard_toc_model.index(index_in_toc[0],0), not vis)
                
        main_window.ui.wizard_path_input_frame.setVisible(False)
        main_window.ui.wizard_question_answer.setVisible(True)
        main_window.ui.wizard_model_input_frame.setVisible(False)

        set_text(main_window.ui.wizard_data_checked_label, "<span style='color:#ff3300'><span style='font-size:16pt;'>&larr;</span> Data not checked yet!</span>")
        
        # Create summary page 
        main_window.question_cards = []
        font7 = QFont()
        font7.setFamily(u"DejaVu Math TeX Gyre")
        font7.setBold(False)
        font7.setItalic(True)
        font7.setWeight(50)
        font8 = QFont()
        font8.setFamily(u"DejaVu Math TeX Gyre")
        font8.setPointSize(11)
    
        for i in range(len(main_window.cfg.settings["wizard_questions"])):
            main_window.question_cards.append({})

            main_window.question_cards[i][f"summary_question_frame_{i}"] = QFrame(main_window.ui.scrollAreaWidgetContents_23)
            main_window.question_cards[i][f"summary_question_frame_{i}"].setObjectName(f"summary_question_frame_{i}")
            main_window.question_cards[i][f"summary_question_frame_{i}"].setMinimumSize(QSize(700, 100))
            main_window.question_cards[i][f"summary_question_frame_{i}"].setMaximumSize(QSize(700, 9999))
            main_window.question_cards[i][f"verticalLayout_61{i}"] = QVBoxLayout(main_window.question_cards[i][f"summary_question_frame_{i}"])
            main_window.question_cards[i][f"verticalLayout_61{i}"].setObjectName(f"verticalLayout_61{i}")
            main_window.question_cards[i][f"summary_question_text_frame{i}"] = QFrame(main_window.question_cards[i][f"summary_question_frame_{i}"])
            main_window.question_cards[i][f"summary_question_text_frame{i}"].setObjectName(f"summary_question_text_frame{i}")
            main_window.question_cards[i][f"summary_question_text_frame{i}"].setFrameShape(QFrame.NoFrame)
            main_window.question_cards[i][f"summary_question_text_frame{i}"].setFrameShadow(QFrame.Raised)
            main_window.question_cards[i][f"horizontalLayout_45{i}"] = QHBoxLayout(main_window.question_cards[i][f"summary_question_text_frame{i}"])
            main_window.question_cards[i][f"horizontalLayout_45{i}"].setObjectName(f"horizontalLayout_45{i}")
            main_window.question_cards[i][f"summary_question_text_bullet{i}"] = QLabel(main_window.question_cards[i][f"summary_question_text_frame{i}"])
            main_window.question_cards[i][f"summary_question_text_bullet{i}"].setObjectName(f"summary_question_text_bullet{i}")
            main_window.question_cards[i][f"summary_question_text_bullet{i}"].setMinimumSize(QSize(20, 20))
            main_window.question_cards[i][f"summary_question_text_bullet{i}"].setMaximumSize(QSize(20, 20))
            main_window.question_cards[i][f"summary_question_text_bullet{i}"].setStyleSheet(u"background-color: rgb(64,144,253);\n")
            main_window.question_cards[i][f"horizontalLayout_45{i}"].addWidget(main_window.question_cards[i][f"summary_question_text_bullet{i}"])
            main_window.question_cards[i][f"summary_question_text{i}"] = QLabel(main_window.question_cards[i][f"summary_question_text_frame{i}"])
            main_window.question_cards[i][f"summary_question_text{i}"].setObjectName(f"summary_question_text{i}")
            main_window.question_cards[i][f"summary_question_text{i}"].setFont(font7)
            main_window.question_cards[i][f"summary_question_text{i}"].setStyleSheet(u"color: rgb(120,120,120);\nfont: italic;")
            main_window.question_cards[i][f"summary_question_text{i}"].setWordWrap(True)
            main_window.question_cards[i][f"horizontalLayout_45{i}"].addWidget(main_window.question_cards[i][f"summary_question_text{i}"])
            main_window.question_cards[i][f"verticalLayout_61{i}"].addWidget(main_window.question_cards[i][f"summary_question_text_frame{i}"])
            main_window.question_cards[i][f"summary_question_text_answer_{i}"] = QLabel(main_window.question_cards[i][f"summary_question_frame_{i}"])
            main_window.question_cards[i][f"summary_question_text_answer_{i}"].setObjectName(f"summary_question_text_answer_{i}")
            main_window.question_cards[i][f"summary_question_text_answer_{i}"].setFont(font8)
            main_window.question_cards[i][f"summary_question_text_answer_{i}"].setWordWrap(True)
            main_window.question_cards[i][f"summary_question_text_answer_{i}"].setIndent(45)
            main_window.question_cards[i][f"verticalLayout_61{i}"].addWidget(main_window.question_cards[i][f"summary_question_text_answer_{i}"])
            main_window.ui.verticalLayout_62.addWidget(main_window.question_cards[i][f"summary_question_frame_{i}"])

        main_window.ui.verticalSpacer_60 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        main_window.ui.verticalLayout_62.addItem(main_window.ui.verticalSpacer_60)

    def configure_from_list(model, _list): 
        """
        Initialize QStandardItemModel ``model`` with ``_list`` list items. This function is not recursive and only 
        can handle depth 1 lists.
                
        Parameters
        ----------
        model : QStandardItemModel
            Model to be filled with items from ``_list``. 

        _list : QStandardItemModel
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
        
    def display_wizard_help_window(main_window, question_number):
        """
        Starts workflow description page. 
                
        Parameters
        ----------
        main_window : QMainWindow
            Main window of the application.
        
        question_number: int
            Number of the question.
        """
        # Load first time
        main_window.basic_dialog_exec(main_window.cfg.settings["wizard_question_additional_info"][main_window.cfg.settings['wizard_question_index']])

        # if not 'workflow_description_images' in main_window.cfg.settings:
        #     main_window.cfg.load_workflow_detail_page()

        # workflow_name = main_window.cfg.settings['workflow_names'][s_workflow].replace("\n"," ") 
        # workflow_images = main_window.cfg.settings['workflow_description_images'][s_workflow]
        # workflow_description = main_window.cfg.settings['workflow_descriptions'][s_workflow]
        # workflow_ready_examples = main_window.cfg.settings['ready_to_use_workflows'][s_workflow]
        # workflow_doc = main_window.cfg.settings['workflow_description_doc'][s_workflow]
        # main_window.workflow_info_exec(workflow_name, workflow_images, workflow_description, workflow_doc,
        #     workflow_ready_examples)
        
    ############### 
    # Workflow page 
    ###############
    def init_workflow_page(main_window):
        """
        Initialize workflow page.
                
        Parameters
        ----------
        main_window : QMainWindow
            Main window of the application.
        """
        main_window.ui.workflow_view1_frame.setEnabled(False)
        main_window.ui.workflow_view2_frame.setEnabled(True)
        main_window.ui.workflow_view3_frame.setEnabled(False)
        main_window.ui.workflow_view4_frame.setEnabled(False)
        main_window.ui.workflow_view5_frame.setEnabled(False)
        main_window.ui.workflow_view6_frame.setEnabled(False)
        main_window.ui.workflow_view7_frame.setEnabled(False)
        main_window.ui.workflow_view8_frame.setEnabled(False)

        main_window.workflow_view_queue = deque([1, 2, 3, 4, 5, 6, 7, 8])

        class MouseObserver(QObject):
            def __init__(self, widget, parent):
                super().__init__(widget)
                self._widget = widget
                self.parent = parent
                self.widget.installEventFilter(self)

            @property
            def widget(self):
                return self._widget

            def eventFilter(self, obj, event):
                if obj is self.widget and event.type() == QEvent.MouseButtonPress:
                    post = int(obj.objectName().split('_')[1][-1])
                    left = False if main_window.workflow_view_queue[0] == post else True
                    UIFunction.move_workflow_view(self.parent, left)
                return super().eventFilter(obj, event)

        main_window.observer1 = MouseObserver(main_window.ui.workflow_view1_frame, main_window)
        main_window.observer2 = MouseObserver(main_window.ui.workflow_view2_frame, main_window)
        main_window.observer3 = MouseObserver(main_window.ui.workflow_view3_frame, main_window)
        main_window.observer4 = MouseObserver(main_window.ui.workflow_view4_frame, main_window)
        main_window.observer5 = MouseObserver(main_window.ui.workflow_view5_frame, main_window)
        main_window.observer6 = MouseObserver(main_window.ui.workflow_view6_frame, main_window)
        main_window.observer7 = MouseObserver(main_window.ui.workflow_view7_frame, main_window)
        main_window.observer8 = MouseObserver(main_window.ui.workflow_view8_frame, main_window)

        main_window.cfg.load_workflow_page()
        main_window.ui.workflow_view1_label.setPixmap(main_window.cfg.settings['workflow_images'][0])
        main_window.ui.workflow_view1_name_label.setText(main_window.cfg.settings['workflow_names'][0])
        main_window.ui.workflow_view2_label.setPixmap(main_window.cfg.settings['workflow_images'][1])
        main_window.ui.workflow_view2_name_label.setText(main_window.cfg.settings['workflow_names'][1])
        main_window.ui.workflow_view3_label.setPixmap(main_window.cfg.settings['workflow_images'][2])
        main_window.ui.workflow_view3_name_label.setText(main_window.cfg.settings['workflow_names'][2])
        main_window.ui.workflow_view4_label.setPixmap(main_window.cfg.settings['workflow_images'][3])
        main_window.ui.workflow_view4_name_label.setText(main_window.cfg.settings['workflow_names'][3])
        main_window.ui.workflow_view5_label.setPixmap(main_window.cfg.settings['workflow_images'][4])
        main_window.ui.workflow_view5_name_label.setText(main_window.cfg.settings['workflow_names'][4])
        main_window.ui.workflow_view6_label.setPixmap(main_window.cfg.settings['workflow_images'][5])
        main_window.ui.workflow_view6_name_label.setText(main_window.cfg.settings['workflow_names'][5])
        main_window.ui.workflow_view7_label.setPixmap(main_window.cfg.settings['workflow_images'][6])
        main_window.ui.workflow_view7_name_label.setText(main_window.cfg.settings['workflow_names'][6])
        main_window.ui.workflow_view8_label.setPixmap(main_window.cfg.settings['workflow_images'][7])
        main_window.ui.workflow_view8_name_label.setText(main_window.cfg.settings['workflow_names'][7])

    def move_workflow_view(main_window, isleft):
        main_window.last_selected_workflow = main_window.cfg.settings['selected_workflow']

        first_element_x_pos = 35
        step_x = 305
        first_not_visible_element_x_pos = 950
        x = first_element_x_pos 
        if isleft:            
            while x+step_x > first_element_x_pos:
                for i in range(8):
                    getattr(main_window.ui, f"workflow_view{main_window.workflow_view_queue[i]}_frame").move(x+(step_x*i), 0)
                    getattr(main_window.ui, f"workflow_view{main_window.workflow_view_queue[i]}_frame").repaint()
                x -= 30
            
            item = main_window.workflow_view_queue.popleft()
            main_window.workflow_view_queue.append(item) 
            item = 0
        else: 
            while x < first_not_visible_element_x_pos:
                for i in range(8):
                    getattr(main_window.ui, f"workflow_view{main_window.workflow_view_queue[i]}_frame").move(x+(step_x*i), 0)
                    getattr(main_window.ui, f"workflow_view{main_window.workflow_view_queue[i]}_frame").repaint()
                x += 30
            
            item = main_window.workflow_view_queue.pop()
            main_window.workflow_view_queue.appendleft(item) 
            item = 2

        main_window.cfg.settings['selected_workflow'] = main_window.workflow_view_queue[1]-1

        # Final positions
        for i in range(8):
            getattr(main_window.ui, f"workflow_view{main_window.workflow_view_queue[i]}_frame").move(first_element_x_pos+(step_x*i), 0)
            getattr(main_window.ui, f"workflow_view{main_window.workflow_view_queue[i]}_frame").repaint()
        
        getattr(main_window.ui, f"workflow_view{main_window.workflow_view_queue[1]}_frame").setEnabled(True)
        getattr(main_window.ui, f"workflow_view{main_window.workflow_view_queue[1]}_frame").setStyleSheet(f"#workflow_view{main_window.workflow_view_queue[1]}_frame "+"{\nborder: 5px solid rgb(64,144,253);\nborder-radius: 25px;\n}")
        getattr(main_window.ui, f"workflow_view{main_window.workflow_view_queue[item]}_frame").setEnabled(False)
        getattr(main_window.ui, f"workflow_view{main_window.workflow_view_queue[item]}_frame").setStyleSheet("background:rgb(240,240,240);\nborder-radius: 25px;")

    ######################
    # General options page 
    ######################
    def init_goptions_page(main_window):
        """
        Initialize general options page.
                
        Parameters
        ----------
        main_window : QMainWindow
            Main window of the application.
        """
        main_window.ui.goptions_advanced_options_scrollarea.setVisible(False)

        main_window.ui.MODEL__SOURCE__LABEL.setVisible(False)
        main_window.ui.MODEL__SOURCE__INFO.setVisible(False)
        main_window.ui.MODEL__SOURCE__INPUT.setVisible(False)

        main_window.ui.PATHS__CHECKPOINT_FILE__INPUT.setVisible(False)
        main_window.ui.PATHS__CHECKPOINT_FILE__INFO.setVisible(False)
        main_window.ui.checkpoint_file_path_browse_bn.setVisible(False)
        main_window.ui.checkpoint_file_path_browse_label.setVisible(False)

        main_window.ui.MODEL__BMZ__SOURCE_MODEL_ID__LABEL.setVisible(False)
        main_window.ui.MODEL__BMZ__SOURCE_MODEL_ID__INFO.setVisible(False)
        main_window.ui.MODEL__BMZ__SOURCE_MODEL_ID__INPUT.setVisible(False)
        main_window.ui.MODEL__BMZ__SOURCE_MODEL_ID__BN.setVisible(False)

        main_window.ui.checkpoint_loading_opt_label.setVisible(False)
        main_window.ui.checkpoint_loading_opt_frame.setVisible(False)

        main_window.ui.MODEL__BMZ__EXPORT__REUSE_BMZ_CONFIG__FRAME.setVisible(False)
        main_window.ui.MODEL__BMZ__EXPORT__FRAME.setVisible(False)

        main_window.ui.SYSTEM__NUM_CPUS__INPUT.addItem("All")
        for i in range(multiprocessing.cpu_count()):
            main_window.ui.SYSTEM__NUM_CPUS__INPUT.addItem(str(i+1))

        main_window.ui.SYSTEM__NUM_WORKERS__INPUT.addItem("0")
        for i in range(min(multiprocessing.cpu_count(),10)):
            main_window.ui.SYSTEM__NUM_WORKERS__INPUT.addItem(str(i+1))

        time = datetime.now().strftime("%Y%m%d-%H%M%S")
        main_window.ui.goptions_yaml_name_input.setText("my_experiment_"+get_text(main_window.ui.PROBLEM__NDIM__INPUT)+"_"+time+".yaml")        

    def change_problem_dimensions(main_window, idx):
        """
        Change all variables in GUI that depend on the image dimension selected. E.g. ``2D`` or ``3D``.

        Parameters
        ----------
        main_window : QMainWindow
            Main window of the application.

        idx : int
            Image dimension to work with. If ``0`` means 2D and 3D otherwise. 
        """
        # 2D
        if idx == 0:
            # Only change values the first time and if they were not modified 
            if get_text(main_window.ui.DATA__TEST__RESOLUTION__INPUT) == "":
                main_window.ui.DATA__PATCH_SIZE__INPUT.setText("(256,256,1)")
                main_window.ui.DATA__PATCH_SIZE__TEST__INPUT.setText("(256,256,1)")
                main_window.ui.DATA__TRAIN__RESOLUTION__INPUT.setText("(1,1)")
                main_window.ui.DATA__TRAIN__OVERLAP__INPUT.setText("(0,0)")
                main_window.ui.DATA__TRAIN__PADDING__INPUT.setText("(0,0)")
                main_window.ui.DATA__VAL__RESOLUTION__INPUT.setText("(1,1)")
                main_window.ui.DATA__VAL__OVERLAP__INPUT.setText("(0,0)")
                main_window.ui.DATA__VAL__PADDING__INPUT.setText("(0,0)")
                main_window.ui.DATA__TEST__RESOLUTION__INPUT.setText("(1,1)")
                main_window.ui.DATA__TEST__OVERLAP__INPUT.setText("(0,0)")
                main_window.ui.DATA__TEST__PADDING__INPUT.setText("(32,32)")
                main_window.ui.DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__INPUT.setText("(512,512)")
                main_window.ui.DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__TEST__INPUT.setText("(512,512)")
                main_window.ui.MODEL__FEATURE_MAPS__INPUT.setText("[16, 32, 64, 128, 256]")
                main_window.ui.MODEL__DROPOUT_VALUES__INPUT.setText("[0., 0., 0., 0., 0.]")
            else:
                if get_text(main_window.ui.TRAIN__ENABLE__INPUT) == "Yes":
                    aux = ast.literal_eval(get_text(main_window.ui.DATA__PATCH_SIZE__INPUT) )
                else:
                    aux = ast.literal_eval(get_text(main_window.ui.DATA__PATCH_SIZE__TEST__INPUT) )
                if isinstance(aux, tuple) and aux == (40,128,128,1):
                    main_window.ui.DATA__PATCH_SIZE__INPUT.setText("(256,256,1)")
                    main_window.ui.DATA__PATCH_SIZE__TEST__INPUT.setText("(256,256,1)")
                aux = ast.literal_eval(get_text(main_window.ui.DATA__TRAIN__RESOLUTION__INPUT) )
                if isinstance(aux, tuple) and aux == (1,1,1):
                    main_window.ui.DATA__TRAIN__RESOLUTION__INPUT.setText("(1,1)")
                aux = ast.literal_eval(get_text(main_window.ui.DATA__TRAIN__OVERLAP__INPUT) )
                if isinstance(aux, tuple) and aux == (0,0,0):
                    main_window.ui.DATA__TRAIN__OVERLAP__INPUT.setText("(0,0)")
                aux = ast.literal_eval(get_text(main_window.ui.DATA__TRAIN__PADDING__INPUT) )
                if isinstance(aux, tuple) and aux == (0,0,0):
                    main_window.ui.DATA__TRAIN__PADDING__INPUT.setText("(0,0)")
                aux = ast.literal_eval(get_text(main_window.ui.DATA__VAL__RESOLUTION__INPUT) )
                if isinstance(aux, tuple) and aux == (1,1,1):
                    main_window.ui.DATA__VAL__RESOLUTION__INPUT.setText("(1,1)")
                aux = ast.literal_eval(get_text(main_window.ui.DATA__VAL__OVERLAP__INPUT) )
                if isinstance(aux, tuple) and aux == (0,0,0):
                    main_window.ui.DATA__VAL__OVERLAP__INPUT.setText("(0,0)")
                aux = ast.literal_eval(get_text(main_window.ui.DATA__VAL__PADDING__INPUT) )
                if isinstance(aux, tuple) and aux == (0,0,0):
                    main_window.ui.DATA__VAL__PADDING__INPUT.setText("(0,0)")
                aux = ast.literal_eval(get_text(main_window.ui.DATA__TEST__RESOLUTION__INPUT) )
                if isinstance(aux, tuple) and aux == (1,1,1):
                    main_window.ui.DATA__TEST__RESOLUTION__INPUT.setText("(1,1)")
                aux = ast.literal_eval(get_text(main_window.ui.DATA__TEST__OVERLAP__INPUT) )
                if isinstance(aux, tuple) and aux == (0,0,0):
                    main_window.ui.DATA__TEST__OVERLAP__INPUT.setText("(0,0)")
                aux = ast.literal_eval(get_text(main_window.ui.DATA__TEST__PADDING__INPUT) )
                if isinstance(aux, tuple) and aux == ((5,16,16)):
                    main_window.ui.DATA__TEST__PADDING__INPUT.setText("(32,32)")
                aux = ast.literal_eval(get_text(main_window.ui.DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__INPUT) )
                if isinstance(aux, tuple) and aux == ((512,512,512)):
                    main_window.ui.DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__INPUT.setText("(512,512)")
                aux = ast.literal_eval(get_text(main_window.ui.DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__TEST__INPUT) )
                if isinstance(aux, tuple) and aux == ((512,512,512)):
                    main_window.ui.DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__TEST__INPUT.setText("(512,512)")
                aux = ast.literal_eval(get_text(main_window.ui.MODEL__FEATURE_MAPS__INPUT) )
                if isinstance(aux, list) and aux == [32, 64, 128]:
                    main_window.ui.MODEL__FEATURE_MAPS__INPUT.setText("[16, 32, 64, 128, 256]")
                    aux = ast.literal_eval(get_text(main_window.ui.MODEL__DROPOUT_VALUES__INPUT) )
                    if isinstance(aux, list) and aux == [0., 0., 0.]:
                        main_window.ui.MODEL__DROPOUT_VALUES__INPUT.setText("[0., 0., 0., 0., 0.]")

            main_window.ui.MODEL__Z_DOWN__INPUT.setVisible(False)
            main_window.ui.MODEL__Z_DOWN__LABEL.setVisible(False)
            main_window.ui.MODEL__Z_DOWN__INFO.setVisible(False)
            main_window.ui.da_z_flip_label.setVisible(False)
            main_window.ui.AUGMENTOR__ZFLIP__INFO.setVisible(False)
            main_window.ui.AUGMENTOR__ZFLIP__INPUT.setVisible(False)
            main_window.ui.da_zoom_in_z_label.setVisible(False)
            main_window.ui.AUGMENTOR__ZOOM_IN_Z__INFO.setVisible(False)
            main_window.ui.AUGMENTOR__ZOOM_IN_Z__INPUT.setVisible(False)
            main_window.ui.test_2d_as_3d_stack_label.setVisible(True)
            main_window.ui.TEST__ANALIZE_2D_IMGS_AS_3D_STACK__INPUT.setVisible(True)
            main_window.ui.TEST__ANALIZE_2D_IMGS_AS_3D_STACK__INFO.setVisible(True)
            main_window.ui.test_full_image_label.setVisible(True)
            main_window.ui.TEST__FULL_IMG__INFO.setVisible(True)  
            main_window.ui.TEST__FULL_IMG__INPUT.setVisible(True)  
            main_window.ui.sem_seg_post_proc_frame_label.setVisible(True) 
            main_window.ui.sem_seg_post_proc_frame_label.setVisible(True) 
            if main_window.cfg.settings['selected_workflow'] == 4:
                models = main_window.cfg.settings['sr_2d_models_real_names']

            # Zarr related variables
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False) 
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__INFO.setVisible(False)
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__INPUT.setVisible(False) 
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__LABEL.setVisible(False)
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__INFO.setVisible(False) 
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__INPUT.setVisible(False)
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__LABEL.setVisible(False) 
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__INFO.setVisible(False)
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__INPUT.setVisible(False) 
            main_window.ui.DATA__TRAIN__INPUT_IMG_AXES_ORDER__LABEL.setVisible(False)
            main_window.ui.DATA__TRAIN__INPUT_IMG_AXES_ORDER__INFO.setVisible(False) 
            main_window.ui.DATA__TRAIN__INPUT_IMG_AXES_ORDER__INPUT.setVisible(False)
            main_window.ui.DATA__TRAIN__INPUT_MASK_AXES_ORDER__LABEL.setVisible(False) 
            main_window.ui.DATA__TRAIN__INPUT_MASK_AXES_ORDER__INFO.setVisible(False)
            main_window.ui.DATA__TRAIN__INPUT_MASK_AXES_ORDER__INPUT.setVisible(False) 

            main_window.ui.DATA__VAL__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False) 
            main_window.ui.DATA__VAL__INPUT_ZARR_MULTIPLE_DATA__INFO.setVisible(False)
            main_window.ui.DATA__VAL__INPUT_ZARR_MULTIPLE_DATA__INPUT.setVisible(False) 
            main_window.ui.DATA__VAL__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__LABEL.setVisible(False)
            main_window.ui.DATA__VAL__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__INFO.setVisible(False) 
            main_window.ui.DATA__VAL__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__INPUT.setVisible(False)
            main_window.ui.DATA__VAL__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__LABEL.setVisible(False) 
            main_window.ui.DATA__VAL__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__INFO.setVisible(False)
            main_window.ui.DATA__VAL__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__INPUT.setVisible(False) 
            main_window.ui.DATA__VAL__INPUT_IMG_AXES_ORDER__LABEL.setVisible(False)
            main_window.ui.DATA__VAL__INPUT_IMG_AXES_ORDER__INFO.setVisible(False) 
            main_window.ui.DATA__VAL__INPUT_IMG_AXES_ORDER__INPUT.setVisible(False)
            main_window.ui.DATA__VAL__INPUT_MASK_AXES_ORDER__LABEL.setVisible(False) 
            main_window.ui.DATA__VAL__INPUT_MASK_AXES_ORDER__INFO.setVisible(False)
            main_window.ui.DATA__VAL__INPUT_MASK_AXES_ORDER__INPUT.setVisible(False) 

            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False)
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False) 
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False)
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False) 
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False)
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False) 
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False)
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False) 
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False)
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False) 
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False)
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False) 
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False)
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False) 
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False)
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False) 
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False)
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False) 
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False)
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False) 
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False)
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False) 
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False)
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False) 
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False)
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False) 
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False)
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False) 
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False)
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False) 
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False)
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False) 
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False)
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False) 
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False)
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False) 
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False)
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False) 
            main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__LABEL.setVisible(False)
        # 3D
        else:
            # Only change values the first time and if they were not modified 
            if get_text(main_window.ui.TRAIN__ENABLE__INPUT) == "Yes":
                aux = ast.literal_eval(get_text(main_window.ui.DATA__PATCH_SIZE__INPUT) )
            else:
                aux = ast.literal_eval(get_text(main_window.ui.DATA__PATCH_SIZE__TEST__INPUT) )
            if isinstance(aux, tuple) and aux == (256,256,1):
                main_window.ui.DATA__PATCH_SIZE__INPUT.setText("(40,128,128,1)")
                main_window.ui.DATA__PATCH_SIZE__TEST__INPUT.setText("(40,128,128,1)")
            aux = ast.literal_eval(get_text(main_window.ui.DATA__TRAIN__RESOLUTION__INPUT) )
            if isinstance(aux, tuple) and aux == (1,1):
                main_window.ui.DATA__TRAIN__RESOLUTION__INPUT.setText("(1,1,1)")
            aux = ast.literal_eval(get_text(main_window.ui.DATA__TRAIN__OVERLAP__INPUT) )
            if isinstance(aux, tuple) and aux == (0,0):
                main_window.ui.DATA__TRAIN__OVERLAP__INPUT.setText("(0,0,0)")
            aux = ast.literal_eval(get_text(main_window.ui.DATA__TRAIN__PADDING__INPUT) )
            if isinstance(aux, tuple) and aux == (0,0):
                main_window.ui.DATA__TRAIN__PADDING__INPUT.setText("(0,0,0)")
            aux = ast.literal_eval(get_text(main_window.ui.DATA__VAL__RESOLUTION__INPUT) )
            if isinstance(aux, tuple) and aux == (1,1):
                main_window.ui.DATA__VAL__RESOLUTION__INPUT.setText("(1,1,1)")
            aux = ast.literal_eval(get_text(main_window.ui.DATA__VAL__OVERLAP__INPUT) )
            if isinstance(aux, tuple) and aux == (0,0):
                main_window.ui.DATA__VAL__OVERLAP__INPUT.setText("(0,0,0)")
            aux = ast.literal_eval(get_text(main_window.ui.DATA__VAL__PADDING__INPUT) )
            if isinstance(aux, tuple) and aux == (0,0):
                main_window.ui.DATA__VAL__PADDING__INPUT.setText("(0,0,0)")
            aux = ast.literal_eval(get_text(main_window.ui.DATA__TEST__RESOLUTION__INPUT) )
            if isinstance(aux, tuple) and aux == (1,1):
                main_window.ui.DATA__TEST__RESOLUTION__INPUT.setText("(1,1,1)")
            aux = ast.literal_eval(get_text(main_window.ui.DATA__TEST__OVERLAP__INPUT) )
            if isinstance(aux, tuple) and aux == (0,0):
                main_window.ui.DATA__TEST__OVERLAP__INPUT.setText("(0,0,0)")
            aux = ast.literal_eval(get_text(main_window.ui.DATA__TEST__PADDING__INPUT) )
            if isinstance(aux, tuple) and aux == ((32,32)):
                main_window.ui.DATA__TEST__PADDING__INPUT.setText("(5,16,16)")
            aux = ast.literal_eval(get_text(main_window.ui.DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__INPUT) )
            if isinstance(aux, tuple) and aux == ((512,512)):
                main_window.ui.DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__INPUT.setText("(512,512,512)")
            aux = ast.literal_eval(get_text(main_window.ui.DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__TEST__INPUT) )
            if isinstance(aux, tuple) and aux == ((512,512)):
                main_window.ui.DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__TEST__INPUT.setText("(512,512,512)")
            aux = ast.literal_eval(get_text(main_window.ui.MODEL__FEATURE_MAPS__INPUT) )
            if isinstance(aux, list) and aux == [16, 32, 64, 128, 256]:
                main_window.ui.MODEL__FEATURE_MAPS__INPUT.setText("[32, 64, 128]")
                aux = ast.literal_eval(get_text(main_window.ui.MODEL__DROPOUT_VALUES__INPUT) )
                if isinstance(aux, list) and aux == [0., 0., 0., 0., 0.]:
                    main_window.ui.MODEL__DROPOUT_VALUES__INPUT.setText("[0., 0., 0.]")
                
            main_window.ui.MODEL__Z_DOWN__INPUT.setVisible(True)
            main_window.ui.MODEL__Z_DOWN__LABEL.setVisible(True)
            main_window.ui.MODEL__Z_DOWN__INFO.setVisible(True)
            main_window.ui.da_z_flip_label.setVisible(True)
            main_window.ui.AUGMENTOR__ZFLIP__INFO.setVisible(True)
            main_window.ui.AUGMENTOR__ZFLIP__INPUT.setVisible(True)
            main_window.ui.da_zoom_in_z_label.setVisible(True)
            main_window.ui.AUGMENTOR__ZOOM_IN_Z__INFO.setVisible(True)
            main_window.ui.AUGMENTOR__ZOOM_IN_Z__INPUT.setVisible(True)
            main_window.ui.test_2d_as_3d_stack_label.setVisible(False)
            main_window.ui.TEST__ANALIZE_2D_IMGS_AS_3D_STACK__INPUT.setVisible(False)
            main_window.ui.TEST__ANALIZE_2D_IMGS_AS_3D_STACK__INFO.setVisible(False)
            main_window.ui.test_full_image_label.setVisible(False)
            main_window.ui.TEST__FULL_IMG__INFO.setVisible(False)
            main_window.ui.TEST__FULL_IMG__INPUT.setVisible(False)
            main_window.ui.TEST__FULL_IMG__INPUT.setCurrentText("No") 
            main_window.ui.sem_seg_post_proc_frame_label.setVisible(False) 
            main_window.ui.sem_seg_post_proc_frame_label.setVisible(False) 
            if main_window.cfg.settings['selected_workflow'] == 4:
                models = main_window.cfg.settings['sr_3d_models_real_names']

        if main_window.cfg.settings['selected_workflow'] == 4:
            main_window.ui.MODEL__ARCHITECTURE__INPUT.clear()
            main_window.ui.MODEL__ARCHITECTURE__INPUT.addItems(models)

    ############
    # Train page 
    ############
    def init_train_page(main_window):       
        """
        Initialize train page.
                
        Parameters
        ----------
        main_window : QMainWindow
            Main window of the application.
        """ 
        # Hide validation paths as it is extracted from train by default 
        main_window.ui.DATA__VAL__PATH__LABEL.setVisible(False)
        main_window.ui.DATA__VAL__PATH__INFO.setVisible(False)
        main_window.ui.DATA__VAL__PATH__INPUT.setVisible(False)
        main_window.ui.val_data_input_browse_bn.setVisible(False)
        main_window.ui.validation_data_gt_label.setVisible(False)
        main_window.ui.validation_data_gt_info.setVisible(False)
        main_window.ui.DATA__VAL__GT_PATH__INPUT.setVisible(False)
        main_window.ui.val_data_gt_input_browse_bn.setVisible(False)
        main_window.ui.percentage_validation_label.setVisible(True)
        main_window.ui.percentage_validation_info.setVisible(True)
        main_window.ui.DATA__VAL__SPLIT_TRAIN__INPUT.setVisible(True)
        main_window.ui.cross_validation_nfolds_label.setVisible(False)
        main_window.ui.cross_validation_nfolds_info.setVisible(False)
        main_window.ui.DATA__VAL__CROSS_VAL_NFOLD__INPUT.setVisible(False)
        main_window.ui.cross_validation_fold_label.setVisible(False)
        main_window.ui.cross_validation_fold_info.setVisible(False)
        main_window.ui.DATA__VAL__CROSS_VAL_FOLD__INPUT.setVisible(False)
        main_window.ui.train_advanced_options_frame.setVisible(False)
        main_window.ui.DATA__PREPROCESS__VAL__LABEL.setVisible(False)
        main_window.ui.DATA__PREPROCESS__VAL__INFO.setVisible(False)
        main_window.ui.DATA__PREPROCESS__VAL__INPUT.setVisible(False)
        main_window.ui.MODEL__MAE_MASK_RATIO__LABEL.setVisible(False)
        main_window.ui.MODEL__MAE_MASK_RATIO__INFO.setVisible(False)
        main_window.ui.MODEL__MAE_MASK_RATIO__INPUT.setVisible(False)
        main_window.ui.adamw_weight_decay_label.setVisible(False)
        main_window.ui.TRAIN__W_DECAY__INFO.setVisible(False)
        main_window.ui.TRAIN__W_DECAY__INPUT.setVisible(False)
        main_window.ui.TRAIN__OPT_BETAS__LABEL.setVisible(False)
        main_window.ui.TRAIN__OPT_BETAS__INFO.setVisible(False)
        main_window.ui.TRAIN__OPT_BETAS__INPUT.setVisible(False)
        main_window.ui.profiler_batch_range_label.setVisible(False)
        main_window.ui.TRAIN__PROFILER_BATCH_RANGE__INPUT.setVisible(False)
        main_window.ui.TRAIN__PROFILER_BATCH_RANGE__INFO.setVisible(False)
        main_window.ui.DATA__NORMALIZATION__PERC_LOWER__LABEL.setVisible(False)
        main_window.ui.DATA__NORMALIZATION__PERC_LOWER__INFO.setVisible(False)
        main_window.ui.DATA__NORMALIZATION__PERC_LOWER__INPUT.setVisible(False)
        main_window.ui.DATA__NORMALIZATION__PERC_UPPER__LABEL.setVisible(False)
        main_window.ui.DATA__NORMALIZATION__PERC_UPPER__INFO.setVisible(False)
        main_window.ui.DATA__NORMALIZATION__PERC_UPPER__INPUT.setVisible(False)
        main_window.ui.custom_mean_label.setVisible(False)
        main_window.ui.DATA__NORMALIZATION__CUSTOM_MEAN__INPUT.setVisible(False)
        main_window.ui.DATA__NORMALIZATION__CUSTOM_MEAN__INFO.setVisible(False)
        main_window.ui.custom_std_label.setVisible(False)
        main_window.ui.DATA__NORMALIZATION__CUSTOM_STD__INPUT.setVisible(False)
        main_window.ui.DATA__NORMALIZATION__CUSTOM_STD__INFO.setVisible(False)
        main_window.ui.preprocessing_frame.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__LABEL.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__INFO.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__INPUT.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__ORDER__LABEL.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__ORDER__INFO.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__ORDER__INPUT.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__MODE__LABEL.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__MODE__INFO.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__MODE__INPUT.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__CVAL__LABEL.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__CVAL__INFO.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__CVAL__INPUT.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__CLIP__LABEL.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__CLIP__INFO.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__CLIP__INPUT.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__PRESERVE_RANGE__LABEL.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__PRESERVE_RANGE__INFO.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__PRESERVE_RANGE__INPUT.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__ANTI_ALIASING__LABEL.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__ANTI_ALIASING__INFO.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__ANTI_ALIASING__INPUT.setVisible(False)
        main_window.ui.DATA__PREPROCESS__GAUSSIAN_BLUR__SIGMA__LABEL.setVisible(False)
        main_window.ui.DATA__PREPROCESS__GAUSSIAN_BLUR__SIGMA__INFO.setVisible(False)
        main_window.ui.DATA__PREPROCESS__GAUSSIAN_BLUR__SIGMA__INPUT.setVisible(False)
        main_window.ui.DATA__PREPROCESS__GAUSSIAN_BLUR__MODE__LABEL.setVisible(False)
        main_window.ui.DATA__PREPROCESS__GAUSSIAN_BLUR__MODE__INFO.setVisible(False)
        main_window.ui.DATA__PREPROCESS__GAUSSIAN_BLUR__MODE__INPUT.setVisible(False)
        main_window.ui.DATA__PREPROCESS__GAUSSIAN_BLUR__CHANNEL_AXIS__LABEL.setVisible(False)
        main_window.ui.DATA__PREPROCESS__GAUSSIAN_BLUR__CHANNEL_AXIS__INFO.setVisible(False)
        main_window.ui.DATA__PREPROCESS__GAUSSIAN_BLUR__CHANNEL_AXIS__INPUT.setVisible(False)
        main_window.ui.DATA__PREPROCESS__MEDIAN_BLUR__KERNEL_SIZE__LABEL.setVisible(False)
        main_window.ui.DATA__PREPROCESS__MEDIAN_BLUR__KERNEL_SIZE__INFO.setVisible(False)
        main_window.ui.DATA__PREPROCESS__MEDIAN_BLUR__KERNEL_SIZE__INPUT.setVisible(False)
        main_window.ui.DATA__PREPROCESS__MATCH_HISTOGRAM__REFERENCE_PATH__LABEL.setVisible(False)
        main_window.ui.DATA__PREPROCESS__MATCH_HISTOGRAM__REFERENCE_PATH__INFO.setVisible(False)
        main_window.ui.DATA__PREPROCESS__MATCH_HISTOGRAM__REFERENCE_PATH__INPUT.setVisible(False)
        main_window.ui.DATA__PREPROCESS__MATCH_HISTOGRAM__REFERENCE_PATH__BN.setVisible(False)
        main_window.ui.DATA__PREPROCESS__CLAHE__KERNEL_SIZE__LABEL.setVisible(False)
        main_window.ui.DATA__PREPROCESS__CLAHE__KERNEL_SIZE__INFO.setVisible(False)
        main_window.ui.DATA__PREPROCESS__CLAHE__KERNEL_SIZE__INPUT.setVisible(False)
        main_window.ui.DATA__PREPROCESS__CLAHE__CLIP_LIMIT__LABEL.setVisible(False)
        main_window.ui.DATA__PREPROCESS__CLAHE__CLIP_LIMIT__INFO.setVisible(False)
        main_window.ui.DATA__PREPROCESS__CLAHE__CLIP_LIMIT__INPUT.setVisible(False)
        main_window.ui.DATA__PREPROCESS__CANNY__LOW_THRESHOLD__LABEL.setVisible(False)
        main_window.ui.DATA__PREPROCESS__CANNY__LOW_THRESHOLD__INFO.setVisible(False)
        main_window.ui.DATA__PREPROCESS__CANNY__LOW_THRESHOLD__INPUT.setVisible(False)
        main_window.ui.DATA__PREPROCESS__CANNY__HIGH_THRESHOLD__LABEL.setVisible(False)
        main_window.ui.DATA__PREPROCESS__CANNY__HIGH_THRESHOLD__INFO.setVisible(False)
        main_window.ui.DATA__PREPROCESS__CANNY__HIGH_THRESHOLD__INPUT.setVisible(False)
        main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__LABEL.setVisible(False)
        main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__INFO.setVisible(False)
        main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__INPUT.setVisible(False)
        main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__LABEL.setVisible(False)
        main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__INFO.setVisible(False)
        main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__INPUT.setVisible(False)
        main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__LABEL.setVisible(False)
        main_window.ui.DATA__VAL__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__LABEL.setVisible(False)
        main_window.ui.DATA__VAL__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__INFO.setVisible(False)
        main_window.ui.DATA__VAL__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__INPUT.setVisible(False)
        main_window.ui.DATA__VAL__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__LABEL.setVisible(False)
        main_window.ui.DATA__VAL__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__INFO.setVisible(False)
        main_window.ui.DATA__VAL__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__INPUT.setVisible(False)
        main_window.ui.preprocessing_test_frame.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__TEST__LABEL.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__TEST__INFO.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__TEST__INPUT.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__ORDER__TEST__LABEL.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__ORDER__TEST__INFO.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__ORDER__TEST__INPUT.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__MODE__TEST__LABEL.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__MODE__TEST__INFO.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__MODE__TEST__INPUT.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__CVAL__TEST__LABEL.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__CVAL__TEST__INFO.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__CVAL__TEST__INPUT.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__CLIP__TEST__LABEL.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__CLIP__TEST__INFO.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__CLIP__TEST__INPUT.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__PRESERVE_RANGE__TEST__LABEL.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__PRESERVE_RANGE__TEST__INFO.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__PRESERVE_RANGE__TEST__INPUT.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__ANTI_ALIASING__TEST__LABEL.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__ANTI_ALIASING__TEST__INFO.setVisible(False)
        main_window.ui.DATA__PREPROCESS__RESIZE__ANTI_ALIASING__TEST__INPUT.setVisible(False)
        main_window.ui.DATA__PREPROCESS__GAUSSIAN_BLUR__SIGMA__TEST__LABEL.setVisible(False)
        main_window.ui.DATA__PREPROCESS__GAUSSIAN_BLUR__SIGMA__TEST__INFO.setVisible(False)
        main_window.ui.DATA__PREPROCESS__GAUSSIAN_BLUR__SIGMA__TEST__INPUT.setVisible(False)
        main_window.ui.DATA__PREPROCESS__GAUSSIAN_BLUR__MODE__TEST__LABEL.setVisible(False)
        main_window.ui.DATA__PREPROCESS__GAUSSIAN_BLUR__MODE__TEST__INFO.setVisible(False)
        main_window.ui.DATA__PREPROCESS__GAUSSIAN_BLUR__MODE__TEST__INPUT.setVisible(False)
        main_window.ui.DATA__PREPROCESS__GAUSSIAN_BLUR__CHANNEL_AXIS__TEST__LABEL.setVisible(False)
        main_window.ui.DATA__PREPROCESS__GAUSSIAN_BLUR__CHANNEL_AXIS__TEST__INFO.setVisible(False)
        main_window.ui.DATA__PREPROCESS__GAUSSIAN_BLUR__CHANNEL_AXIS__TEST__INPUT.setVisible(False)
        main_window.ui.DATA__PREPROCESS__MEDIAN_BLUR__KERNEL_SIZE__TEST__LABEL.setVisible(False)
        main_window.ui.DATA__PREPROCESS__MEDIAN_BLUR__KERNEL_SIZE__TEST__INFO.setVisible(False)
        main_window.ui.DATA__PREPROCESS__MEDIAN_BLUR__KERNEL_SIZE__TEST__INPUT.setVisible(False)
        main_window.ui.DATA__PREPROCESS__MATCH_HISTOGRAM__REFERENCE_PATH__TEST__LABEL.setVisible(False)
        main_window.ui.DATA__PREPROCESS__MATCH_HISTOGRAM__REFERENCE_PATH__TEST__INFO.setVisible(False)
        main_window.ui.DATA__PREPROCESS__MATCH_HISTOGRAM__REFERENCE_PATH__TEST__INPUT.setVisible(False)
        main_window.ui.DATA__PREPROCESS__MATCH_HISTOGRAM__REFERENCE_PATH__TEST__BN.setVisible(False)
        main_window.ui.DATA__PREPROCESS__MATCH_HISTOGRAM__REFERENCE_PATH__BN.setVisible(False)
        main_window.ui.DATA__PREPROCESS__CLAHE__KERNEL_SIZE__TEST__LABEL.setVisible(False)
        main_window.ui.DATA__PREPROCESS__CLAHE__KERNEL_SIZE__TEST__INFO.setVisible(False)
        main_window.ui.DATA__PREPROCESS__CLAHE__KERNEL_SIZE__TEST__INPUT.setVisible(False)
        main_window.ui.DATA__PREPROCESS__CLAHE__CLIP_LIMIT__TEST__LABEL.setVisible(False)
        main_window.ui.DATA__PREPROCESS__CLAHE__CLIP_LIMIT__TEST__INFO.setVisible(False)
        main_window.ui.DATA__PREPROCESS__CLAHE__CLIP_LIMIT__TEST__INPUT.setVisible(False)
        main_window.ui.DATA__PREPROCESS__CANNY__LOW_THRESHOLD__TEST__LABEL.setVisible(False)
        main_window.ui.DATA__PREPROCESS__CANNY__LOW_THRESHOLD__TEST__INFO.setVisible(False)
        main_window.ui.DATA__PREPROCESS__CANNY__LOW_THRESHOLD__TEST__INPUT.setVisible(False)
        main_window.ui.DATA__PREPROCESS__CANNY__HIGH_THRESHOLD__TEST__LABEL.setVisible(False)
        main_window.ui.DATA__PREPROCESS__CANNY__HIGH_THRESHOLD__TEST__INFO.setVisible(False)
        main_window.ui.DATA__PREPROCESS__CANNY__HIGH_THRESHOLD__TEST__INPUT.setVisible(False)
        main_window.ui.lr_schel_min_lr_label.setVisible(False)
        main_window.ui.TRAIN__LR_SCHEDULER__MIN_LR__INPUT.setVisible(False)
        main_window.ui.TRAIN__LR_SCHEDULER__MIN_LR__INFO.setVisible(False)
        main_window.ui.lr_schel_reduce_on_plat_patience_label.setVisible(False)
        main_window.ui.TRAIN__LR_SCHEDULER__REDUCEONPLATEAU_PATIENCE__INPUT.setVisible(False)
        main_window.ui.TRAIN__LR_SCHEDULER__REDUCEONPLATEAU_PATIENCE__INFO.setVisible(False)
        main_window.ui.lr_schel_reduce_on_plat_factor_label.setVisible(False)
        main_window.ui.TRAIN__LR_SCHEDULER__REDUCEONPLATEAU_FACTOR__INPUT.setVisible(False)
        main_window.ui.TRAIN__LR_SCHEDULER__REDUCEONPLATEAU_FACTOR__INFO.setVisible(False)
        main_window.ui.lr_schel_warmupcosine_epochs_label.setVisible(False)
        main_window.ui.TRAIN__LR_SCHEDULER__WARMUP_COSINE_DECAY_EPOCHS__INPUT.setVisible(False)
        main_window.ui.TRAIN__LR_SCHEDULER__WARMUP_COSINE_DECAY_EPOCHS__INFO.setVisible(False)

        main_window.ui.DATA__TRAIN__FILTER_SAMPLES__PROPS__LABEL.setVisible(False) 
        main_window.ui.DATA__TRAIN__FILTER_SAMPLES__PROPS__INFO.setVisible(False)
        main_window.ui.DATA__TRAIN__FILTER_SAMPLES__PROPS__INPUT.setVisible(False) 
        main_window.ui.DATA__TRAIN__FILTER_SAMPLES__VALUES__LABEL.setVisible(False) 
        main_window.ui.DATA__TRAIN__FILTER_SAMPLES__VALUES__INFO.setVisible(False)
        main_window.ui.DATA__TRAIN__FILTER_SAMPLES__VALUES__INPUT.setVisible(False) 
        main_window.ui.DATA__TRAIN__FILTER_SAMPLES__SIGNS__LABEL.setVisible(False) 
        main_window.ui.DATA__TRAIN__FILTER_SAMPLES__SIGNS__INFO.setVisible(False)
        main_window.ui.DATA__TRAIN__FILTER_SAMPLES__SIGNS__INPUT.setVisible(False) 
        main_window.ui.DATA__VAL__FILTER_SAMPLES__PROPS__LABEL.setVisible(False) 
        main_window.ui.DATA__VAL__FILTER_SAMPLES__PROPS__INFO.setVisible(False)
        main_window.ui.DATA__VAL__FILTER_SAMPLES__PROPS__INPUT.setVisible(False) 
        main_window.ui.DATA__VAL__FILTER_SAMPLES__VALUES__LABEL.setVisible(False) 
        main_window.ui.DATA__VAL__FILTER_SAMPLES__VALUES__INFO.setVisible(False)
        main_window.ui.DATA__VAL__FILTER_SAMPLES__VALUES__INPUT.setVisible(False) 
        main_window.ui.DATA__VAL__FILTER_SAMPLES__SIGNS__LABEL.setVisible(False) 
        main_window.ui.DATA__VAL__FILTER_SAMPLES__SIGNS__INFO.setVisible(False)
        main_window.ui.DATA__VAL__FILTER_SAMPLES__SIGNS__INPUT.setVisible(False) 
        main_window.ui.DATA__TEST__FILTER_SAMPLES__PROPS__LABEL.setVisible(False) 
        main_window.ui.DATA__TEST__FILTER_SAMPLES__PROPS__INFO.setVisible(False)
        main_window.ui.DATA__TEST__FILTER_SAMPLES__PROPS__INPUT.setVisible(False) 
        main_window.ui.DATA__TEST__FILTER_SAMPLES__VALUES__LABEL.setVisible(False) 
        main_window.ui.DATA__TEST__FILTER_SAMPLES__VALUES__INFO.setVisible(False)
        main_window.ui.DATA__TEST__FILTER_SAMPLES__VALUES__INPUT.setVisible(False) 
        main_window.ui.DATA__TEST__FILTER_SAMPLES__SIGNS__LABEL.setVisible(False) 
        main_window.ui.DATA__TEST__FILTER_SAMPLES__SIGNS__INFO.setVisible(False)
        main_window.ui.DATA__TEST__FILTER_SAMPLES__SIGNS__INPUT.setVisible(False) 

        main_window.ui.da_frame.setVisible(False)
        main_window.ui.da_random_rot_range_label.setVisible(False)
        main_window.ui.AUGMENTOR__RANDOM_ROT_RANGE__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__RANDOM_ROT_RANGE__INFO.setVisible(False)
        main_window.ui.da_shear_range_label.setVisible(False)
        main_window.ui.AUGMENTOR__SHEAR_RANGE__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__SHEAR_RANGE__INFO.setVisible(False)
        main_window.ui.da_zoom_range_label.setVisible(False)
        main_window.ui.AUGMENTOR__ZOOM_RANGE__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__ZOOM_RANGE__INFO.setVisible(False)
        main_window.ui.da_zoom_in_z_label.setVisible(False)
        main_window.ui.AUGMENTOR__ZOOM_IN_Z__INFO.setVisible(False)
        main_window.ui.AUGMENTOR__ZOOM_IN_Z__INPUT.setVisible(False)
        main_window.ui.da_shift_range_label.setVisible(False)
        main_window.ui.AUGMENTOR__SHIFT_RANGE__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__SHIFT_RANGE__INFO.setVisible(False)
        main_window.ui.da_shift_range_label.setVisible(False)
        main_window.ui.da_elastic_alpha_label.setVisible(False)
        main_window.ui.AUGMENTOR__E_ALPHA__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__E_ALPHA__INFO.setVisible(False)
        main_window.ui.da_elastic_sigma_label.setVisible(False)
        main_window.ui.AUGMENTOR__E_SIGMA__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__E_SIGMA__INFO.setVisible(False)
        main_window.ui.da_elastic_mode_label.setVisible(False)
        main_window.ui.AUGMENTOR__E_MODE__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__E_MODE__INFO.setVisible(False)
        main_window.ui.da_gaussian_sigma_label.setVisible(False)
        main_window.ui.AUGMENTOR__G_SIGMA__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__G_SIGMA__INFO.setVisible(False)
        main_window.ui.da_median_blur_k_size_label.setVisible(False)
        main_window.ui.AUGMENTOR__MB_KERNEL__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__MB_KERNEL__INFO.setVisible(False)
        main_window.ui.da_motion_blur_k_size_label.setVisible(False)
        main_window.ui.AUGMENTOR__MOTB_K_RANGE__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__MOTB_K_RANGE__INFO.setVisible(False)
        main_window.ui.da_gamma_contrast_range_label.setVisible(False)
        main_window.ui.AUGMENTOR__GC_GAMMA__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__GC_GAMMA__INFO.setVisible(False)
        main_window.ui.da_brightness_factor_range_label.setVisible(False)
        main_window.ui.AUGMENTOR__BRIGHTNESS_FACTOR__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__BRIGHTNESS_FACTOR__INFO.setVisible(False)
        main_window.ui.da_brightness_mode_label.setVisible(False)
        main_window.ui.AUGMENTOR__BRIGHTNESS_MODE__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__BRIGHTNESS_MODE__INFO.setVisible(False)
        main_window.ui.da_contrast_factor_range_label.setVisible(False)
        main_window.ui.AUGMENTOR__CONTRAST_FACTOR__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__CONTRAST_FACTOR__INFO.setVisible(False)
        main_window.ui.da_contrast_mode_label.setVisible(False)
        main_window.ui.AUGMENTOR__CONTRAST_MODE__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__CONTRAST_MODE__INFO.setVisible(False)
        main_window.ui.da_dropout_range_label.setVisible(False)
        main_window.ui.AUGMENTOR__DROP_RANGE__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__DROP_RANGE__INFO.setVisible(False)
        main_window.ui.da_cutout_number_iterations_label.setVisible(False)
        main_window.ui.AUGMENTOR__COUT_SIZE__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__COUT_SIZE__INFO.setVisible(False)
        main_window.ui.da_cutout_size_label.setVisible(False)
        main_window.ui.AUGMENTOR__COUT_NB_ITERATIONS__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__COUT_NB_ITERATIONS__INFO.setVisible(False)
        main_window.ui.da_cuout_cval_label.setVisible(False)
        main_window.ui.AUGMENTOR__COUT_CVAL__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__COUT_CVAL__INFO.setVisible(False)
        main_window.ui.da_cutout_to_mask_label.setVisible(False)
        main_window.ui.AUGMENTOR__COUT_APPLY_TO_MASK__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__COUT_APPLY_TO_MASK__INFO.setVisible(False)
        main_window.ui.da_cutblur_size_range_label.setVisible(False)
        main_window.ui.AUGMENTOR__CBLUR_SIZE__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__CBLUR_SIZE__INFO.setVisible(False)
        main_window.ui.da_cutblut_down_range_label.setVisible(False)
        main_window.ui.AUGMENTOR__CBLUR_DOWN_RANGE__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__CBLUR_DOWN_RANGE__INFO.setVisible(False)
        main_window.ui.da_cutblur_inside_label.setVisible(False)
        main_window.ui.AUGMENTOR__CBLUR_INSIDE__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__CBLUR_INSIDE__INFO.setVisible(False)
        main_window.ui.da_cutmix_size_range_label.setVisible(False)
        main_window.ui.AUGMENTOR__CMIX_SIZE__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__CMIX_SIZE__INFO.setVisible(False)
        main_window.ui.da_cutnoise_scale_range_label.setVisible(False)
        main_window.ui.AUGMENTOR__CNOISE_SCALE__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__CNOISE_SCALE__INFO.setVisible(False)
        main_window.ui.da_cutnoise_number_iter_label.setVisible(False)
        main_window.ui.AUGMENTOR__CNOISE_NB_ITERATIONS__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__CNOISE_NB_ITERATIONS__INFO.setVisible(False)
        main_window.ui.da_cutnoise_size_range_label.setVisible(False)
        main_window.ui.AUGMENTOR__CNOISE_SIZE__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__CNOISE_SIZE__INFO.setVisible(False)
        main_window.ui.da_misaligment_rotate_ratio_label.setVisible(False)
        main_window.ui.AUGMENTOR__MS_ROTATE_RATIO__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__MS_ROTATE_RATIO__INFO.setVisible(False)
        main_window.ui.da_misaligment_displacement_label.setVisible(False)
        main_window.ui.AUGMENTOR__MS_DISPLACEMENT__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__MS_DISPLACEMENT__INFO.setVisible(False)
        main_window.ui.da_missing_sections_iteration_range_label.setVisible(False)
        main_window.ui.AUGMENTOR__MISSP_ITERATIONS__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__MISSP_ITERATIONS__INFO.setVisible(False)
        main_window.ui.da_grid_ratio_label.setVisible(False)
        main_window.ui.AUGMENTOR__GRID_RATIO__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__GRID_RATIO__INFO.setVisible(False)
        main_window.ui.da_grid_d_range_label.setVisible(False)
        main_window.ui.AUGMENTOR__GRID_D_RANGE__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__GRID_D_RANGE__INFO.setVisible(False)
        main_window.ui.da_grid_rotate_label.setVisible(False)
        main_window.ui.AUGMENTOR__GRID_ROTATE__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__GRID_ROTATE__INFO.setVisible(False)
        main_window.ui.da_grid_invert_label.setVisible(False)
        main_window.ui.AUGMENTOR__GRID_INVERT__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__GRID_INVERT__INFO.setVisible(False)
        main_window.ui.da_gaussian_noise_mean_label.setVisible(False)
        main_window.ui.AUGMENTOR__GAUSSIAN_NOISE_MEAN__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__GAUSSIAN_NOISE_MEAN__INFO.setVisible(False)
        main_window.ui.da_gaussian_noise_var_label.setVisible(False)
        main_window.ui.AUGMENTOR__GAUSSIAN_NOISE_VAR__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__GAUSSIAN_NOISE_VAR__INFO.setVisible(False)
        main_window.ui.da_gaussian_noise_use_input_img_label.setVisible(False)
        main_window.ui.AUGMENTOR__GAUSSIAN_NOISE_USE_INPUT_IMG_MEAN_AND_VAR__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__GAUSSIAN_NOISE_USE_INPUT_IMG_MEAN_AND_VAR__INFO.setVisible(False)
        main_window.ui.da_salt_amount_label.setVisible(False)
        main_window.ui.AUGMENTOR__SALT_AMOUNT__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__SALT_AMOUNT__INFO.setVisible(False)
        main_window.ui.da_pepper_amount_label.setVisible(False)
        main_window.ui.AUGMENTOR__PEPPER_AMOUNT__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__PEPPER_AMOUNT__INFO.setVisible(False)
        main_window.ui.da_salt_pepper_amount_label.setVisible(False)
        main_window.ui.AUGMENTOR__SALT_AND_PEPPER_AMOUNT__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__SALT_AND_PEPPER_AMOUNT__INFO.setVisible(False)
        main_window.ui.da_salt_pepper_prop_label.setVisible(False)
        main_window.ui.AUGMENTOR__SALT_AND_PEPPER_PROP__INPUT.setVisible(False)
        main_window.ui.AUGMENTOR__SALT_AND_PEPPER_PROP__INFO.setVisible(False)

        # Semantic seg
        main_window.ui.extract_random_patch_frame_label.setVisible(False)
        main_window.ui.extract_random_patch_frame.setVisible(False)

        # Instance seg
        main_window.ui.PROBLEM__INSTANCE_SEG__DISTANCE_CHANNEL_MASK__LABEL.setVisible(False)
        main_window.ui.PROBLEM__INSTANCE_SEG__DISTANCE_CHANNEL_MASK__INFO.setVisible(False)
        main_window.ui.PROBLEM__INSTANCE_SEG__DISTANCE_CHANNEL_MASK__INPUT.setVisible(False)

    ###########
    # Test page 
    ###########
    def init_test_page(main_window):
        """
        Initialize test page.
                
        Parameters
        ----------
        main_window : QMainWindow
            Main window of the application.
        """
        main_window.ui.test_data_gt_label.setVisible(False)
        main_window.ui.DATA__TEST__GT_PATH__INPUT.setVisible(False)
        main_window.ui.DATA__TEST__GT_PATH__INFO.setVisible(False)
        main_window.ui.test_data_gt_input_browse_bn.setVisible(False)
        main_window.ui.DATA__PREPROCESS__TEST__FRAME.setVisible(False)
        main_window.ui.inst_seg_ths_frame.setVisible(False)
        main_window.ui.inst_seg_b_channel_th_label.setVisible(False)
        main_window.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_BINARY_MASK__INPUT.setVisible(False)
        main_window.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_BINARY_MASK__INFO.setVisible(False)
        main_window.ui.inst_seg_c_channel_th_label.setVisible(False)
        main_window.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_CONTOUR__INPUT.setVisible(False)
        main_window.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_CONTOUR__INFO.setVisible(False)
        main_window.ui.inst_seg_fore_mask_th_label.setVisible(False)
        main_window.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_FOREGROUND__INPUT.setVisible(False)
        main_window.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_FOREGROUND__INFO.setVisible(False)
        main_window.ui.inst_seg_p_channel_th_label.setVisible(False)
        main_window.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_POINTS__INPUT.setVisible(False)
        main_window.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_POINTS__INFO.setVisible(False)
        main_window.ui.inst_seg_d_channel_th_label.setVisible(False)
        main_window.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_DISTANCE__INPUT.setVisible(False)
        main_window.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_DISTANCE__INFO.setVisible(False)
        main_window.ui.inst_seg_fore_dil_label.setVisible(False)
        main_window.ui.PROBLEM__INSTANCE_SEG__FORE_EROSION_RADIUS__INPUT.setVisible(False)
        main_window.ui.PROBLEM__INSTANCE_SEG__FORE_EROSION_RADIUS__INFO.setVisible(False)
        main_window.ui.inst_seg_fore_ero_label.setVisible(False)
        main_window.ui.PROBLEM__INSTANCE_SEG__FORE_DILATION_RADIUS__INPUT.setVisible(False)
        main_window.ui.PROBLEM__INSTANCE_SEG__FORE_DILATION_RADIUS__INFO.setVisible(False)
        main_window.ui.inst_seg_small_obj_fil_before_size_label.setVisible(False)
        main_window.ui.PROBLEM__INSTANCE_SEG__DATA_REMOVE_SMALL_OBJ_BEFORE__INPUT.setVisible(False)
        main_window.ui.PROBLEM__INSTANCE_SEG__DATA_REMOVE_SMALL_OBJ_BEFORE__INFO.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__INST_SEG__LABEL.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__INST_SEG__INFO.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__INST_SEG__INPUT.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__PROPS__INST_SEG__LABEL.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__PROPS__INST_SEG__INFO.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__PROPS__INST_SEG__INPUT.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__VALUES__INST_SEG__LABEL.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__VALUES__INST_SEG__INFO.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__VALUES__INST_SEG__INPUT.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__SIGN__INST_SEG__LABEL.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__SIGN__INST_SEG__INFO.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__SIGN__INST_SEG__INPUT.setVisible(False)
        main_window.ui.inst_seg_voronoi_mask_th_label.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__VORONOI_TH__INPUT.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__VORONOI_TH__INFO.setVisible(False)
        main_window.ui.inst_seg_remove_close_points_label.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS__INST_SEG__INFO.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS__INST_SEG__INPUT.setVisible(False)
        main_window.ui.inst_seg_remove_close_points_radius_label.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__INST_SEG__INPUT.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__INST_SEG__INFO.setVisible(False)
        
        main_window.ui.TEST__POST_PROCESSING__MEDIAN_FILTER_SIZE__SEM_SEG__LABEL.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEDIAN_FILTER_SIZE__SEM_SEG__INFO.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEDIAN_FILTER_SIZE__SEM_SEG__INPUT.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEDIAN_FILTER_AXIS__SEM_SEG__LABEL.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEDIAN_FILTER_AXIS__SEM_SEG__INFO.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEDIAN_FILTER_AXIS__SEM_SEG__INPUT.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEDIAN_FILTER_SIZE__INST_SEG__LABEL.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEDIAN_FILTER_SIZE__INST_SEG__INFO.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEDIAN_FILTER_SIZE__INST_SEG__INPUT.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEDIAN_FILTER_AXIS__INST_SEG__LABEL.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEDIAN_FILTER_AXIS__INST_SEG__INFO.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEDIAN_FILTER_AXIS__INST_SEG__INPUT.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEDIAN_FILTER_SIZE__DET__LABEL.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEDIAN_FILTER_SIZE__DET__INFO.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEDIAN_FILTER_SIZE__DET__INPUT.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEDIAN_FILTER_AXIS__DET__LABEL.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEDIAN_FILTER_AXIS__DET__INFO.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEDIAN_FILTER_AXIS__DET__INPUT.setVisible(False)

        main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__DET__LABEL.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__DET__INFO.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__DET__INPUT.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__DET__LABEL.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__DET__INFO.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__DET__INPUT.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__PROPS__DET__LABEL.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__PROPS__DET__INFO.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__PROPS__DET__INPUT.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__VALUES__DET__LABEL.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__VALUES__DET__INFO.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__VALUES__DET__INPUT.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__SIGN__DET__LABEL.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__SIGN__DET__INFO.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__SIGN__DET__INPUT.setVisible(False)
        main_window.ui.det_remove_close_points_radius_label.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__DET__INPUT.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__DET__INFO.setVisible(False)
        main_window.ui.det_watershed_first_dilation_label.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__DET_WATERSHED_FIRST_DILATION__INPUT.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__DET_WATERSHED_FIRST_DILATION__INFO.setVisible(False)
        main_window.ui.det_watershed_donuts_classes_label.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_CLASSES__INPUT.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_CLASSES__INFO.setVisible(False)
        main_window.ui.det_watershed_donuts_patch_label.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_PATCH__INPUT.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_PATCH__INFO.setVisible(False)
        main_window.ui.det_watershed_donuts_nucleus_diam_label.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_NUCLEUS_DIAMETER__INPUT.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_NUCLEUS_DIAMETER__INFO.setVisible(False)
        main_window.ui.det_data_watetshed_check_label.setVisible(False)
        main_window.ui.PROBLEM__DETECTION__DATA_CHECK_MW__INPUT.setVisible(False)
        main_window.ui.PROBLEM__DETECTION__DATA_CHECK_MW__INFO.setVisible(False)
        main_window.ui.test_advanced_options_frame.setVisible(False)
        main_window.ui.process_by_chunks_label.setVisible(False)
        main_window.ui.process_by_chunks_frame.setVisible(False)
        main_window.ui.TEST__BY_CHUNKS__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__LABEL.setVisible(False)
        main_window.ui.TEST__BY_CHUNKS__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__INFO.setVisible(False)
        main_window.ui.TEST__BY_CHUNKS__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__INPUT.setVisible(False)
        main_window.ui.TEST__BY_CHUNKS__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__LABEL.setVisible(False)
        main_window.ui.TEST__BY_CHUNKS__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__INFO.setVisible(False)
        main_window.ui.TEST__BY_CHUNKS__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__INPUT.setVisible(False)
        main_window.ui.TEST__BY_CHUNKS__WORKFLOW_PROCESS__TYPE__LABEL.setVisible(False)
        main_window.ui.TEST__BY_CHUNKS__WORKFLOW_PROCESS__TYPE__INPUT.setVisible(False)
        main_window.ui.TEST__BY_CHUNKS__WORKFLOW_PROCESS__TYPE__INFO.setVisible(False)
        main_window.ui.TEST__DET_BLOB_LOG_MIN_SIGMA__LABEL.setVisible(False)
        main_window.ui.TEST__DET_BLOB_LOG_MIN_SIGMA__INPUT.setVisible(False)
        main_window.ui.TEST__DET_BLOB_LOG_MIN_SIGMA__INFO.setVisible(False)
        main_window.ui.TEST__DET_BLOB_LOG_MAX_SIGMA__LABEL.setVisible(False)
        main_window.ui.TEST__DET_BLOB_LOG_MAX_SIGMA__INPUT.setVisible(False)
        main_window.ui.TEST__DET_BLOB_LOG_MAX_SIGMA__INFO.setVisible(False)
        main_window.ui.TEST__DET_BLOB_LOG_NUM_SIGMA__LABEL.setVisible(False)
        main_window.ui.TEST__DET_BLOB_LOG_NUM_SIGMA__INPUT.setVisible(False)
        main_window.ui.TEST__DET_BLOB_LOG_NUM_SIGMA__INFO.setVisible(False)
        main_window.ui.TEST__DET_PEAK_LOCAL_MAX_MIN_DISTANCE__LABEL.setVisible(False)
        main_window.ui.TEST__DET_PEAK_LOCAL_MAX_MIN_DISTANCE__INFO.setVisible(False)
        main_window.ui.TEST__DET_PEAK_LOCAL_MAX_MIN_DISTANCE__INPUT.setVisible(False)

    def init_run(main_window):
        """
        Initialize run page.
                
        Parameters
        ----------
        main_window : QMainWindow
            Main window of the application.
        """
        if len(main_window.cfg.settings['GPUs']) > 0:
            # Create GPU input field
            # main_window.ui.gpu_input = CheckableComboBox(main_window.ui.gpu_list_frame)
            main_window.ui.gpu_input = QComboBox(main_window.ui.gpu_list_frame)
            main_window.ui.gpu_input.setObjectName(u"gpu_input")
            main_window.ui.gpu_input.setMinimumSize(QSize(400, 30))
            main_window.ui.gpu_input.setMaximumSize(QSize(400, 30))
            font = QFont()
            font.setFamily(u"DejaVu Math TeX Gyre")
            font.setPointSize(12)
            main_window.ui.gpu_input.setFont(font)
            main_window.ui.verticalLayout_40.addWidget(main_window.ui.gpu_input, 0, Qt.AlignHCenter)
            # for i, gpu in enumerate(main_window.cfg.settings['GPUs']):
            #     main_window.ui.gpu_input.addItem("{} : {} ".format(i, gpu.name), check=True if i == 0 else False)
            main_window.ui.gpu_input.addItem("CPU")
            for i, gpu in enumerate(main_window.cfg.settings['GPUs']):
                main_window.ui.gpu_input.addItem("GPU {} : {} ".format(i, gpu.name))
        else:
            main_window.ui.gpu_list_frame.setVisible(False)
            main_window.ui.run_workflow_frame.setFrameShape(QFrame.NoFrame)

    def build_container(main_window):
        """
        Start container bulding process. 
                
        Parameters
        ----------
        main_window : QMainWindow
            Main window of the application.
        """
        main_window.cfg.settings['building_thread'] = None
        main_window.cfg.settings['building_worker'] = None
        main_window.cfg.settings['building_threads'] = QThread()
        outf = main_window.log_dir if main_window.cfg.settings['output_folder'] == "" else main_window.cfg.settings['output_folder']
        main_window.cfg.settings['building_worker'] = build_worker(main_window, main_window.cfg.settings['biapy_container_dockerfile'], 
            main_window.cfg.settings['biapy_container_name'], outf)
        main_window.cfg.settings['building_worker'].moveToThread(main_window.cfg.settings['building_threads'])
        main_window.cfg.settings['building_threads'].started.connect(main_window.cfg.settings['building_worker'].run)
        main_window.cfg.settings['building_worker'].finished_signal.connect(main_window.cfg.settings['building_threads'].quit)
        main_window.cfg.settings['building_worker'].finished_signal.connect(lambda: UIFunction.update_container_status_in_build(main_window, main_window.cfg.settings['building_worker'].finished_good))
        main_window.cfg.settings['building_worker'].close_signal.connect(main_window.cfg.settings['building_worker'].deleteLater) 
        main_window.cfg.settings['building_threads'].finished.connect(main_window.cfg.settings['building_threads'].deleteLater)
        main_window.cfg.settings['building_worker'].update_log_signal.connect(main_window.cfg.settings['building_worker'].gui.update_gui)
        main_window.cfg.settings['building_worker'].update_build_progress_signal.connect(main_window.cfg.settings['building_worker'].gui.update_building_progress)
        main_window.cfg.settings['building_threads'].start()

    def update_container_status_in_build(main_window, signal):
        """
        Updates container status during its building process. 
        
        Parameters
        ----------
        main_window : QMainWindow
            Main window of the application.
        
        signal : int
            Signal from the bulding process thread. 
        """
        # If the container was built correctly 
        if signal == 0:
            main_window.cfg.settings['biapy_container_ready'] = True
            main_window.ui.docker_head_label.setText("Dependencies")
            main_window.ui.docker_frame.setStyleSheet("")

    def run_biapy(main_window):
        """
        Run BiaPy container in a different thread.
                
        Parameters
        ----------
        main_window : QMainWindow
            Main window of the application.
        """
        # Load the YAML file selected
        r = load_yaml_config(main_window)
        if not r: return
        
        # Job name check
        jobname = get_text(main_window.ui.job_name_input)
        if jobname == "":
            main_window.dialog_exec("Job name can not be empty", "jobname")
            return

        # Output folder check
        if main_window.cfg.settings['output_folder'] == "":
            main_window.dialog_exec("Output folder must be defined", "output_folder")
            return 
        if not is_path_exists_or_creatable(main_window.cfg.settings['job_real_output_path']):
            main_window.dialog_exec("Job results folder is invalid. Please set a valid path within your system.", "output_folder")
            return 
        if os.path.exists(main_window.cfg.settings['job_real_output_path']):
            new_jobname = jobname+"_"+datetime.now().strftime("%Y%m%d_%H_%M_%S")
            main_window.yes_no_exec("Job results folder already exists. Do you want to change it to '{}' to avoid overwriting?"\
                .format(new_jobname))
            if main_window.yes_no.answer:
                main_window.ui.job_name_input.setPlainText(new_jobname)

        # Docker installation check
        if not main_window.cfg.settings['docker_found']:
            main_window.dialog_exec("Docker installation not found. Please, install it before running BiaPy in its\
                    <a href=\"https://docs.docker.com/get-docker/\">official documentation</a>. Once you have \
                    done that please restart this application.", "docker_installation")
            return
        if not main_window.cfg.settings['biapy_container_ready']:
            main_window.dialog_exec("You need to build BiaPy's container first. You will be redirected yo the main page "
                "so you can do it.", "docker_installation")
            return

        # Device selection
        device = get_text(main_window.ui.gpu_input)
        use_gpu = True if "GPU" in device else False
        
        # Check if a pull is necessary 
        local_images = main_window.docker_client.images.list()
        local_biapy_image_tag = ""
        old_biapy_images = []
        local_biapy_container_found = False 
        if len(local_images) > 0:    
            # Capture local BiaPy image 
            for i in range(len(local_images)):
                if len(local_images[i].attrs.get("RepoTags")) > 0:
                    if local_images[i].attrs.get("RepoTags")[0] == main_window.cfg.settings['biapy_container_name']:
                        # local_biapy_container_found = True # Activate this when locally want to try new BiaPy code 
                        if len(local_images[i].attrs.get("RepoDigests")) > 0:
                            local_biapy_image_tag = local_images[i].attrs.get("RepoDigests")[0].replace("biapyx/biapy@","")  
                else:
                    if len(local_images[i].attrs.get("RepoDigests"))>0:
                        if 'biapyx/biapy' in local_images[i].attrs.get("RepoDigests")[0]:
                            old_biapy_images.append(local_images[i].attrs['Id'])

            res = requests.get("https://registry.hub.docker.com/v2/repositories/biapyx/biapy/tags/")
            res = res.json()
            dockerhub_image_tag = ""
            for i in range(len(res['results'])):
                if res['results'][i]['name'] == main_window.cfg.settings['biapy_container_name'].split(':')[-1]:
                    dockerhub_image_tag = res['results'][i]['images'][0]['digest']    

            # Remove possible untagged BiaPy containers
            if len(old_biapy_images) > 0:
                main_window.yes_no_exec("Seems that there is one or more old BiaPy containers. Do yo want to remove them to save disk space?")
                if main_window.yes_no.answer:
                    main_window.logger.info("Removing old containers")
                    for i in range(len(old_biapy_images)):
                        main_window.docker_client.images.remove(old_biapy_images[i], force=True)

            # Replace BiaPy container 
            if dockerhub_image_tag != "" and local_biapy_image_tag != "":
                if dockerhub_image_tag != local_biapy_image_tag:
                    main_window.yes_no_exec("There is another BiaPy container ('{}'). Do yo want to remove the current one to "
                        "save disk space?".format(main_window.cfg.settings['biapy_container_name']))
                    if main_window.yes_no.answer:
                        main_window.logger.info("Removing last valid container")
                        main_window.docker_client.images.remove(main_window.cfg.settings['biapy_container_name'], force=True)

        # First time 
        run_biapy_cond = True
        if local_biapy_image_tag == "":
            if not local_biapy_container_found:
                main_window.yes_no_exec("The first time you run BiaPy you need to download its Docker container. "
                    f"This process will be done just once and needs {main_window.cfg.settings['biapy_container_size']} of disk space. Proceed?")
            else:
                main_window.yes_no_exec("Seems that there is an existing BiaPy container locally built ({}). Do you want to continue?"\
                    .format(main_window.cfg.settings['biapy_container_name']))
            run_biapy_cond = main_window.yes_no.answer
        
        if run_biapy_cond:            
            # Initialize thread/worker 
            main_window.cfg.settings['running_threads'].append(QThread())
            worker_id = len(main_window.cfg.settings['running_workers'])
            main_window.cfg.settings['running_workers'].append(run_worker(main_window, main_window.cfg.settings['biapy_cfg'], main_window.cfg.settings['biapy_container_name'], 
                worker_id, main_window.cfg.settings['output_folder'], main_window.cfg.settings['user_host'], use_gpu, use_local_biapy_image=local_biapy_container_found))

            # Set up signals so the mainn thread, in charge of updating the GUI, can do it
            main_window.cfg.settings['running_workers'][worker_id].moveToThread(main_window.cfg.settings['running_threads'][worker_id])
            main_window.cfg.settings['running_threads'][worker_id].started.connect(main_window.cfg.settings['running_workers'][worker_id].run)
            main_window.cfg.settings['running_workers'][worker_id].finished_signal.connect(main_window.cfg.settings['running_threads'][worker_id].quit)
            main_window.cfg.settings['running_workers'][worker_id].finished_signal.connect(main_window.cfg.settings['running_workers'][worker_id].deleteLater)
            main_window.cfg.settings['running_threads'][worker_id].finished.connect(main_window.cfg.settings['running_threads'][worker_id].deleteLater)
            main_window.cfg.settings['running_workers'][worker_id].update_log_signal.connect(main_window.cfg.settings['running_workers'][worker_id].gui.update_gui)
            main_window.cfg.settings['running_workers'][worker_id].update_cont_state_signal.connect(main_window.cfg.settings['running_workers'][worker_id].gui.update_cont_state)
            main_window.cfg.settings['running_workers'][worker_id].update_train_progress_signal.connect(main_window.cfg.settings['running_workers'][worker_id].gui.update_train_progress)
            main_window.cfg.settings['running_workers'][worker_id].update_test_progress_signal.connect(main_window.cfg.settings['running_workers'][worker_id].gui.update_test_progress)
            main_window.cfg.settings['running_workers'][worker_id].update_pulling_progress_signal.connect(main_window.cfg.settings['running_workers'][worker_id].gui.update_pulling_progress)
            main_window.cfg.settings['running_workers'][worker_id].update_pulling_signal.connect(main_window.cfg.settings['running_workers'][worker_id].gui.pulling_progress)
            
            # Start thread 
            main_window.cfg.settings['running_threads'][worker_id].start()
