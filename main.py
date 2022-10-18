import pandas as pd


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Read csv and filter out rows with '?'
def read_csv(name):
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

    print(df)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_csv('Human.csv')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
