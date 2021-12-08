# 1918: 후위 표기식
# 연산자에 우선도를 설정하고, 우선도가 높으면 스택에 push하고, 낮으면 계속 pop을 진행하도록 작성

raw_string = input()
result = ''

opcode_e = {
    '(': 3,
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
    '': 0,
}
opcode_s = {
    '(': 0,
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
    '': 0,

}

stack = ['']

for ch in raw_string:
    if ch.isalpha():
        result += ch
    elif ch == ')':
        while stack[-1] != '(':
            result += stack.pop()
        stack.pop()
    elif opcode_e[ch] > opcode_s[stack[-1]]:
            stack.append(ch)
    else:
        while opcode_e[ch] <= opcode_s[stack[-1]]:
            result += stack.pop()
        stack.append(ch)

while len(stack)>1:
    result += stack.pop()
        
print(result)