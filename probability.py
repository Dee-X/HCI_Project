import pandas as pd


def do_mle(data):
    counts = {}
    counts_above50 = {}
    counts_below50 = {}
    prob_above50 = {}
    prob_below50 = {}

    # MLE: C(val)
    for column in data:
        counts[column] = data[column].value_counts()

    fullCount = len(data.index)

    df_above50 = data[data['Y'] == '>50K.']  # C(>50K)
    df_below50 = data[data['Y'] == '<=50K.']  # C(<=50K)

    for column in df_above50:
        counts_above50[column] = df_above50[column].value_counts()

    for column in df_below50:
        counts_below50[column] = df_below50[column].value_counts()

    for column in counts:
        if column == 'Y':
            break
        # print(column)
        inner_ret_above50 = {}
        inner_ret_below50 = {}
        for val, cnt in counts[column].items():

            # MLE: C(val, >50k)
            above_cnt = counts_above50[column].get(val)
            if above_cnt is None:
                above_cnt = 0

            # MLE: C(val, <=50k)
            below_cnt = counts_below50[column].get(val)
            if below_cnt is None:
                below_cnt = 0

            # MLE: C(val, >50k)/ C(val)
            above_prob = above_cnt / fullCount
            inner_ret_above50[val] = above_prob

            # MLE: C(val, <=50k)/ C(val)
            below_prob = below_cnt / fullCount
            inner_ret_below50[val] = below_prob
        prob_above50[column] = inner_ret_above50
        prob_below50[column] = inner_ret_below50

    # print("Above: \n", prob_above50, "\n\n")
    # print("Below: \n", prob_below50, "\n\n")
    return prob_above50, prob_below50


def test_design(data, prob_above50, prob_below50):
    print('In testing...')
    # print(data)

    print("Above: \n", prob_above50, "\n\n")
    print("Below: \n", prob_below50, "\n\n")

    # for column in data:
        # for val, cnt in data[column].items():
                # print(val)
