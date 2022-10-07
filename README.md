![](https://github.com/qiben-jy/NuclearPowerPlantAccidentData/blob/5ad5c50f6b178dd517378fd16b71f91bf9795b3e/LOGO.png)
# Welcome to NPPAD
### NPPAD: a dataset covering various accidents for nuclear power plants

![GitHub](https://img.shields.io/github/languages/count/qiben-jy/NuclearPowerPlantAccidentData)
![GitHub followers](https://img.shields.io/github/followers/qiben-jy?style=social)
![GitHub](https://img.shields.io/github/watchers/qiben-jy/NuclearPowerPlantAccidentData?style=social)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/qiben-jy/NuclearPowerPlantAccidentData)

This repository contains:

1. The background of this project

2. Introduction to the dataset

3. Related data processing scripts

Hopefully, you can use this project to get the needed accident data for nuclear power plants and then develop new accident diagnosis algorithms and benchmarks.

  <ol>
    <li>
      <a href="#Background">Background</a>
    </li>
    <li>
      <a href="#Introduction to the dataset">Introduction to the dataset</a>
      <ul>
        <li><a href="#Workflow overview">Workflow overview</a></li>
        <li><a href="#Dataset structure">Dataset structure</a></li>
      </ul>
    </li>
    <li><a href="#Related scripts">Related scripts</a>
    </li>
    <li><a href="#Installation">Installation</a></li>
    <li><a href="#Maintainers">Maintainers</a></li>
    <li><a href="#Contributing">Contributing</a></li>
    <li><a href="#License">License</a></li>
  </ol>

## Background
Nuclear energy plays an important role in global energy supply, especially as a key low-carbon source of power. Safe operation is critical in the generation of nuclear energy, i.e. in nuclear power plants. Given the significant impact of human-caused errors on three serious nuclear accidents in history, artificial intelligence technologies are increasingly being used to assist plant operators in making decisions. Specifically, artificial intelligence algorithms are used to identify the presence of accidents and their root causes. A continuing challenge is the lack of an open dataset in the nuclear power plant domain to measure the performance of various algorithms. we presents a first-of-its-kind public dataset created with the help of PCTRAN, a pre-developed and widely used simulation software for nuclear power plants. The dataset, NPPAD, basically covers most of the common types of accidents that can occur in pressurized water reactor nuclear power plants. It contains time-series data on the status or actions of various subsystems as well as the accident types and severity information. The dataset also incorporates other simulation data like the amount of radionuclide released, which can help users to conduct research beyond accident diagnosis.

## Introduction to the dataset
The initial version of the dataset contains 18 types of operating conditions that are possible under full power operation of a three-loop pressurized water reactor nuclear power plant.
### Workflow overview
数据生产流程，对图5和Box1描述（可添加图片,表格等）
### Dataset structure
对box2-6进行描述（可添加图片,表格等）
## Related scripts
在[Data Processing.py](https://github.com/qiben-jy/NuclearPowerPlantAccidentData/blob/350288cd65eefe456fa6f0af72e4417c1678f5fe/Data%20Processing.py)中提供了以下三种脚本：

- Method *mdbtocsv*

分别是将MDB格式文件转为CSV格式
- Method *generate_dataset*

生成可用于监督学习任务的标准数据集

- Method *show_parameters*

可以绘制参数变化曲线的脚本

## Installation
First, Python 3.6 or higher is already installed by default.

To install NPPAD from the soure code:
```
$ git clone https://github.com/thu-inet/NuclearPowerPlantAccidentData 
$ cd NuclearPowerPlantAccidentData/
$ pip install -r requirements.txt
$ python setup.py install
```

## Maintainers

- [Ben Qi](https://github.com/qiben-jy)
- [Xingyu Xiao](https://github.com/Crystalxy123)
- [Jingang Liang](https://github.com/liangjg)
- [THU-INET](https://github.com/thu-inet)

## Contributing
We appreciate all contributions. Please let us know if you encounter a bug by filing an issue.

## License
NPPAD has a MIT license, as found in the [LICENSE](https://github.com/qiben-jy/NuclearPowerPlantAccidentData/blob/ab8c9dc45e594b793097ca9582e959ee7935eeb5/LICENSE) file.