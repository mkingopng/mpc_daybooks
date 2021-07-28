"""
objective: automate the processing & analysis of MPC daybooks.

background: each day when finance does a daily update, accounting transactions for production, AR, stock, and AP are
posted from the module to the general ledger. When this happens, a summary of all the transactions captured by the
module and transferred to GL in that update. These files are *.txt files called daybooks.

MPC daybooks are the manufacturing accounting transactions. These need to be processed and analysed to identify variance
outliers and investigate. The current process is highly manual and can/should be automated.

Objective: The objective of this project is to automate this process in stages

process:
    - iterate through all *.txt files in a directory
    - save the consolidated data to result.txt
    - open & read result.txt to df using the fwf method
    - loop through the rows in the df & remove all rows which have a value not in the list in column 'ACC'
    - export clean data to csv or xlsx
    (complete to this point)

# TODO: #3 some product codes get turned into dates when exporting to CSV. again, i deliberately coerced this to str on
    line 102 to avoid this. not sure why its happening

# TODO: #4 remove the row indexes

# TODO: #5 cast date to date data type

# TODO: automate the analysis.
    - pivot
    - need to use plotly scatter chart. Need hovertext (matplotlib doesn't have overtext does it?).
    - scatterplot with hovertext to pick outliers (work orders with variance type & value)'
    - export to excel. cleaned data to sheet 'data', pivoted data to 'pivot', plot to 'plot'
"""
import pandas as pd
import glob
import re


full_month_file = open('result.txt')
# final_file = open('final_file.txt')
# clean_text = open('clean_text')
directory = '/home/michaelkingston/Documents/GitHub/mpc_daybooks/*.txt'


def read_mpc_txt_files():
    """
    reads all txt files in a folder and returns a single text file
    :return: a single text file consolidating all the information from the txt files in the directory
    """
    read_files = glob.glob(directory)
    with open('result.txt', 'wb') as outfile:
        for f in read_files:
            with open(f, 'rb') as file:
                outfile.write(file.read())
    return outfile


def create_df(full_month_file):
    """
    This function imports the consolidated data from the text file to pd.DataFrame. Have to use the fwf method because the delimiters
    are inconsistent. most of the data types are coerced to string type for to allow us to use the pd.Series methods to
    find incorrectly formatted numbers (eg: 100.00-) and mutating them into acceptable format (eg -100.00).

    need to consider whether there are more appropriate data types for columns excluding 'ACCOUNT'.
    :param full_month_file:
    :return: dataframe
    """
    # read the text file to data frame using fwf method
    mpc_df = pd.read_fwf(full_month_file, colspecs=[(0, 9), (10, 18), (19, 25), (26, 28), (33, 40), (56, 67), (68, 92),
                                         (93, 100), (101, 111)],
                         # specify the column headers
                         names=['TRANS-', 'TRANSDAT', 'ACC', 'CC', 'PRD', 'AMOUNT', 'TEXT', 'WORK.C', 'WO-NO'],
                         # specify the data types
                         dtype={'TRANS-': str, 'TRANSDAT': object, 'ACC': str, 'CC': str, 'PRD': str,
                                'AMOUNT': str, 'TEXT': str, 'WORK.C': str, 'WO-NO': str},
                         # remove unneeded data from header of first page
                         header=4, skiprows=1)
    return mpc_df


def clean_mpc_data(mpc_df):
    """

    :param mpc_df: takes the 'dirty' mpc_df and cleans it
    :return: a dataframe free of unwanted data
    """
    # list of all the values in column 'ACC' that i want to keep
    accounts_list = ['001049', '001021', '100112', '350000', '400001', '400916',
                     '400100', '400902', '400903', '400910', '400911', '400912']
    # remove all the rows with NaN in 'ACC'
    cleaner_mpc_df = mpc_df[mpc_df['ACC'].notna()]
    # check to see if the value in each row for column 'ACC' is in the accounts list
    clean_mpc_df = cleaner_mpc_df[cleaner_mpc_df['ACC'].isin(accounts_list)]
    return clean_mpc_df


def fix_negatives(clean_mpc_df):
    """
    the negative values in the amount column are incorrectly formatted. Need to move the negative symbol from the end
    off the string to the front and cast to float
    :param clean_mpc_df:
    :return final_mpc_df:
    """
    pattern = r'\d+.{0,1}\d*-$'
    mask = clean_mpc_df['AMOUNT'].str.contains(pattern, regex=True)
    clean_mpc_df.loc[mask, 'AMOUNT'] = -clean_mpc_df.loc[mask]['AMOUNT'].str.replace('-', '').astype(float)
    final_mpc_df['AMOUNT'] = clean_mpc_df['AMOUNT'].astype(float)
    return final_mpc_df


if __name__ == '__main__':
    outfile = read_mpc_txt_files()
    mpc_df = create_df(full_month_file)
    clean_mpc_df = clean_mpc_data(mpc_df)
    final_mpc_df = fix_negatives(clean_mpc_df)
    final_mpc_df.to_csv(r'final.csv')
