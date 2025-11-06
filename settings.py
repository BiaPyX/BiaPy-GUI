import os
import platform
import getpass
from PySide6.QtGui import QPixmap, QMovie
from ui_utils import resource_path
from packaging.version import Version

class Settings:

    def __init__(self):
        self.settings = {}
        self.init_default_settings()

    def init_default_settings(self):
        self.settings = {}

        self.settings["init"] = False
        self.settings["page_number"] = 0

        # OS
        self.settings["os_host"] = platform.system()
        if "win" in self.settings["os_host"].lower():
            self.settings["user_host"] = getpass.getuser()
            # environ["USERNAME"] if platform.startswith("win") else environ["USER"]
        else:  # Linux, macOS
            self.settings["user_host"] = str(os.getuid()) + ":" + str(os.getgid())

        # CUDA version match to decide the container to donwload
        self.settings["NVIDIA_driver_list"] = [440.33, 520.61]
        self.settings["CUDA_version"] = [10.2, 11.8]
        self.settings["CUDA_selected"] = "" # to be filled by checking the GPU 

        # BiaPy
        self.settings["biapy_code_version"] = Version("v3.6.6")
        self.settings["biapy_code_github"] = "https://github.com/BiaPyX/BiaPy"
        self.settings["biapy_gui_version"] = Version("v1.2.0")
        self.settings["biapy_gui_github"] = "https://github.com/BiaPyX/BiaPy-GUI"
        self.settings["biapy_container_basename"] = "biapyx/biapy"
        self.settings["biapy_container_name"] = (
            self.settings["biapy_container_basename"] + ":" + str(self.settings["biapy_code_version"]) + "-" + str(self.settings["CUDA_version"][-1])
        )
        self.settings["biapy_container_sizes"] = ["8GB", "12GB"]
        self.settings["biapy_container_size"] = self.settings["biapy_container_sizes"][-1]
        self.settings["biapy_container_dockerfile"] = (
            "https://raw.githubusercontent.com/BiaPyX/BiaPy/master/biapy/utils/env/Dockerfile"
        )
        self.settings["yaml_config_file_path"] = ""
        self.settings["yaml_config_filename"] = ""
        self.settings["output_folder"] = ""
        self.settings["biapy_cfg"] = None
        self.settings["biapy_container_ready"] = False

        # Docker
        self.settings["docker_client"] = None
        self.settings["docker_found"] = False
        self.settings["running_threads"] = []
        self.settings["running_workers"] = []

        # For all pages
        self.settings["info_image"] = QPixmap(resource_path(os.path.join("images", "bn_images", "info.png")))
        self.settings["info_image_clicked"] = resource_path(os.path.join("images", "bn_images", "info_clicked.png"))

        # Wizard icons
        self.settings["wizard_img"] = QPixmap(resource_path(os.path.join("images", "wizard", "wizard.png")))
        self.settings["wizard_animation_img"] = QMovie(
            resource_path(os.path.join("images", "wizard", "wizard_question_animation.gif"))
        )

        # Workflow page
        self.settings["workflow_names"] = [
            "Semantic\nsegmentation",
            "Instance\nsegmentation",
            "Object\ndetection",
            "Image\ndenoising",
            "Super\nresolution",
            "Self-supervised\nlearning",
            "Image\nclassification",
            "Image to image",
        ]
        self.settings["workflow_key_names"] = [
            "SEMANTIC_SEG",
            "INSTANCE_SEG",
            "DETECTION",
            "DENOISING",
            "SUPER_RESOLUTION",
            "SELF_SUPERVISED",
            "CLASSIFICATION",
            "IMAGE_TO_IMAGE",
        ]
        self.settings["selected_workflow"] = 1
        self.settings["dot_images"] = self.settings["dot_images"] = [
            QPixmap(resource_path(os.path.join("images", "bn_images", "dot_enable.svg"))),
            QPixmap(resource_path(os.path.join("images", "bn_images", "dot_disable.svg"))),
        ]

        #################################
        # Questions to identify workflow
        #################################
        self.settings["wizard_question_index"] = 0
        self.settings["wizard_variable_to_map"] = {}
        self.settings["wizard_question_condition"] = {}
        self.settings["wizard_questions"] = []
        self.settings["wizard_possible_answers"] = []
        self.settings["wizard_sections"] = []
        self.settings["wizard_from_toc_to_question_index"] = []
        self.settings["wizard_from_question_index_to_toc"] = []
        self.settings["wizard_question_additional_info"] = []
        self.settings["wizard_question_visible"] = []
        self.settings["wizard_answers"] = {}

        self.settings["wizard_sections"] += [["Problem description", []]]
        self.settings["wizard_from_toc_to_question_index"].append([])
        q_count = 0

        ######
        # Q1 #
        ######
        self.settings["wizard_questions"] = [
            "Are your images in 3D?",
        ]
        self.settings["wizard_variable_to_map"]["Q1"] = {}
        self.settings["wizard_possible_answers"] += [["Yes", "No", "No but I would like to have a 3D stack output"]]
        self.settings["wizard_variable_to_map"]["Q1"]["PROBLEM.NDIM"] = ["3D", "2D", "2D"]
        self.settings["wizard_variable_to_map"]["Q1"]["TEST.ANALIZE_2D_IMGS_AS_3D_STACK"] = [False, False, True]
        self.settings["wizard_answers"]["PROBLEM.NDIM"] = -1
        self.settings["wizard_answers"]["TEST.ANALIZE_2D_IMGS_AS_3D_STACK"] = -1
        self.settings["wizard_sections"][-1][1] += ["Dimensions"]
        self.settings["wizard_from_question_index_to_toc"].append(
            [0, len(self.settings["wizard_from_toc_to_question_index"][-1])]
        )
        self.settings["wizard_from_toc_to_question_index"][-1].append(q_count)
        self.settings["wizard_question_visible"].append(True)
        q_count += 1

        # Q1 additional information
        self.settings["wizard_question_additional_info"] += [
            "<p>\
            The purpose of this question is to determine the type of images you will use. This will help decide which deep learning model will be applied to process your images. The options are:\
            </p>\
            <ul>\
                <li>\
                    <p><strong>2D images</strong>&nbsp;are considered those that can be represented as (x, y, channels). For example, (512, 1024, 2).</p>\
                </li>\
                <li>\
                    <p><strong>3D images</strong>&nbsp;are those that can be represented as (x, y, z, channels). For example, (400, 400, 50, 1).</p>\
                </li>\
            </ul>\
            <p>\
            The last option, &quot;No, but I would like to have a 3D stack output,&quot; refers to working with 2D images. After processing them with the deep learning model, the images will be combined in sequence to create a 3D stack. This option is useful if your 2D images together form a larger 3D volume.\
            </p>"
        ]
        ######
        # Q2 #
        ######
        self.settings["wizard_questions"] += [
            "What would you like to do? Check the Wizard Help for details about each workflow.",
        ]
        self.settings["wizard_possible_answers"] += [
            [
                "Generate masks of different objects/regions within the image",
                "Generate masks for each object in the image",
                "Identify circular objects (e.g. nuclei) in the image using points",
                "Upsample images into higher resolution",
                "Assign a label to each image",
                "Restore a degraded image",
                "Generate new images based on an input one",
            ]
        ]
        self.settings["wizard_variable_to_map"]["Q2"] = {}
        self.settings["wizard_variable_to_map"]["Q2"]["PROBLEM.TYPE"] = [
            "SEMANTIC_SEG",
            "INSTANCE_SEG",
            "DETECTION",
            "DENOISING",
            "SUPER_RESOLUTION",
            "CLASSIFICATION",
            "IMAGE_TO_IMAGE",
            "IMAGE_TO_IMAGE",
        ]
        self.settings["wizard_answers"]["PROBLEM.TYPE"] = -1
        self.settings["wizard_sections"][-1][1] += ["Workflow"]
        self.settings["wizard_from_question_index_to_toc"].append(
            [0, len(self.settings["wizard_from_toc_to_question_index"][-1])]
        )
        self.settings["wizard_from_toc_to_question_index"][-1].append(q_count)
        self.settings["wizard_question_visible"].append(True)
        q_count += 1
        # Q2 additional information
        se = resource_path(os.path.join("images", "semantic_seg_raw.png"))
        self.settings["wizard_question_additional_info"] += [
            "<p>\
                This question determines the type of workflow you want to run. Each option corresponds to a workflow implemented in BiaPy.\
                The options are:\
            </p>\
            <p>\
                <strong>&#8226;&quot;Generate masks of different objects/regions within the image&quot;</strong>&nbsp; refers to the workflow called &quot;Semantic segmentation&quot;. The goal of this workflow is to assign a class to each pixel (or voxel) of the input image, thus producing a label image with semantic masks. The simplest case would be binary classification, as in the figure depicted below. There, only two labels are present in the label image: black pixels (usually with value 0) represent the background, and white pixels represent the foreground (the wound in this case, usually labeled with 1 or 255 value).\
            </p>\
            <div style='float:center;'>\
            <img style='float:center;' src='{}' width='200px'/> \
            </div>\
            <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>\
            <p>\
            Find more information about semantic segmenation workflow in <a href='https://biapy.readthedocs.io/en/latest/workflows/semantic_segmentation.html'>its documentation</a>.\
            </p>\
            \
            <p>\
                <strong>&#8226;&quot;Generate masks for each object in the image&quot;</strong>&nbsp;refers to the workflow called &quot;Instance segmentation&quot;. The goal of this workflow is to assign a unique ID, i.e. an integer value, to each object of the input image, thus producing a label image with instance masks. An example of this task is displayed in the figure below, with an electron microscopy image used as input (left) and its corresponding instance label image identifying each individual mitochondrion (right). Each color in the mask image corresponds to a unique object.\
            </p>\
            <div style='float:center;'>\
            <img style='float:center;' src='{}' width='200px'/> \
            </div>\
            <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>\
            <p>Find more information about instance segmenation workflow in <a href='https://biapy.readthedocs.io/en/latest/workflows/instance_segmentation.html'>its documentation</a>.</p>\
            \
            <p>\
            <strong>&#8226;&quot;Identify circular objects (e.g. nuclei) in the image using points&quot;</strong>&nbsp;refers to the workflow called &quot;Detection&quot;. The goal of this workflow is to localize objects in the input image, not requiring a pixel-level class. Common strategies produce either bounding boxes containing the objects or individual points at their center of mass, which is the one adopted by BiaPy.\
            </p>\
            <p>\
            An example of this task is displayed in the figure below (credits to <a href='https://zenodo.org/records/3715492#.Y4m7FjPMJH6'>Jukkala & Jacquemet</a>), with a fluorescence microscopy image used as input (left) and its corresponding nuclei detection results (rigth). Each red dot in the right image corresponds to a unique predicted object.\
            </p>\
            <div style='float:center;'>\
            <img style='float:center;' src='{}' width='200px'/> \
            </div>\
            <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>\
            <p>\
            Find more information about detection workflow in \
            <a href='https://biapy.readthedocs.io/en/latest/workflows/detection.html'>its documentation</a>.\
            </p>\
            \
            <p>\
            <strong>&#8226;&quot;Clean noisy images&quot;</strong>&nbsp;refers to the workflow called &quot;Denoising&quot;. The goal of this workflow is to remove noise from the input images. BiaPy makes use of <a href='https://openaccess.thecvf.com/content_CVPR_2019/html/Krull_Noise2Void_-_Learning_Denoising_From_Single_Noisy_Images_CVPR_2019_paper.html'>Nosei2Void</a> with any of the U-Net-like models provided. The main advantage of Noise2Void is neither relying on noise image pairs nor clean target images since frequently clean images are simply unavailable.\
            </p>\
            <p>\
            An example of this task is displayed in the figure below, with an noisy fluorescence image and its corresponding denoised output. This image was obtained from a <a href='https://zenodo.org/record/5156913'>Convallaria dataset</a> used in <a href='https://openaccess.thecvf.com/content_CVPR_2019/html/Krull_Noise2Void_-_Learning_Denoising_From_Single_Noisy_Images_CVPR_2019_paper.html'>Nosei2Void</a>\
            project.\
            </p>\
            <div style='float:center;'>\
            <img style='float:center;' src='{}' width='200px'/> \
            </div>\
            <br><br><br><br><br><br><br><br><br><br><br><br><br><br>\
            <p>\
            Find more information about denoising workflow in \
            <a href='https://biapy.readthedocs.io/en/latest/workflows/denoising.html'>its documentation</a>.\
            </p>\
            \
            <p>\
            <strong>&#8226;&quot;Upsample images into higher resolution&quot;</strong>&nbsp;refers to the workflow called &quot;Super resolution&quot;. The goal of this workflow is to reconstruct high-resolution (HR) images from low-resolution (LR) ones. If there is a difference in the size of the LR and HR images, typically determined by a scale factor (x2, x4), this task is known as single-image super-resolution. If the size of the LR and HR images is the same, this task is usually referred to as image restoration.\
            </p>\
            <p>\
            An example of this task is displayed in the figure below, with a LR fluorescence microscopy image used as input (left) and its corresponding HR image (x2 scale factor). Credits of this image to <a href='https://figshare.com/articles/dataset/BioSR/13264793'>F-actin dataset by Qiao et al</a>.\
            </p>\
            <div style='float:center;'>\
            <img style='float:center;' src='{}' width='200px'/> \
            </div>\
            <br><br><br><br><br><br><br><br><br><br><br><br><br><br>\
            <p>\
            Find more information about super-resolution workflow in <a href='https://biapy.readthedocs.io/en/latest/workflows/super_resolution.html'>its documentation</a>.\
            </p>\
            <p>\
            <strong>&#8226;&quot;Assign a label to each image&quot;</strong>&nbsp;refers to the workflow called &quot;Classification&quot;. The goal of this workflow is to assign a label to the input image. In the figure below a few examples of this workflow's input are depicted where each image is classified as a result. Images obtained from <a href='https://medmnist.com/'>MedMNIST v2</a>, concretely from DermaMNIST dataset which is a large collection of multi-source dermatoscopic images of common pigmented skin lesions.\
            </p>\
            <div style='float:center;'>\
            <img style='float:center;' src='{}' width='200px'/> \
            </div>\
            <br><br><br><br><br><br><br><br><br><br><br><br><br>\
            <p>\
            Find more information about classification workflow in \
            <a href='https://biapy.readthedocs.io/en/latest/workflows/classification.html'>its documentation</a>.\
            </p>\
            <p>\
            <strong>&#8226;&quot;I want to restore a degraded image&quot; and &quot;I want to generate new images based on an input one&quot;</strong>&nbsp;both questions refers to the workflow called &quot;Image to image&quot;. The goal of this workflow aims at translating/mapping input images into target images. This workflow is as the super-resolution one but with no upsampling, e.g. with the scaling factor to x1.\
            </p>\
            <p>\
            In the figure below an example of paired microscopy images (brightfield) is depicted. The images were obtained from <a href='https://lightmycells.grand-challenge.org/'>Light My Cells dataset</a>. \
            </p>\
            <div style='float:center;'>\
            <img style='float:center;' src='{}' width='200px'/> \
            </div>\
            <br><br><br><br><br><br><br><br><br><br><br><br><br><br>\
            <p>\
            Find more information about image to image workflow in \
            <a href='https://biapy.readthedocs.io/en/latest/workflows/image_to_image.html'>its documentation</a>.\
            </p>\
            ".format(
                resource_path(os.path.join("images", "wizard","semantic_seg_collage.png")), 
                resource_path(os.path.join("images", "wizard","instance_seg_collage.png")), 
                resource_path(os.path.join("images", "wizard","detection_collage.png")), 
                resource_path(os.path.join("images", "wizard","denoising_collage.png")), 
                resource_path(os.path.join("images", "wizard","sr_collage.png")), 
                resource_path(os.path.join("images", "wizard","classification_collage.png")), 
                resource_path(os.path.join("images", "wizard","i2i_collage.png")), 
            )
            ]

        ######
        # Q3 #
        ######
        self.settings["wizard_questions"] += [
            "Do you want to use a pre-trained model?",
        ]
        self.settings["wizard_possible_answers"] += [
            [
                "No, I want to build a model from scratch",
                "Yes, I have a model previously trained in BiaPy",
                "Yes, I want to check if there is a pretrained model I can use",
            ]
        ]
        self.settings["wizard_variable_to_map"]["Q3"] = {}
        self.settings["wizard_variable_to_map"]["Q3"]["MODEL.SOURCE"] = ["biapy", "biapy", "bmz"]
        self.settings["wizard_variable_to_map"]["Q3"]["MODEL.LOAD_CHECKPOINT"] = [False, True, False]
        self.settings["wizard_variable_to_map"]["Q3"]["MODEL.LOAD_MODEL_FROM_CHECKPOINT"] = [False, True, False]
        self.settings["wizard_answers"]["MODEL.SOURCE"] = -1 
        self.settings["wizard_answers"]["MODEL.LOAD_CHECKPOINT"] = -1 
        self.settings["wizard_answers"]["MODEL.LOAD_MODEL_FROM_CHECKPOINT"] = -1
        self.settings["wizard_sections"][-1][1] += ["Model source"]
        self.settings["wizard_from_question_index_to_toc"].append(
            [0, len(self.settings["wizard_from_toc_to_question_index"][-1])]
        )
        self.settings["wizard_from_toc_to_question_index"][-1].append(q_count)
        self.settings["wizard_question_visible"].append(True)
        q_count += 1
        # Q3 additional information
        self.settings["wizard_question_additional_info"] += [
            "<p>\
            This question determines how the deep learning model will be built. Based on your choice, additional questions may appear to guide the model setup process.\
            </p>\
            <p>\
            Before using a deep learning model, it must be trained. The idea is to train the model on a specific task and then apply it to new images. For example, you could train a model to classify images based on their labels. If the training is successful, the model should be able to classify new images automatically.\
            </p>\
            <p>\
            Training is a crucial step to ensure good results, but it requires labeled data, also known as 'ground truth'. Using the image classification example, you would need to label the training images first, like 'image1.png' as class 1, 'image2.png' as class 2, etc. Because training can be time-consuming, using a pre-trained model can be a major advantage. A pre-trained model has already been trained on a dataset and has some level of knowledge.\
            </p>\
            <p>\
            If your images are similar to those used to train the pre-trained model, you might get good results without retraining it. If not, having similar images will at least make the retraining process faster and require fewer images. That's why it’s always a good idea to check for available pre-trained models that match your needs. Here are the options available:\
            </p>\
            <ul>\
                <li>\
                    <p><strong>'No, I want to build a model from scratch'</strong>&nbsp; This option configures BiaPy to create a model from the ground up. No additional input will be required, and BiaPy will automatically configure the model based on the selected workflow and image dimensions.</p>\
                </li>\
                <li>\
                    <p><strong>'Yes, I have a model previously trained in BiaPy'</strong>&nbsp; Choose this option if you already have a model trained with BiaPy. The model must be stored in the folder you’ve selected for saving results, specifically in the 'checkpoints' folder, as a file with a '.pth' extension. You’ll need to specify this file when prompted after selecting this option.</p>\
                </li>\
                <li>\
                    <p><strong>'Yes, I want to check if there is a pretrained model I can use'</strong>&nbsp; This option allows you to load a pre-trained model from an external source. Currently, BiaPy supports loading models from the <a href='https://bioimage.io/#/'>BioImage Model Zoo</a> and <a href='https://pytorch.org/vision/stable/models.html'>Torchvision</a>. Depending on the workflow and image dimensions, you can search for compatible models to use.</p>\
                </li>\
            </ul>\
            "
        ]

        ######
        # Q4 #
        ######
        self.settings["wizard_question_condition"]["Q4"] = {
            "or_cond": [ ],
            "and_cond": [
                ["MODEL.SOURCE", "biapy"],
                ["MODEL.LOAD_CHECKPOINT", True],
            ],
        }
        self.settings["wizard_questions"] += [
            "Please select the pretrained model trained with BiaPy before:",
        ]
        self.settings["wizard_possible_answers"] += [["MODEL_BIAPY",]]
        self.settings["wizard_variable_to_map"]["Q4"] = {}
        self.settings["wizard_variable_to_map"]["Q4"]["PATHS.CHECKPOINT_FILE"] = ""
        self.settings["wizard_answers"]["PATHS.CHECKPOINT_FILE"] = -1
        self.settings["wizard_sections"][-1][1] += ["Path to model"]
        self.settings["wizard_from_question_index_to_toc"].append(
            [0, len(self.settings["wizard_from_toc_to_question_index"][-1])]
        )
        self.settings["wizard_from_toc_to_question_index"][-1].append(q_count)
        self.settings["wizard_question_visible"].append(False)
        q_count += 1
        # Q4 additional information
        self.settings["wizard_question_additional_info"] += [
            "<p>\
            This question is about setting the path to the pre-trained model in BiaPy. The model should be stored in the folder you previously selected for saving results. Specifically, in the 'checkpoints' folder, there will be a file with a '.pth' extension, which represents the checkpoint of the pre-trained model. You need to locate this file on your system by clicking the 'Browse' button.\
            </p>\
            "
        ]

        ######
        # Q5 #
        ######
        self.settings["wizard_question_condition"]["Q5"] = {
            "or_cond": [
                [
                    "MODEL.SOURCE",
                    ["bmz", "torchvision"]
                ],
                [
                    "PROBLEM.TYPE",
                    [
                        "SEMANTIC_SEG",
                        "INSTANCE_SEG",
                        "DETECTION",
                        "DENOISING",
                        "SUPER_RESOLUTION",
                        "SELF_SUPERVISED",
                        "CLASSIFICATION",
                        "IMAGE_TO_IMAGE",
                    ]
                ],
                [
                    "PROBLEM.NDIM", 
                    ["2D", "3D"]
                ], 
            ],
            "and_cond": [], 
        }
        self.settings["wizard_questions"] += [
            "Please select a pretrained model by pressing 'Check models' below. This process "
            "requires internet connection and may take a while.",
        ]
        self.settings["wizard_possible_answers"] += [["MODEL_OTHERS",]]
        self.settings["wizard_variable_to_map"]["Q5"] = {}
        self.settings["wizard_variable_to_map"]["Q5"]["MODEL.BMZ.SOURCE_MODEL_ID"] = ""
        self.settings["wizard_answers"]["MODEL.BMZ.SOURCE_MODEL_ID"] = -1
        self.settings["wizard_sections"][-1][1] += ["Select model"]
        self.settings["wizard_from_question_index_to_toc"].append(
            [0, len(self.settings["wizard_from_toc_to_question_index"][-1])]
        )
        self.settings["wizard_from_toc_to_question_index"][-1].append(q_count)
        self.settings["wizard_question_visible"].append(False)
        q_count += 1
        # Q5 additional information
        self.settings["wizard_question_additional_info"] += [
            "<p>\
            This question allows you to load a pre-trained model from an external source. Currently, BiaPy supports loading models from the <a href='https://bioimage.io/#/'>BioImage Model Zoo</a> and <a href='https://pytorch.org/vision/stable/models.html'>Torchvision</a>.\
            </p>\
            <p>\
            To search for all available models, click the 'Check models' button. This will start an online search, which requires an internet connection and may take several minutes. Once the process is complete, a new window will appear, displaying all the pre-trained models that can be used for the selected workflow and image dimensions.\
            </p>"
        ]

        ######
        # Q6 #
        ######
        self.settings["wizard_question_condition"]["Q6"] = {
            "or_cond": [
                [
                    "PROBLEM.TYPE",  # Depends on Q2
                    [
                        "SEMANTIC_SEG",
                        "INSTANCE_SEG",
                        "DETECTION",
                        "CLASSIFICATION",
                        "IMAGE_TO_IMAGE",
                    ],
                ]
            ],
            "and_cond": [
                [
                    "MODEL.SOURCE",
                    "biapy"
                ], 
            ],
        }
        self.settings["wizard_questions"] += [
            "What is the average object width/height in pixels?",
        ]
        self.settings["wizard_possible_answers"] += [
            [
                "0-25 px",
                "25-100 px",
                "100-200 px",
                "200-500 px",
                "More than 500 px",
            ]
        ]
        self.settings["wizard_variable_to_map"]["Q6"] = {}
        self.settings["wizard_variable_to_map"]["Q6"]["DATA.PATCH_SIZE_XY"] = [
            (256, 256),
            (256, 256),
            (512, 512),
            (512, 512),
            (1024, 1024),
        ]
        self.settings["wizard_variable_to_map"]["Q6"]["TEST.POST_PROCESSING.REMOVE_CLOSE_POINTS_RADIUS"] = [
            10,
            20,
            30,
            30,
            30,
        ]
        self.settings["wizard_answers"]["DATA.PATCH_SIZE_XY"] = -1
        self.settings["wizard_answers"]["TEST.POST_PROCESSING.REMOVE_CLOSE_POINTS_RADIUS"] = -1
        self.settings["wizard_sections"] += [["Data", []]]
        self.settings["wizard_from_toc_to_question_index"].append([])
        self.settings["wizard_sections"][-1][1] += ["Object size (xy)"]
        self.settings["wizard_from_question_index_to_toc"].append(
            [1, len(self.settings["wizard_from_toc_to_question_index"][-1])]
        )
        self.settings["wizard_from_toc_to_question_index"][-1].append(q_count)
        self.settings["wizard_question_visible"].append(False)
        q_count += 1
        # Q6 additional information
        self.settings["wizard_question_additional_info"] += [
            "<p>\
            This question is meant to determine the size of the objects of interest in your images. For example, if you're working on cell nucleus segmentation, you should have a general idea of the size these nuclei will appear in the images.\
            </p>\
            <p>\
            Continuing with the example, in the figure below, several cell nuclei are shown, all roughly the same size. If we measure one at random and find it is 24 pixels wide and 44 pixels tall, we can estimate the size range as '25-100 px'. These measurements don't need to be exact, but they help guide BiaPy to set up a more optimized workflow.\
            </p>\
            <div style='float:center;'>\
            <img style='float:center;' src='{}' width='200px'/> \
            </div>\
            <br><br><br><br><br><br><br><br><br><br><br><br><br><br>\
            ".format(resource_path(os.path.join("images", "wizard", "object_size.png")))
        ]

        ######
        # Q7 #
        ######
        self.settings["wizard_question_condition"]["Q7"] = {
            "and_cond": [
                [
                    "PROBLEM.NDIM", 
                    "3D"
                ], 
                [
                    "MODEL.SOURCE", 
                    "biapy"
                ]
            ],
            "or_cond": [
                [
                    "PROBLEM.TYPE",
                    [
                        "SEMANTIC_SEG",
                        "INSTANCE_SEG",
                        "DETECTION",
                        "CLASSIFICATION",
                        "IMAGE_TO_IMAGE",
                    ],
                ]
            ],
        }
        self.settings["wizard_questions"] += [
            "How many slices can an object be represented in?",
        ]
        self.settings["wizard_possible_answers"] += [
            [
                "1-5 slices",
                "5-10 slices",
                "10-20 slices",
                "20-60 slices",
                "More than 60 slices",
            ]
        ]
        self.settings["wizard_variable_to_map"]["Q7"] = {}
        self.settings["wizard_variable_to_map"]["Q7"]["DATA.PATCH_SIZE_Z"] = [5, 10, 20, 40, 80]
        self.settings["wizard_answers"]["DATA.PATCH_SIZE_Z"] = -1
        self.settings["wizard_sections"][-1][1] += ["Object size (z)"]
        self.settings["wizard_from_question_index_to_toc"].append(
            [1, len(self.settings["wizard_from_toc_to_question_index"][-1])]
        )
        self.settings["wizard_from_toc_to_question_index"][-1].append(q_count)
        self.settings["wizard_question_visible"].append(False)
        q_count += 1
        # Q7 additional information
        self.settings["wizard_question_additional_info"] += [
            "<p>\
            This question aims to determine the size of the objects of interest in your images along the Z axis. For example, if you're working on cell nucleus segmentation, you should have a rough idea of how many slices the nuclei will appear across in the images. Refer to the image below for a clearer, visual understanding of this concept.\
            </p>\
            <div style='float:center;'>\
            <img style='float:center;' src='{}' width='200px'/> \
            </div>\
            <br><br><br><br><br><br><br><br><br><br><br><br><br><br>\
            ".format(resource_path(os.path.join("images", "wizard", "object_slices.png")))
        ]
        
        ######
        # Q8 #
        ######
        self.settings["wizard_questions"] += [
            "What do you want to do?",
        ]
        self.settings["wizard_possible_answers"] += [
            [
                "Train a model",
                "Test a model",
                "Train and test the model",
            ]
        ]
        self.settings["wizard_variable_to_map"]["Q8"] = {}
        self.settings["wizard_variable_to_map"]["Q8"]["TRAIN.ENABLE"] = [True, False, True]
        self.settings["wizard_variable_to_map"]["Q8"]["TEST.ENABLE"] = [False, True, True]
        self.settings["wizard_answers"]["TRAIN.ENABLE"] = -1
        self.settings["wizard_answers"]["TEST.ENABLE"] = -1
        self.settings["wizard_sections"][-1][1] += ["Phases"]
        self.settings["wizard_from_question_index_to_toc"].append(
            [1, len(self.settings["wizard_from_toc_to_question_index"][-1])]
        )
        self.settings["wizard_from_toc_to_question_index"][-1].append(q_count)
        self.settings["wizard_question_visible"].append(True)
        q_count += 1
        # Q8 additional information
        self.settings["wizard_question_additional_info"] += [
            "<p>\
            This question is meant to determine which phases of the workflow you want to perform.\
            </p>\
            <p>\
            Before using a deep learning model, it needs to be trained. The goal is to train the model on a specific task, then apply it to new images. For instance, you might train a model to classify images based on their labels. If the training is successful, the model should be able to classify new images automatically. This final phase is known as 'Test', sometimes referred to as 'Inference' or 'Prediction', which all describe the process of applying the model's knowledge to new data.\
            </p>\
            "
        ]

        ######
        # Q9 #
        ######
        self.settings["wizard_question_condition"]["Q9"] = {
            "and_cond": [
                [
                    "TRAIN.ENABLE", 
                    True
                ]
            ],
            "or_cond": [],
        }
        self.settings["wizard_questions"] += [
            "Could you please specify the location of the training raw image folder? After that, click on the 'Check data' button to analyze the data.",
        ]
        self.settings["wizard_possible_answers"] += [["PATH"]]
        self.settings["wizard_variable_to_map"]["Q9"] = {}
        self.settings["wizard_variable_to_map"]["Q9"]["DATA.TRAIN.PATH"] = ""
        self.settings["wizard_answers"]["DATA.TRAIN.PATH"] = -1
        self.settings["wizard_answers"]["CHECKED DATA.TRAIN.PATH"] = -1
        self.settings["wizard_sections"][-1][1] += ["Train data (raw)"]
        self.settings["wizard_from_question_index_to_toc"].append(
            [1, len(self.settings["wizard_from_toc_to_question_index"][-1])]
        )
        self.settings["wizard_from_toc_to_question_index"][-1].append(q_count)
        self.settings["wizard_question_visible"].append(False)
        q_count += 1
        # Q9 additional information
        self.settings["wizard_question_additional_info"] += [
            "<p>\
            In this step, you need to specify the folder where the images for training the network are located. All these images must have the same number of channels. It's also important that each channel contains the same type of information to avoid confusing the model.\
            </p>\
            <p>\
            The 'Check data' button will verify if the images within the selected folder can be read correctly by analyzing them one by one. This process may take some time, but it ensures that the images will be correctly read later in BiaPy. For this specific case, the following will be checked:\
            </p>\
            <ul>\
                <li>\
                    <p>All images can be read properly.</p>\
                </li>\
                <li>\
                    <p>All images have the same number of input channels.</p>\
                </li>\
                <li>\
                    <p>All images are within the same value range. For example, if the images are in uint8 format, their values should be between 0 and 255. This must be true for all images.</p>\
                </li>\
            </ul>\
            "
        ]
        #######
        # Q10 #
        #######
        self.settings["wizard_question_condition"]["Q10"] = {
            "and_cond": [
                [
                    "TRAIN.ENABLE", 
                    True
                ]
            ],
            "or_cond": [
                [
                    "PROBLEM.TYPE",
                    [
                        "SEMANTIC_SEG",
                        "INSTANCE_SEG",
                        "DETECTION",
                        "SUPER_RESOLUTION",
                        "IMAGE_TO_IMAGE",
                    ],
                ]
            ],
        }
        self.settings["wizard_questions"] += [
            "Could you please specify the location of the training ground truth (target) folder? After that, click on the 'Check data' button to analyze the data.",
        ]
        self.settings["wizard_possible_answers"] += [["PATH"]]
        self.settings["wizard_variable_to_map"]["Q10"] = {}
        self.settings["wizard_variable_to_map"]["Q10"]["DATA.TRAIN.GT_PATH"] = ""
        self.settings["wizard_answers"]["DATA.TRAIN.GT_PATH"] = -1
        self.settings["wizard_answers"]["CHECKED DATA.TRAIN.GT_PATH"] = -1
        self.settings["wizard_sections"][-1][1] += ["Train target (ground truth)"]
        self.settings["wizard_from_question_index_to_toc"].append(
            [1, len(self.settings["wizard_from_toc_to_question_index"][-1])]
        )
        self.settings["wizard_from_toc_to_question_index"][-1].append(q_count)
        self.settings["wizard_question_visible"].append(False)
        q_count += 1
        # Q10 additional information
        self.settings["wizard_question_additional_info"] += [
            "<p>\
            In this step, you need to specify the directory where the training target data, also known as 'ground truth', is located. This target data will be used to train the network.\
            </p>\
            <p>\
            The 'Check data' button will verify that the files in the selected folder can be read properly by analyzing them one by one. This process may take some time, but it ensures that the data will be correctly read by BiaPy later.\
            </p>\
            <p>\
            The target and its verification vary depending on the workflow:\
            </p>\
            <ul>\
            <li>\
            For <strong>Semantic segmentation</strong>, single-channel images are expected, specifically semantic masks. In these masks, each pixel will have a specific integer value corresponding to the class it belongs to. The checks performed include: 1) ensuring all images can be read correctly; 2) verifying that all images have the same number of input channels. Additionally, the number of classes to predict will be automatically extracted based on the different classes found in the images.\
            </li>\
            <li>\
            For <strong>Instance segmentation</strong>, one or two-channel images are expected. The first channel must always contain the instance masks, where each pixel has an integer value representing the object it belongs to. If two channels are provided, the second channel should contain the class of each instance. The checks performed include: 1) ensuring all images can be read correctly; 2) verifying that all images have the same number of input channels. If two channels are present, as in semantic segmentation, the number of classes to predict will be automatically extracted from the different classes found.\
            </li>\
            <li>\
            For <strong>Detection</strong>, files with the coordinates of object centers (centroids) are expected. The checks include: 1) ensuring the files can be read correctly; 2) verifying that the required columns for creating the coordinates are present in each file. Additionally, if the files contain a 'class' column, the number of classes will automatically be set to the highest value found in that column across all files.\
            </li>\
            <li>\
            For <strong>Super-resolution</strong>, high-resolution images are expected, meaning these images will be 2x or 4x larger than the versions in the 'Train data (raw)' folder from the previous step. The checks include: 1) ensuring all images can be read correctly; 2) verifying that all images have the same number of input channels; 3) checking that all images are within the same value range. For example, if the images are uint8, their values should be between 0 and 255 across all images.\
            </li>\
            <li>\
            For <strong>Image-to-Image</strong>, images are expected. The checks include: 1) ensuring all images can be read correctly; 2) verifying that all images have the same number of input channels; 3) checking that all images are within the same value range. For instance, if the images are uint8, the values should range between 0 and 255 across all images.\
            </li>\
            </ul>\
            "
        ]

        #######
        # Q11 #
        #######
        self.settings["wizard_question_condition"]["Q11"] = {
            "and_cond": [
                [
                    "TEST.ENABLE", 
                    True
                ]
            ],
            "or_cond": [],
        }
        self.settings["wizard_questions"] += [
            "Could you please specify the location of the test raw image folder? After that, click on the 'Check data' button to analyze the data.",
        ]
        self.settings["wizard_possible_answers"] += [["PATH"]]
        self.settings["wizard_variable_to_map"]["Q11"] = {}
        self.settings["wizard_variable_to_map"]["Q11"]["DATA.TEST.PATH"] = ""
        self.settings["wizard_answers"]["DATA.TEST.PATH"] = -1
        self.settings["wizard_answers"]["CHECKED DATA.TEST.PATH"] = -1
        self.settings["wizard_sections"][-1][1] += ["Test data (raw)"]
        self.settings["wizard_from_question_index_to_toc"].append(
            [1, len(self.settings["wizard_from_toc_to_question_index"][-1])]
        )
        self.settings["wizard_from_toc_to_question_index"][-1].append(q_count)
        self.settings["wizard_question_visible"].append(False)
        q_count += 1
        # Q11 additional information
        self.settings["wizard_question_additional_info"] += [
            "<p>\
            In this step, you need to specify the folder where the images for testing the network are located. All these images must have the same number of channels. It's also important that each channel contains the same type of information to avoid confusing the model.\
            </p>\
            <p>\
            The 'Check data' button will verify if the images within the selected folder can be read correctly by analyzing them one by one. This process may take some time, but it ensures that the images will be correctly read later in BiaPy. For this specific case, the following will be checked:\
            </p>\
            <ul>\
                <li>\
                    <p>All images can be read properly.</p>\
                </li>\
                <li>\
                    <p>All images have the same number of input channels.</p>\
                </li>\
                <li>\
                    <p>All images are within the same value range. For example, if the images are in uint8 format, their values should be between 0 and 255. This must be true for all images.</p>\
                </li>\
            </ul>\
            "
        ]

        #######
        # Q12 #
        #######
        self.settings["wizard_question_condition"]["Q12"] = {
            "and_cond": [
                [
                    "TEST.ENABLE", 
                    True
                ]
            ],
            "or_cond": [
                [
                    "PROBLEM.TYPE",
                    [
                        "SEMANTIC_SEG",
                        "INSTANCE_SEG",
                        "DETECTION",
                        "SUPER_RESOLUTION",
                        "IMAGE_TO_IMAGE",
                    ],
                ]
            ],
        }
        self.settings["wizard_questions"] += [
            "Do you have test ground truth (target) data?",
        ]
        self.settings["wizard_possible_answers"] += [
            [
                "No",
                "Yes",
            ]
        ]
        self.settings["wizard_variable_to_map"]["Q12"] = {}
        self.settings["wizard_variable_to_map"]["Q12"]["DATA.TEST.LOAD_GT"] = [False, True]
        self.settings["wizard_answers"]["DATA.TEST.LOAD_GT"] = -1
        self.settings["wizard_sections"][-1][1] += ["Test target data availability"]
        self.settings["wizard_from_question_index_to_toc"].append(
            [1, len(self.settings["wizard_from_toc_to_question_index"][-1])]
        )
        self.settings["wizard_from_toc_to_question_index"][-1].append(q_count)
        self.settings["wizard_question_visible"].append(False)
        q_count += 1
        # Q12 additional information
        self.settings["wizard_question_additional_info"] += [
            "<p>\
            This question is meant to determine whether you have target data, or ground truth, for the test data. If you have this, BiaPy will be able to calculate various metrics, which will vary depending on the selected workflow, to measure the model's performance.\
            </p>\
            <p>\
            If you answer 'Yes', a follow-up question will appear, asking for the path to the target data.\
            </p>\
            "
        ]
        
        self.settings["wizard_number_of_questions"] = len(self.settings["wizard_questions"])
        self.settings["wizard_question_answered_index"] = [-1]*len(self.settings["wizard_questions"])
        self.settings["wizard_question_visible_default"] = self.settings["wizard_question_visible"].copy()
        self.settings["original_wizard_answers"] = self.settings["wizard_answers"].copy()

        #######
        # Q13 #
        #######
        self.settings["wizard_question_condition"]["Q13"] = {
            "and_cond": [
                [
                    "TEST.ENABLE", 
                    True
                ],
                [
                    "DATA.TEST.LOAD_GT", 
                    True
                ]
            ],
            "or_cond": [
                [
                    "PROBLEM.TYPE",
                    [
                        "SEMANTIC_SEG",
                        "INSTANCE_SEG",
                        "DETECTION",
                        "SUPER_RESOLUTION",
                        "IMAGE_TO_IMAGE",
                    ],
                ]
            ],
        }
        self.settings["wizard_questions"] += [
            "Could you please specify the location of the test ground truth (target) folder? After that, click on the 'Check data' button to analyze the data.",
        ]
        self.settings["wizard_possible_answers"] += [["PATH"]]
        self.settings["wizard_variable_to_map"]["Q13"] = {}
        self.settings["wizard_variable_to_map"]["Q13"]["DATA.TEST.GT_PATH"] = ""
        self.settings["wizard_answers"]["DATA.TEST.GT_PATH"] = -1
        self.settings["wizard_answers"]["CHECKED DATA.TEST.GT_PATH"] = -1
        self.settings["wizard_sections"][-1][1] += ["Test target (ground truth)"]
        self.settings["wizard_from_question_index_to_toc"].append(
            [1, len(self.settings["wizard_from_toc_to_question_index"][-1])]
        )
        self.settings["wizard_from_toc_to_question_index"][-1].append(q_count)
        self.settings["wizard_question_visible"].append(False)
        q_count += 1
        # Q13 additional information
        self.settings["wizard_question_additional_info"] += [
            "<p>\
            In this step, you need to specify the directory where the test target data, also known as 'ground truth', is located. This target data will be used to train the network.\
            </p>\
            <p>\
            The 'Check data' button will verify that the files in the selected folder can be read properly by analyzing them one by one. This process may take some time, but it ensures that the data will be correctly read by BiaPy later.\
            </p>\
            <p>\
            The target and its verification vary depending on the workflow:\
            </p>\
            <ul>\
            <li>\
            For <strong>Semantic segmentation</strong>, single-channel images are expected, specifically semantic masks. In these masks, each pixel will have a specific integer value corresponding to the class it belongs to. The checks performed include: 1) ensuring all images can be read correctly; 2) verifying that all images have the same number of input channels. Additionally, the number of classes to predict will be automatically extracted based on the different classes found in the images.\
            </li>\
            <li>\
            For <strong>Instance segmentation</strong>, one or two-channel images are expected. The first channel must always contain the instance masks, where each pixel has an integer value representing the object it belongs to. If two channels are provided, the second channel should contain the class of each instance. The checks performed include: 1) ensuring all images can be read correctly; 2) verifying that all images have the same number of input channels. If two channels are present, as in semantic segmentation, the number of classes to predict will be automatically extracted from the different classes found.\
            </li>\
            <li>\
            For <strong>Detection</strong>, files with the coordinates of object centers (centroids) are expected. The checks include: 1) ensuring the files can be read correctly; 2) verifying that the required columns for creating the coordinates are present in each file. Additionally, if the files contain a 'class' column, the number of classes will automatically be set to the highest value found in that column across all files.\
            </li>\
            <li>\
            For <strong>Super-resolution</strong>, high-resolution images are expected, meaning these images will be 2x or 4x larger than the versions in the\
            'Train data (raw)' folder from the previous step. The checks include: 1) ensuring all images can be read correctly; 2) verifying that all images have the same number of input channels; 3) checking that all images are within the same value range. For example, if the images are uint8, their values should be between 0 and 255 across all images.\
            </li>\
            <li>\
            For <strong>Image-to-Image</strong>, images are expected. The checks include: 1) ensuring all images can be read correctly; 2) verifying that\
            all images have the same number of input channels; 3) checking that all images are within the same value range. For instance, if\
            the images are uint8, the values should range between 0 and 255 across all images.\
            </li>\
            </ul>\
            "
        ]
        
        self.settings["wizard_number_of_questions"] = len(self.settings["wizard_questions"])
        self.settings["wizard_question_answered_index"] = [-1]*len(self.settings["wizard_questions"])
        self.settings["wizard_question_visible_default"] = self.settings["wizard_question_visible"].copy()
        self.settings["original_wizard_answers"] = self.settings["wizard_answers"].copy()

    def translate_model_names(self, model, dim, inv=False):
        s = "_models_real_names" if not inv else "_models"
        s2 = "_models" if not inv else "_models_real_names"
        for x in ["semantic", "instance", "detection", "denoising", "sr", "ssl", "classification", "i2i"]:
            try:
                d = ""
                if x in ["sr", "ssl", "i2i"] and dim == "2D":
                    d = "_2d_"
                elif x in ["sr", "ssl", "i2i"] and dim == "3D":
                    d = "_3d_"
                idx = list(self.settings[x + d + s]).index(model)
            except:
                pass
            else:
                return list(self.settings[x + d + s2])[idx]
            
    def translate_names(self, model, key_str="", inv=False):
        s = f"_{key_str}_real_names" if not inv else f"_{key_str}"
        s2 = f"_{key_str}" if not inv else f"_{key_str}_real_names"
        for x in ["semantic", "instance", "detection", "denoising", "sr", "ssl", "classification", "i2i"]:
            try:
                idx = list(self.settings[x + s]).index(model)
            except:
                pass
            else:
                return list(self.settings[x + s2])[idx]
            
    