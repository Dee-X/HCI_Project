import pandas as pd
from probability import do_mle, test_design
from sklearn.model_selection import train_test_split


# Read csv and filter out rows with '?'
def read_csv(name):
    unique = {}
    data = pd.read_csv(name, skipinitialspace=True)
    df = pd.DataFrame(data)

    for column in df:
        if column == 'Y':
            break
        else:
            df = df[df[column] != '?']
            unique[column] = df[column].unique()

    # Split data into two different datasets
    train, test = train_test_split(df, test_size=0.3)

    prob_above50, prob_below50 = do_mle(train)

    test_design(test, prob_above50, prob_below50)


if __name__ == '__main__':
    read_csv('Human.csv')
