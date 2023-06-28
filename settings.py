import os 
from PySide2.QtGui import QPixmap
from ui_utils import resource_path

def get_default_settings():
    settings = {}

    settings['init'] = False 
    settings['page_number'] = 0

    # OS
    settings['os_host'] = None
    settings['user_host'] = None

    # Biapy 
    settings['biapy_container_name'] = "danifranco/biapy:v1.0"
    settings['biapy_container_dockerfile'] = "https://raw.githubusercontent.com/danifranco/BiaPy/master/utils/env/Dockerfile"
    settings['yaml_config_file_path'] =''
    settings['yaml_config_filename'] = ''
    settings['output_folder'] = ''
    settings['biapy_cfg'] = None
    settings['biapy_container_ready'] = False

    # Docker 
    settings['docker_client'] = None
    settings['docker_found'] = False
    settings['running_threads'] = []
    settings['running_workers'] = []

    # For all pages 
    settings['advanced_frame_images'] = None

    # Workflow page
    settings['workflow_names'] = ["Semantic\nSegmentation", "Instance\nsegmentation", "Object\ndetection", "Image\ndenoising", "Super\nresolution",\
        "Self-supervised\nlearning", "Image\nclassification"]
    settings['workflow_images'] = None
    settings['workflow_images_selec'] = None
    settings['workflow_description_images'] = None
    settings['workflow_descriptions'] = None
    settings['selected_workflow'] = 1
    settings['dot_images'] = None
    settings['continue_bn_icons'] = None

    # Semantic segmentation
    settings['semantic_models'] = ['unet', 'resunet', 'attention_unet', 'fcn32', \
            'fcn8', 'tiramisu', 'mnet', 'multiresunet', 'seunet', 'unetr']
    # Instance segmentation
    settings['instance_models'] = ['unet', 'resunet', 'seunet', 'attention_unet']
    # Detection
    settings['detection_models'] = ['unet', 'resunet', 'seunet', 'attention_unet']
    # Denoising
    settings['denoising_models'] = ['unet', 'resunet', 'seunet', 'attention_unet']
    # Super resolution
    settings['sr_models'] = ['edsr', 'srunet', 'rcan', 'dfcan', 'wdsr']
    # Self-supervised learning
    settings['ssl_models'] = ['unet', 'resunet', 'seunet', 'attention_unet']
    # Classification
    settings['classification_models'] = ['simple_cnn', 'EfficientNetB0']

    # Paths
    settings['train_data_input_path'] = None
    settings['train_data_gt_input_path'] = None
    settings['validation_data_input_path'] = None
    settings['validation_data_gt_input_path'] = None
    settings['test_data_input_path'] = None
    settings['test_data_gt_input_path'] = None


    settings['workflow_images'] = [
        QPixmap(resource_path(os.path.join("images","semantic_seg.png"))),
        QPixmap(resource_path(os.path.join("images","instance_seg.png"))),
        QPixmap(resource_path(os.path.join("images","detection.png"))),
        QPixmap(resource_path(os.path.join("images","denoising.png"))),
        QPixmap(resource_path(os.path.join("images","sr.png"))),
        QPixmap(resource_path(os.path.join("images","ssl.png"))),
        QPixmap(resource_path(os.path.join("images","classification.png")))
    ]

    settings['workflow_images_selec'] = [
        QPixmap(resource_path(os.path.join("images","semantic_seg_selected.png"))),
        QPixmap(resource_path(os.path.join("images","instance_seg_selected.png"))),
        QPixmap(resource_path(os.path.join("images","detection_selected.png"))),
        QPixmap(resource_path(os.path.join("images","denoising_selected.png"))),
        QPixmap(resource_path(os.path.join("images","sr_selected.png"))),
        QPixmap(resource_path(os.path.join("images","ssl_selected.png"))),
        QPixmap(resource_path(os.path.join("images","classification_selected.png")))
    ]
    
    settings['workflow_description_images'] = [
        [QPixmap(resource_path(os.path.join("images","semantic_seg_raw.png"))),QPixmap(resource_path(os.path.join("images","semantic_seg_label.png")))],
        [QPixmap(resource_path(os.path.join("images","instance_seg_raw.png"))),QPixmap(resource_path(os.path.join("images","instance_seg_label.png")))],
        [QPixmap(resource_path(os.path.join("images","detection_raw.png"))),QPixmap(resource_path(os.path.join("images","detection_csv_input.png")))],
        [QPixmap(resource_path(os.path.join("images","denoising_raw.png"))),QPixmap(resource_path(os.path.join("images","denoising_pred.png")))],
        [QPixmap(resource_path(os.path.join("images","sr_raw.png"))),QPixmap(resource_path(os.path.join("images","sr_pred.png")))],
        [QPixmap(resource_path(os.path.join("images","ssl_raw.png"))),QPixmap(resource_path(os.path.join("images","ssl_pred.png")))],
        [QPixmap(resource_path(os.path.join("images","classification_raw.png"))),QPixmap(resource_path(os.path.join("images","classification_label.png")))]
    ]

    settings['workflow_descriptions'] = [
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

    settings['advanced_frame_images'] = [
        QPixmap(resource_path(os.path.join("images","bn_images","up_arrow.svg"))),
        QPixmap(resource_path(os.path.join("images","bn_images","down_arrow.svg")))
    ]
    settings['dot_images'] = [
        QPixmap(resource_path(os.path.join("images","bn_images","dot_enable.svg"))),
        QPixmap(resource_path(os.path.join("images","bn_images","dot_disable.svg")))
    ]
    
    return settings