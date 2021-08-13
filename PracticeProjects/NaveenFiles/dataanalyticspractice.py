import pandas as pd
import numpy as np
'''import seaborn as sns
import matplotlib.pyplot as plt
% matplotlip inline
sns.set(color_codes=True)'''

table = pd.read_csv('~/Documents/Test_Salary_Table.csv')
print(table.head)
print(table.dtypes)
print(table.columns)
