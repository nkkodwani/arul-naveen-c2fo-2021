##########
#LEARNING PANDAS
##########

import pandas as pd
import numpy as np


# df = pd.read_csv('~/Desktop/developer_survey_2019/survey_results_public.csv', index_col='Respondent')
# schema_df = pd.read_csv('~/Desktop/developer_survey_2019/survey_results_schema.csv', index_col = 'Column')

# schema_df.sort_index(inplace=True) #inplace means that the sort will stay w/ the df
# print(schema_df)





people = {
    'first' : ['Arul', 'Naveen', 'Andreanna'],
    'last' : ['Sethi', 'Kodwani', 'Edwards'], 
    'email' : ['ArulSethi02@gmail.com', 'NKKodwani@gmail.com', 'Andreanna.Ale909@gmail.com']
}
df = pd.DataFrame(people)
#a series is a lsit of data with more funcitonality than a list. Like a row of data
#print(df[['last', 'email']]) #two columns != a series
#print(df.columns)
#print(df.iloc[[0,1]]) #integer location; returns a series of the first row of data
#print(df.iloc[[0,1], 2]) #gets the email addresses of first two rows
#print(df.loc[[0,1], ['email', 'first']]) #gets email addresses and last name of first two rows; search by label instead of int
print(df.index)
df.rename(columns={'first':'first_name', 'last':'last_name'}, inplace = True)
df.loc[2, ['email']] = 'andreanna.edwards@ku.edu' #can also use df.at[]
df['email'] = df['email'].str.lower()
print(df)


