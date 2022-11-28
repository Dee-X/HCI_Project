import pandas as pd
from probability import do_mle, test_design
from sklearn.model_selection import train_test_split
from os import path
import sys


# Read csv and filter out rows with '?'
def read_csv(name):
    f = open("output.txt", "w")
    # f = open(path.join(path.dirname(sys.executable), "output.txt"), "w")
    
    unique = {}
    data = pd.read_csv(name, skipinitialspace=True)
    # data = pd.read_csv(path.join(path.dirname(__file__), name), skipinitialspace=True)
    df = pd.DataFrame(data)

    for column in df:
        df = df[df[column] != '?']
        unique[column] = df[column].unique()

    temp_df = df.copy(deep=True)

    codes = {}
    print("Amount of unique values in each column: \n")
    f.write("Amount of unique values in each column: \n")
    for k, v in unique.items():
        count = 0
        temp = {}
        print(' {:<3}: {:<6}'.format(k, len(v)))
        f.write(' {:<3}: {:<6}\n'.format(k, len(v)))

        for i in (range(len(v))):
            temp[v[i]] = count
            count += 1
        codes[k] = temp

    for i, j in temp_df.iterrows():
        for column in temp_df.columns:
            val = j[column]
            temp_df.at[i, column] = codes[column][val]

    # Split data into two different datasets
    train, test = train_test_split(temp_df, test_size=0.3)

    prob_above50, prob_below50 = do_mle(train, codes)

    for (k, v), (k2, v2) in zip(prob_above50.items(), prob_below50.items()):
        print("{:<35} {:<22} || {:<22}".format(k, '>50k', '<=50k'))
        f.write("{:<35} {:<22} || {:<22}\n".format(k, '>50k', '<=50k'))
        print('=' * 85)
        f.write('=' * 85)
        f.write('\n')
        key_list = list(codes[k].keys())
        val_list = list(codes[k].values())
        for (k11, v11), (k22, v22) in zip(v.items(), v2.items()):
            # print(k11, v11, k22, v22)

            position = val_list.index(k11)
            print("{:<6}: {:<27} {:<22} || {:<22}".format(k11, key_list[position], v11, v22))
            f.write("{:<6}: {:<27} {:<22} || {:<22}\n".format(k11, key_list[position], v11, v22))

        print("\n")
        f.write("\n")

    acc = test_design(test, prob_above50, prob_below50, codes)
    
    print("Accuracy of Model: ", acc)
    # f.write("Accuracy of Model: ", acc, "\n")
    
    f.write("Accuracy of Model: {:<35}\n".format(acc))
    
    f.close()


if __name__ == '__main__':
    print("Working...")
    read_csv('Human.csv')
    
    while True:
        pass
