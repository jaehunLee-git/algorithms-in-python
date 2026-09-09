import math

# 최소공배수 함수 구현
def lcm(a, b):
    return a * b // math.gcd(a, b)

def solution(signals):
    time = 1
    
    # 모든 신호등의 주기가 동시에 반복되는 구간 = 각 신호등 주기의 최소공배수
    for signal in signals:
        total = sum(signal)
        time = lcm(time, total)
        
    # 1초부터 모든 시간에 대해
    for i in range(1, time + 1):
        isAllYellow = True
        
        # 각 신호등별로 노란색인지 판단
        for signal in signals:
            g, y, r = signal
            total = g + y + r
            index = i % total
            
            if not (index <= g + y and index > g):
                isAllYellow = False
                break
                
        if isAllYellow:
            return i
        
    return -1