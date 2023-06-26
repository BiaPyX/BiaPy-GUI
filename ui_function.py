import os
import sys
import docker
import json
import re
import multiprocessing
import yaml
import ast
import time
import traceback
from datetime import datetime, timedelta
import getpass

from ui_run import Ui_RunBiaPy 
from main import * 
from biapy_config import Config
from biapy_check_configuration import check_configuration

init = False 
page_number = 0

# Biapy 
yaml_config_file_path =''
yaml_config_filename = ''
output_folder = ''
biapy_cfg = None

# Docker 
docker_client = None
docker_found = False
running_threads = []
running_workers = []

# For all pages 
advanced_frame_images = None

# Workflow page
workflow_names = ["Semantic\nSegmentation", "Instance\nsegmentation", "Object\ndetection", "Image\ndenoising", "Super\nresolution",\
    "Self-supervised\nlearning", "Image\nclassification"]
workflow_images = None
workflow_images_selec = None
workflow_description_images = None
workflow_descriptions = None
selected_workflow = 1
dot_images = None
continue_bn_icons = None

# Semantic segmentation
semantic_models = ['unet', 'resunet', 'attention_unet', 'fcn32', \
        'fcn8', 'tiramisu', 'mnet', 'multiresunet', 'seunet', 'unetr']
# Instance segmentation
instance_models = ['unet', 'resunet', 'seunet', 'attention_unet']
# Detection
detection_models = ['unet', 'resunet', 'seunet', 'attention_unet']
# Denoising
denoising_models = ['unet', 'resunet', 'seunet', 'attention_unet']
# Super resolution
sr_models = ['edsr', 'srunet', 'rcan', 'dfcan', 'wdsr']
# Self-supervised learning
ssl_models = ['unet', 'resunet', 'seunet', 'attention_unet']
# Classification
classification_models = ['simple_cnn', 'EfficientNetB0']

# Paths
train_data_input_path = None
train_data_gt_input_path = None
validation_data_input_path = None
validation_data_gt_input_path = None
test_data_input_path = None
test_data_gt_input_path = None

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class UIFunction(MainWindow):

    def initStackTab(self):
        global init
        global workflow_images
        global workflow_images_selec
        global workflow_description_images
        global workflow_descriptions
        global dot_images
        global advanced_frame_images
        global continue_bn_icons
        
        if init==False:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            self.ui.frame_home.setStyleSheet("background:rgb(255,255,255)") 
            APFunction.check_docker(self)
            
            self.ui.biapy_logo_label.setPixmap(QPixmap(resource_path(os.path.join("images","superminimal_ark_biapy2.png"))))
            self.ui.docker_logo.setPixmap(QPixmap(resource_path(os.path.join("images","superminimal_ark_biapy2.png"))))
            self.ui.bn_close.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","closeAsset 43.png"))))
            self.ui.bn_min.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","hideAsset 53.png"))))

            self.ui.bn_home.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","home.png"))))
            self.ui.bn_workflow.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","workflow.png"))))
            self.ui.bn_goptions.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","goptions.png"))))
            self.ui.bn_train.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","train.png"))))
            self.ui.bn_test.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","test.png"))))
            self.ui.bn_run_biapy.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","run.png"))))

            self.ui.left_arrow_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","left_arrow.svg"))))
            self.ui.right_arrow_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","right_arrow.svg"))))
            self.ui.goptions_advanced_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","down_arrow.svg"))))
            self.ui.train_advanced_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","down_arrow.svg"))))
            self.ui.test_advanced_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","down_arrow.svg"))))

            workflow_images = [
                QPixmap(resource_path(os.path.join("images","semantic_seg.png"))),
                QPixmap(resource_path(os.path.join("images","instance_seg.png"))),
                QPixmap(resource_path(os.path.join("images","detection.png"))),
                QPixmap(resource_path(os.path.join("images","denoising.png"))),
                QPixmap(resource_path(os.path.join("images","sr.png"))),
                QPixmap(resource_path(os.path.join("images","ssl.png"))),
                QPixmap(resource_path(os.path.join("images","classification.png")))
            ]

            workflow_images_selec = [
                QPixmap(resource_path(os.path.join("images","semantic_seg_selected.png"))),
                QPixmap(resource_path(os.path.join("images","instance_seg_selected.png"))),
                QPixmap(resource_path(os.path.join("images","detection_selected.png"))),
                QPixmap(resource_path(os.path.join("images","denoising_selected.png"))),
                QPixmap(resource_path(os.path.join("images","sr_selected.png"))),
                QPixmap(resource_path(os.path.join("images","ssl_selected.png"))),
                QPixmap(resource_path(os.path.join("images","classification_selected.png")))
            ]
            
            workflow_description_images = [
                [QPixmap(resource_path(os.path.join("images","semantic_seg_raw.png"))),QPixmap(resource_path(os.path.join("images","semantic_seg_label.png")))],
                [QPixmap(resource_path(os.path.join("images","instance_seg_raw.png"))),QPixmap(resource_path(os.path.join("images","instance_seg_label.png")))],
                [QPixmap(resource_path(os.path.join("images","detection_raw.png"))),QPixmap(resource_path(os.path.join("images","detection_csv_input.png")))],
                [QPixmap(resource_path(os.path.join("images","denoising_raw.png"))),QPixmap(resource_path(os.path.join("images","denoising_pred.png")))],
                [QPixmap(resource_path(os.path.join("images","sr_raw.png"))),QPixmap(resource_path(os.path.join("images","sr_pred.png")))],
                [QPixmap(resource_path(os.path.join("images","ssl_raw.png"))),QPixmap(resource_path(os.path.join("images","ssl_pred.png")))],
                [QPixmap(resource_path(os.path.join("images","classification_raw.png"))),QPixmap(resource_path(os.path.join("images","classification_label.png")))]
            ]

            workflow_descriptions = [
                # Semantic segmentation
               '<p>The goal of this workflow is assign a class to each pixel of the input image.</p>\
                <ul>\
                    <li><dl>\
                        <dt><strong>Input:</strong></dt><dd><ul>\
                            <li><p>Image.</p></li>\
                            <li><p>Class mask where each pixel is labeled with an integer representing a class.</p></li>\
                        </ul></dd></dl>\
                    </li>\
                    <li><dl>\
                        <dt><strong>Output:</strong></dt><dd><ul>\
                        <li><p>Image with the probability of being part of each class.</p></li>\
                        </ul></dd></dl>\
                    </li>\
                </ul>\
                <p>In the figure above an example of this workflow’s <strong>input</strong> is depicted. \
                This image is a wound of a Drosophila embryo and the goal is to segment the contour of that wound\
                correctly. There, only two labels are present in the mask: black pixels, with value 0, represent the background \
                and white ones the contour of the wound, labeled with 1. </p>\
                <p>The <strong>output</strong> in case that only two classes are present, as in this example, will be an image \
                where each pixel will have the probability of being of class 1.</p>\
                <p>If there are <strong>3 or more classes</strong>, the output will be a multi-channel image, \
                with the same number of channels as classes, and the same pixel in each channel will be the \
                probability (in <code><span>[0-1]</span></code> \
                range) of being of the class that represents that channel number. For instance, with 3 classes, \
                e.g. background, mitochondria and contours, the fist channel will represent background, the second\
                 mitochondria and the last contour class.</p>',

                # Instance segmentation
               '<p>The goal of this workflow is assign an unique id, i.e. integer, to each object of the input image.</p>\
                <ul>\
                    <li><dl>\
                        <dt><strong>Input:</strong></dt><dd><ul>\
                            <li><p>Image.</p></li>\
                            <li><p>Instance mask where each object is identify with a unique label.</p></li>\
                        </ul></dd></dl>\
                    </li>\
                    <li><dl>\
                        <dt><strong>Output:</strong></dt><dd><ul>\
                        <li><p>Image with objects identified with a unique label.</p></li>\
                        </ul></dd></dl>\
                    </li>\
                </ul>\
                <p>In the figure above an example of this workflow’s input is depicted. Each color in the mask corresponds \
                to a unique object.</p>',
                
                # Detection
               '<p>The goal of this workflow is to localize objects in the input image, not requiring a pixel-level class. \
                Common strategies produce either bounding boxes containing the objects or individual points at their center \
                of mass, which is the one adopted by BiaPy.</p>\
                <ul>\
                    <li><dl>\
                        <dt><strong>Input:</strong></dt><dd><ul>\
                            <li><p>Image.</p></li>\
                            <li><p><code><span>.csv</span></code> file containing the list of points to detect.</p></li>\
                        </ul></dd></dl>\
                    </li>\
                    <li><dl>\
                        <dt><strong>Output:</strong></dt><dd><ul>\
                        <li><p>Image with the detected points as white dots.</p></li>\
                        <li><p><code><span>.csv</span></code> file with the list of detected points in napari format. </p></li>\
                        <li><p>A <code><span>_prob.csv</span></code> file \
                        with the same list of points as above but now with their detection probability (also in napary format).</p></li>\
                    </li>\
                </ul>\
                <br>\
                <p>Description of the <code><span>.csv</span></code> file:</p>\
                <div><ul>\
                <li><p>Each row represents the middle point of the object to be detected. Each column is a coordinate in the image \
                dimension space.</p></li>\
                <li><p>The first column name does not matter but it needs to be there. No matter also the enumeration and order for \
                that column.</p></li>\
                <li><p>If the images are <code><span>3D</span></code>, three columns need to be present and their names must be <code>\
                <span>[axis-0,</span> <span>axis-1,</span> <span>axis-2]</span></code>, which represent \
                <code><span>(z,y,x)</span></code> axes. If the images are <code><span>2D</span></code>, only two columns are required \
                <code><span>[axis-0,</span> <span>axis-1]</span></code>, which represent <code><span>(y,x)</span></code> axes.</p></li>\
                <li><p>For multi-class detection problem add an additional <code> <span>class</span></code> column to the file. The \
                classes need to start from <code><span>1</span></code> and consecutive, i.e. <code><span>1,2,3,4...</span></code> and \
                not like <code><span>1,4,8,6...</span></code>.</p></li> <li><p>Coordinates can be float or int but they will be \
                converted into ints so they can be translated to pixels. \
                </p></li> </ul> </div></p>\
                This way, the input <code><span>_prob.csv</span></code> file will be used to generate a mask to train the model. That mask\
                will contain the central points as is depicted below in the Model\'s GT image:\
                <br>\
                <table style="text-align: center;">\
                <tbody>\
                <tr><td style="text-align: center;">\
                <img src="images","detection_raw.png"> <p><span>Input image.</span></p>\
                </td>\
                <td style="text-align: center;">\
                <img src="images","detection_label.png"><p><span>Model\'s GT.</span></p>\
                </td>\
                </tr>\
                </tbody>\
                </table>',

                # Denoising
               '<p>The goal is to remove noise from an image. Our library includes \
                <a href="https://openaccess.thecvf.com/content_CVPR_2019/html/Krull_Noise2Void_-_Learning_Denoising_From_Single_Noisy_Images_CVPR_2019_paper.html">Nosei2Void</a>\
                using any of the U-Net versions provided. The main advantage of \
                <a href="https://openaccess.thecvf.com/content_CVPR_2019/html/Krull_Noise2Void_-_Learning_Denoising_From_Single_Noisy_Images_CVPR_2019_paper.html">Nosei2Void</a> \
                is neither relying on noise image pairs nor clean target images since frequently \
                clean images are simply unavailable.</p>\
                <ul>\
                    <li><dl>\
                        <dt><strong>Input:</strong></dt><dd><ul>\
                            <li><p>Noisy image.</p></li>\
                        </ul></dd></dl>\
                    </li>\
                    <li><dl>\
                        <dt><strong>Output:</strong></dt><dd><ul>\
                        <li><p>Image with noise.</p></li>\
                        </ul></dd></dl>\
                    </li>\
                </ul>\
                <p>In the figure above an example of this workflow’s <strong>input</strong> is depicted. \
                This image was obtained from a <a href="https://zenodo.org/record/5156913">Convallaria dataset</a> \
                used in \
                <a href="https://openaccess.thecvf.com/content_CVPR_2019/html/Krull_Noise2Void_-_Learning_Denoising_From_Single_Noisy_Images_CVPR_2019_paper.html">Nosei2Void</a>\
                project.</p>',      

                # Super resolution
               '<p>The goal of this workflow aims at reconstructing high-resolution (HR) images from low-resolution (LR) ones.</p>\
                <ul>\
                    <li><dl>\
                        <dt><strong>Input:</strong></dt><dd><ul>\
                            <li><p>LR image.</p></li>\
                        </ul></dd></dl>\
                    </li>\
                    <li><dl>\
                        <dt><strong>Output:</strong></dt><dd><ul>\
                        <li><p>HR image.</p></li>\
                        </ul></dd></dl>\
                    </li>\
                </ul>\
                <p>In the figure above an example of this workflow’s <strong">input</strong> is depicted \
                to make a x2 upsampling. The images were obtained from\
                <a href="https://github.com/HenriquesLab/ZeroCostDL4Mic">ZeroCostDL4Mic</a> project. \
                <p>Notice that in this example the LR and HR images has been resized but actually they are \
                <code><span>502x502</span></code> and <code><span>1004x1004</span></code>, respectively.</p>',

                # Self-supervised learning
               '<p>The idea of this workflow is to pretrain the backbone model by solving a so-called pretext \
                task without labels. This way, the model learns a representation that can be later transferred \
                to solve a downstream task in a labeled (but smaller) dataset. In BiaPy we adopt the pretext \
                task of recover a worstened version of the input image. </p>\
                <ul>\
                    <li><dl>\
                        <dt><strong>Input:</strong></dt><dd><ul>\
                            <li><p>Image.</p></li>\
                        </ul></dd></dl>\
                    </li>\
                    <li><dl>\
                        <dt><strong>Output:</strong></dt><dd><ul>\
                        <li><p>Pretrained model.</p></li>\
                        </ul></dd></dl>\
                    </li>\
                </ul>\
                <p>The worstened version of the input is automatically created by BiaPy. Each input image is used \
                to create its worstened version and the model’s task is to recover the input image from its worstened version.\
                In the figure above an example of the two pair images used in this workflow is depicted.</p>',

                # Classification
               '<p>The goal of this workflow is to assing a label to the input image.</p>\
                <ul>\
                    <li><dl>\
                        <dt><strong>Input:</strong></dt><dd><ul>\
                            <li><p>Image.</p></li>\
                        </ul></dd></dl>\
                    </li>\
                    <li><dl>\
                        <dt><strong>Output:</strong></dt><dd><ul>\
                        <li><p><code><span>.csv</span></code> file with the assigned class to each image.</p></li>\
                        </ul></dd></dl>\
                    </li>\
                </ul>\
                <p>In the figure above a few examples of this workflow’s <strong>input</strong> are depicted. \
                Each of these examples are of a different class and were obtained from \
                <a href="https://www.nature.com/articles/s41597-022-01721-8">MedMNIST v2</a>, concretely from \
                DermaMNIST dataset which is a large collection of multi-source dermatoscopic images of common \
                pigmented skin lesions.</p>']

            advanced_frame_images = [
                QPixmap(resource_path(os.path.join("images","bn_images","up_arrow.svg"))),
                QPixmap(resource_path(os.path.join("images","bn_images","down_arrow.svg")))
            ]
            dot_images = [
                QPixmap(resource_path(os.path.join("images","bn_images","dot_enable.svg"))),
                QPixmap(resource_path(os.path.join("images","bn_images","dot_disable.svg")))
            ]

            UIFunction.init_main_page(self)
            UIFunction.init_goptions_page(self)
            UIFunction.init_train_page(self)
            UIFunction.init_test_page(self)

            init = True
        
    def buttonPressed(self, buttonName, to_page):
        global page_number

        for each in self.ui.frame_bottom_west.findChildren(QFrame):
            if "biapy" not in each.objectName() or "frame_run_biapy" == each.objectName():
                each.setStyleSheet("background:rgb(64,144,253)")

        # Use global page_number to move as the user selected continue button
        if to_page == -1:
            move = True
            # if page_number != 1:
            #     move = UIFunction.check_input(self, page_number)
            # Do not move until the errors are corrected 
            if not move: return

            if buttonName == "up":
                page_number += 1
            else:
                page_number -= 1
            to_page = page_number
        

        if buttonName=='bn_home' or (buttonName=='down' and to_page == 0):
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            self.ui.frame_home.setStyleSheet("background:rgb(255,255,255)") 
            page_number = 0

        elif buttonName=='bn_workflow' or ('bn_' not in buttonName and to_page == 1):
            self.ui.continue_bn.setText("Continue")
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_create_yaml)
            self.ui.stackedWidget_create_yaml_frame.setCurrentWidget(self.ui.workflow_selection_page)
            self.ui.frame_workflow.setStyleSheet("background:rgb(255,255,255)") 
            UIFunction.set_workflow_page(self)
            page_number = 1
            UIFunction.adjust_window_progress(self, page_number)

        elif buttonName=='bn_goptions' or ('bn_' not in buttonName and to_page == 2):
            self.ui.continue_bn.setText("Continue")
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_create_yaml)
            self.ui.stackedWidget_create_yaml_frame.setCurrentWidget(self.ui.goptions_page)
            self.ui.frame_goptions.setStyleSheet("background:rgb(255,255,255)") 
            page_number = 2
            UIFunction.adjust_window_progress(self, page_number)

        elif buttonName=='bn_train' or ('bn_' not in buttonName and to_page == 3):
            self.ui.continue_bn.setText("Continue")
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_create_yaml)
            self.ui.stackedWidget_create_yaml_frame.setCurrentWidget(self.ui.train_page)
            self.ui.frame_train.setStyleSheet("background:rgb(255,255,255)") 
            page_number = 3
            UIFunction.adjust_window_progress(self, page_number)

        elif buttonName=='bn_test' or ('bn_' not in buttonName and to_page == 4):
            self.ui.continue_bn.setText("Generate YAML")
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_create_yaml)
            self.ui.stackedWidget_create_yaml_frame.setCurrentWidget(self.ui.test_page)
            self.ui.frame_test.setStyleSheet("background:rgb(255,255,255)") 
            page_number = 4
            UIFunction.adjust_window_progress(self, page_number)

        elif buttonName=='bn_run_biapy' or ('bn_' not in buttonName and to_page == 5):            
            error = False
            if ('bn_' not in buttonName and to_page == 5):
                error = APFunction.create_yaml_file(self)

            # If there is an error do not make the movement, as the error dialog will redirect the user to the 
            # field that raises the error 
            if not error:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_run_biapy)
                self.ui.frame_run_biapy.setStyleSheet("background:rgb(255,255,255)") 
                page_number = 5

        UIFunction.move_between_pages(self, to_page)

    def obtain_workflow_description(self, offset):
        global selected_workflow
        global workflow_descriptions

        s_workflow = selected_workflow + offset
        if s_workflow < 0:
            s_workflow = len(workflow_names)-1
        if s_workflow == len(workflow_names):
            s_workflow = 0

        workflow_name = workflow_names[s_workflow].replace("\n"," ") 
        workflow_images = workflow_description_images[s_workflow]
        workflow_description = workflow_descriptions[s_workflow]
        self.workflow_info_exec(workflow_name, workflow_images, workflow_description)

    def expand_hide_advanced_options(self, advanced_options_bn_tag, advanced_options_frame_tag):
        expand = not getattr(self.ui, advanced_options_frame_tag).isVisible()
        getattr(self.ui, advanced_options_bn_tag).setIcon(advanced_frame_images[0] if expand else advanced_frame_images[1])
        getattr(self.ui, advanced_options_frame_tag).setVisible(expand)
    
    def combobox_hide_visible_action(self, combobox, frames_dict, frames_dict_values_to_set=None):
        for key in frames_dict:
            visible_values = frames_dict[key]
            if not isinstance(visible_values, list):
                visible_values = [visible_values]

            vis = True if str(getattr(self.ui, combobox).currentText()) in visible_values else False
            getattr(self.ui, key).setVisible(vis)

        if frames_dict_values_to_set is not None:
            for key in frames_dict_values_to_set:
                getattr(self.ui, key).setCurrentText(frames_dict_values_to_set[key])
     
    def mark_syntax_error(self, obj, validator_type=["empty"]):
        global output_folder        
        global yaml_config_file_path
        global yaml_config_filename
        error = False
        for v in validator_type:
            if v == "empty" and APFunction.get_text(self, getattr(self.ui, obj)) == "":
                error = True
            elif v == "exists" and not os.path.exists(APFunction.get_text(self, getattr(self.ui, obj))):
                error = True
        if error:
            getattr(self.ui, obj).setStyleSheet("border: 2px solid red;")
        else:
            getattr(self.ui, obj).setStyleSheet("")

            out = APFunction.get_text(self, getattr(self.ui, obj))
            if obj == "goptions_browse_yaml_path_input":
                yaml_config_file_path = out
            elif obj == "select_yaml_name_label":
                out_write = os.path.basename(out)
                yaml_config_filename = out_write
                yaml_config_file_path = os.path.dirname(out)
                self.ui.job_name_input.setPlainText(os.path.splitext(out_write)[0]+"_experiment")
            elif obj == "output_folder_input":
                output_folder = out 
        
    def examine(self, save_in_obj_tag=None, is_file=True):
        global train_data_input_path
        global train_data_gt_input_path
        global validation_data_input_path
        global validation_data_gt_input_path
        global test_data_input_path
        global test_data_gt_input_path

        if not is_file:
            out = QFileDialog.getExistingDirectory(self, 'Select a directory')
            out_write = os.path.basename(os.path.normpath(out))
        else:
            out = QFileDialog.getOpenFileName()[0]
            out_write = os.path.basename(out)

        if out == "": return # If no file was selected 

        if save_in_obj_tag is not None:
            getattr(self.ui, save_in_obj_tag).setText(out)
            getattr(self.ui, save_in_obj_tag).moveCursor(QtGui.QTextCursor.End, QtGui.QTextCursor.MoveAnchor)
            if save_in_obj_tag == "train_data_input":
                train_data_input_path = out 
            elif save_in_obj_tag == "train_data_gt_input":
                train_data_gt_input_path = out 
            elif save_in_obj_tag == "validation_data_input":
                validation_data_input_path = out 
            elif save_in_obj_tag == "validation_data_gt_input":
                validation_data_gt_input_path = out 
            elif save_in_obj_tag == "test_data_input":
                test_data_input_path = out 
            elif save_in_obj_tag == "test_data_gt_input":
                test_data_gt_input_path = out  

    def move_between_pages(self, to_page):
        global selected_workflow
        global page_number

        # Semantic seg
        if selected_workflow == 0:
            jobname = "my_semantic_segmentation"
            models = semantic_models
            self.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.train_workflow_specific_tab_semantic_seg_page)
            self.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.test_workflow_specific_tab_semantic_seg_page)
        # Instance seg
        elif selected_workflow == 1:
            jobname = "my_instance_segmentation"
            models = instance_models
            self.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.train_workflow_specific_tab_instance_seg_page)
            self.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.test_workflow_specific_tab_instance_seg_page)
        # Detection
        elif selected_workflow == 2:
            jobname = "my_detection"
            models = detection_models
            self.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.train_workflow_specific_tab_detection_page)
            self.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.test_workflow_specific_tab_detection_page)
        # Denoising
        elif selected_workflow == 3:
            jobname = "my_denoising"
            models = denoising_models
            self.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.train_workflow_specific_tab_denoising_page)
            self.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.test_workflow_specific_tab_denoising_page)
        # Super resolution
        elif selected_workflow == 4:
            jobname = "my_super_resolution"
            models = sr_models
            self.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.train_workflow_specific_tab_sr_page)
            self.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.test_workflow_specific_tab_sr_page)
        # Self-supevised learning
        elif selected_workflow == 5:
            jobname = "my_self_supervised_learning"
            models = ssl_models
            self.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.train_workflow_specific_tab_ssl_page)
            self.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.test_workflow_specific_tab_ssl_page)
        # Classification
        elif selected_workflow == 6:
            jobname = "my_classification"
            models = classification_models
            goptions_tab_widget_visible = True
            self.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.train_workflow_specific_tab_classification_page)
            self.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.test_workflow_specific_tab_classification_page)
        
        actual_name = APFunction.get_text(self, self.ui.job_name_input)
        if actual_name in ["", "my_semantic_segmentation", "my_instance_segmentation", "my_detection", "my_denoising", \
            "my_super_resolution", "my_self_supervised_learning", "my_classification"]:
            if to_page == 5:
                self.ui.job_name_input.setPlainText(jobname)

        # General options page
        if to_page == 2:
            self.ui.goptions_advanced_options_scrollarea.setVisible(False)

        # Train page
        self.ui.model_input.clear()
        self.ui.model_input.addItems(models)

    ###########
    # Home page 
    ###########
    def init_main_page(self):
        pixmap = QPixmap(resource_path(os.path.join("images","horizontal-logo-monochromatic-white.png")))
        pixmap = pixmap.scaled(QSize(201,51),aspectRatioMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio)

        self.ui.docker_logo.setPixmap(pixmap)

    def adjust_window_progress(self, page_number):
        self.ui.window1_bn.setIcon(dot_images[0] if page_number == 1 else dot_images[1])
        self.ui.window2_bn.setIcon(dot_images[0] if page_number == 2 else dot_images[1])
        self.ui.window3_bn.setIcon(dot_images[0] if page_number == 3 else dot_images[1])
        self.ui.window4_bn.setIcon(dot_images[0] if page_number == 4 else dot_images[1])

    ###############
    # Workflow page 
    ###############
    def move_workflow_view(self, isleft):
        global selected_workflow
        if isleft:
            selected_workflow = selected_workflow - 1 if selected_workflow != 0 else len(workflow_names)-1
        else: 
            selected_workflow = selected_workflow + 1 if selected_workflow != len(workflow_names)-1 else 0
        UIFunction.set_workflow_page(self)

    def set_workflow_page(self):
        global selected_workflow
        global workflow_images
        global workflow_images_selec
        global workflow_names

        # Left view
        self.ui.workflow_view1_label.setPixmap(workflow_images[selected_workflow-1])
        self.ui.workflow_view1_name_label.setText(workflow_names[selected_workflow-1])

        # Mid view
        self.ui.workflow_view2_label.setPixmap(workflow_images_selec[selected_workflow])
        self.ui.workflow_view2_name_label.setText(workflow_names[selected_workflow])

        # Right view
        p = selected_workflow+1 if selected_workflow+1 < len(workflow_names) else 0
        self.ui.workflow_view3_label.setPixmap(workflow_images[p])
        self.ui.workflow_view3_name_label.setText(workflow_names[p])        

    ######################
    # General options page 
    ######################

    def init_goptions_page(self):
        global selected_workflow

        self.ui.goptions_advanced_options_scrollarea.setVisible(False)
        self.ui.checkpoint_file_path_input.setVisible(False)
        self.ui.checkpoint_file_path_browse_bn.setVisible(False)
        self.ui.checkpoint_file_path_browse_label.setVisible(False)

        self.ui.maxcpu_combobox.addItem("-1")
        for i in range(multiprocessing.cpu_count()):
            self.ui.maxcpu_combobox.addItem(str(i+1))

    ############
    # Train page 
    ############

    def init_train_page(self):
        global selected_workflow
        
        # Hide validation paths as it is extracted from train by default 
        self.ui.validation_data_label.setVisible(False)
        self.ui.validation_data_input.setVisible(False)
        self.ui.val_data_input_browse_bn.setVisible(False)
        self.ui.validation_data_gt_label.setVisible(False)
        self.ui.validation_data_gt_input.setVisible(False)
        self.ui.val_data_gt_input_browse_bn.setVisible(False)
        self.ui.val_in_memory_label.setVisible(False)
        self.ui.val_in_memory_comboBox.setVisible(False)
        self.ui.percentage_validation_label.setVisible(True)
        self.ui.percentage_validation_input.setVisible(True)
        self.ui.cross_validation_nfolds_label.setVisible(False)
        self.ui.cross_validation_nfolds_input.setVisible(False)
        self.ui.cross_validation_fold_label.setVisible(False)
        self.ui.cross_validation_fold_input.setVisible(False)
        self.ui.train_advanced_options_frame.setVisible(False)
        self.ui.profiler_batch_range_label.setVisible(False)
        self.ui.profiler_batch_range_input.setVisible(False)
        self.ui.custom_mean_label.setVisible(False)
        self.ui.custom_mean_input.setVisible(False)
        self.ui.custom_std_label.setVisible(False)
        self.ui.custom_std_input.setVisible(False)
        self.ui.lr_schel_min_lr_label.setVisible(False)
        self.ui.lr_schel_min_lr_input.setVisible(False)
        self.ui.lr_schel_reduce_on_plat_patience_label.setVisible(False)
        self.ui.lr_schel_reduce_on_plat_patience_input.setVisible(False)
        self.ui.lr_schel_reduce_on_plat_factor_label.setVisible(False)
        self.ui.lr_schel_reduce_on_plat_factor_input.setVisible(False)
        self.ui.lr_schel_warmupcosine_lr_label.setVisible(False)
        self.ui.lr_schel_warmupcosine_lr_input.setVisible(False)
        self.ui.lr_schel_warmupcosine_epochs_label.setVisible(False)
        self.ui.lr_schel_warmupcosine_epochs_input.setVisible(False)
        self.ui.lr_schel_warmupcosine_hold_epochs_label.setVisible(False)
        self.ui.lr_schel_warmupcosine_hold_epochs_input.setVisible(False)
        self.ui.da_random_rot_range_label.setVisible(False)
        self.ui.da_random_rot_range_input.setVisible(False)
        self.ui.da_shear_range_label.setVisible(False)
        self.ui.da_shear_range_input.setVisible(False)
        self.ui.da_zoom_range_label.setVisible(False)
        self.ui.da_zoom_range_input.setVisible(False)
        self.ui.da_shift_range_input.setVisible(False)
        self.ui.da_shift_range_label.setVisible(False)
        self.ui.da_elastic_alpha_label.setVisible(False)
        self.ui.da_elastic_alpha_input.setVisible(False)
        self.ui.da_elastic_sigma_label.setVisible(False)
        self.ui.da_elastic_sigma_input.setVisible(False)
        self.ui.da_elastic_mode_label.setVisible(False)
        self.ui.da_elastic_mode_input.setVisible(False)
        self.ui.da_gaussian_sigma_label.setVisible(False)
        self.ui.da_gaussian_sigma_input.setVisible(False)
        self.ui.da_median_blur_k_size_label.setVisible(False)
        self.ui.da_median_blur_k_size_input.setVisible(False)
        self.ui.da_motion_blur_k_size_label.setVisible(False)
        self.ui.da_motion_blur_k_size_input.setVisible(False)
        self.ui.da_gamma_contrast_range_label.setVisible(False)
        self.ui.da_gamma_contrast_range_input.setVisible(False)
        self.ui.da_brightness_factor_range_label.setVisible(False)
        self.ui.da_brightness_factor_range_input.setVisible(False)
        self.ui.da_brightness_mode_label.setVisible(False)
        self.ui.da_brightness_mode_input.setVisible(False)
        self.ui.da_contrast_factor_range_label.setVisible(False)
        self.ui.da_contrast_factor_range_input.setVisible(False)
        self.ui.da_contrast_mode_label.setVisible(False)
        self.ui.da_contrast_mode_input.setVisible(False)
        self.ui.da_brightness_em_factor_label.setVisible(False)
        self.ui.da_brightness_em_factor_input.setVisible(False)
        self.ui.da_brightness_em_mode_label.setVisible(False)
        self.ui.da_brightness_em_mode_input.setVisible(False)
        self.ui.da_contrast_em_factor_label.setVisible(False)
        self.ui.da_contrast_em_factor_input.setVisible(False)
        self.ui.da_contrast_em_mode_label.setVisible(False)
        self.ui.da_contrast_em_mode_input.setVisible(False)
        self.ui.da_dropout_range_label.setVisible(False)
        self.ui.da_dropout_range_input.setVisible(False)
        self.ui.da_cutout_size_label.setVisible(False)
        self.ui.da_cutout_size_input.setVisible(False)
        self.ui.da_cuout_cval_label.setVisible(False)
        self.ui.da_cuout_cval_input.setVisible(False)
        self.ui.da_cutout_to_mask_label.setVisible(False)
        self.ui.da_cutout_to_mask_input.setVisible(False)
        self.ui.da_cutblur_size_range_label.setVisible(False)
        self.ui.da_cutblur_size_range_input.setVisible(False)
        self.ui.da_cutblut_down_range_label.setVisible(False)
        self.ui.da_cutblut_down_range_input.setVisible(False)
        self.ui.da_cutblur_inside_label.setVisible(False)
        self.ui.da_cutblur_inside_input.setVisible(False)
        self.ui.da_cutmix_size_range_label.setVisible(False)
        self.ui.da_cutmix_size_range_input.setVisible(False)
        self.ui.da_cutnoise_scale_range_label.setVisible(False)
        self.ui.da_cutnoise_scale_range_input.setVisible(False)
        self.ui.da_cutnoise_number_iter_label.setVisible(False)
        self.ui.da_cutnoise_number_iter_input.setVisible(False)
        self.ui.da_cutnoise_size_range_label.setVisible(False)
        self.ui.da_cutnoise_size_range_input.setVisible(False)
        self.ui.da_misaligment_rotate_ratio_label.setVisible(False)
        self.ui.da_misaligment_rotate_ratio_input.setVisible(False)
        self.ui.da_misaligment_displacement_label.setVisible(False)
        self.ui.da_misaligment_displacement_input.setVisible(False)
        self.ui.da_missing_sections_iteration_range_label.setVisible(False)
        self.ui.da_missing_sections_iteration_range_input.setVisible(False)
        self.ui.da_grid_ratio_label.setVisible(False)
        self.ui.da_grid_ratio_input.setVisible(False)
        self.ui.da_grid_d_range_label.setVisible(False)
        self.ui.da_grid_d_range_input.setVisible(False)
        self.ui.da_grid_rotate_label.setVisible(False)
        self.ui.da_grid_rotate_input.setVisible(False)
        self.ui.da_grid_invert_label.setVisible(False)
        self.ui.da_grid_invert_input.setVisible(False)
        self.ui.da_gaussian_noise_mean_label.setVisible(False)
        self.ui.da_gaussian_noise_mean_input.setVisible(False)
        self.ui.da_gaussian_noise_var_label.setVisible(False)
        self.ui.da_gaussian_noise_var_input.setVisible(False)
        self.ui.da_gaussian_noise_use_input_img_label.setVisible(False)
        self.ui.da_gaussian_noise_use_input_img_input.setVisible(False)
        self.ui.da_salt_amount_label.setVisible(False)
        self.ui.da_salt_amount_input.setVisible(False)
        self.ui.da_pepper_amount_label.setVisible(False)
        self.ui.da_pepper_amount_input.setVisible(False)
        self.ui.da_salt_pepper_amount_label.setVisible(False)
        self.ui.da_salt_pepper_amount_input.setVisible(False)
        self.ui.da_salt_pepper_prop_label.setVisible(False)
        self.ui.da_salt_pepper_prop_input.setVisible(False)

        # Semantic seg
        self.ui.extract_random_patch_frame_label.setVisible(False)
        self.ui.extract_random_patch_frame.setVisible(False)

    def model_combobox_changed(self, model_name):
        if model_name in ['unet', 'resunet', 'seunet', 'attention_unet']:
            self.ui.unet_model_like_frame.setVisible(True)
            self.ui.unet_model_like_label.setVisible(True)
            self.ui.tiramisu_frame.setVisible(False)
            self.ui.tiramisu_label.setVisible(False)
            self.ui.unetr_frame.setVisible(False)
            self.ui.unetr_label.setVisible(False)
        elif model_name == "tiramisu":
            self.ui.unet_model_like_frame.setVisible(False)
            self.ui.unet_model_like_label.setVisible(False)
            self.ui.tiramisu_frame.setVisible(True)
            self.ui.tiramisu_label.setVisible(True)
            self.ui.unetr_frame.setVisible(False)
            self.ui.unetr_label.setVisible(False)
        elif model_name == "unetr":
            self.ui.unet_model_like_frame.setVisible(False)
            self.ui.unet_model_like_label.setVisible(False)
            self.ui.tiramisu_frame.setVisible(False)
            self.ui.tiramisu_label.setVisible(False)
            self.ui.unetr_frame.setVisible(True)
            self.ui.unetr_label.setVisible(True)
        else:
            self.ui.unet_model_like_frame.setVisible(False)
            self.ui.unet_model_like_label.setVisible(False)
            self.ui.tiramisu_frame.setVisible(False)
            self.ui.tiramisu_label.setVisible(False)
            self.ui.unetr_frame.setVisible(False)
            self.ui.unetr_label.setVisible(False)

    ###########
    # Test page 
    ###########
    
    def init_test_page(self):
        self.ui.test_data_gt_label.setVisible(False)
        self.ui.test_data_gt_input.setVisible(False)
        self.ui.test_data_gt_input_browse_bn.setVisible(False)
        self.ui.use_val_as_test.setVisible(False)
        self.ui.use_val_as_test_input.setVisible(False)
        self.ui.inst_seg_p_channel_th_label.setVisible(False)
        self.ui.inst_seg_p_channel_th_input.setVisible(False)
        self.ui.inst_seg_d_channel_th_label.setVisible(False)
        self.ui.inst_seg_d_channel_th_input.setVisible(False)
        self.ui.inst_seg_fore_dil_label.setVisible(False)
        self.ui.inst_seg_fore_dil_input.setVisible(False)
        self.ui.inst_seg_fore_ero_label.setVisible(False)
        self.ui.inst_seg_fore_ero_input.setVisible(False)
        self.ui.inst_seg_small_obj_fil_before_size_label.setVisible(False)
        self.ui.inst_seg_small_obj_fil_before_size_input.setVisible(False)
        self.ui.inst_seg_small_obj_fil_after_size_label.setVisible(False)
        self.ui.inst_seg_small_obj_fil_after_size_input.setVisible(False)
        self.ui.test_advanced_options_frame.setVisible(False)

class APFunction():
    
    def get_text(self, obj):
        if isinstance(obj, QComboBox):
            return obj.currentText()
        elif isinstance(obj, QLineEdit):
            return obj.text()
        else: #QTextBrowser
            return obj.toPlainText()

    def create_yaml_file(self):
        global selected_workflow
        global yaml_config_file_path
        global yaml_config_filename
        
        print("Creating YAML file") 
        biapy_config = {}

        # System
        biapy_config['SYSTEM'] = {}
        
        biapy_config['SYSTEM']['NUM_CPUS'] = int(APFunction.get_text(self,self.ui.maxcpu_combobox))

        # Problem specification
        workflow_names_yaml = ['SEMANTIC_SEG', 'INSTANCE_SEG', 'DETECTION', 'DENOISING', 'SUPER_RESOLUTION', 
            'SELF_SUPERVISED', 'CLASSIFICATION']
        biapy_config['PROBLEM'] = {}
        biapy_config['PROBLEM']['TYPE'] = workflow_names_yaml[selected_workflow]
        biapy_config['PROBLEM']['NDIM'] = APFunction.get_text(self, self.ui.dimensions_comboBox)

        ### INSTANCE_SEG
        if selected_workflow == 1:
            biapy_config['PROBLEM']['INSTANCE_SEG'] = {}
            biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_CHANNELS'] = APFunction.get_text(self, self.ui.inst_seg_data_channels_input)
            biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_CHANNEL_WEIGHTS'] = APFunction.get_text(self, self.ui.inst_seg_channel_weigths_input) 
            if APFunction.get_text(self, self.ui.inst_seg_contour_mode_combobox) != "thick":
                biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_CONTOUR_MODE'] = APFunction.get_text(self, self.ui.inst_seg_contour_mode_combobox)

            if 'B' in APFunction.get_text(self,self.ui.inst_seg_data_channels_input):
                biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_MW_TH_BINARY_MASK'] = float(APFunction.get_text(self, self.ui.inst_seg_b_channel_th_input))
                biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_MW_TH_FOREGROUND'] = float(APFunction.get_text(self, self.ui.inst_seg_fore_mask_th_input))
            if 'C' in APFunction.get_text(self,self.ui.inst_seg_data_channels_input):
                biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_MW_TH_CONTOUR'] = float(APFunction.get_text(self, self.ui.inst_seg_c_channel_th_input))
            if 'D' in APFunction.get_text(self,self.ui.inst_seg_data_channels_input):    
                biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_MW_TH_DISTANCE'] = float(APFunction.get_text(self, self.ui.inst_seg_d_channel_th_input))
            if 'P' in APFunction.get_text(self,self.ui.inst_seg_data_channels_input): 
                biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_MW_TH_POINTS'] = float(APFunction.get_text(self, self.ui.inst_seg_p_channel_th_input))
            if APFunction.get_text(self, self.ui.inst_seg_small_obj_fil_before_input) == "Yes":
                biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_REMOVE_BEFORE_MW'] = True
                biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_REMOVE_SMALL_OBJ_BEFORE'] = int(APFunction.get_text(self, self.ui.inst_seg_small_obj_fil_before_size_input))
            if APFunction.get_text(self, self.ui.inst_seg_small_obj_fil_after_input) == "Yes":
                biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_REMOVE_AFTER_MW'] = True
                biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_REMOVE_SMALL_OBJ_AFTER'] = int(APFunction.get_text(self, self.ui.inst_seg_small_obj_fil_after_size_input))
            if APFunction.get_text(self, self.ui.inst_seg_moph_op_input) != "[]":
                biapy_config['PROBLEM']['INSTANCE_SEG']['SEED_MORPH_SEQUENCE'] = ast.literal_eval(APFunction.get_text(self, self.ui.inst_seg_moph_op_input) )
            if APFunction.get_text(self, self.ui.inst_seg_moph_op_rad_input) != "[]":
                biapy_config['PROBLEM']['INSTANCE_SEG']['SEED_MORPH_RADIUS'] =  ast.literal_eval(APFunction.get_text(self, self.ui.inst_seg_moph_op_rad_input))
            if APFunction.get_text(self, self.ui.inst_seg_ero_dil_fore_input) == "Yes":
                biapy_config['PROBLEM']['INSTANCE_SEG']['ERODE_AND_DILATE_FOREGROUND'] = True
                biapy_config['PROBLEM']['INSTANCE_SEG']['FORE_EROSION_RADIUS'] = int(APFunction.get_text(self, self.ui.inst_seg_fore_dil_input))
                biapy_config['PROBLEM']['INSTANCE_SEG']['FORE_DILATION_RADIUS'] = int(APFunction.get_text(self, self.ui.inst_seg_fore_ero_input))

            # biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_MW_OPTIMIZE_THS'] = False
            # biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_CHECK_MW'] = True
            
        ### DETECTION
        elif selected_workflow == 2:
            biapy_config['PROBLEM']['DETECTION'] = {}
            biapy_config['PROBLEM']['DETECTION']['CENTRAL_POINT_DILATION'] = int(APFunction.get_text(self, self.ui.det_central_point_dilation_input))
            biapy_config['PROBLEM']['DETECTION']['CHECK_POINTS_CREATED'] = True if APFunction.get_text(self, self.ui.det_central_point_dilation_input) == "Yes" else False
            if APFunction.get_text(self, self.ui.det_data_watetshed_check_input) == "Yes" and APFunction.get_text(self, self.ui.det_watershed_input) == "Yes":
                biapy_config['PROBLEM']['DETECTION']['DATA_CHECK_MW'] = True

        ### DENOISING
        elif selected_workflow == 3:
            biapy_config['PROBLEM']['DENOISING'] = {}
            biapy_config['PROBLEM']['DENOISING']['N2V_PERC_PIX'] = float(APFunction.get_text(self, self.ui.deno_n2v_perc_pix_input))
            biapy_config['PROBLEM']['DENOISING']['N2V_MANIPULATOR'] = APFunction.get_text(self, self.ui.deno_n2v_manipulator_input)
            biapy_config['PROBLEM']['DENOISING']['N2V_NEIGHBORHOOD_RADIUS'] = int(APFunction.get_text(self, self.ui.deno_n2v_neighborhood_radius_input))
            biapy_config['PROBLEM']['DENOISING']['N2V_STRUCTMASK'] = True if APFunction.get_text(self, self.ui.deno_n2v_neighborhood_struct_input) == "Yes" else False

        ### SUPER_RESOLUTION
        elif selected_workflow == 4:
            biapy_config['PROBLEM']['SUPER_RESOLUTION'] = {}
            biapy_config['PROBLEM']['SUPER_RESOLUTION']['UPSCALING'] = int(APFunction.get_text(self, self.ui.sr_upscaling_input))

        ### SELF_SUPERVISED
        elif selected_workflow == 5:
            biapy_config['PROBLEM']['SELF_SUPERVISED'] = {}
            biapy_config['PROBLEM']['SELF_SUPERVISED']['RESIZING_FACTOR'] = int(APFunction.get_text(self, self.ui.ssl_resizing_factor_input))
            biapy_config['PROBLEM']['SELF_SUPERVISED']['NOISE'] = float(APFunction.get_text(self, self.ui.ssl_noise_input))

        # Dataset
        biapy_config['DATA'] = {}
        if APFunction.get_text(self, self.ui.check_gen_input) == "Yes":
            biapy_config['DATA']['CHECK_GENERATORS'] = True

        biapy_config['DATA']['PATCH_SIZE'] = APFunction.get_text(self, self.ui.patch_size_input)
        if APFunction.get_text(self, self.ui.extract_random_patch_input) == "Yes":
            biapy_config['DATA']['EXTRACT_RANDOM_PATCH'] = True
            if APFunction.get_text(self, self.ui.sem_seg_random_patch_prob_map_input) == "Yes":
                biapy_config['DATA']['PROBABILITY_MAP'] = True
                biapy_config['DATA']['W_FOREGROUND'] = float(APFunction.get_text(self, self.ui.sem_seg_random_patch_fore_weights_input))
                biapy_config['DATA']['W_BACKGROUND'] = float(APFunction.get_text(self, self.ui.sem_seg_random_patch_back_weights_input)) 
        else:
            biapy_config['DATA']['EXTRACT_RANDOM_PATCH'] = False

        if APFunction.get_text(self, self.ui.reflect_to_complete_shape_input) == "Yes":
            biapy_config['DATA']['REFLECT_TO_COMPLETE_SHAPE'] = True

        if APFunction.get_text(self, self.ui.normalization_type_input) == "custom":
            biapy_config['DATA']['NORMALIZATION'] = {}
            biapy_config['DATA']['NORMALIZATION']['TYPE'] = 'custom'
            biapy_config['DATA']['NORMALIZATION']['CUSTOM_MEAN'] = float(APFunction.get_text(self, self.ui.custom_mean_input)) 
            biapy_config['DATA']['NORMALIZATION']['CUSTOM_STD'] = float(APFunction.get_text(self, self.ui.custom_std_input)) 

        # Train
        if APFunction.get_text(self, self.ui.enable_train_input) == "Yes":
            biapy_config['DATA']['TRAIN'] = {}

            # biapy_config['DATA']['TRAIN']['CHECK_DATA'] = True
            
            biapy_config['DATA']['TRAIN']['IN_MEMORY'] = True if APFunction.get_text(self, self.ui.train_in_memory_comboBox) == "Yes" else False
            biapy_config['DATA']['TRAIN']['PATH'] = APFunction.get_text(self, self.ui.train_data_input)
            biapy_config['DATA']['TRAIN']['GT_PATH'] = APFunction.get_text(self, self.ui.train_data_gt_input)
            if int(APFunction.get_text(self, self.ui.replicate_data_input)) != 0:
                biapy_config['DATA']['TRAIN']['REPLICATE'] = int(APFunction.get_text(self, self.ui.replicate_data_input))
            biapy_config['DATA']['TRAIN']['OVERLAP'] = APFunction.get_text(self, self.ui.train_overlap_input)
            biapy_config['DATA']['TRAIN']['PADDING'] = APFunction.get_text(self, self.ui.train_padding_input)
            if APFunction.get_text(self, self.ui.train_resolution_input) != "(1,1,1)" and APFunction.get_text(self, self.ui.train_resolution_input) != "(1,1)":
                biapy_config['DATA']['TRAIN']['RESOLUTION'] = APFunction.get_text(self, self.ui.train_resolution_input)
            
            if selected_workflow == 0 and int(APFunction.get_text(self, self.ui.sem_seg_minimum_fore_percentage_input)) != 0:
                biapy_config['DATA']['TRAIN']['MINIMUM_FOREGROUND_PER'] = int(APFunction.get_text(self, self.ui.sem_seg_minimum_fore_percentage_input))
            if selected_workflow == 1 and int(APFunction.get_text(self, self.ui.inst_seg_minimum_fore_percentage_input)) != 0:
                biapy_config['DATA']['TRAIN']['MINIMUM_FOREGROUND_PER'] = int(APFunction.get_text(self, self.ui.inst_seg_minimum_fore_percentage_input))
            if selected_workflow == 2 and int(APFunction.get_text(self, self.ui.det_minimum_fore_percentage_input)) != 0:
                biapy_config['DATA']['TRAIN']['MINIMUM_FOREGROUND_PER'] = int(APFunction.get_text(self, self.ui.det_minimum_fore_percentage_input))
            
            # Validation
            biapy_config['DATA']['VAL'] = {}

            if APFunction.get_text(self, self.ui.validation_type_comboBox) == "Extract from train (split training)":
                biapy_config['DATA']['VAL']['FROM_TRAIN'] = True
                biapy_config['DATA']['VAL']['SPLIT_TRAIN'] = float(APFunction.get_text(self, self.ui.percentage_validation_input))
                biapy_config['DATA']['VAL']['RANDOM'] = True if APFunction.get_text(self, self.ui.random_val_input) == "Yes" else False 
            elif APFunction.get_text(self, self.ui.validation_type_comboBox) == "Extract from train (cross validation)":
                biapy_config['DATA']['VAL']['FROM_TRAIN'] = True
                biapy_config['DATA']['VAL']['CROSS_VAL'] = True
                biapy_config['DATA']['VAL']['CROSS_VAL_NFOLD'] = int(APFunction.get_text(self, self.ui.cross_validation_nfolds_input))
                biapy_config['DATA']['VAL']['CROSS_VAL_FOLD'] = int(APFunction.get_text(self, self.ui.cross_validation_fold_input))
                biapy_config['DATA']['VAL']['RANDOM'] = True if APFunction.get_text(self, self.ui.random_val_input) == "Yes" else False 
            # Not extracted from train (path needed)
            else:
                biapy_config['DATA']['VAL']['FROM_TRAIN'] = False
                biapy_config['DATA']['VAL']['IN_MEMORY'] = True if APFunction.get_text(self, self.ui.val_in_memory_comboBox) == "Yes" else False 
                biapy_config['DATA']['VAL']['PATH'] = APFunction.get_text(self, self.ui.validation_data_input)
                biapy_config['DATA']['VAL']['GT_PATH'] = APFunction.get_text(self, self.ui.validation_data_gt_input)
                biapy_config['DATA']['VAL']['OVERLAP'] = APFunction.get_text(self, self.ui.validation_overlap_input)
                biapy_config['DATA']['VAL']['PADDING'] = APFunction.get_text(self, self.ui.validation_padding_input)

            biapy_config['DATA']['VAL']['RESOLUTION'] = APFunction.get_text(self, self.ui.validation_resolution_input)

        # Test
        if APFunction.get_text(self, self.ui.enable_test_input) == "Yes":
            biapy_config['DATA']['TEST'] = {}
            # biapy_config['DATA']['TEST']['CHECK_DATA'] = True
            if APFunction.get_text(self, self.ui.test_data_in_memory_input) == "Yes":
                biapy_config['DATA']['TEST']['IN_MEMORY'] = True
            else:
                biapy_config['DATA']['TEST']['IN_MEMORY'] = False
            if APFunction.get_text(self, self.ui.use_val_as_test_input) == "Yes" and\
                APFunction.get_text(self, self.ui.validation_type_comboBox) == "Extract from train (cross validation)":
                biapy_config['DATA']['TEST']['USE_VAL_AS_TEST'] = True
            else:
                if APFunction.get_text(self, self.ui.test_exists_gt_input) == "Yes":
                    biapy_config['DATA']['TEST']['LOAD_GT'] = True
                    biapy_config['DATA']['TEST']['GT_PATH'] = APFunction.get_text(self, self.ui.test_data_gt_input)
                else:
                    biapy_config['DATA']['TEST']['LOAD_GT'] = False
                biapy_config['DATA']['TEST']['PATH'] = APFunction.get_text(self, self.ui.test_data_input)
                
            biapy_config['DATA']['TEST']['OVERLAP'] = APFunction.get_text(self, self.ui.test_overlap_input)
            biapy_config['DATA']['TEST']['PADDING'] = APFunction.get_text(self, self.ui.test_padding_input)
            if APFunction.get_text(self, self.ui.test_median_padding_input) == "Yes":
                biapy_config['DATA']['TEST']['MEDIAN_PADDING'] = True 
            biapy_config['DATA']['TEST']['RESOLUTION'] = APFunction.get_text(self, self.ui.test_resolution_input)
            if APFunction.get_text(self, self.ui.test_argmax_input) == "Yes":
                biapy_config['DATA']['TEST']['ARGMAX_TO_OUTPUT'] = True


        # Data augmentation (DA)
        biapy_config['AUGMENTOR'] = {}
        if APFunction.get_text(self, self.ui.da_enable_input) == "Yes":
            biapy_config['AUGMENTOR']['ENABLE'] = True  
            biapy_config['AUGMENTOR']['DA_PROB'] = float(APFunction.get_text(self, self.ui.da_prob_input))
            biapy_config['AUGMENTOR']['AUG_SAMPLES'] = True if APFunction.get_text(self, self.ui.da_check_input) == "Yes" else False 
            biapy_config['AUGMENTOR']['DRAW_GRID'] = True if APFunction.get_text(self, self.ui.da_draw_grid_input) == "Yes" else False 
            if int(APFunction.get_text(self, self.ui.da_num_samples_check_input)) != 10:
                biapy_config['AUGMENTOR']['AUG_NUM_SAMPLES'] = int(APFunction.get_text(self, self.ui.da_num_samples_check_input))
            biapy_config['AUGMENTOR']['SHUFFLE_TRAIN_DATA_EACH_EPOCH'] = True if APFunction.get_text(self, self.ui.da_shuffle_train_input) == "Yes" else False 
            biapy_config['AUGMENTOR']['SHUFFLE_VAL_DATA_EACH_EPOCH'] = True if APFunction.get_text(self, self.ui.da_shuffle_val_input) == "Yes" else False 
            if APFunction.get_text(self, self.ui.da_rot90_input) == "Yes":
                biapy_config['AUGMENTOR']['ROT90'] = True 
            if APFunction.get_text(self, self.ui.da_random_rot_input) == "Yes":
                biapy_config['AUGMENTOR']['RANDOM_ROT'] = True  
                biapy_config['AUGMENTOR']['RANDOM_ROT_RANGE'] = APFunction.get_text(self, self.ui.da_random_rot_range_input)
            if APFunction.get_text(self, self.ui.da_shear_input) == "Yes":
                biapy_config['AUGMENTOR']['SHEAR'] = True  
                biapy_config['AUGMENTOR']['SHEAR_RANGE'] = APFunction.get_text(self, self.ui.da_shear_range_input)
            if APFunction.get_text(self, self.ui.da_zoom_input) == "Yes":
                biapy_config['AUGMENTOR']['ZOOM'] = True  
                biapy_config['AUGMENTOR']['ZOOM_RANGE'] = APFunction.get_text(self, self.ui.da_zoom_range_input)
            if APFunction.get_text(self, self.ui.da_shift_input) == "Yes":
                biapy_config['AUGMENTOR']['SHIFT'] = True 
                biapy_config['AUGMENTOR']['SHIFT_RANGE'] = APFunction.get_text(self, self.ui.da_shift_range_input)
            if APFunction.get_text(self, self.ui.da_shift_input) == "Yes" or APFunction.get_text(self, self.ui.da_zoom_input) == "Yes" or\
                APFunction.get_text(self, self.ui.da_shear_input) == "Yes" or APFunction.get_text(self, self.ui.da_random_rot_input) == "Yes":
                biapy_config['AUGMENTOR']['AFFINE_MODE'] = APFunction.get_text(self, self.ui.da_affine_mode_input)
            if APFunction.get_text(self, self.ui.da_vertical_flip_input) == "Yes":
                biapy_config['AUGMENTOR']['VFLIP'] = True 
            if APFunction.get_text(self, self.ui.da_horizontal_flip_input) == "Yes":
                biapy_config['AUGMENTOR']['HFLIP'] = True 
            if APFunction.get_text(self, self.ui.da_z_flip_input) == "Yes":
                biapy_config['AUGMENTOR']['ZFLIP'] = True 
            if APFunction.get_text(self, self.ui.da_elastic_input) == "Yes":
                biapy_config['AUGMENTOR']['ELASTIC'] = True 
                biapy_config['AUGMENTOR']['E_ALPHA'] = APFunction.get_text(self, self.ui.da_elastic_alpha_input)
                biapy_config['AUGMENTOR']['E_SIGMA'] = int(APFunction.get_text(self, self.ui.da_elastic_sigma_input))
                biapy_config['AUGMENTOR']['E_MODE'] = APFunction.get_text(self, self.ui.da_elastic_mode_input)
            if APFunction.get_text(self, self.ui.da_gaussian_blur_input) == "Yes":
                biapy_config['AUGMENTOR']['G_BLUR'] = True 
                biapy_config['AUGMENTOR']['G_SIGMA'] = APFunction.get_text(self, self.ui.da_gaussian_sigma_input)
            if APFunction.get_text(self, self.ui.da_median_blur_input) == "Yes":
                biapy_config['AUGMENTOR']['MEDIAN_BLUR'] = True 
                biapy_config['AUGMENTOR']['MB_KERNEL'] = APFunction.get_text(self, self.ui.da_median_blur_k_size_input)
            if APFunction.get_text(self, self.ui.da_motion_blur_input) == "Yes":
                biapy_config['AUGMENTOR']['MOTION_BLUR'] = True 
                biapy_config['AUGMENTOR']['MOTB_K_RANGE'] = APFunction.get_text(self, self.ui.da_motion_blur_k_size_input)
            if APFunction.get_text(self, self.ui.da_gamma_contrast_input) == "Yes":
                biapy_config['AUGMENTOR']['GAMMA_CONTRAST'] = True
                biapy_config['AUGMENTOR']['GC_GAMMA'] = APFunction.get_text(self, self.ui.da_gamma_contrast_range_input)
            if APFunction.get_text(self, self.ui.da_brightness_input) == "Yes":
                biapy_config['AUGMENTOR']['BRIGHTNESS'] = True
                biapy_config['AUGMENTOR']['BRIGHTNESS_FACTOR'] = APFunction.get_text(self, self.ui.da_brightness_factor_range_input)
                biapy_config['AUGMENTOR']['BRIGHTNESS_MODE'] = APFunction.get_text(self, self.ui.da_brightness_mode_input)
            if APFunction.get_text(self, self.ui.da_contrast_input) == "Yes":
                biapy_config['AUGMENTOR']['CONTRAST'] = True
                biapy_config['AUGMENTOR']['CONTRAST_FACTOR'] = APFunction.get_text(self, self.ui.da_contrast_factor)
                biapy_config['AUGMENTOR']['CONTRAST_MODE'] = APFunction.get_text(self, self.ui.da_contrast_mode_input)
            if APFunction.get_text(self, self.ui.da_brightness_em_input) == "Yes":
                biapy_config['AUGMENTOR']['BRIGHTNESS_EM'] = True
                biapy_config['AUGMENTOR']['BRIGHTNESS_EM_FACTOR'] = APFunction.get_text(self, self.ui.da_brightness_em_factor_input)
                biapy_config['AUGMENTOR']['BRIGHTNESS_EM_MODE'] = APFunction.get_text(self, self.ui.da_brightness_em_mode_input)
            if APFunction.get_text(self, self.ui.da_contrast_em_input) == "Yes":
                biapy_config['AUGMENTOR']['CONTRAST_EM'] = True
                biapy_config['AUGMENTOR']['CONTRAST_EM_FACTOR'] = APFunction.get_text(self, self.ui.da_contrast_em_factor_input)
                biapy_config['AUGMENTOR']['CONTRAST_EM_MODE'] = APFunction.get_text(self, self.ui.da_contrast_em_mode_input)
            if APFunction.get_text(self, self.ui.da_dropout_input) == "Yes":
                biapy_config['AUGMENTOR']['DROPOUT'] = True
                biapy_config['AUGMENTOR']['DROP_RANGE'] = APFunction.get_text(self, self.ui.da_dropout_range_input)
            if APFunction.get_text(self, self.ui.da_cutout_input) == "Yes":
                biapy_config['AUGMENTOR']['CUTOUT'] = True
                biapy_config['AUGMENTOR']['COUT_NB_ITERATIONS'] = APFunction.get_text(self, self.ui.da_cutout_number_iterations_input)
                biapy_config['AUGMENTOR']['COUT_SIZE'] = APFunction.get_text(self, self.ui.da_cutout_size_input)
                biapy_config['AUGMENTOR']['COUT_CVAL'] = float(APFunction.get_text(self, self.ui.da_cuout_cval_input))
                biapy_config['AUGMENTOR']['COUT_APPLY_TO_MASK'] = True if APFunction.get_text(self, self.ui.da_cutout_to_mask_input) == "Yes" else False 
            if APFunction.get_text(self, self.ui.da_cutblur_input) == "Yes":
                biapy_config['AUGMENTOR']['CUTBLUR'] = True
                biapy_config['AUGMENTOR']['CBLUR_SIZE'] = APFunction.get_text(self, self.ui.da_cutblur_size_range_input)
                biapy_config['AUGMENTOR']['CBLUR_DOWN_RANGE'] = APFunction.get_text(self, self.ui.da_cutblut_down_range_input)
                biapy_config['AUGMENTOR']['CBLUR_INSIDE'] = True if APFunction.get_text(self, self.ui.da_cutblur_inside_input) == "Yes" else False 
            if APFunction.get_text(self, self.ui.da_cutmix_input) == "Yes":
                biapy_config['AUGMENTOR']['CUTMIX'] = True
                biapy_config['AUGMENTOR']['CMIX_SIZE'] = APFunction.get_text(self, self.ui.da_cutmix_size_range_input)
            if APFunction.get_text(self, self.ui.da_cutnoise_input) == "Yes":
                biapy_config['AUGMENTOR']['CUTNOISE'] = True
                biapy_config['AUGMENTOR']['CNOISE_SCALE'] = APFunction.get_text(self, self.ui.da_cutnoise_scale_range_input)
                biapy_config['AUGMENTOR']['CNOISE_NB_ITERATIONS'] = APFunction.get_text(self, self.ui.da_cutnoise_number_iter_input)
                biapy_config['AUGMENTOR']['CNOISE_SIZE'] = APFunction.get_text(self, self.ui.da_cutnoise_size_range_input)
            if APFunction.get_text(self, self.ui.da_misaligment_input) == "Yes":
                biapy_config['AUGMENTOR']['MISALIGNMENT'] = True
                biapy_config['AUGMENTOR']['MS_DISPLACEMENT'] = int(APFunction.get_text(self, self.ui.da_misaligment_displacement_input))
                biapy_config['AUGMENTOR']['MS_ROTATE_RATIO'] = float(APFunction.get_text(self, self.ui.da_misaligment_rotate_ratio_input))
            if APFunction.get_text(self, self.ui.da_missing_sections_input) == "Yes":
                biapy_config['AUGMENTOR']['MISSING_SECTIONS'] = True
                biapy_config['AUGMENTOR']['MISSP_ITERATIONS'] = APFunction.get_text(self, self.ui.da_missing_sections_iteration_range_input)
            if APFunction.get_text(self, self.ui.da_grayscale_input) == "Yes":
                biapy_config['AUGMENTOR']['GRAYSCALE'] = True
            if APFunction.get_text(self, self.ui.da_channel_shuffle_input) == "Yes":
                biapy_config['AUGMENTOR']['CHANNEL_SHUFFLE'] = True
            if APFunction.get_text(self, self.ui.da_gridmask_input) == "Yes":
                biapy_config['AUGMENTOR']['GRIDMASK'] = True
                biapy_config['AUGMENTOR']['GRID_RATIO'] = float(APFunction.get_text(self, self.ui.da_grid_ratio_input))
                biapy_config['AUGMENTOR']['GRID_D_RANGE'] = APFunction.get_text(self, self.ui.da_grid_d_range_input)
                biapy_config['AUGMENTOR']['GRID_ROTATE'] = float(APFunction.get_text(self, self.ui.da_grid_rotate_input))
                biapy_config['AUGMENTOR']['GRID_INVERT'] = True if APFunction.get_text(self, self.ui.da_grid_invert_input) == "Yes" else False 
            if APFunction.get_text(self, self.ui.da_gaussian_noise_input) == "Yes":
                biapy_config['AUGMENTOR']['GAUSSIAN_NOISE'] = True
                biapy_config['AUGMENTOR']['GAUSSIAN_NOISE_MEAN'] = float(APFunction.get_text(self, self.ui.da_gaussian_noise_mean_input))
                biapy_config['AUGMENTOR']['GAUSSIAN_NOISE_VAR'] = float(APFunction.get_text(self, self.ui.da_gaussian_noise_var_input))
                biapy_config['AUGMENTOR']['GAUSSIAN_NOISE_USE_INPUT_IMG_MEAN_AND_VAR'] = True if APFunction.get_text(self, self.ui.da_gaussian_noise_use_input_img_input) == "Yes" else False 
            if APFunction.get_text(self, self.ui.da_poisson_noise_input) == "Yes":
                biapy_config['AUGMENTOR']['POISSON_NOISE'] = True
            if APFunction.get_text(self, self.ui.da_salt_input) == "Yes":
                biapy_config['AUGMENTOR']['SALT'] = True
                biapy_config['AUGMENTOR']['SALT_AMOUNT'] = float(APFunction.get_text(self, self.ui.da_salt_amount_input))
            if APFunction.get_text(self, self.ui.da_pepper_input) == "Yes":
                biapy_config['AUGMENTOR']['PEPPER'] = True
                biapy_config['AUGMENTOR']['PEPPER_AMOUNT'] = float(APFunction.get_text(self, self.ui.da_pepper_amount_input))
            if APFunction.get_text(self, self.ui.da_salt_pepper_input) == "Yes":
                biapy_config['AUGMENTOR']['SALT_AND_PEPPER'] = True
                biapy_config['AUGMENTOR']['SALT_AND_PEPPER_AMOUNT'] = float(APFunction.get_text(self, self.ui.da_salt_pepper_amount_input))
                biapy_config['AUGMENTOR']['SALT_AND_PEPPER_PROP'] = float(APFunction.get_text(self, self.ui.da_salt_pepper_prop_input))
        else:
            biapy_config['AUGMENTOR']['ENABLE'] = False

        # Model definition
        biapy_config['MODEL'] = {}
        biapy_config['MODEL']['ARCHITECTURE'] = APFunction.get_text(self, self.ui.model_input)
        if APFunction.get_text(self, self.ui.model_input) in ['unet', 'resunet', 'seunet', 'attention_unet']:
            biapy_config['MODEL']['FEATURE_MAPS'] = ast.literal_eval(APFunction.get_text(self, self.ui.feature_maps_input))
            if APFunction.get_text(self, self.ui.spatial_dropout_input) == "Yes":
                biapy_config['MODEL']['SPATIAL_DROPOUT'] = True  
            biapy_config['MODEL']['DROPOUT_VALUES'] = ast.literal_eval(APFunction.get_text(self, self.ui.dropout_input)) 
            biapy_config['MODEL']['BATCH_NORMALIZATION'] = True if APFunction.get_text(self, self.ui.batch_normalization_input) == "Yes" else False 
            if APFunction.get_text(self, self.ui.kernel_init_input) != "he_normal":
                biapy_config['MODEL']['KERNEL_INIT'] = APFunction.get_text(self, self.ui.kernel_init_input)
            if int(APFunction.get_text(self, self.ui.kernel_size_input)) != 3:
                biapy_config['MODEL']['KERNEL_SIZE'] = int(APFunction.get_text(self, self.ui.kernel_size_input))
            if APFunction.get_text(self, self.ui.upsample_layer_input) != "convtranspose":
                biapy_config['MODEL']['UPSAMPLE_LAYER'] = APFunction.get_text(self, self.ui.upsample_layer_input) 
            if APFunction.get_text(self, self.ui.activation_input) != 'elu':
                biapy_config['MODEL']['ACTIVATION'] = APFunction.get_text(self, self.ui.activation_input)
            if APFunction.get_text(self, self.ui.last_activation_input) != 'sigmoid':
                biapy_config['MODEL']['LAST_ACTIVATION'] = APFunction.get_text(self, self.ui.last_activation_input)
            biapy_config['MODEL']['N_CLASSES'] = int(APFunction.get_text(self, self.ui.number_of_classes_input))
            biapy_config['MODEL']['Z_DOWN'] = ast.literal_eval(APFunction.get_text(self, self.ui.z_down_input)) 
        elif APFunction.get_text(self, self.ui.model_input) == "tiramisu":
            biapy_config['MODEL']['TIRAMISU_DEPTH'] = int(APFunction.get_text(self, self.ui.tiramisu_depth_input))
            biapy_config['MODEL']['FEATURE_MAPS'] = int(APFunction.get_text(self, self.ui.tiramisu_feature_maps_input))
            biapy_config['MODEL']['DROPOUT_VALUES'] = float(APFunction.get_text(self, self.ui.tiramisu_dropout_input))
        elif APFunction.get_text(self, self.ui.model_input) == "unetr":
            biapy_config['MODEL']['UNETR_TOKEN_SIZE'] = int(APFunction.get_text(self, self.ui.unetr_token_size_input))
            biapy_config['MODEL']['UNETR_EMBED_DIM'] = int(APFunction.get_text(self, self.ui.unetr_embed_dims_input))
            biapy_config['MODEL']['UNETR_DEPTH'] = int(APFunction.get_text(self, self.ui.unetr_depth_input))
            biapy_config['MODEL']['UNETR_MLP_HIDDEN_UNITS'] = ast.literal_eval(APFunction.get_text(self, self.ui.unetr_mlp_hidden_units_input))
            biapy_config['MODEL']['UNETR_NUM_HEADS'] = int(APFunction.get_text(self, self.ui.unetr_num_heads_input))
            biapy_config['MODEL']['UNETR_VIT_HIDD_MULT'] = int(APFunction.get_text(self, self.ui.unetr_vit_hidden_multiple_input)) 

        if APFunction.get_text(self, self.ui.checkpoint_load_input) == "Yes":
            biapy_config['MODEL']['LOAD_CHECKPOINT'] = True 
            biapy_config['PATHS'] = {}
            if APFunction.get_text(self, self.ui.checkpoint_file_path_input) != "":
                biapy_config['PATHS']['CHECKPOINT_FILE'] = APFunction.get_text(self, self.ui.checkpoint_file_path_input)

        # Loss (in detection only)
        if selected_workflow == 2:
            biapy_config['LOSS'] = {}
            biapy_config['LOSS']['TYPE'] = APFunction.get_text(self, self.ui.det_loss_type_input)

        # Training phase
        biapy_config['TRAIN'] = {}
        if APFunction.get_text(self, self.ui.enable_train_input) == "Yes":
            biapy_config['TRAIN']['ENABLE'] = True 
            biapy_config['TRAIN']['OPTIMIZER'] = APFunction.get_text(self, self.ui.optimizer_input)
            biapy_config['TRAIN']['LR'] = float(APFunction.get_text(self, self.ui.learning_rate_input))
            biapy_config['TRAIN']['BATCH_SIZE'] = int(APFunction.get_text(self, self.ui.batch_size_input))
            biapy_config['TRAIN']['EPOCHS'] = int(APFunction.get_text(self, self.ui.number_of_epochs_input)) 
            biapy_config['TRAIN']['PATIENCE'] = int(APFunction.get_text(self, self.ui.patience_input))

            # LR Scheduler
            if APFunction.get_text(self, self.ui.lr_schel_input) != "":
                biapy_config['TRAIN']['LR_SCHEDULER'] = {}
                biapy_config['TRAIN']['LR_SCHEDULER']['NAME'] = APFunction.get_text(self, self.ui.lr_schel_input) 
                if APFunction.get_text(self, self.ui.lr_schel_input) in ["warmupcosine","reduceonplateau"]: 
                    biapy_config['TRAIN']['LR_SCHEDULER']['MIN_LR'] = float(APFunction.get_text(self, self.ui.lr_schel_min_lr_input)) 
                if APFunction.get_text(self, self.ui.lr_schel_input) == "reduceonplateau": 
                    biapy_config['TRAIN']['LR_SCHEDULER']['REDUCEONPLATEAU_FACTOR'] = float(APFunction.get_text(self, self.ui.lr_schel_reduce_on_plat_factor_input)) 
                    biapy_config['TRAIN']['LR_SCHEDULER']['REDUCEONPLATEAU_PATIENCE'] = int(APFunction.get_text(self, self.ui.lr_schel_reduce_on_plat_patience_input))
                if APFunction.get_text(self, self.ui.lr_schel_input) == "warmupcosine":  
                    biapy_config['TRAIN']['LR_SCHEDULER']['WARMUP_COSINE_DECAY_LR'] = float(APFunction.get_text(self, self.ui.lr_schel_warmupcosine_lr_input))
                    biapy_config['TRAIN']['LR_SCHEDULER']['WARMUP_COSINE_DECAY_EPOCHS'] = int(APFunction.get_text(self, self.ui.lr_schel_warmupcosine_epochs_input))
                    biapy_config['TRAIN']['LR_SCHEDULER']['WARMUP_COSINE_DECAY_HOLD_EPOCHS'] = int(APFunction.get_text(self, self.ui.lr_schel_warmupcosine_hold_epochs_input))

            # Callbacks
            if APFunction.get_text(self, self.ui.early_stopping_input) != 'val_loss':
                biapy_config['TRAIN']['EARLYSTOPPING_MONITOR'] = APFunction.get_text(self, self.ui.early_stopping_input) 
            if APFunction.get_text(self, self.ui.checkpoint_monitor_input) != 'val_loss':
                biapy_config['TRAIN']['CHECKPOINT_MONITOR'] = APFunction.get_text(self, self.ui.checkpoint_monitor_input)
            if APFunction.get_text(self, self.ui.profiler_input) == "Yes": 
                biapy_config['TRAIN']['PROFILER'] = True 
                biapy_config['TRAIN']['PROFILER_BATCH_RANGE'] = APFunction.get_text(self, self.ui.profiler_batch_range_input)
        else:
            biapy_config['TRAIN']['ENABLE'] = False 

        # Test
        biapy_config['TEST'] = {}
        if APFunction.get_text(self, self.ui.enable_test_input) == "Yes":    
            biapy_config['TEST']['ENABLE'] = True  
            biapy_config['TEST']['REDUCE_MEMORY'] = True if APFunction.get_text(self, self.ui.test_reduce_memory_input) == "Yes" else False 
            biapy_config['TEST']['VERBOSE'] = True if APFunction.get_text(self, self.ui.test_verbose_input) == "Yes" else False 
            biapy_config['TEST']['AUGMENTATION'] = True if APFunction.get_text(self, self.ui.test_tta_input) == "Yes" else False
            if APFunction.get_text(self, self.ui.test_evaluate_input) == "Yes" :
                biapy_config['TEST']['EVALUATE'] = True 
            if APFunction.get_text(self, self.ui.test_2d_as_3d_stack_input) == "Yes" and APFunction.get_text(self, self.ui.dimensions_comboBox) == "2D":
                biapy_config['TEST']['ANALIZE_2D_IMGS_AS_3D_STACK'] = True

            biapy_config['TEST']['STATS'] = {}
            biapy_config['TEST']['STATS']['PER_PATCH'] = True if APFunction.get_text(self, self.ui.test_per_patch_input) == "Yes" else False 
            biapy_config['TEST']['STATS']['MERGE_PATCHES'] = True if APFunction.get_text(self, self.ui.test_merge_patches_input) == "Yes" else False 
            if APFunction.get_text(self, self.ui.test_full_image_input) == "Yes" and APFunction.get_text(self, self.ui.dimensions_comboBox) == "2D":
                biapy_config['TEST']['STATS']['FULL_IMG'] = True 

            ### Instance segmentation
            if selected_workflow == 1:
                biapy_config['TEST']['MATCHING_STATS'] = True if APFunction.get_text(self, self.ui.inst_seg_matching_stats_input) == "Yes" else False 
                biapy_config['TEST']['MATCHING_STATS_THS'] = ast.literal_eval(APFunction.get_text(self, self.ui.inst_seg_matching_stats_ths_input)) 
                if APFunction.get_text(self, self.ui.inst_seg_matching_stats_colores_img_ths_input) != "[0.3]":
                    biapy_config['TEST']['MATCHING_STATS_THS_COLORED_IMG'] = ast.literal_eval(APFunction.get_text(self, self.ui.inst_seg_matching_stats_colores_img_ths_input))
                # biapy_config['TEST']['MATCHING_SEGCOMPARE'] = False 

            ### Detection
            elif selected_workflow == 2:
                biapy_config['TEST']['DET_LOCAL_MAX_COORDS'] = True if APFunction.get_text(self, self.ui.det_local_max_coords_input) == "Yes" else False 
                biapy_config['TEST']['DET_MIN_TH_TO_BE_PEAK'] = ast.literal_eval(APFunction.get_text(self, self.ui.det_min_th_to_be_peak_input))
                biapy_config['TEST']['DET_TOLERANCE'] = ast.literal_eval(APFunction.get_text(self, self.ui.det_tolerance_input))

            # Post-processing
            biapy_config['TEST']['POST_PROCESSING'] = {}
            ### Semantic segmentation
            if selected_workflow == 0:
                if APFunction.get_text(self, self.ui.sem_seg_yz_filtering_input) == "Yes":
                    biapy_config['TEST']['POST_PROCESSING']['YZ_FILTERING'] = True 
                    biapy_config['TEST']['POST_PROCESSING']['YZ_FILTERING_SIZE'] = int(APFunction.get_text(self, self.ui.sem_seg_yz_filtering_size_input))
                if APFunction.get_text(self, self.ui.sem_seg_z_filtering_input) == "Yes":
                    biapy_config['TEST']['POST_PROCESSING']['Z_FILTERING'] = True 
                    biapy_config['TEST']['POST_PROCESSING']['Z_FILTERING_SIZE'] = int(APFunction.get_text(self, self.ui.sem_seg_z_filtering_size_input))
            ### Instance segmentation
            elif selected_workflow == 1:
                if APFunction.get_text(self, self.ui.inst_seg_yz_filtering_input) == "Yes":
                    biapy_config['TEST']['POST_PROCESSING']['YZ_FILTERING'] = True 
                    biapy_config['TEST']['POST_PROCESSING']['YZ_FILTERING_SIZE'] = int(APFunction.get_text(self, self.ui.inst_seg_yz_filtering_size_input))
                if APFunction.get_text(self, self.ui.inst_seg_z_filtering_input) == "Yes":
                    biapy_config['TEST']['POST_PROCESSING']['Z_FILTERING'] = True
                    biapy_config['TEST']['POST_PROCESSING']['Z_FILTERING_SIZE'] = int(APFunction.get_text(self, self.ui.inst_seg_z_filtering_size_input))
                if float(APFunction.get_text(self, self.ui.inst_seg_circularity_filtering_input)) != -1:
                    biapy_config['TEST']['POST_PROCESSING']['WATERSHED_CIRCULARITY'] = float(APFunction.get_text(self, self.ui.inst_seg_circularity_filtering_input))
                if APFunction.get_text(self, self.ui.inst_seg_data_channels_input) in ["BC", "BCM"] and APFunction.get_text(self, self.ui.inst_seg_voronoi_input) == "Yes":
                    biapy_config['TEST']['POST_PROCESSING']['VORONOI_ON_MASK'] = True 
                if APFunction.get_text(self, self.ui.inst_seg_data_channels_input) == "BP":
                    if int(APFunction.get_text(self, self.ui.inst_seg_repare_large_blobs_input)) != -1:
                        biapy_config['TEST']['POST_PROCESSING']['REPARE_LARGE_BLOBS_SIZE'] = int(APFunction.get_text(self, self.ui.inst_seg_repare_large_blobs_input))
                    if APFunction.get_text(self, self.ui.inst_seg_remove_close_points_input) == "Yes":
                        biapy_config['TEST']['POST_PROCESSING']['REMOVE_CLOSE_POINTS'] = True 
                        biapy_config['TEST']['POST_PROCESSING']['REMOVE_CLOSE_POINTS_RADIUS'] = ast.literal_eval(APFunction.get_text(self, self.ui.inst_seg_remove_close_points_radius_input))
            ### Detection
            elif selected_workflow == 2:
                if APFunction.get_text(self, self.ui.det_yz_filtering_input) == "Yes":
                    biapy_config['TEST']['POST_PROCESSING']['YZ_FILTERING'] = True 
                    biapy_config['TEST']['POST_PROCESSING']['YZ_FILTERING_SIZE'] = int(APFunction.get_text(self, self.ui.det_yz_filtering_size_input))
                if APFunction.get_text(self, self.ui.det_z_filtering_input) == "Yes":
                    biapy_config['TEST']['POST_PROCESSING']['Z_FILTERING'] = True 
                    biapy_config['TEST']['POST_PROCESSING']['Z_FILTERING_SIZE'] = int(APFunction.get_text(self, self.ui.det_z_filtering_size_input))
                if APFunction.get_text(self, self.ui.det_remove_close_points_input) == "Yes":
                    biapy_config['TEST']['POST_PROCESSING']['REMOVE_CLOSE_POINTS'] = True 
                    biapy_config['TEST']['POST_PROCESSING']['REMOVE_CLOSE_POINTS_RADIUS'] = float(APFunction.get_text(self, self.ui.det_remove_close_points_radius_input))
                if APFunction.get_text(self, self.ui.det_watershed_input) == "Yes":
                    biapy_config['TEST']['POST_PROCESSING']['DET_WATERSHED'] = True
                    biapy_config['TEST']['POST_PROCESSING']['DET_WATERSHED_FIRST_DILATION'] = ast.literal_eval(APFunction.get_text(self, self.ui.det_watershed_first_dilation_input) )
                    biapy_config['TEST']['POST_PROCESSING']['DET_WATERSHED_DONUTS_CLASSES'] = ast.literal_eval(APFunction.get_text(self, self.ui.det_watershed_donuts_classes_input) )
                    biapy_config['TEST']['POST_PROCESSING']['DET_WATERSHED_DONUTS_PATCH'] = ast.literal_eval(APFunction.get_text(self, self.ui.det_watershed_donuts_patch_input) )
                    biapy_config['TEST']['POST_PROCESSING']['DET_WATERSHED_DONUTS_NUCLEUS_DIAMETER'] = int(APFunction.get_text(self, self.ui.det_watershed_donuts_nucleus_diam_input)) 
            if APFunction.get_text(self, self.ui.test_apply_bin_mask_input) == "Yes":
                biapy_config['TEST']['POST_PROCESSING']['APPLY_MASK'] = True   

            if not biapy_config['TEST']['POST_PROCESSING']:
                del biapy_config['TEST']['POST_PROCESSING']
        else:
            biapy_config['TEST']['ENABLE'] = False

        # Checking the directory
        if yaml_config_file_path == "":
            self.errorexec("YAML file path must be defined", "yaml_config_file_path")
            return True
        if not os.path.exists(yaml_config_file_path):
            self.errorexec("The directory '{}' does not exist. That folder was selected to store the YAML file"\
                .format(yaml_config_file_path), "yaml_config_file_path")
            return True

        # Checking YAML file name
        yaml_config_filename = APFunction.get_text(self, self.ui.goptions_yaml_name_input)
        if yaml_config_filename == "":
            self.errorexec("The YAML filename must be defined", "goptions_yaml_name_input")
            return True
        if not yaml_config_filename.endswith(".yaml") and not yaml_config_filename.endswith(".yml"):
            self.errorexec("The YAML filename must have .yaml or .yml extension. You should change it to: {}"\
                .format(yaml_config_filename+".yaml"), "goptions_yaml_name_input")
            return True

        # Writing YAML file
        with open(os.path.join(yaml_config_file_path, yaml_config_filename), 'w') as outfile:
            yaml.dump(biapy_config, outfile, default_flow_style=False)

        # Update GUI with the new YAML file path
        self.ui.select_yaml_name_label.setText(os.path.join(yaml_config_file_path, yaml_config_filename))

        # Load configuration
        APFunction.load_yaml_config(self, False)
        
        # Advise user where the YAML file has been saved 
        message = "{}".format(os.path.join(yaml_config_file_path, yaml_config_filename))
        self.dialogexec(message)
            
        return False

    def load_yaml_config(self, checks=True):
        global yaml_config_file_path
        global biapy_cfg

        if checks:
            if yaml_config_filename == "":
                self.errorexec("A YAML file must be selected", "select_yaml_name_label")
                return
            yaml_file = APFunction.get_text(self, self.ui.select_yaml_name_label)
            if not os.path.exists(yaml_file):
                self.errorexec("The YAML file does not exist!", "select_yaml_name_label")
            if not str(yaml_file).endswith(".yaml") and not str(yaml_file).endswith(".yml"):
                self.errorexec("The YAML filename must have .yaml or .yml extension", "select_yaml_name_label")

        biapy_cfg = Config("/home/","jobname")
        
        errors = ""
        try:
            biapy_cfg._C.merge_from_file(os.path.join(yaml_config_file_path, yaml_config_filename))
            biapy_cfg = biapy_cfg.get_cfg_defaults()
            check_configuration(biapy_cfg)
        except Exception as errors:   
            errors = str(errors)
            self.ui.check_yaml_file_errors_label.setText(errors)
            self.ui.check_yaml_file_errors_frame.setStyleSheet("border: 2px solid red;")    
        else:
            self.ui.check_yaml_file_errors_label.setText("No errors found in the YAML file")
            self.ui.check_yaml_file_errors_frame.setStyleSheet("")

    def check_docker(self):
        global docker_found
        try:
            # Needs user to be added to Docker group: 
            # Linux: 
            #       sudo usermod -aG docker $USER
            #       newgrp docker
            docker_client = docker.from_env()
            docker_found = True
        except:
            docker_found = False
            print(traceback.format_exc())

        if docker_found:
            self.ui.docker_status_label.setText("<br>Docker installation found. You are ready to run BiaPy!")
            self.ui.dependencies_label.setText("Dependency check")
            self.ui.docker_frame.setStyleSheet("")
        else:
            self.ui.docker_status_label.setText("Docker installation not found. Please, install it before running BiaPy in its\
                 <a href=\"https://docs.docker.com/get-docker/\">official documentation</a>. Once you have done that please\
                  restart this application.")
            self.ui.dependencies_label.setText("Dependency error")
            self.ui.docker_frame.setStyleSheet("#docker_frame { border: 3px solid red; }")

    def run_biapy(self, biapy_container_name="none"):
        global output_folder
        global running_containers
        global biapy_cfg

        # Load the YAML file selected
        APFunction.load_yaml_config(self)

        # Job name check
        jobname = APFunction.get_text(self, self.ui.job_name_input)
        if jobname == "":
            self.errorexec("Job name can not be empty", "jobname")
            return
        if os.path.basename(APFunction.get_text(self, self.ui.select_yaml_name_label)) == jobname:
            self.errorexec("Job name can not have the same name as the YAML configuration file", "jobname")
            return

        # Output folder check
        if output_folder == "":
            self.errorexec("Output folder must be defined", "output_folder")
            return 

        # Docker installation check
        if not docker_found:
            self.errorexec("Docker installation not found. Please, install it before running BiaPy in its\
                 <a href=\"https://docs.docker.com/get-docker/\">official documentation</a>. Once you have \
                 done that please restart this application.", "docker_installation")
            return

        running_threads.append(QThread())
        worker_id = len(running_workers)
        running_workers.append(Worker(self, biapy_cfg, biapy_container_name, worker_id))
        running_workers[worker_id].moveToThread(running_threads[worker_id])
        running_threads[worker_id].started.connect(running_workers[worker_id].run)
        running_workers[worker_id].finished_signal.connect(running_threads[worker_id].quit)
        running_workers[worker_id].finished_signal.connect(running_workers[worker_id].deleteLater)
        running_threads[worker_id].finished.connect(running_threads[worker_id].deleteLater)
        
        # Only the main thread can touch the GUI
        def update_gui(signal):
            # Initialize the GUI
            if signal == 0:
                running_workers[worker_id].init_gui()
            elif signal == 1:
                running_workers[worker_id].gui.update_log()
            else:
                print("Nothing")

        running_workers[worker_id].update_log_signal.connect(update_gui)
        running_workers[worker_id].update_cont_state_signal.connect(running_workers[worker_id].gui.update_cont_state)
        running_workers[worker_id].update_train_progress_signal.connect(running_workers[worker_id].gui.update_train_progress)
        running_workers[worker_id].update_test_progress_signal.connect(running_workers[worker_id].gui.update_test_progress)
        running_threads[worker_id].start()

class runBiaPy_Ui(QDialog):
    def __init__(self, parent_worker):
        super(runBiaPy_Ui, self).__init__()
        self.run_window = Ui_RunBiaPy()
        self.parent_worker = parent_worker
        self.run_window.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.run_window.bn_min.clicked.connect(lambda: self.showMinimized())
        self.run_window.bn_close.clicked.connect(lambda: self.close_all())
        self.run_window.bn_close.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","closeAsset 43.png"))))
        self.run_window.bn_min.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","hideAsset 53.png"))))
        self.run_window.stop_container_bn.clicked.connect(lambda: self.parent_worker.stop_worker())
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

    def set_out_file(self, container_stdout_file):
        self.container_stdout_file = container_stdout_file

    def close_all(self):
        self.parent_worker.stop_worker()
        self.parent_worker.finished_signal.emit()
        self.close()
        
    def init_log(self, container_info):
        self.run_window.biapy_container_info_label.setText(container_info)
        self.run_window.run_biapy_log.setText(' ')

    def update_log(self):
        finished_good = False
        with open(self.container_stdout_file, 'r') as f:
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

class Worker(QObject):
    finished_signal = QtCore.Signal()
    update_log_signal = QtCore.Signal(int)
    update_cont_state_signal = QtCore.Signal(int)
    update_train_progress_signal = QtCore.Signal(int)
    update_test_progress_signal = QtCore.Signal(int)

    def __init__(self, main_gui, config, container_name, worker_id):
        super(Worker, self).__init__()
        self.main_gui = main_gui
        self.config = config
        self.container_name = container_name
        self.worker_id = worker_id
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
            
            jobname = APFunction.get_text(self.main_gui, self.main_gui.ui.job_name_input)
            cfg_file = APFunction.get_text(self.main_gui, self.main_gui.ui.select_yaml_name_label)
            command=["-cfg", "{}".format(cfg_file), "-rdir", "{}".format(output_folder),
                "-name", "{}".format(jobname), "-rid", "0", "-gpu", 
                "{}".format(APFunction.get_text(self.main_gui, self.main_gui.ui.gpu_input))]
            user = getpass.getuser()
            
            # Create the result dir
            container_out_dir = os.path.join(output_folder, jobname)
            container_stdout_file = os.path.join(container_out_dir, jobname+"_out_"+dt_string)
            container_stderr_file = os.path.join(container_out_dir, jobname+"_err_"+dt_string)
            os.makedirs(container_out_dir, exist_ok=True)
            
            # Docker mount points 
            volumes = {}
            volumes[cfg_file] = {"bind": cfg_file, "mode": "ro"}
            volumes[output_folder] = {"bind": output_folder, "mode": "rw"}
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
                bytearray(QUrl.fromLocalFile(container_stdout_file).toEncoded()).decode(), container_stdout_file,
                bytearray(QUrl.fromLocalFile(container_stderr_file).toEncoded()).decode(), container_stderr_file)
            
            self.update_log_signal.emit(0)

            # Log the output in a file             
            f = open(container_stdout_file, "w")
            f.write("#########################################################\n")
            f.write(self.container_info.replace("<tr><td>", "").replace("</td><td>", ": ").replace("</td></tr>", "")\
                .replace("<table>", "\n").replace("</table>", "\n").replace('<b>','').replace('</b>','').replace('<br>','').strip())
            f.write("#########################################################\n")
            self.gui.set_out_file(container_stdout_file)

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
            ferr = open(container_stderr_file, "w")
            ferr.write("#########################################################\n")
            ferr.write(self.container_info+"\n")
            ferr.write("#########################################################\n")
            ferr.write(traceback.format_exc())
            ferr.close()
            if f is not None: f.close()
            self.finished_signal.emit()
