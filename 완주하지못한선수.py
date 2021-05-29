def solution(participant, completion):
    dic = dict(zip(participant, [0 for i in range(0, len(participant))]))
    
    for i in completion:
        if i in dic:
            dic[i] += 1
       
    for j in participant:
        if j in dic:
            dic[j] -= 1
            
            if dic[j] < 0:
                return j
        else:
            return j