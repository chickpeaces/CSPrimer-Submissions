def is_char(ch):
    return type(ch) == str and len(ch) == 1

def is_newline(ch):
    return is_char(ch) and c == '\n'

def is_comment(ch):
    return is_char(ch) and c == ';'

def is_left_paren(ch):
    return is_char(ch) and (ch=='(' or ch=='{' or ch=='[')

def is_right_paren(ch):
    return is_char(ch) and (ch==')' or ch=='}' or ch==']')

def is_match_paren(chl, chr):
    return (is_char(chl) and is_char(chr)) and (chl=='(' and chr==')') or  (chl=='{' and chr=='}') or (chl=='[' and chr==']')

if __name__ == "__main__":
    stack= []
    line_count= 1
    comment_state= False
    with open("stretch.rkt", encoding='utf-8') as file:
        lines= file.readlines()
        for line in lines:
            for i in range(len(line)):
                c= line[i]
                if is_left_paren(c) and not comment_state:
                    stack.append(c)
                elif is_right_paren(c) and not comment_state:
                    if not is_match_paren(stack.pop(), c):
                        print("line {}: mismatched parenthesis".format(line_count))
                        print(line)
                        for _ in range(i):
                            print(" ", end="")
                        print("^")
                        break
                elif is_comment(c) and not comment_state:
                    comment_state= True
                elif is_newline(c):
                    comment_state= False
                    line_count+= 1