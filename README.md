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

将MDB格式文件转为CSV格式

```
    def mdbtocsv(self):
        driver = '{Microsoft Access Driver (*.mdb, *.accdb)}'
        if (os.path.exists(self.operation_data_csv_path) == False):
            os.makedirs(self.operation_data_csv_path) #Create folder of operation parameters
        if (os.path.exists(self.dose_data_csv_path) == False):
            os.makedirs(self.dose_data_csv_path)  #Create folder of dose parameters
        for accident in os.listdir(self.data_path):
            accident_path = self.data_path + '\\'+ accident
            os.chdir(self.project_path) # Make sure it is the project path
            for name in os.listdir(accident_path):
                if not (re.search(r'Transient Report.txt',name))  :
                    os.chdir(self.project_path) # Make sure the database conect normally
                    mdb_file = accident_path + '\\' + name
                    print(mdb_file)
                    cnxn = pyodbc.connect(f'Driver={driver};DBQ={mdb_file}')
                    if re.search(r'\d+' + '.mdb', name) : #Operation data
                        data_table = pd.read_sql('SELECT * FROM PlotData', cnxn)
                        data_table.sort_values(by=['TIME'], ascending=True,
                                               inplace=True)  # Some mdbs have problems with not being in time order
                        csv_accident_path = self.operation_data_csv_path + '\\' + accident
                        if (os.path.exists(csv_accident_path) == False):
                            os.makedirs(csv_accident_path)
                        os.chdir(csv_accident_path)
                        csv_name = name.replace('mdb','csv')
                        data_table.to_csv(csv_name, header=True, index=False)
                    elif re.search(r'\d+' + 'dose' + '.mdb', name) : #Dose data
                        data_table = pd.read_sql('SELECT * FROM ListDS', cnxn)
                        data_table.sort_values(by=['TIME'], ascending=True,
                                               inplace=True)  # Some mdbs have problems with not being in time order
                        csv_accident_path = self.dose_data_csv_path + '\\' + accident
                        if(os.path.exists(csv_accident_path) == False):
                            os.makedirs(csv_accident_path)
                        os.chdir(csv_accident_path)
                        csv_name = name.replace('mdb', 'csv')
                        data_table.to_csv(csv_name, header=True, index=False)
```

- Method *generate_dataset*

生成可用于监督学习任务的标准数据集
```
    def generate_dataset(self, dataset_source_path):
        class Mydataset(Dataset):
            def __int__(self, dataset_path):
                self.dataset_path = dataset_path
                self.feature = []
                self.label = []
                """
                1. Read all csv files in order
                2. Add labels(accident types) to self.label, 
                add features(operation data or dose data) to self.feature
                """
                for accident in os.listdir(self.dataset_path):
                    accident_path = self.data_path + '\\' + accident
                    for size_name in os.listdir(accident_path):
                        csv_data_path = accident_path + '\\' + size_name
                        self.label.append(accident)
                        sample_df = pd.read_csv(csv_data_path)
                        sample_value = (sample_df.iloc[:150, 1:]).values  # Take the data of 1500s
                        sample_list = list(chain.from_iterable(sample_value))  # Convert 2-D list to 1-D list
                        self.feature.append(sample_list)
                self.label = (pd.Categorical(self.label)).codes
                assert len(self.label) == len(self.feature)
                self.length = len(self.feature)
            def __getitem__(self, index):
                x = self.feature[index]
                x = torch.Tensor(x)
                y = self.label[index]
                return {"x": x, "y": y}

            def __len__(self):
                return self.length
        return Mydataset(dataset_source_path)
```
- Method *show_parameters*

可以绘制参数变化曲线的脚本
```
    def show_parametes(self, variables, plot_data_path, figture_save_path):
        if (os.path.exists(figture_save_path) == False):
            os.makedirs(figture_save_path)
        plot_data = pd.read_csv(plot_data_path)
        plot_df = plot_data[variables]
        plot_df.set_index(plot_df.columns[0],inplace=True)
        fig_plot = plot_df.plot()
        plt.xlabel(variables[0])
        plt.show()
        fig_name = ''
        for var in range(1,len(variables)):
            fig_name = fig_name  + variables[var] + '-'
        print(fig_name)
        fig_save = fig_plot.get_figure()
        fig_path = figture_save_path + "\\" + fig_name
        fig_save.savefig(fig_path)
```
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