import sys
input = sys.stdin.readline

def solution(places):
    answer = []

    idx = 0
    for room in places:
        idx += 1
        Person = []
        for i in range(5):
            for j in range(5):
                if room[i][j] == 'P':
                    Person.append((i,j))
        
        isPossible = True
        for i in range(len(Person)-1):
            r1 = Person[i][0]
            c1 = Person[i][1]
            for j in range(i+1, len(Person)):
                r2 = Person[j][0]
                c2 = Person[j][1]

                manhaten = abs(c1-c2) + abs(r1-r2)

                if manhaten == 1: 
                    isPossible = False
                    break
                elif manhaten == 2:
                    if r1 == r2 or c1 == c2:
                        tmp_r = (r1+r2)//2
                        tmp_c = (c1+c2)//2
                        if room[tmp_r][tmp_c] == 'O':
                            isPossible = False
                            break
                    else:
                        if room[r1][c2] == 'O' or room[r2][c1] == 'O':
                                isPossible = False
                                break
            if not isPossible:
                break
                
        if isPossible:
            answer.append(1)
        else:
            answer.append(0)

                    
            

    return answer