import pandas as pd


def do_mle(data):
    # print('In MLE...')
    # print(data)
    counts = {}

    for column in data:
        counts[column] = data[column].value_counts()

    # for key, values in counts.items():
    #     print(key, ': ', values)

    test = counts['x14']
    print(test)


def test_design(data):
    print('In testing...')
    # print(data)
