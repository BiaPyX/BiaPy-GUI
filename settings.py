import os 
import platform
import getpass

from PySide2.QtGui import QPixmap
from ui_utils import resource_path

class Settings():
    
    def __init__(self):
        self.settings = {}
        self.init_default_settings()

    def init_default_settings(self):
        self.settings = {}

        self.settings['init'] = False 
        self.settings['page_number'] = 0

        # OS
        self.settings['os_host'] = platform.system()
        self.settings['user_to_replace'] = "biapy_user" 
        if "win" in self.settings['os_host'].lower():
            self.settings['user_host'] = getpass.getuser()
            #environ["USERNAME"] if platform.startswith("win") else environ["USER"]
        else: # Linux, macOS
            self.settings['user_host'] = str(os.getuid())+":"+str(os.getgid())

        # Biapy 
        self.settings['biapy_container_name'] = "danifranco/biapy:v1.0"
        self.settings['biapy_container_dockerfile'] = "https://raw.githubusercontent.com/danifranco/BiaPy/master/utils/env/Dockerfile"
        self.settings['yaml_config_file_path'] =''
        self.settings['yaml_config_filename'] = ''
        self.settings['output_folder'] = ''
        self.settings['biapy_cfg'] = None
        self.settings['biapy_container_ready'] = False

        # Docker 
        self.settings['docker_client'] = None
        self.settings['docker_found'] = False
        self.settings['running_threads'] = []
        self.settings['running_workers'] = []

        # For all pages 
        self.settings['advanced_frame_images'] = [
            QPixmap(resource_path(os.path.join("images","bn_images","up_arrow.svg"))),
            QPixmap(resource_path(os.path.join("images","bn_images","down_arrow.svg")))
        ]

        # Workflow page
        self.settings['workflow_names'] = ["Semantic\nSegmentation", "Instance\nsegmentation", "Object\ndetection", "Image\ndenoising", "Super\nresolution",\
            "Self-supervised\nlearning", "Image\nclassification"]
        self.settings['selected_workflow'] = 1
        self.settings['dot_images'] = self.settings['dot_images'] = [
            QPixmap(resource_path(os.path.join("images","bn_images","dot_enable.svg"))),
            QPixmap(resource_path(os.path.join("images","bn_images","dot_disable.svg")))
        ]
        self.settings['continue_bn_icons'] = None

        # Semantic segmentation
        self.settings['semantic_models'] = ['unet', 'resunet', 'attention_unet', 'fcn32', \
                'fcn8', 'tiramisu', 'mnet', 'multiresunet', 'seunet', 'unetr']
        self.settings['semantic_models_real_names'] = ['U-Net', 'Residual U-Net', 'Attention U-Net', 'FCN32', \
                'FCN8', 'Tiramisu', 'MNet', 'MultiResUnet', 'SEUnet', 'UNETR']
        # Instance segmentation
        self.settings['instance_models'] = ['unet', 'resunet', 'seunet', 'attention_unet', 'unetr']
        self.settings['instance_models_real_names'] = ['U-Net', 'Residual U-Net', 'SEUnet', 'Attention U-Net', 'UNETR']
        # Detection
        self.settings['detection_models'] = ['unet', 'resunet', 'seunet', 'attention_unet', 'unetr']
        self.settings['detection_models_real_names'] = ['U-Net', 'Residual U-Net', 'SEUnet', 'Attention U-Net', 'UNETR']
        # Denoising
        self.settings['denoising_models'] = ['unet', 'resunet', 'seunet', 'attention_unet', 'unetr']
        self.settings['denoising_models_real_names'] = ['U-Net', 'Residual U-Net', 'SEUnet', 'Attention U-Net', 'UNETR']
        # Super resolution
        self.settings['sr_models'] = ['edsr', 'rcan', 'dfcan', 'wdsr']
        self.settings['sr_models_real_names'] = ['EDSR', 'RCAN', 'DFCAN', 'WDSR']
        # Self-supervised learning
        self.settings['ssl_models'] = ['mae', 'unet', 'resunet', 'seunet', 'attention_unet', 'unetr']
        self.settings['ssl_models_real_names'] = ['MAE', 'U-Net', 'Residual U-Net', 'SEUnet', 'Attention U-Net', 'UNETR']
        # Classification
        self.settings['classification_models'] = ['ViT', 'simple_cnn', 'EfficientNetB0']
        self.settings['classification_models_real_names'] = ['ViT', 'EfficientNetB0', 'Simple CNN']
        
        # Paths
        self.settings['train_data_input_path'] = None
        self.settings['train_data_gt_input_path'] = None
        self.settings['validation_data_input_path'] = None
        self.settings['validation_data_gt_input_path'] = None
        self.settings['test_data_input_path'] = None
        self.settings['test_data_gt_input_path'] = None

    def translate_model_names(self, model, inv=False):
        s = "_models_real_names" if not inv else "_models"
        s2 = "_models" if not inv else "_models_real_names"
        for x in ["semantic", "instance", "detection", "denoising", "sr", "ssl", "classification"]:
            try:
                idx = list(self.settings[x+s]).index(model)
            except:
                pass
            else:
                return list(self.settings[x+s2])[idx]

    def load_workflow_page(self):
        self.settings['workflow_images'] = [
            QPixmap(resource_path(os.path.join("images","semantic_seg.png"))),
            QPixmap(resource_path(os.path.join("images","instance_seg.png"))),
            QPixmap(resource_path(os.path.join("images","detection.png"))),
            QPixmap(resource_path(os.path.join("images","denoising.png"))),
            QPixmap(resource_path(os.path.join("images","sr.png"))),
            QPixmap(resource_path(os.path.join("images","ssl.png"))),
            QPixmap(resource_path(os.path.join("images","classification.png")))
        ]

    def load_workflow_detail_page(self):    
        self.settings['workflow_description_images'] = [
            [QPixmap(resource_path(os.path.join("images","semantic_seg_raw.png"))),QPixmap(resource_path(os.path.join("images","semantic_seg_label.png")))],
            [QPixmap(resource_path(os.path.join("images","instance_seg_raw.png"))),QPixmap(resource_path(os.path.join("images","instance_seg_label.png")))],
            [QPixmap(resource_path(os.path.join("images","detection_raw.png"))),QPixmap(resource_path(os.path.join("images","detection_csv_input.png")))],
            [QPixmap(resource_path(os.path.join("images","denoising_raw.png"))),QPixmap(resource_path(os.path.join("images","denoising_pred.png")))],
            [QPixmap(resource_path(os.path.join("images","sr_raw.png"))),QPixmap(resource_path(os.path.join("images","sr_pred.png")))],
            [QPixmap(resource_path(os.path.join("images","ssl_raw.png"))),QPixmap(resource_path(os.path.join("images","ssl_pred.png")))],
            [QPixmap(resource_path(os.path.join("images","classification_raw.png"))),QPixmap(resource_path(os.path.join("images","classification_label.png")))]
        ]
        self.settings['workflow_description_doc'] = [
            "https://biapy.readthedocs.io/en/latest/workflows/semantic_segmentation.html",
            "https://biapy.readthedocs.io/en/latest/workflows/instance_segmentation.html",
            "https://biapy.readthedocs.io/en/latest/workflows/detection.html",
            "https://biapy.readthedocs.io/en/latest/workflows/denoising.html",
            "https://biapy.readthedocs.io/en/latest/workflows/super_resolution.html",
            "https://biapy.readthedocs.io/en/latest/workflows/self_supervision.html",
            "https://biapy.readthedocs.io/en/latest/workflows/classification.html"
        ]

        self.settings['ready_to_use_workflows'] = [
            [ # Semantic segmentation
                {
                    'name': 'Embryo wound segmentation (2D)', 
                    'image': QPixmap(resource_path(os.path.join("images","ready_to_use_examples",'semantic_seg_2d_droso_embryo.png'))), 
                    'data': 'https://drive.google.com/file/d/1qehkWYVJRXfMwvbpayKhb4nmPyYvclAj/view?usp=sharing', 
                    'template': 'https://github.com/danifranco/BiaPy/blob/master/templates/semantic_segmentation/2d_semantic_segmentation.yaml'
                },
                {
                    'name': 'Mitochondria segmentation (3D)', 
                    'image': QPixmap(resource_path(os.path.join("images","ready_to_use_examples",'semantic_seg_3d_mitochondria.png'))), 
                    'data': 'https://drive.google.com/file/d/10Cf11PtERq4pDHCJroekxu_hf10EZzwG/view?usp=drive_link', 
                    'template': 'https://github.com/danifranco/BiaPy/blob/master/templates/semantic_segmentation/3d_semantic_segmentation.yaml'
                }
            ],
            [ # Instance segmentation
                {
                    'name': 'Cell instance segmentation (2D)', 
                    'image': QPixmap(resource_path(os.path.join("images","ready_to_use_examples",'instance_seg_2d_cell.png'))), 
                    'data': 'https://drive.google.com/file/d/1b7_WDDGEEaEoIpO_1EefVr0w0VQaetmg/view?usp=drive_link', 
                    'template': 'https://github.com/danifranco/BiaPy/blob/master/templates/instance_segmentation/2d_instances_segmentation.yaml'
                },
                {
                    'name': 'Nuclei instance segmentation (3D)', 
                    'image': QPixmap(resource_path(os.path.join("images","ready_to_use_examples",'instance_seg_3d_nuclei.png'))), 
                    'data': 'https://drive.google.com/file/d/1fdL35ZTNw5hhiKau1gadaGu-rc5ZU_C7/view?usp=drive_link', 
                    'template': 'https://github.com/danifranco/BiaPy/blob/master/templates/instance_segmentation/3d_instances_segmentation.yaml'
                },
            ],
            [ # Detection
                {
                    'name': 'Cell detection (2D)', 
                    'image': QPixmap(resource_path(os.path.join("images","ready_to_use_examples",'instance_seg_2d_cell.png'))), 
                    'data': 'https://drive.google.com/file/d/1pWqQhcWY15b5fVLZDkPS-vnE-RU6NlYf/view?usp=drive_link', 
                    'template': 'https://github.com/danifranco/BiaPy/blob/master/templates/detection/2d_detection.yaml'
                },
                {
                    'name': 'Nuclei detection (3D)', 
                    'image': QPixmap(resource_path(os.path.join("images","ready_to_use_examples",'detection_3d_nuclei.png'))), 
                    'data': 'https://drive.google.com/file/d/19P4AcvBPJXeW7QRj92Jh1keunGa5fi8d/view?usp=drive_link', 
                    'template': 'https://github.com/danifranco/BiaPy/blob/master/templates/detection/3d_detection.yaml'
                }
            ],
            [ # Denoising
                {
                    'name': 'C. Majalist denoising (2D)', 
                    'image': QPixmap(resource_path(os.path.join("images","ready_to_use_examples",'denoising_2d_c_majalis.png'))), 
                    'data': 'https://drive.google.com/file/d/1TFvOySOiIgVIv9p4pbHdEbai-d2YGDvV/view?usp=drive_link', 
                    'template': 'https://github.com/danifranco/BiaPy/blob/master/templates/denoising/2d_denoising.yaml'
                },
                {
                    'name': 'Fly wing denoising (3D)', 
                    'image': QPixmap(resource_path(os.path.join("images","ready_to_use_examples",'denoising_3d_flywing.png'))), 
                    'data': 'https://drive.google.com/file/d/1OIjnUoJKdnbClBlpzk7V5R8wtoLont-r/view?usp=drive_link', 
                    'template': 'https://github.com/danifranco/BiaPy/blob/master/templates/denoising/3d_denoising.yaml'
                }
            ],
            [ # SR
                {
                    'name': 'F-actin super-resolution (2D)', 
                    'image': QPixmap(resource_path(os.path.join("images","ready_to_use_examples",'sr_2d_factin.png'))), 
                    'data': 'https://drive.google.com/file/d/1rtrR_jt8hcBEqvwx_amFBNR7CMP5NXLo/view?usp=sharing', 
                    'template': 'https://github.com/danifranco/BiaPy/blob/master/templates/classification/2d_super-resolution.yaml'
                },
                {
                    'name': 'Cardiomyoblast super-resolution (3D)', 
                    'image': QPixmap(resource_path(os.path.join("images","ready_to_use_examples",'sr_3d_cardiomyoblast.png'))), 
                    'data': 'https://drive.google.com/file/d/1rtrR_jt8hcBEqvwx_amFBNR7CMP5NXLo/view?usp=sharing', 
                    'template': 'https://github.com/danifranco/BiaPy/blob/master/templates/classification/3d_super-resolution.yaml'
                },
                {
                    'name': 'Urban super-resolution (2D)', 
                    'image': QPixmap(resource_path(os.path.join("images","ready_to_use_examples",'sr_2d_urban100.png'))), 
                    'data': 'https://drive.google.com/file/d/1Dzlz2dbFw-fz4JDykrWu-SU0v45YBjbj/view?usp=sharing', 
                    'template': 'https://github.com/danifranco/BiaPy/blob/master/templates/classification/2d_super-resolution.yaml'
                }
            ],
            [ # SSL
                {
                    'name': 'Self-supervision in EM images (2D)', 
                    'image': QPixmap(resource_path(os.path.join("images","ready_to_use_examples",'semantic_seg_3d_mitochondria.png'))), 
                    'data': 'https://drive.google.com/file/d/1DfUoVHf__xk-s4BWSKbkfKYMnES-9RJt/view?usp=drive_link', 
                    'template': 'https://github.com/danifranco/BiaPy/blob/master/templates/classification/2d_self-supervised.yaml'
                },
                {
                    'name': 'Self-supervision in EM images (3D)', 
                    'image': QPixmap(resource_path(os.path.join("images","ready_to_use_examples",'detection_3d_nuclei.png'))), 
                    'data': 'https://drive.google.com/file/d/19P4AcvBPJXeW7QRj92Jh1keunGa5fi8d/view?usp=drive_link', 
                    'template': 'https://github.com/danifranco/BiaPy/blob/master/templates/classification/3d_self-supervised.yaml'
                }
            ],
            [ # Classification
                {
                    'name': 'Skin lesion classification (2D)', 
                    'image': QPixmap(resource_path(os.path.join("images","ready_to_use_examples",'classification_2d_dermaMNIST.png'))), 
                    'data': 'https://drive.google.com/file/d/15_pnH4_tJcwhOhNqFsm26NQuJbNbFSIN/view?usp=drive_link', 
                    'template': 'https://github.com/danifranco/BiaPy/blob/master/templates/classification/classification_2d.yaml'
                },
                {
                    'name': 'Organ classification (3D)', 
                    'image': QPixmap(resource_path(os.path.join("images","ready_to_use_examples",'classification_3d_organMNIST.png'))), 
                    'data': 'https://drive.google.com/file/d/1pypWJ4Z9sRLPlVHbG6zpwmS6COkm3wUg/view?usp=drive_link', 
                    'template': 'https://github.com/danifranco/BiaPy/blob/master/templates/classification/classification_3d.yaml'
                },
                {
                    'name': 'Butterfly classification (2D)', 
                    'image': QPixmap(resource_path(os.path.join("images","ready_to_use_examples",'classification_2d_butterfly.jpg'))), 
                    'data': 'https://drive.google.com/file/d/1m4_3UAgUsZ8FDjB4HyfA50Sht7_XkfdB/view?usp=drive_link', 
                    'template': 'https://github.com/danifranco/BiaPy/blob/master/templates/classification/classification_2d.yaml'
                }
            ]
        ]

        self.settings['workflow_descriptions'] = [
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
            <img src="'+resource_path(os.path.join("images","detection_raw.png"))+'"> <p><span>Input image.</span></p>\
            </td>\
            <td style="text-align: center;">\
            <img src="'+resource_path(os.path.join("images","detection_label.png"))+'"><p><span>Model\'s GT.</span></p>\
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
