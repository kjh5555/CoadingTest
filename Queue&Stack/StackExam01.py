#'(){}[]'를 포함하고 있는 문자열 S가 주어졌을 떄 괄호가 유효한지 아닌지 판별하시오


'''
1. input : s = ")()'
   output: false

2. input : s = "([]}'
   output: false   

3. input : s = "{()[]}'
   output: true     
'''

def isvalid(s):
    stack=[]
    for i in s:
        if i == '(':
            stack.append(')')
        elif i == '{':
            stack.append('}')
        elif i == '[':
            stack.append(']')
        elif not stack or stack.pop() != i:
            return print(False)
    return print(True)


isvalid('{(([]))[]}')