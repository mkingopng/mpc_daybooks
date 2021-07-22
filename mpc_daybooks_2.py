"""
objective: automate the processing & analysis of MPC daybooks.

background: each day when finance does a daily update, accounting transactions for production, AR, stock, and AP are
posted from the module to the general ledger. When this happens, a summary of all the transactions captured by the
module and transfered to GL in that update. These files are *.txt files called daybooks.

MPC daybooks are the manufacturing accounting transactions. These need to be processed and analysed to identify variance
outliers and investigate. The current process is highly manual and can/should be automated.

Objective: The objective of this project is to automate this process in stages

process:
    - iterate through all *.txt files in a directory
        - open & read the file to df
        - loop through the rows in the df.
            - remove the headers, rows 114 - 119, +115
            - OR remove all rows which have a non-numeric value in column 'ACC' index[2]
        - remove the mid & summary sections
        - append the clean data to a clean df
    - export clean data to csv or xlsx
    - automate the analysis. Probably need to use plotly scatter chart. Need hovertext.
        pivot
        scatterplot with hovertext to pick outliers (work orders with variances)

"""
import pandas as pd
import numpy as np
import os
import xlsxwriter

# specify the directory
directory_in_str = '/home/michaelkingston/Documents/GitHub/mpc_daybooks/07_JUL_2020/'
# directory = os.fsencode(directory_in_str)
list2 = []
error_message = ' is throwing an error'

# file = 'WIP_JNL_MPC_TRN_562310_020720.txt'


def read_mpc_files():
    mpc_df = pd.read_fwf(filename, colspecs=[(0, 9), (10, 18), (19, 25), (26, 28), (33, 40), (56, 67), (68, 92),
                                         (93, 100), (101, 111)],
                         names=['TRANS-', 'TRANSDAT', 'ACC', 'CC', 'PRD', 'AMOUNT', 'TEXT', 'WORK.C', 'WO-NO'],
                         # generally sticking to string so i can use isnumeric() or notnumeric()
                         dtype={'TRANS-': str, 'TRANSDAT': object, 'ACC': str, 'CC': str, 'PRD': str,
                                'AMOUNT': str, 'TEXT': str, 'WORK.C': str, 'WO-NO': str},
                         # remove unneeded data from header of first page
                         header=4, skiprows=1)

    # for debugging
    # print(mpc_df.head(119))
    # print(list(mpc_df.columns))
    return mpc_df


def clean_mpc_data(mpc_df):
    accounts_list = ['001049', '001021', '100112', '350000', '400001', '400916',
                     '400100', '400902', '400903', '400910', '400911', '400912']

    # remove all the rows with NaN in 'ACC'
    cleaner_mpc_df1 = mpc_df[mpc_df['ACC'].notna()]

    # check to see if the value in each row for column 'ACC' is in the accounts list
    clean_mpc_df = cleaner_mpc_df1[cleaner_mpc_df1['ACC'].isin(accounts_list)]
    print(clean_mpc_df)
    return clean_mpc_df


def append_df():
    july_df = pd.DataFrame()
    july_df.append(clean_mpc_df)
    # print(july_df)
    return july_df


def export_df_to_xlsx():
    # export the cleaned data to .csv or .xlsx
    clean_mpc_df.to_excel(r'clean_mpc_data.xlsx', index=False)


if __name__ == '__main__':

    july_df = pd.DataFrame()
    for filename in os.listdir(directory_in_str):
        with open(directory_in_str + filename) as infile:
            try:
                print(filename)
                next(infile)
                # mpc_df = read_mpc_files()
                # clean_mpc_df = clean_mpc_data(mpc_df)
                # july_df.append(clean_mpc_df)
            except:
                print(f"{filename} is throwing an error")
    print('DONE!!!')
    print(july_df.head())

    # this works without the loop
    # mpc_df = read_mpc_files()
    # clean_mpc_df = clean_mpc_data(mpc_df)
    # july_df = append_df()
    # export_df_to_xlsx()

