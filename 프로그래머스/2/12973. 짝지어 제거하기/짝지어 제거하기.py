def solution(s):
    answer = 0
    
    st = []

    for i in s:
        if len(st) > 0:
            tmp = st.pop()
            if tmp != i:
                st.append(tmp)
                st.append(i)
        else:
            st.append(i)
    
    if len(st) == 0: answer = 1



    return answer
