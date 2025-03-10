def solution(price, money, count):
    answer = money

    i = 1
    while count > 0:
        answer -= price*i
        count -= 1
        i += 1


    return -answer if answer < 0 else 0