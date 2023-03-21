import pandas as pd

# Load the first CSV file into a pandas DataFrame
path_file = 'data3\main_0.csv'
df1 = pd.read_csv(path_file, index_col=0)
merged_df = df1

for i in range(0,10):

    # df_new = pd.read_csv(f'data2\df{i}.csv')
    df_new = pd.read_csv(f'data3\main_{i}.csv', index_col=0)
    
    # if set(['album', 'writer(s)']).issubset(df_new.columns):
    #     df_new  = df_new .drop(['album', 'writer(s)'], axis=1)
    merged_df = pd.concat([df1, df_new], axis=0, ignore_index=True)
    # merged_df = merged_df.dropna(axis=0)
    df1 = merged_df
    # Write the merged DataFrame to a new CSV file
# merged_df.to_csv("data3\merged_df.csv", index=False)
merged_df.to_csv("data3\main_df.csv", index= False)
