from collections import deque

def solution(plans):
    answer = []
    
    # 문자열 시간 -> 정수로 변환
    for target in plans:
        hour, min = int(target[1].split(":")[0]), int(target[1].split(":")[1])
        target[1] = hour*60 + min
        target[2] = int(target[2])
    
    # 시작 시간을 기준으로 오름차순
    plans.sort(key=lambda x:x[1])

    # 큐에 순서대로 삽입 -> popleft로 사용
    queue = deque(i for i in range(len(plans)))
    # 잠시 멈춘 작업 보관 스택 -> pop해서 사용
    tmp = []
    

    while True:
        # 시작 task 가져오기
        i = queue.popleft()
        # 큐에 남아있는 task가 없으면 answer에 추가 후 break
        if len(queue) == 0:    
            answer.append(plans[i][0])
            break
        
        # 다음 task 가져온 후 다시 넣음 (정보만 사용하기 위함)
        j = queue.popleft()
        queue.appendleft(j)
    
        # 시간 비교
        if plans[i][1] + plans[i][2] > plans[j][1]:     # 시간 초과 시 -> 남아있는 시간 수정 및 tmp에 삽입
            plans[i][2] -= (plans[j][1] - plans[i][1])
            tmp.append(i)
        elif plans[i][1] + plans[i][2] == plans[j][1]:  # 딱 맞춰 끝나면 answer에 삽입
            answer.append(plans[i][0])
        else:                                           # 시간이 남으면 answer에 삽입
            answer.append(plans[i][0])                  
            if tmp:                                     # 남는 시간동안 tmp에 있는 잔업 처리
                tmp_idx = tmp.pop()
                plans[tmp_idx][1] = plans[i][1] + plans[i][2]   # 시작 시간 설정
                queue.appendleft(tmp_idx)                       # 큐의 맨 앞에 넣어줌
    
    while tmp:                                          # tmp에 남아있는 일들을 pop해서 처리 순서대로 처리
        answer.append(plans[tmp.pop()][0])

    return answer