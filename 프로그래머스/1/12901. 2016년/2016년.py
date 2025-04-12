def solution(a, b):
    month = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    week = {0:'THU', 1:'FRI', 2:'SAT', 3:'SUN', 4:'MON', 5:'TUE', 6:'WED'}
    return week[(sum(month[:a])+b)%7]
