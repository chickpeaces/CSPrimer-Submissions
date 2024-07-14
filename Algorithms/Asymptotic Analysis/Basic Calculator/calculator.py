from sys import argv

TOKEN_PARENTHESIS = ['(', ')']
TOKEN_OPERATOR = ['*', '/', '+', '-']
TOKEN_WHITESPACE = [' ', '\t', '\r', '\n']
TOKEN_NUMBER = ['0','1','2','3','4','5','6','7','8','9']

def is_space(c):
    return c in TOKEN_WHITESPACE

def is_parenthesis(c):
    return c in TOKEN_PARENTHESIS

def is_number(c):
    return c in TOKEN_NUMBER

def is_operator(c):
    return c in TOKEN_OPERATOR

def alphanum_to_int(s):
    output= 0
    for c in s:
        output= (output + int(c)) * 10
    return output // 10

def calculate( x, y, op):
    if op == '+':
        return x + y
    if op == '-':
        return x - y
    if op == '*':
        return x * y
    if op == '/':
        return x // y

if __name__ == '__main__':
    #parenthesis, multiplication, division, addition, subtraction
    stack= []
    op1, op2, num, opr, output= 0, 0, '', '', 0
    if len(argv) <= 1:
        print("missing arithmetic expression as program input")
    elif len(argv) > 1:
        for expr in argv[1:]:
            print("{} = ".format(expr), end='')
            c_idx= 0
            for c in expr:
                if is_space(c):
                    pass
                if is_parenthesis(c):
                    if c == '(':
                        stack.append(c)
                    elif c == ')':
                        op2= stack.pop()
                        opr= stack.pop()
                        op1= stack.pop()
                        if stack[-1] == '(':
                            stack.pop()
                        if opr == '/' and op2 == 0:
                            print("\ncannot divide by zero")
                            break
                        else:
                            output= calculate(op1, op2, opr)
                        if c_idx == len(expr)-1 and len(stack) == 0:
                            print("{0}".format(output))
                        else:
                            stack.append(output)
                if is_operator(c):
                    stack.append(c)
                if is_number(c):
                    num+= c
                    if not is_number(expr[c_idx+1]):
                        stack.append(alphanum_to_int(num))
                        num= ''
                c_idx+= 1
