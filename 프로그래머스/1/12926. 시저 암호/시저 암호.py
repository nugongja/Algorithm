def solution(s, n):
    return ''.join([chr(65+(ord(i)+n-65)%26) if i.isupper() else
                    chr(97+(ord(i)+n-97)%26) if i.islower() else
                    ' ' for i in s])
