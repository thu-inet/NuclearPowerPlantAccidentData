![](https://github.com/qiben-jy/NuclearPowerPlantAccidentData/blob/5ad5c50f6b178dd517378fd16b71f91bf9795b3e/LOGO.png)
# Welcome to NPPAD
### NPPAD: An Open Time-series Dataset Covering Various Accidents for Nuclear Power Plants

![GitHub](https://img.shields.io/github/languages/count/thu-inet/NuclearPowerPlantAccidentData)
![GitHub followers](https://img.shields.io/github/followers/thu-inet?style=social)
![GitHub](https://img.shields.io/github/watchers/thu-inet/NuclearPowerPlantAccidentData?style=social)
![License](https://img.shields.io/github/license/thu-inet/NuclearPowerPlantAccidentData)
![Contributors](https://img.shields.io/github/contributors/thu-inet/NuclearPowerPlantAccidentData)
![Open Pull Requests](https://img.shields.io/github/issues-pr/thu-inet/NuclearPowerPlantAccidentData)
![HitCount](http://hits.dwyl.com/thu-inet/NuclearPowerPlantAccidentData.svg)
![Made with Love](https://img.shields.io/badge/Made%20with-Love-ff69b4)




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
      <a href="#Introduction-to-the-dataset">Introduction to the dataset</a>
      <ul>
        <li><a href="#Workflow-overview">Workflow overview</a></li>
        <li><a href="#Dataset-structure">Dataset structure</a></li>
      </ul>
    </li>
    <li><a href="#Related-scripts">Related scripts</a>
    </li>
    <li><a href="#Installation">Installation</a></li>
    <li><a href="#Maintainers">Maintainers</a></li>
    <li><a href="#Contributing">Contributing</a></li>
    <li><a href="#License">License</a></li>
     <li><a href="#Citing">Citing</a></li>
     <li><a href="#Related-work">Related work</a></li>
  </ol>

## Background
Nuclear energy plays an important role in global energy supply, especially as a key low-carbon source of power. 
Safe operation is critical in the generation of nuclear energy, i.e. in nuclear power plants. Given the significant 
impact of human-caused errors on three serious nuclear accidents in history, artificial intelligence technologies are 
increasingly being used to assist plant operators in making decisions. Specifically, artificial intelligence algorithms 
are used to identify the presence of accidents and their root causes. A continuing challenge is the lack of an open dataset 
in the nuclear power plant domain to measure the performance of various algorithms. we presents a first-of-its-kind public 
dataset created with the help of [PCTRAN](https://github.com/thu-inet/NuclearPowerPlantAccidentData/tree/main/Simulator), a pre-developed and widely used simulation software for nuclear power plants. The 
dataset, [NPPAD](https://github.com/thu-inet/NuclearPowerPlantAccidentData/tree/main/NPPAD), basically covers most of the common types of accidents that can occur in pressurized water reactor nuclear
power plants. It contains time-series data on the status or actions of various subsystems as well as the accident types and
severity information. The dataset also incorporates other simulation data like the amount of radionuclide released, which 
can help users to conduct research beyond accident diagnosis.

## Introduction to the dataset

### Workflow overview
<img src="https://github.com/thu-inet/NuclearPowerPlantAccidentData/blob/main/Figures/fig1.png" width="375">  
Fig. 1 Overall Workflow Of The Simulation Data Generation   
<br/>
<br/>
The overall workflow implemented in the script to generate the nuclear power plant accident dataset is shown in Fig. 1. First, we started the software by an automation script. Once the software is launched, the nuclear plant operating at 100% power is initialized.Then we select different operating conditions. If the normal operating condition is treated, the simulator will run for a certain time that we configured to get the data output. Besides, for abnormal operating conditions, accident type, accident parameters and simulation time are configured, and then simulation data is output. The accidents covered in this work is shown in Table 1 . Specifically, the parameter selection screen is shown in the Fig. 2.  
<br/>
<br/>
<img src="https://github.com/thu-inet/NuclearPowerPlantAccidentData/blob/main/Figures/fig3.png" width="375">     
Fig. 2 Accident type selection and parameter setting  
<br/>
<br/>
After that, PCTRAN will simulate automatedly. The detailed process of accident simulation in PCTRAN is shown in Box 1. First, a set of input parameters are configured according to the operations. which decide the way of the corresponding simulations. And we can get the output data in a certain time.
Finally, we get the dataset NPPAD with different conditions.  
PS: The dataset in this work does not include cases where mitigation system failures are superimposed on nuclear plant accidents, as such superimposed cases are too numerous to cover. 
<br/>
<br/>
Table1 Accident sets covered by NPPAD

Folder name|Accident| Type     | Severity                  |
:----------|:-------|:---------|:--------------------------|
NORM|Normal operating| -        | -                         |
LOCA|Loss of Coolant Accident (Hot Leg)| Severity | % of 100 cm2              |
LOCAC|Loss of Coolant Accident (Cold Leg)| Severity | % of 100 cm2              |
SLBIC|Steam Line Break Inside Containment| Severity | % of 100 cm2              |
SLBOC|Steam Line Break Outside Containment| Severity | % of 100 cm2              |
SP|Spark Presence for Hydrogen Burn| Other    | -                         |
LACP|Loss of AC Power|Other    | -        |
LOF|Loss of Flow (Locked Rotor)| Other    | -                         |
ATWS|Anticipated Transient Without Scram| Other    | -                         
TT|Turbine Trip| Other    | -                         |
SGATR|Steam Generator A Tube Rupture| Severity | % of 1 full tube rupture  |
SGBTR|Steam Generator B Tube Rupture| Severity | % of 1 full tube rupture  |
RW|Rod Withdrawal| Severity | % (+/-) withdrawn         |
RI|Rod Insertion| Severity | % (+/-) insertion         |
FLB|Feedwater Line Break| Severity | % of 100 cm2              |
MD|Moderator Dilution| Severity | % of unborated injection  |
LR|Load Rejection| Severity | % of full load rejected   |
LLB|Letdown Line Break in auxiliary buildings| Severity | % of nominal letdown flow |

Table 2 Description of accident parameters

| ID  | Label                                   | Units           | Name  |
|-----|-----------------------------------------|-----------------|-------|
| 1   | Time (sec)                              | sec             | TIME  |
| 2   | Temp RCS average (°C)                   | °C              | TAVG  |
| 3   | Temp Hot leg A (°C)                     | °C              | THA   |
| 4   | Temp Hot leg B (°C)                     | °C              | THB   |
| 5   | Temp Cold leg A (°C)                    | °C              | TCA   |
| 6   | Temp Cold leg B (°C)                    | °C              | TCB   |
| 7   | Flow Reactor coolant loop A (t/hr)      | t/hr            | WRCA  |
| 8   | Flow Reactor coolant loop B (t/hr)      | t/hr            | WRCB  |
| 9   | Pressure Steam generator A (bar)        | bar             | PSGA  |
| 10  | Pressure Steam generator B (bar)        | bar             | PSGB  |
| 11  | Flow SG A feedwater (t/hr)              | t/hr            | WFWA  |
| 12  | Flow SG B feedwater (t/hr)              | t/hr            | WFWB  |
| 13  | Flow SG A steam (t/hr)                  | t/hr            | WSTA  |
| 14  | Flow SG B steam (t/hr)                  | t/hr            | WSTB  |
| 15  | Volume RCS liquid (M3)                  | M3              | VOL   |
| 16  | Level Pressurizer (%)                   | %               | LVPZ  |
| 17  | Void of RCS (%)                         | %               | VOID  |
| 18  | Flow RCS leak (t/hr)                    | t/hr            | WLR   |
| 19  | Flow Przr PORV and safeties (t/hr)      | t/hr            | WUP   |
| 20  | Spec Enthalpy Przr discharge (kJ/kg)    | kJ/kg           | HUP   |
| 21  | Spec Enthalpy RCS leak (kJ/kg)          | kJ/kg           | HLW   |
| 22  | Flow HPI (t/hr)                         | t/hr            | WHPI  |
| 23  | Flow Total ECCS (t/hr)                  | t/hr            | WECS  |
| 24  | PowerTotal megawatt thermal (MW)        | MW              | QMWT  |
| 25  | Level SG A wide range (M)               | M               | LSGA  |
| 26  | Level SG B wide range (M)               | M               | LSGB  |
| 27  | Power SG A heat removal (MW)            | MW              | QMGA  |
| 28  | Power SG B heat removal (MW)            | MW              | QMGB  |
| 29  | Level SG A narrow range (%)             | %               | NSGA  |
| 30  | Level SG B narrow range (%)             | %               | NSGB  |
| 31  | Power Turbine load (%)                  | %               | TBLD  |
| 32  | Flow SG A tube leak (t/hr)              | t/hr            | WTRA  |
| 33  | Flow SG B tube leak (t/hr)              | t/hr            | WTRB  |
| 34  | Temp Przr saturation (°C)               | °C              | TSAT  |
| 35  | Power RHR removal rate (MW)             | MW              | QRHR  |
| 36  | Level Core water (M)                    | M               | LVCR  |
| 37  | Temp Loop A subcooling margin (°C)      | °C              | SCMA  |
| 38  | Temp Loop B subcooling margin (°C)      | °C              | SCMB  |
| 39  | Fraction Clad failure (%)               | %               | FRCL  |
| 40  | Press Reactor building (bar)            | bar             | PRB   |
| 41  | Press Partial RB air (bar)              | bar             | PRBA  |
| 42  | Temp Reactor building (°C)              | °C              | TRB   |
| 43  | Level RB sump water (M)                 | M               | LWRB  |
| 44  | Ratio Departure from nuclear boiling    | -               | DNBR  |
| 45  | Power Fan cooler heat removal (MW)      | MW              | QFCL  |
| 46  | Flow Total break entering RB (t/hr)     | t/hr            | WBK   |
| 47  | Flow Pressurizer spray (t/hr)           | t/hr            | WSPY  |
| 48  | Flow Containment spray (t/hr)           | t/hr            | WCSP  |
| 49  | Power Pressurizer heater (KW)           | KW              | HTR   |
| 50  | Mass H2 generated by Zr-H2O (kg)        | kg              | MH2   |
| 51  | Concentration RB hydrogen (%)           | %               | CNH2  |
| 52  | Reactivity Soluble boron (%dk/k)        | %dk/k           | RHBR  |
| 53  | Reactivity Mod temp (%dk/k)             | %dk/k           | RHMT  |
| 54  | Reactivity Fuel (Doppler) (%dk/k)       | %dk/k           | RHFL  |
| 55  | Reactivity Rod (%dk/k)                  | %dk/k           | RHRD  |
| 56  | Reactivity Total (%dk/k)                | %dk/k           | RH    |
| 57  | Power Nuclear Flux (%)                  | %               | PWNT  |
| 58  | Power Core thermal (%)                  | %               | PWR   |
| 59  | Temp Submerged fuel avg (°C)            | °C              | TFSB  |
| 60  | Temp Peak fuel (°C)                     | °C              | TFPK  |
| 61  | Temp Average fuel (°C)                  | °C              | TF    |
| 62  | Temp Peak clad (°C)                     | °C              | TPCT  |
| 63  | Flow Accumulator (t/hr)                 | t/hr            | WCFT  |
| 64  | Flow LPSI (RHR) (t/hr)                  | t/hr            | WLPI  |
| 65  | Flow Charging (t/hr)                    | t/hr            | WCHG  |
| 66  | Rad Monitor RB air (CPM)                | CPM             | RM1   |
| 67  | Rad Monitor Steam Line (CPM)            | CPM             | RM2   |
| 68  | Rad Monitor Condenser Off-gas (CPM)     | CPM             | RM3   |
| 69  | Rad Monitor Aux Building Air (CPM)      | CPM             | RM4   |
| 70  | Activity RC Coolant (CPM)               | CPM             | RC87  |
| 71  | Concentration RC I-131 Eq (GBq/cc)      | GBq/cc          | RC131 |
| 72  | Rad Rel Rate RB (GBq/s)                 | GBq/s           | STRB  |
| 73  | Rad Rel Rate SG Valves (GBq/s)          | GBq/s           | STSG  |
| 74  | Rad Rel Rate Cdsr Off-gas (GBq/s)       | GBq/s           | STTB  |
| 75  | Mass Total Leakage out of RB (kg)       | Kg              | RBLK  |
| 76  | Mass Total Leakage out of SGs (kg)      | Kg              | SGLK  |
| 77  | Dose Rate EAB Thyroid (mSv/hr)          | mSv/hr          | DTHY  |
| 78  | Dose Rate EAB Whole Body (mSv/hr)       | mSv/hr          | DWB   |
| 79  | Press RCS (bar)                         | bar             | P     |
| 80  | Flow SG A MSV/ADV (t/h)                 | t/hr            | WRLA  |
| 81  | Flow SG B MSV/ADV (t/h)                 | t/hr            | WRLB  |
| 82  | Flow Letdown (t/hr)                     | t/hr            | WLD   |
| 83  | Integrated Break Flow (kg)              | Kg              | MBK   |
| 84  | Integrated Break Energy (MJ)            | MJ              | EBK   |
| 85  | Volume RWST Water (M3)                  | M3              | TKLV  |
| 86  | Fraction Zr Oxidation )%)               | %               | FRZR  |
| 87  | Mass of Corium in DW (Kg)               | Kg              | MDBR  |
| 88  | Mass of molten concrete (Kg)            | Kg              | MCRT  |
| 89  | Mass of CCI gases (Kg)                  | Kg              | MGAS  |
| 90  | Temp of Debris in Cavity (°C)           | °C              | TDBR  |
| 91  | Temp of Debris in Lower Plenum (°C)     | °C              | TSLP  |
| 92  | Temp of Molten Concrete (°C)            | °C              | TCRT  |
| 93  | Concentration RCS Boron (ppm)           | ppm             | PPM   |
| 94  | Ratio Loop A Flow                       | -               | RRCA  |
| 95  | Ratio Loop B Flow                       | -               | RRCB  |
| 96  | Ratio Core Flow                         | -               | RRCO  |
| 97  | Flow FW Line Break (kg/s)               | kg/s            | WFLB  |

### Dataset structure
<img src="https://github.com/thu-inet/NuclearPowerPlantAccidentData/blob/main/Figures/fig2.png" width="475">
<img src="https://github.com/thu-inet/NuclearPowerPlantAccidentData/blob/main/Figures/fig4.png" width="275">
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
```

## Maintainers

- [Ben Qi](https://github.com/Ben-learner)
- [Xingyu Xiao](https://github.com/Crystalxy123)
- [Jingang Liang](https://github.com/liangjg)
- [THU-INET](https://github.com/thu-inet)

## Contributing
We appreciate all contributions. Please let us know if you encounter a bug by filing an issue.

## License
NPPAD has a MIT license, as found in the [LICENSE](https://github.com/qiben-jy/NuclearPowerPlantAccidentData/blob/ab8c9dc45e594b793097ca9582e959ee7935eeb5/LICENSE) file.

## Citing
Citing NPPAD in your research:
```
Qi, B., Xiao, X., Liang, J. et al. An open time-series simulated dataset covering various accidents 
for nuclear power plants.Sci Data 9, 766 (2022). https://doi.org/10.1038/s41597-022-01879-1
```
## Related work
[Qi B, Xiao X, Liang J, et al. An open time-series simulated dataset covering various accidents for nuclear power plants[J]. Scientific data, 2022, 9(1): 766.](https://doi.org/10.1038/s41597-022-01879-1)

[Xiao, X.; Qi, B.; Liang, J.; Tong, J.; Deng, Q.; Chen, P. Enhancing LOCA Breach Size Diagnosis with Fundamental Deep Learning Models and Optimized Dataset Construction. Energies 2024, 17, 159.](https://doi.org/10.3390/en17010159)

[Qi B, Liang J, Tong J. Fault diagnosis techniques for nuclear power plants: a review from the artificial intelligence perspective[J]. Energies, 2023, 16(4): 1850.](https://doi.org/10.3390/en16041850)

[Qi B, Zhang L, Liang J, et al. Combinatorial techniques for fault diagnosis in nuclear power plants based on Bayesian neural network and simplified Bayesian network-artificial neural network[J]. Frontiers in Energy Research, 2022, 10: 920194.](https://doi.org/10.3389/fenrg.2022.920194)

[Qi B, Sun J, Sui Z, et al. Multimodal learning using large language models to improve transient identification of nuclear power plants[J]. Progress in Nuclear Energy, 2024, 177: 105421.](https://doi.org/10.1016/j.pnucene.2024.105421)

[Qi B, Wang Y, Xiao X, et al. Underlying Deep Learning Networks Diagnosis Evaluation and Generative Adversarial Network Data Augmentation Based on a Benchmark Accident Dataset[C]//International Conference on Nuclear Engineering. American Society of Mechanical Engineers, 2024, 88254: V005T05A019.](https://doi.org/10.1115/ICONE31-134996)

[Xiao X, Liu S, Zuo Z, et al. A Text Intelligence-Based Approach for Automatic Generation of Fault Trees in Nuclear Power Plants[C]//International Conference on Nuclear Engineering. American Society of Mechanical Engineers, 2024, 88308: V010T12A004.](https://doi.org/10.1115/ICONE31-134226)