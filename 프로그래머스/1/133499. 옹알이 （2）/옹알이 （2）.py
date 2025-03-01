def solution(babbling):
    answer = 0
    
    for words in babbling:
        if ("ayaaya" in words) or ("yeye" in words) or ("woowoo" in words) or ("mama" in words):
            continue

        words = words.replace("aya", " ").replace("ye", " ").replace("woo", " ").replace("ma", " ")
        words = words.replace(" ","")
        if len(words) == 0:
            answer += 1

    return answer
    