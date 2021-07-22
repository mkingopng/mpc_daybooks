import pandas as pd
import numpy as np
import os
import xlsxwriter

# specify the directory
directory_in_str = '/Users/michaelkingston/PycharmProjects/principles_of_programming-main/data/07_JUL_2020'

directory = os.fsencode(directory_in_str)


def clean_mpc_files(mpc_july20_df=pd.DataFrame()):
    # for file in os.listdir(directory):
    #     filename = os.fsdecode(file)
    #     if filename.endswith('*.txt'):
    #         clean_mpc_files()
    #         print(mpc_july20_df)
    mpc_df = pd.read_fwf(filename, colspecs=[(0, 9),
                                             (10, 18),
                                             (19, 25),
                                             (26, 28),
                                             (33, 40),
                                             (56, 67),
                                             (68, 92),
                                             (93, 100),
                                             (101, 111)],
                         names=['TRANS-',
                                'TRANSDAT',
                                'ACC',
                                'CC',
                                'PRD',
                                'AMOUNT',
                                'TEXT',
                                'WORK.C',
                                'WO-NO'],
                         dtype={'TRANS-': object,
                                'TRANSDAT': object,
                                'ACC': object,
                                'CC': object,
                                'PRD': object,
                                'AMOUNT': object,
                                'TEXT': object,
                                'WORK.C': object,
                                'WO-NO': object},
                         header=4, skiprows=1)

    # modify the dataframe with ACC as index
    data_with_index = mpc_df.set_index("ACC")

    # drop redundant rows
    data_with_index = data_with_index.drop(['------',
                                            'ONS',
                                            'D',
                                            'Z',
                                            'L',
                                            'N',
                                            'T',
                                            'PRJ',
                                            'ACC',
                                            '20===',
                                            '======',
                                            'TRAN',
                                            '0004',
                                            'IANCES',
                                            'S U',
                                            'T O',
                                            'OVERY',
                                            'LIER I',
                                            'I.P.',
                                            '- - -',
                                            'CLOSED'])

    # drop any null values
    clean_mpc_df = data_with_index[data_with_index.index.notnull()]
    # print(clean_mpc_df)

    # append to the full month dataframe
    mpc_july20_df = mpc_july20_df.append(clean_mpc_df)
    print(mpc_july20_df)


if __name__ == '__main__':
    filename = 'MPC_010620.txt'
    clean_mpc_files()



    # print(mpc_july20_df.head())