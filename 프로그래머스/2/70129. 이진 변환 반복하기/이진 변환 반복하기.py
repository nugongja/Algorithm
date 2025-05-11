def solution(s):
    cnt = 0
    zero_cnt = 0
    while s != "1":
        zero_cnt += len(s) - len(s.replace("0", ""))
        cnt += 1

        tmp = len(s.replace("0", ""))
        s = ""
        while tmp != 0:
            s += str(tmp%2)
            tmp //= 2
        

    return [cnt, zero_cnt]