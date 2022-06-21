import pandas as pd
import pyodbc,os
import matplotlib.pyplot as plt
mdb_file = r'.\\DATA\LOCA\50.mdb'
driver = '{Microsoft Access Driver (*.mdb, *.accdb)}'
cnxn = pyodbc.connect(f'Driver={driver};DBQ={mdb_file}')
crsr = cnxn.cursor()
# for table_info in crsr.tables(tableType='TABLE'):
#     print(table_info)
data_table = pd.read_sql('SELECT * FROM PlotData',cnxn)
# variables = ['TIME','TFPK','TFSB','TPCT']
variables = ['TIME','HLW']
plot_df = data_table[variables]
plot_df.set_index(plot_df.columns[0],inplace=True)
fig_plot = plot_df.plot()
plt.xlabel('Time(sec)')
# plt.ylabel('Temperature(℃)')
# plt.ylabel('Pressure(bar)')
# plt.ylabel('Flow(t/hr)')
plt.ylabel('RCS leak (kJ/kg)')

# plt.ylabel('Fraction Clad failure(%)')
# plt.ylabel('Water level (M)')
plt.show()
fig_name = ''
for var in range(1,len(variables)):
    fig_name = fig_name  + variables[var] + '-'
print(fig_name)
fig_save = fig_plot.get_figure()
fig_save.savefig(f'.\\Data_figture\\{fig_name}')
