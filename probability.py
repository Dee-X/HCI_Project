import pandas as pd


def do_mle(data):
    # print('In MLE...')
    # print(data)
    counts = {}
    counts_above50 = {}
    counts_below50 = {}

    for column in data:
        counts[column] = data[column].value_counts()

    # for key, values in counts.items():
    #     print(key, ': ', values)

    df_above50 = data[data['Y'] == '>50K.']
    df_below50 = data[data['Y'] == '<=50K.']

    for column in df_above50:
        counts_above50[column] = df_above50[column].value_counts()

    for column in df_below50:
        counts_below50[column] = df_below50[column].value_counts()

    test = counts['x14'].get('Mexico')
    # print(test)

    test2 = counts_above50['x14'].get('Mexico')
    # print(test2)

    test3 = counts_below50['x14'].get('Mexico')
    # print(test3)

    for column in counts:
        print(column)
        for val, cnt in counts[column].items():
            above_cnt = counts_above50[column].get(val)
            if above_cnt is None:
                above_cnt = 0
            below_cnt = counts_below50[column].get(val)
            if below_cnt is None:
                below_cnt = 0
            print(val, ' Above: ', above_cnt, "/", cnt)
            above_prob = above_cnt/cnt
            print(val, ' Below: ', below_cnt, "/" , cnt)
            below_prob = below_cnt/cnt
            print(above_prob)
            print(below_prob)

    # print(counts_below50)
    # print(counts_above50)
    # print(df_above50)
    # print(df_below50)


def test_design(data):
    print('In testing...')
    # print(data)
