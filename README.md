![](https://github.com/qiben-jy/NuclearPowerPlantAccidentData/blob/5ad5c50f6b178dd517378fd16b71f91bf9795b3e/LOGO.png)
# Welcome to NPPAD
### NPPAD: An Open Time-series Dataset Covering Various Accidents for Nuclear Power Plants

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
Nuclear energy plays an important role in global energy supply, especially as a key low-carbon source of power. 
Safe operation is critical in the generation of nuclear energy, i.e. in nuclear power plants. Given the significant 
impact of human-caused errors on three serious nuclear accidents in history, artificial intelligence technologies are 
increasingly being used to assist plant operators in making decisions. Specifically, artificial intelligence algorithms 
are used to identify the presence of accidents and their root causes. A continuing challenge is the lack of an open dataset 
in the nuclear power plant domain to measure the performance of various algorithms. we presents a first-of-its-kind public 
dataset created with the help of [PCTRAN](https://github.com/thu-inet/NuclearPowerPlantAccidentData/tree/main/Simulator), a pre-developed and widely used simulation software for nuclear power plants. The 
dataset, NPPAD, basically covers most of the common types of accidents that can occur in pressurized water reactor nuclear
power plants. It contains time-series data on the status or actions of various subsystems as well as the accident types and
severity information. The dataset also incorporates other simulation data like the amount of radionuclide released, which 
can help users to conduct research beyond accident diagnosis.

## Introduction to the dataset
The initial version of the dataset contains 18 types of operating conditions that are possible under full power operation of a three-loop pressurized water reactor nuclear power plant.
### Workflow overview
Fig.1 Overall Workflow Of The Simulation Data Generation  
<img src="https://github.com/thu-inet/NuclearPowerPlantAccidentData/blob/main/Figures/fig1.png" width="375">
The overall workflow implemented in the script to generate the nuclear power plant accident dataset is shown in Fig. 1.  
First, we started the software by an automation script. Once the software is launched, the nuclear plant operating at 100% power is initialized.
Then we select different operating conditions. If the normal operating condition is treated, the simulator will run for a certain time that we configured to get the data output. Besides, for abnormal operating conditions, accident type, accident parameters and simulation time are configured, and then simulation data is output. The accidents covered in this work is shown in Table 1 . Specifically, The parameter selection screen is shown in the figure.
After that, PCTRAN will simulate automatedly. The detailed process of accident simulation in PCTRAN is shown in Box 1. First, a set of input parameters are configured according to the operations. which decide the way of the corresponding simulations. And we can get the output data in a certain time.
Finally, we get the dataset NPPAD.zip with different conditions.  
PS: The dataset in this work does not include cases where mitigation system failures are superimposed on nuclear plant accidents, as such superimposed cases are too numerous to cover. 

Table1 Accident sets covered by NPPAD  

Folder name|Accident|Type|Severity|
:----------|:-------|:---|:-------|
NORM|Normal operating|-|-|
LOCA|Loss of Coolant Accident (Hot Leg)|Severity|% of 100 cm2|
LOCAC|Loss of Coolant Accident (Cold Leg)|Severity|% of 100 cm2|
SLBIC|Steam Line Break Inside Containment|Severity|% of 100 cm2|
SLBOC|Steam Line Break Outside Containment|Severity|% of 100 cm2|
SP|Spark Presence for Hydrogen Burn|Other|Only one situation|
LACP|Loss of AC Power|Other|Only one situation|
LOF|Loss of Flow (Locked Rotor)|Other|Only one situation|
ATWS|Anticipated Transient Without Scram|Other|Only one situation
TT|Turbine Trip|Other|Only one situation|
SGATR|Steam Generator A Tube Rupture|Severity|% of 1 full tube rupture|
SGBTR|Steam Generator B Tube Rupture|Severity|% of 1 full tube rupture|
RW|Rod Withdrawal|Severity|% (+/-) withdrawn|
RI|Rod Insertion|Severity|% (+/-) insertion|
FLB|Feedwater Line Break|Severity|% of 100 cm2|
MD|Moderator Dilution|Severity|% of unborated injection|
LR|Load Rejection|Severity|% of full load rejected|
LLB|Letdown Line Break in auxiliary buildings|Severity|% of nominal letdown flow|
### Dataset structure
<img src="https://github.com/thu-inet/NuclearPowerPlantAccidentData/blob/main/Figures/fig2.png" width="375">
The NPPAD dataset covers 18 types of operating conditions, with Box 2 shows partially. Each operating condition sample contains three files, two in mdb format and the other in txt format. The mdb file can be opened directly through Microsoft Access. For example, the content of 1.mdb (PlotData) is shown in box 3, it represents the time series of the status parameters with a 1% of 100 cm2 break of LOCA, while PlotData represents the sub-table in the 1.mdb file. Another useful sub-table is ListPlotVariables, as shown in Box 6, which describes the parameters corresponding to the abbreviations in PlotData. And in box 4, 1Dose.mdb represents the time series of the radionuclide in the nuclear power plant. In addition to the mdb format, we also provide CSV format in the folders Operation_csv_data and Dose_csv_data. Besides, 1Transient Report.txt in box 5 describes the actions in the subsystems of the nuclear plant over the simulation time for each accident, which can help the user to understand the changes in the plant status. The numbers in front of the files in other operating conditions (e.g. 1.mdb, 2.mdb) correspond to the severity of the accident, and the exact meaning can be determined by column ‘severity’ of Table 1.
## Related scripts
The following three scripts are provided in [Data Processing.py](https://github.com/thu-inet/NuclearPowerPlantAccidentData/blob/main/Data%20Processing.py)

- **Method *mdbtocsv***

Use this method to convert files from *mdb* format to *csv* format, the files [Dose_csv_data](https://github.com/thu-inet/NuclearPowerPlantAccidentData/tree/main/Dose_csv_data) and [Operation_csv_data](https://github.com/thu-inet/NuclearPowerPlantAccidentData/tree/main/Operation_csv_data) in this project are the result of converting the original dataset [DATA](https://github.com/thu-inet/NuclearPowerPlantAccidentData/tree/main/DATA) into csv format.


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

- **Method *generate_dataset***

Use this method to generate a standard dataset for supervised learning tasks.
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
- **Method *show_parameters***

Use this method to plot the variation of physical parameters.
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
