def solution(n):
    
    fb = [0]*(n+1)
    
    fb[0] = 0
    fb[1] = 1
    
    for i in range(2, n+1):
        fb[i] = (fb[i-2] + fb[i-1])%1234567
        
    
    
    
    return fb[n]