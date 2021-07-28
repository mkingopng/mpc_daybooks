import re

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

# cleaner_mpc_df2 = cleaner_mpc_df1[cleaner_mpc_df1[['ACC']].applymap(np.isreal).all()]

# clean_mpc_df = cleaner_mpc_df1[~cleaner_mpc_df1['ACC'].isin(accounts_list)]
# clean_mpc_df = cleaner_mpc_df1[~cleaner_mpc_df1.datecolumn.isin(accounts_list)]
# (cleaner_mpc_df1[cleaner_mpc_df1['ACC'].str.isnumeric()])

# mask = cleaner_mpc_df1.pipe(lambda x: (x['ACC'].isin(accounts_list)) | (x['ACC'].isna()), )
# clean_mpc_df = cleaner_mpc_df1.drop(cleaner_mpc_df1[mask].index)
#
# with open('result.txt', "r") as f:
#     lines = f.read()
# print(type(lines))

# list = []
# for word in lines:
#     re.findall(r"^\d-", lines)
#     list.append()
#
# re.sub()
#
# regex = re.compile('([a-zA-Z]\"[a-zA-Z])', re.S)
# myfile = 'foo"s bar'
# myfile2 = regex.sub(lambda m: m.group().replace('"', "%", 1), myfile)
# print(myfile2)
my_list = ['100.00-', '200.00-', '300.00-']
my_string = 'it cost 100.00- to fly from 200.00- to 300.00- and back'


def find(my_string):
    new_string = ''
    word = re.compile(r"\d-\s")
    for word in my_string.split():
        word.findall(word, my_string)
        new_word = word[-1:] + word[:-1]
        print(new_word)
    return new_string


if __name__ == '__main__':
    find(my_string)
    # print(new_string)


# my_string = '100.00-'
# my_new_string = my_string[-1:] + my_string[:-1]
# print(my_new_string)

pattern = re.compile("/([0-9]-)/g")

for i, line in enumerate(open('/home/michaelkingston/Documents/GitHub/mpc_daybooks/result.txt')):
    for match in re.finditer(pattern, line):
        print('Found on line %s: %s' % (i+1, match.group()))
