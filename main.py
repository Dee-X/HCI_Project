import pandas as pd


# Read csv and filter out rows with '?'
def read_csv(name):
    unique = {}
    data = pd.read_csv(name)
    df = pd.DataFrame(data)
    df.columns = [
        "x1",
        "x2",
        "x3",
        "x4",
        "x5",
        "x6",
        "x7",
        "x8",
        "x9",
        "x10",
        "x11",
        "x12",
        "x13",
        "x14",
        "Y"
    ]

    for column in df:
        if column == 'Y':
            break
        else:
            df = df[df[column] != ' ?']
            unique[column] = df[column].unique()

    # unique['x1'] = df.x1.unique()
    # unique['x2'] = df.x2.unique()
    # unique['x3'] = df.x3.unique()
    # unique['x4'] = df.x4.unique()
    # unique['x5'] = df.x5.unique()
    # unique['x6'] = df.x6.unique()
    # unique['x7'] = df.x7.unique()
    # unique['x8'] = df.x8.unique()
    # unique['x9'] = df.x9.unique()
    # unique['x10'] = df.x10.unique()
    # unique['x11'] = df.x11.unique()
    # unique['x12'] = df.x12.unique()
    # unique['x13'] = df.x13.unique()
    # unique['x14'] = df.x14.unique()

    print(df)
    # print(unique)

    for key, values in unique.items():
        print(key, ': ', values)


if __name__ == '__main__':
    read_csv('Human.csv')
