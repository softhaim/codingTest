# 4659

''''
모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.

'''

'''
입력
입력은 여러개의 테스트 케이스로 이루어져 있다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 테스트할 패스워드가 주어진다.

마지막 테스트 케이스는 end이며, 패스워드는 한글자 이상 20글자 이하의 문자열이다. 또한 패스워드는 대문자를 포함하지 않는다.

출력
각 테스트 케이스를 '예제 출력'의 형태에 기반하여 품질을 평가하여라.
'''

import sys

input = sys.stdin.readline

test_case = list()

vowel = {'a','e','i','o','u'}
end_this_sentence = False

while True: 
    input_text = input().strip()
    if input_text == 'end':
        break
    '''
    여기서 조건인 
    1. 모음 하나 포함.
    2. 모음과 자음이 연속으로 3개면 안됨.
    3. 같은 글자 연속 2번 안됨. 단 ee, oo 는 허용
    '''
    # 모음이 안들어가면 안됨.
    if not bool(set(input_text) & vowel):
        print(f'<{input_text}> is not acceptable.')
        continue
    
    for i in range(len(input_text)-2):
        # 연속으로 모음이나 자음 3개면 안됨.
        if (input_text[i] in vowel and input_text[i+1] in vowel and input_text[i+2] in vowel) or \
            (input_text[i] not in vowel and input_text[i+1] not in vowel and input_text[i+2] not in vowel):
            end_this_sentence = True
            break
        # 같은 글자 연속 2번은 안됨. 단 ee, oo 는 허용
        elif (input_text[i] == input_text[i+1]) and (input_text[i:i+2] not in ['ee', 'oo']):
            end_this_sentence = True
            break
    # 위 반복에서 가장 마지막은 안하기에 최종 확인
    if not end_this_sentence and len(input_text)>=2 and (input_text[-1] == input_text[-2]) and input_text[-2:] not in ['ee', 'oo']:
            end_this_sentence = True
        
    if not end_this_sentence:    
        print(f'<{input_text}> is acceptable.')
    else:
        print(f'<{input_text}> is not acceptable.')
        end_this_sentence = False
