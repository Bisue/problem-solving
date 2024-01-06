# [카카오 인턴] 수식 최대화 (2020 카카오 인턴십)
# https://school.programmers.co.kr/learn/courses/30/lessons/67257

from itertools import permutations

def parse(expression):
    tokens = []
    buffer = []
    
    for ch in expression:
        if ch in ['+', '-', '*']:
            tokens.append(int(''.join(buffer)))
            tokens.append(ch)
            buffer = []
        else:
            buffer.append(ch)
            
    tokens.append(int(''.join(buffer)))
            
    return tokens

def calculate(operators, tokens):
    temp = [t for t in tokens]
    for operator in operators:
        st = []
        operand = None
        for token in temp:
            if token == operator:
                operand = st.pop()
            else:
                if operand is None:
                    st.append(token)
                else:
                    if operator == '*':
                        st.append(operand * token)
                    elif operator == '+':
                        st.append(operand + token)
                    elif operator == '-':
                        st.append(operand - token)
                    operand = None
        
        temp = st
        st = []
        
    return abs(temp[0])
    

def solution(expression):
    tokens = parse(expression)
    
    answer = 0
    for operators in permutations(['+', '-', '*']):
        answer = max(answer, calculate(operators, tokens))
    
    return answer
