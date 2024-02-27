# Dominic Jason 2203959


def exact_change(user_total):
    dollar = user_total // 100
    user_total %= 100
    quarter = user_total // 25
    user_total %= 25
    dime = user_total // 10
    user_total %= 10
    nickel = user_total // 5
    user_total %= 5
    penny = user_total

    if dollar == 1:
        print(dollar, "dollar")
    elif dollar > 1:
        print(dollar, "dollars")
    if quarter == 1:
        print(quarter, "quarter")
    elif quarter > 1:
        print(quarter, "quarters")
    if dime == 1:
        print(dime, "dime")
    elif dime > 1:
        print(dime, "dimes")
    if nickel == 1:
        print(nickel, "nickel")
    elif nickel > 1:
        print(nickel, "nickels")
    if penny == 1:
        print(penny, "penny")
    elif penny > 1:
        print(penny, "pennies")
    return dollar, quarter, dime, nickel, penny


if __name__ == '__main__':
    input_val = int(input())
    if input_val == 0:
        print('no change')
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)
