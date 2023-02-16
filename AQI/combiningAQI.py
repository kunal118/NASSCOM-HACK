import pandas as pd

import os
# assign directory

def merge_files(data):
    
    # data = data.drop(data.columns[[0]],axis =1)
    # print(data)

    #Create a filter for all rows with sub headings etc non-useful rows
    filter = data.isnull().sum(axis = 1) <5
    data['filter'] = filter

    # data = data.drop(data.columns[[0]],axis =1) 
   
   #remove blank columns
    for column in data.columns:
        if(data[column].isna().all()):
            data = data.drop(column,axis = 1)
                
    # data.drop(data.iloc)

    #Applpting the filter
    data = data[data['filter'] == True]
    data = data.drop('filter',axis = 1)
    
    #Setting the first row as column headings and deleting first row
    data.columns = data.iloc[0]
    data =data.drop(data.index[0],axis = 0)
    # print(data.head())
    return data
    
   
    
   
# merge_files(pd.read_csv(r'Z:\NASSCOM\AQI\MonthlyAQI2022.csv'))

directory = r'Z:\NASSCOM\AQI'
 
# # iterate over files in
# # that directory
final_df = pd.DataFrame()
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    
    # checking if it is a csv file
    
    if os.path.isfile(f) and f.endswith('.csv'):
        print(f)
        print("")
        data = pd.read_csv(f)
        data = merge_files(data)
        # print(data.head())
        if(final_df.shape == (0,0)):
            final_df = data
        else:
            final_df = final_df.merge(data, how='outer')
        # print(final_df.head())
        # print("..................................")
        # print("................................................................")

        
print(final_df.head())
final_df.to_csv('finalAQI.csv',index=False)
        











# print(data[data[data.columns[0]] == 1])

