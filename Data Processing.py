import pandas as pd
import pyodbc, os, re
import matplotlib.pyplot as plt
import torch
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from itertools import chain

class Pre_processing:
    def __init__(self, data_path, operation_data_csv_path, dose_data_csv_path, project_path):
        self.data_path = data_path
        self.operation_data_csv_path = operation_data_csv_path
        self.dose_data_csv_path = dose_data_csv_path
        self.project_path = project_path
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

if __name__ == "__main__":

    pre_data = Pre_processing(r".\\DATA1", r".\\Operation_csv_data",r".\\Dose_csv_data",os.getcwd())
    pre_data.mdbtocsv()
    # pre_data.show_parametes(['TIME','P'], r".\\Operation_csv_data\LOCA\1.csv", r".\\Data_figture\LOCA\1")

    #test
    # test_path = r'E:\software\PythonProject\pythonProject\NuclearPowerPlantAccidentData\Operation_csv_data\ATWS\1.csv'
    # test_data = pd.read_csv(test_path)
    # test_data1 = test_data.iloc[:150,1:].values
    # test_data2 = list(chain.from_iterable(test_data1))
    # print(len(test_data2))



