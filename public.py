import pandas as pd
import glob

full_month_file = open('result.txt')
directory = '../data/*.txt'


def read_mpc_txt_files():
    read_files = glob.glob(directory)
    with open('result.txt', 'wb') as outfile:
        for f in read_files:
            with open(f, 'rb') as file:
                outfile.write(file.read())
    return outfile


def create_df(full_month_file):
    mpc_df = pd.read_fwf(full_month_file, colspecs=[(0, 9), (10, 18), (19, 25), (26, 28), (33, 40), (56, 67), (68, 92),
                                                    (93, 100), (101, 111)],
                         names=['TRANS-', 'TRANSDAT', 'ACC', 'CC', 'PRD', 'AMOUNT', 'TEXT', 'WORK.C', 'WO-NO'],
                         dtype={'TRANS-': str, 'TRANSDAT': object, 'ACC': str, 'CC': str, 'PRD': str,
                                'AMOUNT': str, 'TEXT': str, 'WORK.C': str, 'WO-NO': str},
                         header=4, skiprows=1)
    return mpc_df


def clean_mpc_data(mpc_df):
    accounts_list = ['001049', '001021', '100112', '350000', '400001', '400916',
                     '400100', '400902', '400903', '400910', '400911', '400912']
    cleaner_mpc_df = mpc_df[mpc_df['ACC'].notna()]
    clean_mpc_df = cleaner_mpc_df[cleaner_mpc_df['ACC'].isin(accounts_list)]
    return clean_mpc_df


def fix_negatives(clean_mpc_df):
    pattern = r'\d+.{0,1}\d*-$'
    mask = clean_mpc_df['AMOUNT'].str.contains(pattern, regex=True)
    clean_mpc_df.loc[mask, 'AMOUNT'] = -clean_mpc_df.loc[mask]['AMOUNT'].str.replace('-', '').astype(float)
    clean_mpc_df['AMOUNT'] = clean_mpc_df['AMOUNT'].astype(float)
    return clean_mpc_df


if __name__ == '__main__':
    outfile = read_mpc_txt_files()
    mpc_df = create_df(full_month_file)
    clean_mpc_df = clean_mpc_data(mpc_df)
    final_mpc_df = fix_negatives(clean_mpc_df)
    final_mpc_df.to_excel(r'dec20.xlsx', sheet_name='data_base', index=False)
