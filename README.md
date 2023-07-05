# Graphical user interface for BiaPy: Bioimage analysis pipelines in Python

<kbd>
  <img src="https://raw.githubusercontent.com/danifranco/BiaPy-GUI/main/images/BiaPy_GUI_main_page.png">
</kbd>

[BiaPy](https://github.com/danifranco/BiaPy) is an open source Python library for building bioimage analysis pipelines. This repository is actively under development by the Biomedical Computer Vision group at the [University of the Basque Country](https://www.ehu.eus/en/en-home) and the [Donostia International Physics Center](http://dipc.ehu.es/). 


## Run GUI 

- [Windows 64-bit (outdated)](https://github.com/danifranco/BiaPy-GUI/raw/main/dist-win/BiaPy.exe) 
- [Linux 64-bit](https://github.com/danifranco/BiaPy-GUI/raw/main/dist-linux/BiaPy) 
- [macOS 64-bit](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/danifranco/BiaPy-GUI/raw/main/dist-macOS/BiaPy.app) 

## For developers (through console):

Download the repository first:

```shell
git clone https://github.com/danifranco/BiaPy-GUI.git
```

This will create a folder called ``BiaPy-GUI`` that contains all the files of the repository. Then you need to create a conda environment and install the dependencies:

```shell
conda create -n biapy-gui python=3.10.10
conda activate biapy-gui
pip install -r requirements.txt
```

After that simply run the ``main.py`` :

```shell
cd BiaPy-GUI
python main.py
```

To create the binary files:

```shell
cd BiaPy-GUI
pyinstaller -F main.py
```

You can also modify the main.spec file (e.g. to add new images) and redo the binary:
```shell
pyinstaller main.spec
```

This will create a ``main.spec`` file and a ``dist`` folder with ``BiaPy`` binary inside it. 

## Citation                                                                                                             
                                                                                                                        
This repository is the base of the following work:                                                                      
                                                                                                                        
```bibtex
@inproceedings{franco-barranco2023biapy,
    author = {Daniel Franco-Barranco and Jes{\'{u}}s A. Andr{\'{e}}s-San Rom{\'{a}}n and Pedro G{\'{o}}mez-G{\'{a}}lvez and Luis M. Escudero and Arrate Mu{\~n}oz-Barrutia and Ignacio Arganda-Carreras},
    title = {{BiaPy: a ready-to-use library for Bioimage Analysis Pipelines}},
    booktitle={2023 IEEE 20th International Symposium on Biomedical Imaging (ISBI 2023)},
    year={2023},
    organization={IEEE}
}
``` 