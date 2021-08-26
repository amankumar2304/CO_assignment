import matplotlib.pyplot as plt
import sys
x = sys.stdin.read().splitlines()

bonus = {}
cycle = 0
bonus_extra = {}
mem = []
for k in x:
    mem.append(k)

for j in range(len(mem), 256):
    mem.append("0000000000000000")

# opcode Table
opcode = {"00000": "add", "00001": "sub", "00010": "mov", "00011": "mov", "00100": "ld", "00101": "st", "00110": "mul",
          "00111": "div", "01000": "rs", "01001": "ls", "01010": "xor", "01011": "or", "01100": "and", "01101": "not",
          "01110": "cmp", "01111": "jmp", "10000": "jlt", "10001": "jgt", "10010": "je", "10011": "hlt"}

# Registers
reg = {"1": "000", "2": "001", "3": "010", "4": "011", "5": "100", "6": "101", "7": "110", "8": "111", }


def getkey(val):
    for key, value in reg.items():
        if val == value:
            return key


def dectobin(n):
    return bin(n).replace("0b", "")


def bininvert(n):
    s = ""
    for i in n:
        if i == '0':
            s += '1'
        elif i == '1':
            s += '0'
    return s


def bintodict(n):
    return int(n, 2)


list1 = ['00000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000',
         '0000000000000000', '0000000000000000', '0000000000000000']

i = 0

while(i < len(x)):
    c = x[i][0:5]
    bonus[cycle] = i
    #add
    if (c == '00000'):
        list1[-1] = '0000000000000000'
        p = x[i][7:10]
        q = x[i][10:13]
        r = x[i][13:16]
        p = int(getkey(p))
        q = int(getkey(q))
        r = int(getkey(r))
        p1 = bintodict(list1[p])
        q1 = bintodict(list1[q])
        r1 = bintodict(list1[r])
        p1 = q1 + r1
        if p1 > (2 ** 16 - 1):
            p1 = 65535
            list1[-1] = '0000000000001000'
        p1 = dectobin(p1)
        p1 = '0000000000000000' + p1
        im = p1[len(p1) - 16:len(p1)]
        list1[p] = im
        print(
            list1[0] + " " + list1[1] + " " + list1[2] + " " + list1[3] + " " + list1[4] + " " + list1[5] + " " + list1[
                6] + " " + list1[7] + " " + list1[8])

        a = bintodict(list1[0])
        a += 1
        a = dectobin(a)
        a = "00000000" + a
        im1 = a[len(a) - 8:len(a)]
        list1[0] = im1
        i += 1

    # sub
    if (c == '00001'):
        list1[-1] = '0000000000000000'
        p = x[i][7:10]
        q = x[i][10:13]
        r = x[i][13:16]
        p = int(getkey(p))
        q = int(getkey(q))
        r = int(getkey(r))
        p1 = bintodict(list1[p])
        q1 = bintodict(list1[q])
        r1 = bintodict(list1[r])
        if (r1 > q1):
            p1 = 0
            list1[-1] = '0000000000001000'
        else:
            p1 = q1 - r1
        p1 = dectobin(p1)
        p1 = '0000000000000000' + p1
        im = p1[len(p1) - 16:len(p1)]
        list1[p] = im
        print(
            list1[0] + " " + list1[1] + " " + list1[2] + " " + list1[3] + " " + list1[4] + " " + list1[5] + " " + list1[
                6] + " " + list1[7] + " " + list1[8])
        a = bintodict(list1[0])
        a += 1
        a = dectobin(a)
        a = "00000000" + a
        im1 = a[len(a) - 8:len(a)]
        list1[0] = im1
        i += 1

    # mul
    if (c == '00110'):
        list1[-1] = '0000000000000000'
        p = x[i][7:10]
        q = x[i][10:13]
        r = x[i][13:16]
        p = int(getkey(p))
        q = int(getkey(q))
        r = int(getkey(r))
        p1 = bintodict(list1[p])
        q1 = bintodict(list1[q])
        r1 = bintodict(list1[r])
        p1 = q1 * r1
        if p1 > (2 ** 16 - 1):
            p1 = 65535
            list1[-1] = '0000000000001000'
        p1 = dectobin(p1)
        p1 = '0000000000000000' + p1
        im = p1[len(p1) - 16:len(p1)]
        list1[p] = im
        print(
            list1[0] + " " + list1[1] + " " + list1[2] + " " + list1[3] + " " + list1[4] + " " + list1[5] + " " + list1[
                6] + " " + list1[7] + " " + list1[8])
        a = bintodict(list1[0])
        a += 1
        a = dectobin(a)
        a = "00000000" + a
        im1 = a[len(a) - 8:len(a)]
        list1[0] = im1
        i += 1

    # xor
    if (c == '01010'):
        list1[-1] = '0000000000000000'
        p = x[i][7:10]
        q = x[i][10:13]
        r = x[i][13:16]
        p = int(getkey(p))
        q = int(getkey(q))
        r = int(getkey(r))
        p1 = bintodict(list1[p])
        q1 = bintodict(list1[q])
        r1 = bintodict(list1[r])
        p1 = q1 ^ r1
        p1 = dectobin(p1)
        p1 = '0000000000000000' + p1
        im = p1[len(p1) - 16:len(p1)]
        list1[p] = im
        print(
            list1[0] + " " + list1[1] + " " + list1[2] + " " + list1[3] + " " + list1[4] + " " + list1[5] + " " + list1[
                6] + " " + list1[7] + " " + list1[8])
        a = bintodict(list1[0])
        a += 1
        a = dectobin(a)
        a = "00000000" + a
        im1 = a[len(a) - 8:len(a)]
        list1[0] = im1
        i += 1

    # or
    if (c == '01011'):
        list1[-1] = '0000000000000000'
        p = x[i][7:10]
        q = x[i][10:13]
        r = x[i][13:16]
        p = int(getkey(p))
        q = int(getkey(q))
        r = int(getkey(r))
        p1 = bintodict(list1[p])
        q1 = bintodict(list1[q])
        r1 = bintodict(list1[r])
        p1 = q1 | r1
        p1 = dectobin(p1)
        p1 = '0000000000000000' + p1
        im = p1[len(p1) - 16:len(p1)]
        list1[p] = im
        print(
            list1[0] + " " + list1[1] + " " + list1[2] + " " + list1[3] + " " + list1[4] + " " + list1[5] + " " + list1[
                6] + " " + list1[7] + " " + list1[8])
        a = bintodict(list1[0])
        a += 1
        a = dectobin(a)
        a = "00000000" + a
        im1 = a[len(a) - 8:len(a)]
        list1[0] = im1
        i += 1

    # and
    if (c == '01100'):
        list1[-1] = '0000000000000000'
        p = x[i][7:10]
        q = x[i][10:13]
        r = x[i][13:16]
        p = int(getkey(p))
        q = int(getkey(q))
        r = int(getkey(r))
        p1 = bintodict(list1[p])
        q1 = bintodict(list1[q])
        r1 = bintodict(list1[r])
        p1 = q1 & r1
        p1 = dectobin(p1)
        p1 = '0000000000000000' + p1
        im = p1[len(p1) - 16:len(p1)]
        list1[p] = im
        print(
            list1[0] + " " + list1[1] + " " + list1[2] + " " + list1[3] + " " + list1[4] + " " + list1[5] + " " + list1[
                6] + " " + list1[7] + " " + list1[8])
        a = bintodict(list1[0])
        a += 1
        a = dectobin(a)
        a = "00000000" + a
        im1 = a[len(a) - 8:len(a)]
        list1[0] = im1
        i += 1

    # mov imm
    if (c == "00010"):
        list1[-1] = '0000000000000000'
        p = x[i][5:8]
        p = int(getkey(p))
        list1[p] = x[i][8:16]
        list1[p] = '00000000' + list1[p]
        print(list1[0] + " " + list1[1] + " " + list1[2] + " " + list1[3] + " " + list1[4] + " " + list1[5] + " " +
              list1[6] + " " + list1[7] + " " + list1[8])
        a = bintodict(list1[0])
        a += 1
        a = dectobin(a)
        a = "00000000" + a
        im1 = a[len(a) - 8:len(a)]
        list1[0] = im1
        i += 1

    # rs
    if (c == "01000"):
        list1[-1] = '0000000000000000'
        p = x[i][5:8]
        p = int(getkey(p))
        p1 = bintodict(list1[p])
        r1 = bintodict(x[i][8:16])
        a = p1 >> r1
        a = dectobin(a)
        a = '0000000000000000' + a
        im = a[len(a) - 16:len(a)]
        list1[p] = im
        print(list1[0] + " " + list1[1] + " " + list1[2] + " " + list1[3] + " " + list1[4] + " " + list1[5] + " " +
              list1[6] + " " + list1[7] + " " + list1[8])
        a = bintodict(list1[0])
        a += 1
        a = dectobin(a)
        a = "00000000" + a
        im1 = a[len(a) - 8:len(a)]
        list1[0] = im1
        i += 1

    # ls
    if (c == "01001"):
        list1[-1] = '0000000000000000'
        p = x[i][5:8]
        p = int(getkey(p))
        p1 = bintodict(list1[p])
        r1 = bintodict(x[i][8:16])
        a = p1 << r1
        a = dectobin(a)
        a = '0000000000000000' + a
        im = a[len(a) - 16:len(a)]
        list1[p] = im
        print(list1[0] + " " + list1[1] + " " + list1[2] + " " + list1[3] + " " + list1[4] + " " + list1[5] + " " +
              list1[6] + " " + list1[7] + " " + list1[8])
        a = bintodict(list1[0])
        a += 1
        a = dectobin(a)
        a = "00000000" + a
        im1 = a[len(a) - 8:len(a)]
        list1[0] = im1
        i += 1

    # mov reg
    if (c == '00011'):
        if (x[i][13:16] != '111'):
            list1[-1] = '0000000000000000'
        p = x[i][10:13]
        q = x[i][13:16]
        p1 = int(getkey(p))
        q1 = int(getkey(q))
        list1[p1] = list1[q1]
        if (x[i][13:16] == '111'):
            list1[-1] = '0000000000000000'
        print(
            list1[0] + " " + list1[1] + " " + list1[2] + " " + list1[3] + " " + list1[4] + " " + list1[5] + " " + list1[
                6] + " " + list1[7] + " " + list1[8])
        a = bintodict(list1[0])
        a += 1
        a = dectobin(a)
        a = "00000000" + a
        im1 = a[len(a) - 8:len(a)]
        list1[0] = im1
        i += 1

    # div
    if (c == '00111'):
        list1[-1] = '0000000000000000'
        p = x[i][10:13]
        q = x[i][13:16]
        p1 = int(getkey(p))
        q1 = int(getkey(q))
        p2 = bintodict(list1[p1])
        q2 = bintodict(list1[q1])
        r = p2 // q2
        y = p2 % q2
        r = dectobin(r)
        y = dectobin(y)
        y = "0000000000000000" + y
        im = y[len(y) - 16:len(y)]
        list1[2] = im
        r = "0000000000000000" + r
        im2 = r[len(r) - 16:len(r)]
        list1[1] = im2
        print(
            list1[0] + " " + list1[1] + " " + list1[2] + " " + list1[3] + " " + list1[4] + " " + list1[5] + " " + list1[
                6] + " " + list1[7] + " " + list1[8])
        a = bintodict(list1[0])
        a += 1
        a = dectobin(a)
        a = "00000000" + a
        im1 = a[len(a) - 8:len(a)]
        list1[0] = im1
        i += 1

    # not
    if (c == '01101'):
        list1[-1] = '0000000000000000'
        p = x[i][10:13]
        q = x[i][13:16]
        p1 = int(getkey(p))
        q1 = int(getkey(q))
        q2 = bininvert(list1[q1])
        list1[p1] = q2
        print(
            list1[0] + " " + list1[1] + " " + list1[2] + " " + list1[3] + " " + list1[4] + " " + list1[5] + " " + list1[
                6] + " " + list1[7] + " " + list1[8])
        a = bintodict(list1[0])
        a += 1
        a = dectobin(a)
        a = "00000000" + a
        im1 = a[len(a) - 8:len(a)]
        list1[0] = im1
        i += 1

    # cmp
    if (c == '01110'):
        list1[-1] = '0000000000000000'
        p = x[i][10:13]
        q = x[i][13:16]
        p1 = int(getkey(p))
        q1 = int(getkey(q))
        p2 = bintodict(list1[p1])
        q2 = bintodict(list1[q1])
        if (p2 > q2):
            list1[-1] = '0000000000000010'
        elif (p2 < q2):
            list1[-1] = '0000000000000100'
        elif (p2 == q2):
            list1[-1] = '0000000000000001'
        print(
            list1[0] + " " + list1[1] + " " + list1[2] + " " + list1[3] + " " + list1[4] + " " + list1[5] + " " + list1[
                6] + " " + list1[7] + " " + list1[8])
        a = bintodict(list1[0])
        a += 1
        a = dectobin(a)
        a = "00000000" + a
        im1 = a[len(a) - 8:len(a)]
        list1[0] = im1
        i += 1

    # st
    if (c == '00101'):
        list1[-1] = '0000000000000000'
        p = x[i][5:8]
        q = x[i][8:16]
        q1 = bintodict(q)
        p1 = int(getkey(p))
        mem[q1] = list1[p1]
        print(list1[0] + " " + list1[1] + " " + list1[2] + " " + list1[3] + " " + list1[4] + " " + list1[5] + " " +
              list1[6] + " " + list1[7] + " " + list1[8])
        a = bintodict(list1[0])
        a += 1
        a = dectobin(a)
        a = "00000000" + a
        im1 = a[len(a) - 8:len(a)]
        list1[0] = im1
        bonus_extra[cycle] = i
        i += 1

    # ld
    if (c == '00100'):
        list1[-1] = '0000000000000000'
        p = x[i][8:16]
        p1 = bintodict(p)
        q = x[i][5:8]
        q1 = int(getkey(q))
        list1[q1] = mem[p1]
        print(list1[0] + " " + list1[1] + " " + list1[2] + " " + list1[3] + " " + list1[4] + " " + list1[5] + " " +
              list1[6] + " " + list1[7] + " " + list1[8])
        a = bintodict(list1[0])
        a += 1
        a = dectobin(a)
        a = "00000000" + a
        im1 = a[len(a) - 8:len(a)]
        list1[0] = im1
        bonus_extra[cycle] = i
        i += 1

    # jmp
    if (c == '01111'):
        list1[-1] = '0000000000000000'
        print(list1[0] + " " + list1[1] + " " + list1[2] + " " + list1[3] + " " + list1[4] + " " + list1[
                5] + " " +
                  list1[6] + " " + list1[7] + " " + list1[8])
        p = x[i][8:16]
        p1 = bintodict(p)
        p2 = p1
        p2 = dectobin(p1)
        p2 = "00000000" + p2
        im5 = p2[len(p2) - 8:len(p2)]
        list1[0] = im5
        bonus_extra[cycle] = i
        i = p1
        bonus_extra[cycle] = i
        cycle = cycle + 1

    # jlt
    if c == '10000':
        if list1[-1] == '0000000000000100':
            list1[-1] = '0000000000000000'
            print(list1[0] + " " + list1[1] + " " + list1[2] + " " + list1[3] + " " + list1[4] + " " + list1[
                5] + " " +
                  list1[6] + " " + list1[7] + " " + list1[8])
            p = x[i][8:16]
            p1 = bintodict(p)
            p2 = p1
            p2 = dectobin(p1)
            p2 = "00000000" + p2
            im5 = p2[len(p2) - 8:len(p2)]
            list1[0] = im5
            bonus_extra[cycle] = i
            i = p1
            bonus_extra[cycle] = i
            cycle = cycle + 1
        else:
            list1[-1] = '0000000000000000'
            print(list1[0] + " " + list1[1] + " " + list1[2] + " " + list1[3] + " " + list1[4] + " " + list1[
                5] + " " +
                  list1[6] + " " + list1[7] + " " + list1[8])
            a = bintodict(list1[0])
            a += 1
            a = dectobin(a)
            a = "00000000" + a
            im1 = a[len(a) - 8:len(a)]
            list1[0] = im1
            i += 1

    # jgt
    if c == '10001':
        if list1[-1] == '0000000000000010':
            list1[-1] = '0000000000000000'
            print(list1[0] + " " + list1[1] + " " + list1[2] + " " + list1[3] + " " + list1[4] + " " + list1[
                5] + " " +
                  list1[6] + " " + list1[7] + " " + list1[8])
            p = x[i][8:16]
            p1 = bintodict(p)
            p2 = p1
            p2 = dectobin(p1)
            p2 = "00000000" + p2
            im5 = p2[len(p2) - 8:len(p2)]
            list1[0] = im5
            bonus_extra[cycle] = i
            i = p1
            bonus_extra[cycle] = i
            cycle = cycle + 1
        else:
            list1[-1] = '0000000000000000'
            print(list1[0] + " " + list1[1] + " " + list1[2] + " " + list1[3] + " " + list1[4] + " " + list1[
                5] + " " +
                  list1[6] + " " + list1[7] + " " + list1[8])
            a = bintodict(list1[0])
            a += 1
            a = dectobin(a)
            a = "00000000" + a
            im1 = a[len(a) - 8:len(a)]
            list1[0] = im1
            i += 1

    # je
    if c == '10010':
        if list1[-1] == '0000000000000001':
            list1[-1] = '0000000000000000'
            print(list1[0] + " " + list1[1] + " " + list1[2] + " " + list1[3] + " " + list1[4] + " " + list1[
                5] + " " +
                  list1[6] + " " + list1[7] + " " + list1[8])
            p = x[i][8:16]
            p1 = bintodict(p)
            p2 = p1
            p2 = dectobin(p1)
            p2 = "00000000" + p2
            im5 = p2[len(p2) - 8:len(p2)]
            list1[0] = im5
            bonus_extra[cycle] = i
            i = p1
            bonus_extra[cycle] = i
            cycle = cycle + 1

        else:
            list1[-1] = '0000000000000000'
            print(list1[0] + " " + list1[1] + " " + list1[2] + " " + list1[3] + " " + list1[4] + " " + list1[
                5] + " " +
                  list1[6] + " " + list1[7] + " " + list1[8])
            a = bintodict(list1[0])
            a += 1
            a = dectobin(a)
            a = "00000000" + a
            im1 = a[len(a) - 8:len(a)]
            list1[0] = im1
            i += 1

    if c == '10011':
        print(
            list1[0] + " " + list1[1] + " " + list1[2] + " " + list1[3] + " " + list1[4] + " " + list1[5] + " " + list1[
                6] + " " + list1[7] + " " + list1[8])
        break
    cycle = cycle + 1

for i in mem:
    print(i)


for k in bonus.keys():
    x = k
    y = bonus[k]
    plt.scatter(x,y,color = 'b')
    for j in bonus_extra.keys():
        if j == k:
            q = bonus_extra[j]
            plt.scatter(x,q,color = 'b')
plt.show()