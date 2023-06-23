# Graphical user interface for BiaPy: Bioimage analysis pipelines in Python

![BiaPy GUI](./images/BiaPy_GUI_main_page.png)

[BiaPy](https://github.com/danifranco/BiaPy) is an open source Python library for building bioimage analysis pipelines. This repository is actively under development by the Biomedical Computer Vision group at the [University of the Basque Country](https://www.ehu.eus/en/en-home) and the [Donostia International Physics Center](http://dipc.ehu.es/). 


## Run GUI locally

Download the repository first:

```shell
git clone https://github.com/danifranco/BiaPy-GUI.git
```

This will create a folder called ``BiaPy-GUI`` that contains all the files of the repository. Then you need to create a conda environment using the file located in ``BiaPy-GUI/environment.yml`` :

```shell
conda env create -f BiaPy-GUI/environment.yml
conda activate biapy-gui
```

After that simply run the ``main.py`` :

```shell
cd BiaPy-GUI
python main.py
```

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