
def generate(s):
    close_to_open ={
        ")":"(",
        "}":"{",
        "]":"["
    }
   
    stack = []
    for bracket in s:
        if bracket in close_to_open:
            if not stack:
                return False
            top = stack.pop()
            if close_to_open[bracket] != top:
                return False
        else:
            stack.append(bracket)
        if stack:
            return False
        else:
            return True    

s="(){}[]"
callValue = generate(s)
print(callValue)   
# close_to_open = {')': '(', ']': '[', '}': '{'}

# bracket = ')'

# if bracket in close_to_open:
#     print(f"{bracket} is a closing bracket and its corresponding opening bracket is {close_to_open[bracket]}")
# else:
#     print(f"{bracket} is not a recognized closing bracket")
