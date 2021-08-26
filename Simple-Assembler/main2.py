import sys
x = sys.stdin.read().splitlines()
y=[]
for i in range(len(x)):
    y.append(x[i].split(" "))

# opcode Table
opcode = {"00000": "add", "00001": "sub", "00010": "mov", "00011": "mov", "00100": "ld", "00101": "st", "00110": "mul",
          "00111": "div", "01000": "rs", "01001": "ls", "01010": "xor", "01011": "or", "01100": "and", "01101": "not",
          "01110": "cmp", "01111": "jmp", "10000": "jlt", "10001": "jgt", "10010": "je", "10011": "hlt"}

# Registers
reg = {"R0": "000", "R1": "001", "R2": "010", "R3": "011", "R4": "100", "R5": "101", "R6": "110", "FLAGS": "111", }

def dectobin(n):
    return bin(n).replace("0b", "")

# sub,mul,add,xor,or,and
def A(op, r1, r2, r3):
    s = op + "00" + r1 + r2 + r3
    return s

# mov imm,rs,ls
def B(op, r1, im):
    s = op + r1 + im
    return s

# mov reg,div,not,cmp
def C(op, r1, r2):
    s = op + "00000" + r1 + r2
    return s

# ld,st
def D(op, r1, ma):
    s = op + r1 + ma
    return s

# jmp,jlt,jgt,je
def E(op, ma):
    s = op + "000" + ma
    return s

# hlt
def F():
    s = "1001100000000000"
    return s

def getkey(val):
    for key, value in opcode.items():
        if val == value:
            return key

def binaryconvert(y, opcode, reg,mem):
    if (y[0] == "add"):
        op = getkey("add")
        r1 = reg.get(y[1])
        r2 = reg.get(y[2])
        r3 = reg.get(y[3])
        print(A(op, r1, r2, r3))

    elif (y[0][-1] == ":" and y[1] == 'add'):
        op = getkey("add")
        r1 = reg.get(y[2])
        r2 = reg.get(y[3])
        r3 = reg.get(y[4])
        print(A(op, r1, r2, r3))

    elif (y[0] == "sub"):
        op = getkey("sub")
        r1 = reg.get(y[1])
        r2 = reg.get(y[2])
        r3 = reg.get(y[3])
        print(A(op, r1, r2, r3))

    elif (y[0][-1] == ":" and y[1] == 'sub'):
        op = getkey("sub")
        r1 = reg.get(y[2])
        r2 = reg.get(y[3])
        r3 = reg.get(y[4])
        print(A(op, r1, r2, r3))

    elif (y[0] == "mul"):
        op = getkey("mul")
        r1 = reg.get(y[1])
        r2 = reg.get(y[2])
        r3 = reg.get(y[3])
        print(A(op, r1, r2, r3))

    elif (y[0][-1] == ":" and y[1] == 'mul'):
        op = getkey("mul")
        r1 = reg.get(y[2])
        r2 = reg.get(y[3])
        r3 = reg.get(y[4])
        print(A(op, r1, r2, r3))

    elif (y[0] == "xor"):
        op = getkey("xor")
        r1 = reg.get(y[1])
        r2 = reg.get(y[2])
        r3 = reg.get(y[3])
        print(A(op, r1, r2, r3))

    elif (y[0][-1] == ":" and y[1] == 'xor'):
        op = getkey("xor")
        r1 = reg.get(y[2])
        r2 = reg.get(y[3])
        r3 = reg.get(y[4])
        print(A(op, r1, r2, r3))

    elif (y[0] == "or"):
        op = getkey("or")
        r1 = reg.get(y[1])
        r2 = reg.get(y[2])
        r3 = reg.get(y[3])
        print(A(op, r1, r2, r3))

    elif (y[0][-1] == ":" and y[1] == 'or'):
        op = getkey("or")
        r1 = reg.get(y[2])
        r2 = reg.get(y[3])
        r3 = reg.get(y[4])
        print(A(op, r1, r2, r3))

    elif (y[0] == "and"):
        op = getkey("and")
        r1 = reg.get(y[1])
        r2 = reg.get(y[2])
        r3 = reg.get(y[3])
        print(A(op, r1, r2, r3))

    elif (y[0][-1] == ":" and y[1] == 'and'):
        op = getkey("and")
        r1 = reg.get(y[2])
        r2 = reg.get(y[3])
        r3 = reg.get(y[4])
        print(A(op, r1, r2, r3))

    elif (y[0] == "mov"):
        if ("$" in y[2]):
            op = "00010"
            r1 = reg.get(y[1])
            im = dectobin(int(y[2][1:len(y[2])]))
            z = "00000000" + im
            im1 = z[len(z) - 8:len(z)]
            print(B(op, r1, im1))

        else:
            op = "00011"
            r1 = reg.get(y[1])
            r2 = reg.get(y[2])
            print(C(op, r1, r2))

    elif (y[0][-1] == ":" and y[1] == "mov"):
        if ("$" in y[3]):
            op = "00010"
            r1 = reg.get(y[2])
            im = dectobin(int(y[3][1:len(y[3])]))
            z = "00000000" + im
            im1 = z[len(z) - 8:len(z)]
            print(B(op, r1, im1))

        else:
            op = "00011"
            r1 = reg.get(y[2])
            r2 = reg.get(y[3])
            print(C(op, r1, r2))

    elif (y[0] == "hlt"):
        print(F())

    elif (y[0][-1] == ":" and y[1] == "hlt"):
        print(F())

    elif (y[0] == "rs"):
        op = getkey("rs")
        r1 = reg.get(y[1])
        im = dectobin(int(y[2][1:len(y[2])]))
        z = "00000000" + im
        im1 = z[len(z) - 8:len(z)]
        print(B(op, r1, im1))

    elif (y[0][-1] == ":" and y[0] == "rs"):
        op = getkey("rs")
        r1 = reg.get(y[2])
        im = dectobin(int(y[3][1:len(y[3])]))
        z = "00000000" + im
        im1 = z[len(z) - 8:len(z)]
        print(B(op, r1, im1))

    elif (y[0] == "ls"):
        op = getkey("ls")
        r1 = reg.get(y[1])
        im = dectobin(int(y[2][1:len(y[2])]))
        z = "00000000" + im
        im1 = z[len(z) - 8:len(z)]
        print(B(op, r1, im1))

    elif (y[0][-1] == ":" and y[0] == "ls"):
        op = getkey("ls")
        r1 = reg.get(y[2])
        im = dectobin(int(y[3][1:len(y[3])]))
        z = "00000000" + im
        im1 = z[len(z) - 8:len(z)]
        print(B(op, r1, im1))

    elif (y[0][-1] == ':' and y[1] == "div"):
        op = getkey('div')
        r1 = reg.get(y[2])
        r2 = reg.get(y[3])
        print(C(op, r1, r2))

    elif (y[0] == 'not'):
        op = getkey('not')
        r1 = reg.get(y[1])
        r2 = reg.get(y[2])
        print(C(op, r1, r2))

    elif (y[0][-1] == ':' and y[1] == "not"):
        op = getkey('not')
        r1 = reg.get(y[2])
        r2 = reg.get(y[3])
        print(C(op, r1, r2))

    elif (y[0] == 'cmp'):
        op = getkey('cmp')
        r1 = reg.get(y[1])
        r2 = reg.get(y[2])
        print(C(op, r1, r2))

    elif (y[0][-1] == ':' and y[1] == "cmp"):
        op = getkey('cmp')
        r1 = reg.get(y[2])
        r2 = reg.get(y[3])
        print(C(op, r1, r2))

    elif (y[0] == 'ld'):
        op = getkey('ld')
        r1 = reg.get(y[1])
        mam = mem.get(y[2])
        im = dectobin(int(mam))
        z = "00000000" + im
        im1 = z[len(z) - 8:len(z)]
        print(D(op, r1, im1))

    elif (y[0][-1] == ':' and y[1] == "ld"):
        op = getkey('ld')
        r1 = reg.get(y[2])
        mam = mem.get(y[3])
        im = dectobin(int(mam))
        z = "00000000" + im
        im1 = z[len(z) - 8:len(z)]
        print(D(op, r1, im1))

    elif (y[0] == 'st'):
        op = getkey('st')
        r1 = reg.get(y[1])
        mam = mem.get(y[2])
        im = dectobin(int(mam))
        z = "00000000" + im
        im1 = z[len(z) - 8:len(z)]
        print(D(op, r1, im1))

    elif (y[0][-1] == ':' and y[1] == "st"):
        op = getkey('st')
        r1 = reg.get(y[2])
        mam = mem.get(y[3])
        im = dectobin(int(mam))
        z = "00000000" + im
        im1 = z[len(z) - 8:len(z)]
        print(D(op, r1, im1))

    elif (y[0] == 'jmp'):
        op = getkey('jmp')
        mam = mem.get(y[1])
        im = dectobin(int(mam))
        z = "00000000" + im
        im1 = z[len(z) - 8:len(z)]
        print(E(op, im1))

    elif (y[0][-1] == ':' and y[1] == 'jmp'):
        op = getkey('jmp')
        mam = mem.get(y[2])
        im = dectobin(int(mam))
        z = "00000000" + im
        im1 = z[len(z) - 8:len(z)]
        print(E(op, im1))

    elif (y[0] == 'jlt'):
        op = getkey('jlt')
        mam = mem.get(y[1])
        im = dectobin(int(mam))
        z = "00000000" + im
        im1 = z[len(z) - 8:len(z)]
        print(E(op, im1))

    elif (y[0][-1] == ':' and y[1] == 'jlt'):
        op = getkey('jlt')
        mam = mem.get(y[2])
        im = dectobin(int(mam))
        z = "00000000" + im
        im1 = z[len(z) - 8:len(z)]
        print(E(op, im1))

    elif (y[0] == 'jgt'):
        op = getkey('jgt')
        mam = mem.get(y[1])
        im = dectobin(int(mam))
        z = "00000000" + im
        im1 = z[len(z) - 8:len(z)]
        print(E(op, im1))

    elif (y[0][-1] == ':' and y[1] == 'jgt'):
        op = getkey('jgt')
        mam = mem.get(y[2])
        im = dectobin(int(mam))
        z = "00000000" + im
        im1 = z[len(z) - 8:len(z)]
        print(E(op, im1))

    elif (y[0] == 'je'):
        op = getkey('je')
        mam = mem.get(y[1])
        im = dectobin(int(mam))
        z = "00000000" + im
        im1 = z[len(z) - 8:len(z)]
        print(E(op, im1))

    elif (y[0][-1] == ':' and y[1] == 'je'):
        op = getkey('je')
        mam = mem.get(y[2])
        im = dectobin(int(mam))
        z = "00000000" + im
        im1 = z[len(z) - 8:len(z)]
        print(E(op, im1))
    
    # elif (y[0]=="var"):
    #     if(len(y)!= 2):
    #         print("syntax error")    

def typo(y, opcode, reg, mem, k):
    # Label
    if y[0][-1] == ":":
        if y[1] not in opcode.values():
            print("Invalid Instruction on Line " + str(k+1))
            return True

        # Flags
        elif ("FLAGS" in y):
            if (len(y) == 4 and y[1] == 'mov' and y[2] in reg.keys()):
                return False

            else:
                print("Illegal Use of Flag on Line " + str(k + 1))
                return True

        # Type A Label
        elif (y[1] == 'and' or y[1] == 'or' or y[1] == 'add' or y[1] == 'sub' or y[1] == 'xor' or
                y[1] == 'mul'):
            if len(y) != 5:
                print("Syntax Error on Line " + str(k + 1))
                return True

            elif (len(y) == 5 and (y[2] not in reg.keys() or y[3] not in reg.keys() or y[4] not in reg.keys())):
                print("Invalid Register on Line " + str(k + 1))
                return True

            else:
                return False

        # Type B Label
        elif (y[1] == 'rs' or y[1] == 'ls'):
            if len(y) != 4:
                print("Syntax Error on Line " + str(k + 1))
                return True

            elif (y[2] not in reg.keys() or y[3][0] != "$"):
                print("Typo Error on Line " + str(k + 1))
                return True

            elif (int(y[3][1:len(y[3])]) > 255 or int(y[3][1:len(y[3])]) < 0):
                print("Illegal immediate value on Line " + str(k + 1))
                return True

            else:
                return False

        # mov Label
        elif (y[1] == 'mov'):
            if len(y) != 4:
                print("Syntax Error on Line " + str(k + 1))
                return True

            else:
                if y[3][0] == "$":
                    if y[2] not in reg.keys():
                        print("Invalid Register on Line " + str(k + 1))
                        return True

                    elif (int(y[3][1:len(y[3])]) > 255 or int(y[3][1:len(y[3])]) < 0):
                        print("Illegal immediate value on Line " + str(k + 1))
                        return True

                    else:
                        return False

                elif y[3] in reg.keys():
                    if y[2] not in reg.keys():
                        print("Invalid Register on Line " + str(k + 1))
                        return True

                    else:
                        return False

                else:
                    print("Typo Error on Line " + str(k + 1))
                    return True
        
        # Type C Label
        elif y[1] == 'not' or y[1] == 'cmp' or y[1] == 'div':
            if len(y) != 4:
                print("Syntax Error on Line " + str(k + 1))
                return True

            elif y[2] not in reg.keys() or y[3] not in reg.keys():
                print("Invalid Register on Line " + str(k + 1))
                return True

            else:
                return False

        #Type D Label
        elif y[1] == 'ld' or y[1] == 'st':
            if len(y) != 4:
                print("Syntax Error on Line " + str(k + 1))
                return True

            elif y[2] not in reg.keys() or y[3] not in mem.keys():
                print("Invalid Register on Line " + str(k + 1))
                return True

            else:
                return False

        #Type E Label
        elif y[1] == 'jmp' or y[1] == 'jlt' or y[1] == 'jgt' or y[1] == 'je':
            if len(y) != 3:
                print("Syntax Error on Line " + str(k + 1))
                return True
            
            elif y[2] not in mem.keys():
                print("Invalid Memory Address on Line " + str(k + 1))
                return True

            else:
                return False

        # Type F Label
        elif y[1] == "hlt":
            if len(y) != 2:
                print("hlt not Declared Correctly on Line " + str(k + 1))
                return True

            else:
                return False

    else:
        if y[0] not in opcode.values():
            if y[0] == "var":
                if len(y) == 2:
                    return False
                else:
                    print("Variable not Declarted Correctly on Line " + str(k + 1))
                    return True


        # Flags
        elif ("FLAGS" in y):
            if (len(y) == 3 and y[0] == 'mov' and y[1] in reg.keys()):
                return False

            else:
                print("Illegal Use of Flag on Line " + str(k + 1))
                return True

        # Type A
        elif (y[0] == 'and' or y[0] == 'or' or y[0] == 'add' or y[0] == 'sub' or y[0] == 'xor' or
                y[0] == 'mul'):
            if len(y) != 4:
                print("Syntax Error on Line " + str(k + 1))
                return True

            elif (len(y) == 4 and (y[1] not in reg.keys() or y[2] not in reg.keys() or y[3] not in reg.keys())):
                print("Invalid Register on Line " + str(k + 1))
                return True

            else:
                return False

        # Type B
        elif (y[0] == 'rs' or y[0] == 'ls'):
            if len(y) != 3:
                print("Syntax Error on Line " + str(k + 1))
                return True

            elif (y[1] not in reg.keys() or y[2][0] != "$"):
                print("Invalid Register on Line " + str(k + 1))
                return True

            elif (int(y[2][1:len(y[2])]) > 255 or int(y[2][1:len(y[2])]) < 0):
                print("Illegal immediate value on Line " + str(k + 1))
                return True

            else:
                return False

        # mov
        elif (y[0] == 'mov'):
            if len(y) != 3:
                print("Syntax Error on Line " + str(k + 1))
                return True

            else:
                if y[2][0] == "$":
                    if y[1] not in reg.keys(): 
                        print("Invalid Register on Line " + str(k + 1))
                        return True

                    elif (int(y[2][1:len(y[2])]) > 255 or int(y[2][1:len(y[2])]) < 0):
                        print("Illegal immediate value on Line " + str(k + 1))
                        return True

                    else:
                        return False

                elif y[2] in reg.keys():
                    if y[1] not in reg.keys():
                        print("Invalid Register on Line " + str(k + 1))
                        return True

                    else:
                        return False

                else:
                    print("Typo Error on Line " + str(k + 1))
                    return True

        # Type C
        elif y[0] == 'not' or y[0] == 'cmp' or y[0] == 'div':
            if len(y) != 3:
                print("Syntax Error on Line " + str(k + 1))
                return True

            elif y[1] not in reg.keys() or y[2] not in reg.keys():
                print("Invalid Register on Line " + str(k + 1))
                return True

            else:
                return False

        #Type D
        elif y[0] == 'ld' or y[0] == 'st':
            if len(y) != 3:
                print("Syntax Error on Line " + str(k + 1))
                return True

            elif y[1] not in reg.keys() or y[2] not in mem.keys():
                print("Typo Error on Line " + str(k + 1))
                return True

            else:
                return False

        #Type E
        elif y[0] == 'jmp' or y[0] == 'jlt' or y[0] == 'jgt' or y[0] == 'je':
            if len(y) != 2:
                print("Syntax Error on Line " + str(k + 1))
                return True
            
            elif y[1] not in mem.keys():
                print("Invalid Memory Address on Line " + str(k + 1))
                return True

            else:
                return False

        # Type F
        elif y[0] == "hlt":
            if len(y) != 1:
                print("hlt nor Declared correctly on Line " + str(k + 1))
                return True

            else:
                return False

def main(y, opcode, reg):
    a = 0
    b = 0
    mem = {}
    c = 0
    x = 0
    list1 = []
    for i in range(len(y)):
        if y[i][0] != 'var':
            c = i
            break
    for j in range(len(y)):
        if y[j][0] == "var":
            if len(y[j]) == 2:
                mem[y[j][1]] = len(y) - c + j
                list1.append(y[j][1])
            else:
                b = 1
                break

    for k in range(len(y)):
        if y[k][0][-1] == ":":
            mem[y[k][0][0:-1]] = k - c
            list1.append(y[k][0][0:-1])
            
    for i in range(c,len(y)):
        if y[i][0] == "var":
            a = 1
            print("Variable not declared at the beginning on Line " + str(i + 1))
            b = 1
            break

    for i in range(0,len(list1)):
        if list1.count(list1[i]) > 1:
            x = 1
            b = 1
            break       
    
    for k in range(0,len(y)):
        if(y[k][0] == 'hlt'):
            if (k != len(y) - 1):
                if a != 1:
                    b = 1
                    print("hlt not used as last instruction on Line " + str(k + 1))
                    break
                else:
                    b = 1
                    break
                
        if a == 1:
            b = 1
            break

        if len(y[-1]) == 2 and y[-1][0][-1] == ":" and y[-1][1] != 'hlt':
            b = 1
            print("Missing hlt instruction in the End")
            break

        if len(y[-1]) == 1 and y[-1][0] != 'hlt':
            b = 1
            print("Missing hlt instruction in the End")
            break

        if (typo(y[k], opcode, reg, mem,k)):
            b = 1
            break
        if x == 1:
            print("Misuse of variables as labels or vice versa on Line " + str(k + 1))
            b = 1
            break  
    
    if b == 0:
        for k in range(len(y)):    
            binaryconvert(y[k],opcode,reg,mem)
        
main(y, opcode, reg)
