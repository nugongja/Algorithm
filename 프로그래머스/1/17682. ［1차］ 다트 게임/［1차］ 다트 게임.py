import re

def solution(dartResult):
    answer = 0

    dartResult = re.findall(r'\d+|[SDT*#]', dartResult)
    
    st = []
    for token in dartResult:
        if token == 'S' or token == 'D' or token == 'T':
            i = 1
            if token == 'D': i = 2
            elif token == 'T': i = 3
            st.append(st.pop()**i)
        elif token == '*' or token == '#':
            if token == '*':
                tmp = st.pop()
                if len(st) >= 1:
                    st.append(st.pop()*2)
                st.append(tmp*2)
            else:
                st.append(st.pop()*-1)
        else:
            st.append(int(token))


    answer = sum(st)

    return answer
