import pandas as pd
from probability import do_mle, test_design
from sklearn.model_selection import train_test_split


# Read csv and filter out rows with '?'
def read_csv(name):
    unique = {}
    data = pd.read_csv(name, skipinitialspace=True)
    df = pd.DataFrame(data)

    for column in df:
        df = df[df[column] != '?']
        unique[column] = df[column].unique()

    temp_df = df.copy(deep=True)
    # Split data into two different datasets
    train, test = train_test_split(df, test_size=0.3)

    prob_above50, prob_below50 = do_mle(train)

    for (k, v), (k2, v2) in zip(prob_above50.items(), prob_below50.items()):
        print("{:<27} {:<22} || {:<22}".format(k, '>50k', '<=50k'))
        print('=' * 76)
        for (k11, v11), (k22, v22) in zip(v.items(), v2.items()):
            # print(k11, v11, k22, v22)
            print("{:<27} {:<22} || {:<22}".format(k11, v11, v22))

        print("\n")

    test_design(test, prob_above50, prob_below50)
    codes = {}
    for k, v in unique.items():
        count = 0
        temp = {}

        for i in (range(len(v))):
            temp[v[i]] = count
            count += 1
        codes[k] = temp

    for i, j in temp_df.iterrows():
        for column in temp_df.columns:
            val = j[column]
            temp_df.at[i, column] = codes[column][val]

    print(df)
    print(temp_df)


if __name__ == '__main__':
    read_csv('Human.csv')
