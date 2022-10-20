import pandas as pd
import probability
from sklearn.model_selection import train_test_split

str_columns = ['x2', 'x4', 'x6', 'x7', 'x8', 'x9', 'x10', 'x14', 'Y']


# Read csv and filter out rows with '?'
def read_csv(name):
    unique = {}
    data = pd.read_csv(name, skipinitialspace=True)
    df = pd.DataFrame(data)
    df.columns = ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8", "x9", "x10", "x11", "x12", "x13", "x14", "Y"]

    for column in df:
        if column == 'Y':
            break
        else:
            df = df[df[column] != '?']
            unique[column] = df[column].unique()

    # Split data into two different datasets
    train, test = train_test_split(df, test_size=0.3)

    probability.do_mle(train)
    probability.test_design(test)


if __name__ == '__main__':
    read_csv('Human.csv')
