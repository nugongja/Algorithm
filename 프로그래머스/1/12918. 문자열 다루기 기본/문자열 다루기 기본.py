def solution(s):
    if not (len(s) == 4 or len(s) == 6):
        return False
    try:
        int(s)
        return True
    except:
        return False