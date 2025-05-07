def solution(s):
    st = []
    for i in range(len(s)):
        st.append(s[i])
    
    isValid = True
    close_cnt = 0
    while st:
        tmp = st.pop()
        if tmp == ')':
            close_cnt += 1
        else:
            close_cnt -= 1
            if close_cnt < 0:
                isValid = False
                break
    
    if close_cnt > 0:
        isValid = False
        
    

    return isValid