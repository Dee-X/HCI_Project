import pandas as pd
from probability import do_mle, test_design
from sklearn.model_selection import train_test_split

# str_columns = ['x2', 'x4', 'x6', 'x7', 'x8', 'x9', 'x10', 'x14', 'Y']


# Read csv and filter out rows with '?'
def read_csv(name):
    unique = {}
    records = {}
    data = pd.read_csv(name, skipinitialspace=True)
    df = pd.DataFrame(data)
    # df.columns = ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8", "x9", "x10", "x11", "x12", "x13", "x14", "Y"]

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
    
    print("BREAK POINT")
    
    records[0] = df.x1
    records[1] = df.x2
    records[2] = df.x3
    records[3] = df.x4
    records[4] = df.x5
    records[5] = df.x6
    records[6] = df.x7
    records[7] = df.x8
    records[8] = df.x9
    records[9] = df.x10
    records[10] = df.x11
    records[11] = df.x12
    records[12] = df.x13
    records[13] = df.x14
    records[14] = df.Y
    

if __name__ == '__main__':
    read_csv('Human.csv')
