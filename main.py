
equation = [0,"+",13,"*",0,"/",0,"+",0,"+",12,"*",0,"-",0,"-",11,"+",0,"*",0,"/",0,"-",10]
length = len(equation)
options = [i for i in range(1, 10)]

def create(answer, equation):
    for i in range(len(equation)):
        if equation[i] == 0:
            equation[i] = answer.pop(0)
            
    return equation.copy()

def plug(val, equation):
    for i in range(len(equation)):
        if equation[i] == 0:
            equation[i] = val
            return equation
        
def printequ(equ):
    for i in range(len(equ)):
        print(equ[i], end="")

def solve(answer, equ, eq, pemdas):
    equation = equ.copy()
    eqtmp = eq.copy()
    if len(answer) == 0:
        ans = 0
        if pemdas:
            ans = calcpemdas(equation)
        else:
            ans = calculate(equation)
            
        if ans == 66:
            print(ans, eq)
        return
    
    for i in range(len(answer)):
        equation = plug(answer[i], equation)
        eqtmp.append(answer[i])
        tmp = answer.copy()
        tmp.pop(i)
        solve(tmp, equation, eqtmp, pemdas)
        equation = equ.copy()
        eqtmp = eq.copy()
        
    return eq    
    
def calcpemdas(equation):
    i = 0
    while len(equation) > i:
        if equation[i] == "*":
            equation[i-1] = equation[i-1] * equation[i+1]
            equation.pop(i)
            equation.pop(i)
            i -= 1
        elif equation[i] == "/":
            equation[i-1] = equation[i-1] / equation[i+1]
            equation.pop(i)
            equation.pop(i)
            i -= 1
        i += 1
    
    i = 0
    while len(equation) > 1:
        if equation[i] == "+":
            equation[i-1] = equation[i-1] + equation[i+1]
            equation.pop(i)
            equation.pop(i)
            i -= 1
        elif equation[i] == "-":
            equation[i-1] = equation[i-1] - equation[i+1]
            equation.pop(i)
            equation.pop(i)
            i -= 1
        i += 1
        
    return equation[0]
    
def calculate(equation):
    eq = []
    for i in range(length):
        # print(equation)
        
        eq.append(equation.pop(0))

        if len(eq) == 3:
            if eq[1] == "+":
                eq = [add(eq)]
            elif eq[1] == "-":
                eq = [sub(eq)]
            elif eq[1] == "*":
                eq = [mul(eq)]
            elif eq[1] == "/":
                eq = [div(eq)]
                
        # print(eq)
        
    return eq[0]

def div(eq):
    a = eq[0]
    b = eq[2]
    return a / b
    
def mul(eq):
    a = eq[0]
    b = eq[2]
    return a * b
    
def sub(eq):
    a = eq[0]
    b = eq[2]
    return a - b
    
def add(eq):
    a = eq[0]
    b = eq[2]
    return a + b
    
# no pemdas
print("no pemdas")
solve(options, equation, [], False)

# # pemdas
print("pemdas")
solve(options, equation, [], True)



