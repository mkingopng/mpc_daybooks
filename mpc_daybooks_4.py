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
    - export clean data to csv or xlsx (complete to this point)

    - move the '-' symbol to the front of the string in column 'AMOUNT'

    - automate the analysis. Probably need to use plotly scatter chart. Need hovertext.
        pivot
        scatterplot with hovertext to pick outliers (work orders with variances)

"""
import pandas as pd
import glob

file = 'result.txt'


def read_mpc_txt_files():
    read_files = glob.glob('/home/michaelkingston/Documents/GitHub/mpc_daybooks/07_JUL_2020/*.txt')
    with open('result.txt', 'wb') as outfile:
        for f in read_files:
            with open(f, 'rb') as infile:
                outfile.write(infile.read())
    return outfile


def create_df(file):
    mpc_df = pd.read_fwf(file, colspecs=[(0, 9), (10, 18), (19, 25), (26, 28), (33, 40), (56, 67), (68, 92),
                                         (93, 100), (101, 111)],
                         names=['TRANS-', 'TRANSDAT', 'ACC', 'CC', 'PRD', 'AMOUNT', 'TEXT', 'WORK.C', 'WO-NO'],
                         dtype={'TRANS-': str, 'TRANSDAT': object, 'ACC': str, 'CC': str, 'PRD': str,
                                'AMOUNT': str, 'TEXT': str, 'WORK.C': str, 'WO-NO': str},
                         # remove unneeded data from header of first page
                         header=4, skiprows=1)
    return mpc_df


def clean_mpc_data(mpc_df):
    # list of all the values in column 'ACC' that i want to keep
    accounts_list = ['001049', '001021', '100112', '350000', '400001', '400916',
                     '400100', '400902', '400903', '400910', '400911', '400912']
    # remove all the rows with NaN in 'ACC'
    cleaner_mpc_df1 = mpc_df[mpc_df['ACC'].notna()]
    # check to see if the value in each row for column 'ACC' is in the accounts list
    clean_mpc_df = cleaner_mpc_df1[cleaner_mpc_df1['ACC'].isin(accounts_list)]
    for row in clean_mpc_df['ACC']:
        if (clean_mpc_df.loc[clean_mpc_df['AMOUNT'].str.endswith('-'):
            new_string = string([-1] + x[:-1])  # this is the problem
            continue
    return clean_mpc_df


if __name__ == '__main__':
    outfile = read_mpc_txt_files()
    mpc_df = create_df(file)
    clean_mpc_df = clean_mpc_data(mpc_df)
    clean_mpc_df.to_csv(r'july_mpc.csv')