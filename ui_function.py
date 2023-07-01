import os
import sys
import docker
import json
import re
import multiprocessing

import settings
from main import * 
from run_functions import run_worker
from build_functions import build_worker
from ui_utils import get_text, resource_path, set_workflow_page, update_container_status, oninit_checks, load_yaml_config

class UIFunction(MainWindow):

    def initStackTab(self):
        if self.settings['init']==False:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            self.ui.frame_home.setStyleSheet("background:rgb(255,255,255)") 
            oninit_checks(self)
            
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

            UIFunction.init_main_page(self)
            UIFunction.init_goptions_page(self)
            UIFunction.init_train_page(self)
            UIFunction.init_test_page(self)

            self.settings['init'] = True
    
    def obtain_workflow_description(self, offset):
        s_workflow = self.settings['selected_workflow'] + offset
        if s_workflow < 0:
            s_workflow = len(self.settings['workflow_names'])-1
        if s_workflow == len(self.settings['workflow_names']):
            s_workflow = 0

        workflow_name = self.settings['workflow_names'][s_workflow].replace("\n"," ") 
        workflow_images = self.settings['workflow_description_images'][s_workflow]
        workflow_description = self.settings['workflow_descriptions'][s_workflow]
        self.workflow_info_exec(workflow_name, workflow_images, workflow_description)

    ###########
    # Home page 
    ###########
    def init_main_page(self):
        pixmap = QPixmap(resource_path(os.path.join("images","horizontal-logo-monochromatic-white.png")))
        pixmap = pixmap.scaled(QSize(201,51),aspectRatioMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.ui.docker_logo.setPixmap(pixmap)

    ###############
    # Workflow page 
    ###############
    def move_workflow_view(self, isleft):
        if isleft:
            self.settings['selected_workflow'] = self.settings['selected_workflow'] - 1 if self.settings['selected_workflow'] != 0 else len(self.settings['workflow_names'])-1
        else: 
            self.settings['selected_workflow'] = self.settings['selected_workflow'] + 1 if self.settings['selected_workflow'] != len(self.settings['workflow_names'])-1 else 0
        set_workflow_page(self)

    ######################
    # General options page 
    ######################
    def init_goptions_page(self):
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

    def build_container(self):
        self.settings['building_thread'] = None
        self.settings['building_worker'] = None
        self.settings['building_threads'] = QThread()
        outf = self.log_dir if self.settings['output_folder'] == "" else self.settings['output_folder']
        self.settings['building_worker'] = build_worker(self, self.settings['biapy_container_dockerfile'], 
            self.settings['biapy_container_name'], outf)
        self.settings['building_worker'].moveToThread(self.settings['building_threads'])
        self.settings['building_threads'].started.connect(self.settings['building_worker'].run)
        self.settings['building_worker'].finished_signal.connect(self.settings['building_threads'].quit)
        self.settings['building_worker'].finished_signal.connect(lambda: update_container_status(self, self.settings['building_worker'].finished_good))
        self.settings['building_worker'].close_signal.connect(self.settings['building_worker'].deleteLater) 
        self.settings['building_threads'].finished.connect(self.settings['building_threads'].deleteLater)
        self.settings['building_worker'].update_log_signal.connect(self.settings['building_worker'].gui.update_gui)
        self.settings['building_worker'].update_build_progress_signal.connect(self.settings['building_worker'].gui.update_building_progress)
        self.settings['building_threads'].start()
        
    def run_biapy(self):
        # Load the YAML file selected
        load_yaml_config(self)

        # Job name check
        jobname = get_text(self.ui.job_name_input)
        if jobname == "":
            self.error_exec("Job name can not be empty", "jobname")
            return
        if os.path.basename(get_text(self.ui.select_yaml_name_label)) == jobname:
            self.error_exec("Job name can not have the same name as the YAML configuration file", "jobname")
            return

        # Output folder check
        if self.settings['output_folder'] == "":
            self.error_exec("Output folder must be defined", "output_folder")
            return 

        # Docker installation check
        if not self.settings['docker_found']:
            self.error_exec("Docker installation not found. Please, install it before running BiaPy in its\
                    <a href=\"https://docs.docker.com/get-docker/\">official documentation</a>. Once you have \
                    done that please restart this application.", "docker_installation")
            return
        if not self.settings['biapy_container_ready']:
            self.error_exec("You need to build BiaPy's container first. You will be redirected yo the main page "
                "so you can do it.", "docker_installation")
            return

        self.settings['running_threads'].append(QThread())
        worker_id = len(self.settings['running_workers'])
        self.settings['running_workers'].append(run_worker(self, self.settings['biapy_cfg'], self.settings['biapy_container_name'], 
            worker_id, self.settings['output_folder'], self.settings['user_host']))
        self.settings['running_workers'][worker_id].moveToThread(self.settings['running_threads'][worker_id])
        self.settings['running_threads'][worker_id].started.connect(self.settings['running_workers'][worker_id].run)
        self.settings['running_workers'][worker_id].finished_signal.connect(self.settings['running_threads'][worker_id].quit)
        self.settings['running_workers'][worker_id].finished_signal.connect(self.settings['running_workers'][worker_id].deleteLater)
        self.settings['running_threads'][worker_id].finished.connect(self.settings['running_threads'][worker_id].deleteLater)
        self.settings['running_workers'][worker_id].update_log_signal.connect(self.settings['running_workers'][worker_id].gui.update_gui)
        self.settings['running_workers'][worker_id].update_cont_state_signal.connect(self.settings['running_workers'][worker_id].gui.update_cont_state)
        self.settings['running_workers'][worker_id].update_train_progress_signal.connect(self.settings['running_workers'][worker_id].gui.update_train_progress)
        self.settings['running_workers'][worker_id].update_test_progress_signal.connect(self.settings['running_workers'][worker_id].gui.update_test_progress)
        self.settings['running_threads'][worker_id].start()
