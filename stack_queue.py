'''
스택(stack): 후입선출.
접시를 쌓는 것 생각 => 마지막에 쌓은 접시를 제일 먼저 꺼내게 됨

stack = []
stack.append(1)
stack.append(2)
stack.append(3)
stack.pop()  #3
stack.pop()  #2
stack.pop()  #1
시간복잡도: O(1)

큐(queue): 선입선출.
줄 서는 것 생각 => 먼저 선 사람이 먼저 입장함

queue = []
queue.append(1)
queue.append(2)
queue.append(3)
queue.pop(0)  #1
queue.pop(0)  #2
queue.pop(0)  #3
앞에서 하나를 비우고 뒤에 있는 모든 데이터들을 한칸씩 앞으로 당김
=> 시간복잡도: O(n)

실제로 파이썬에서 queue 사용할때 
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()  #1
queue.popleft()  #2
queue.popleft()  #3

'''

#예제1) 유효한 괄호 문제
def solution(s):
    stack = []
    table = {
        ')': '(',
        '}': '{',
        ']': '[',
    }
    for char in s:
        if char not in table:
            stack.append(char)
        elif table[char]!=stack.pop():
            return False
        print(stack)
    return len(stack)==0



#(){} )()
'''
#예제2) 프린터
from collections import deque

def solution(priorities, location):
    deq = deque([(p,i) for (i,p) in enumerate(priorities)]) #인덱스 묶어줌
    answer = 0  #인쇄가 완료된 문서 개수
    
    while deq:        
        target = deq.popleft() #맨앞에 있는 요소 빼내기
        
        if max(deq)[0] > target[0]: #뒤에 최고우선순위가 있다면
            deq.append(target) #맨 뒤로보내기
            
        else:
            answer += 1 #최고 우선순위라면 문서 인쇄됨
            if target[1] == location: #현재 target의 인덱스가 내가 요청한문서 위치(location)라면
                break

    return answer
    '''


if __name__ =="__main__":
    s="((())"
    print(solution(s))
    