def calculate_coins(summ):
    convert_sum = summ * 100
    overage_sum = convert_sum
    all_coins = {1: 0, 2: 0, 100: 0, 5: 0, 10: 0, 50: 0, 20: 0}
    key_list = list(all_coins.keys())
    key_list.sort()
    count_key_list = len(key_list) - 1
    while overage_sum > 0 and count_key_list >= 0:
        if key_list[count_key_list] > overage_sum:
            count_key_list -= 1
        else:
            all_coins[key_list[count_key_list]] += 1
            overage_sum -= key_list[count_key_list]
    return all_coins
