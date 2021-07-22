# if not mpc_df[mpc_df['ACC'].apply(lambda x: type(x) in [int, np.int64, float, np.float64])]:
#     mpc_df.drop()
# else:
#     pass


# clean_mpc_df = (mpc_df.drop('ACC', axis=1).mpc_df['ACC'].apply(pd.to_numeric, errors='coerce'))
# clean_mpc_df = mpc_df[mpc_df.ACC.apply(lambda x: x.isdigit())].set_index('ACC')

# would a for loop work?
# for row in mpc_df:
#     if row in row_index_list:
#         mpc_df.drop()
#         row += 115

# clean_mpc_df = mpc_df.ACC.drop(mpc_df.ACC.isin(accounts_list))

# take all the notna() values to a new df to eliminate NaN's from column 'ACC'
# cleaner_mpc_df1 = mpc_df[mpc_df['ACC'].notna()]
# print(cleaner_mpc_df1)

# cleaner_mpc_df2 = cleaner_mpc_df1[cleaner_mpc_df1[['ACC']].applymap(np.isreal).all()]

# print(clean_mpc_df)

# Eliminate invalid data from df

# clean_mpc_df = cleaner_mpc_df1[~cleaner_mpc_df1['ACC'].isin(accounts_list)]
    # clean_mpc_df = cleaner_mpc_df1[~cleaner_mpc_df1.datecolumn.isin(accounts_list)]
    # (cleaner_mpc_df1[cleaner_mpc_df1['ACC'].str.isnumeric()])

    # clean_mpc_df = cleaner_mpc_df1[~cleaner_mpc_df1['ACC'].isin(accounts_list).any()]

    # mask = cleaner_mpc_df1.pipe(lambda x: (x['ACC'].isin(accounts_list)) | (x['ACC'].isna()), )
    # clean_mpc_df = cleaner_mpc_df1.drop(cleaner_mpc_df1[mask].index)