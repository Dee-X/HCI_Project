import pandas as pd
import math


def do_mle(data, codes):
    counts = {}
    counts_above50 = {}
    counts_below50 = {}
    prob_above50 = {}
    prob_below50 = {}
    data_length = len(data.index)

    # MLE: C(val)
    for column in data:
        counts[column] = data[column].value_counts()

    df_above50 = data[data['Y'] == codes['Y']['>50K.']]  # C(>50K)
    # df_above50 = data[data['Y'] == '>50K.']  # C(>50K)
    df_below50 = data[data['Y'] == codes['Y']['<=50K.']]  # C(<=50K)
    # df_below50 = data[data['Y'] == '<=50K.']  # C(<=50K)

    above_full_count = len(df_above50.index)
    below_full_count = len(df_below50.index)

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
            # above_prob = above_cnt / above_full_count
            above_prob = above_cnt / data_length
            inner_ret_above50[val] = above_prob

            # MLE: C(val, <=50k)/ C(val)
            # below_prob = below_cnt / below_full_count
            below_prob = below_cnt / data_length
            inner_ret_below50[val] = below_prob
        prob_above50[column] = inner_ret_above50
        prob_below50[column] = inner_ret_below50

    return prob_above50, prob_below50


def test_design(data, prob_above50, prob_below50, codes):
    data_length = len(data.index)
    assigned_list = []

    # i: row, j: items
    for i, j in data.iterrows():
        below_entropy = 0
        above_entropy = 0
        for column in data.columns:
            val = j[column]
            if column == 'Y':
                break
            above = prob_above50[column]
            below = prob_below50[column]
            above_prob = above.get(val, 0)
            below_prob = below.get(val, 0)

            # Corpus Cross Entropy: -1/n*SUM(log_2(p(x)))
            if above_prob != 0:
                above_entropy += math.log(above_prob, 2)
            if below_prob != 0:
                below_entropy += math.log(below_prob, 2)
        # break
        above_entropy = above_entropy * (-1 / data_length)
        below_entropy = below_entropy * (-1 / data_length)

        if below_entropy > above_entropy:
            assigned_list.append(codes['Y']['>50K.'])
        else:
            assigned_list.append(codes['Y']['<=50K.'])

    data['Assigned'] = assigned_list

    find_accuracy(data)


def find_accuracy(data):
    data_length = len(data.index)
    sum_l = 0

    for i, j in data.iterrows():
        actual = j['Y']
        assigned = j['Assigned']
        l = 0
        if actual == assigned:
            l = 1
        else:
            l = 0

        sum_l += l

    acc = (1/data_length) * sum_l

    print("\n\nAccuracy of Model: ", acc)
