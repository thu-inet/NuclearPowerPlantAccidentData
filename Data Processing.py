# data_path = r".\\DATA"
# for accident in os.listdir(data_path):
#     accident_path = data_path + '\\' + accident
#     print(accident_path)
#     for name in os.listdir(accident_path):
#         if re.match(r'\d+'+'.mdb', name): #operation data
#             print('Operation data:', name)
#         elif re.match(r'\d+' + 'dose' + '.mdb', name):  # Dose data
#             print('dose data:', name)
# mdb_file = r'.\\DATA\LOCA\1.mdb'
# driver = '{Microsoft Access Driver (*.mdb, *.accdb)}'
# cnxn = pyodbc.connect(f'Driver={driver};DBQ={mdb_file}')
# crsr = cnxn.cursor()
# for table_info in crsr.tables(tableType='TABLE'):
#     print(table_info)
# data_table = pd.read_sql('SELECT * FROM PlotData',cnxn)
# data_table.sort_values(by=['TIME'], ascending=True, inplace=True) #Some mdbs have problems with not being in time order
# print(data_table)
# target_path = r'.\\CSV_DATA\LOCA'
# if (os.path.exists(target_path) == False):
#     os.makedirs(target_path)
#     print(os.getcwd())
# os.chdir(target_path)
# data_table.to_csv('1.csv', header=True, index=False)
# # variables = ['TIME','TFPK','TFSB','TPCT']
# variables = ['TIME','HLW']
# plot_df = data_table[variables]
# plot_df.set_index(plot_df.columns[0],inplace=True)
# # plot_df.sort_values(by=['TIME'], ascending=True, inplace=True)
# print(plot_df)
# fig_plot = plot_df.plot()
# plt.xlabel('Time(sec)')
# # plt.ylabel('Temperature(℃)')
# # plt.ylabel('Pressure(bar)')
# # plt.ylabel('Flow(t/hr)')
# plt.ylabel('RCS leak (kJ/kg)')

# plt.ylabel('Fraction Clad failure(%)')
# plt.ylabel('Water level (M)')

# plt.show()
# fig_name = ''
# for var in range(1,len(variables)):
#     fig_name = fig_name  + variables[var] + '-'
# print(fig_name)
# fig_save = fig_plot.get_figure()
# fig_save.savefig(f'.\\Data_figture\\{fig_name}')

class Pre_processing:
    def __init__(self, data_path, operation_data_csv_path, dose_data_csv_path):
        self.data_path = data_path
        self.operation_data_cav_path = operation_data_csv_path
        self.dose_data_cav_path = dose_data_csv_path
    def mdbtocsv(self):
        driver = '{Microsoft Access Driver (*.mdb, *.accdb)}'
        if (os.path.exists(self.operation_data_cav_path) == False):
            os.makedirs(self.operation_data_cav_path)
        if (os.path.exists(self.dose_data_cav_path) == False):
            os.makedirs(self.dose_data_cav_path)
        for accident in os.listdir(self.data_path):
            accident_path = self.data_path + '\\'+ accident
            for name in os.listdir(accident_path):
                mdb_file = accident_path + '\\' + name
                print(mdb_file)
                cnxn = pyodbc.connect(f'Driver={driver};DBQ={rdb_file}')
                # crsr = cnxn.cursor()
                if re.match(r'\d+' + '.mdb', name): #Operation data
                    data_table = pd.read_sql('SELECT * FROM PlotData', cnxn)
                    data_table.sort_values(by=['TIME'], ascending=True,
                                           inplace=True)  # Some mdbs have problems with not being in time order
                    os.chdir(self.operation_data_cav_path)
                    csv_name = name.replace('mdb','csv')
                    data_table.to_csv(csv_name, header=True, index=False)
                elif re.match(r'\d+' + 'dose' + '.mdb', name): #Dose data
                    data_table = pd.read_sql('SELECT * FROM ListDS', cnxn)
                    data_table.sort_values(by=['TIME'], ascending=True,
                                           inplace=True)  # Some mdbs have problems with not being in time order
                    os.chdir(self.dose_data_cav_path)
                    csv_name = name.replace('mdb', 'csv')
                    data_table.to_csv(csv_name, header=True, index=False)

    def generate_dataset(self):
        pass

    def show_parametes(self):
        pass
if __name__ == "__main__":
    import pandas as pd
    import pyodbc, os, re
    import matplotlib.pyplot as plt
    pre_data = Pre_processing(r".\\DATA", r".\\DATA\Operation_csv_data",r".\\DATA\Dose_csv_data")
    pre_data.mdbtocsv()