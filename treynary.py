from PIL import Image
import os
abc = "abcdefghijklmnopqrstvwuyxz1234567890 @."
cipher = {}
number = 0
number1 = 0
number2 = 0
number3 = 0
number4 = 0
for i in abc:
    number += 1
    if number > 2:
        number = 0
        number1 += 1
    if number1 > 2:
        number2 += 1
        number1 = 0
    if number2 > 2:
        number2 = 0
        number3 += 1
    cipher[i] = str(number3)+str(number2)+str(number1)+str(number)
def cypher(user_input):
    lit = []
    for i in user_input:
        lit.append(cipher[i])
    count = 0
    count1 = 0
    img =  Image.open(os.path.dirname(os.path.realpath(__file__))+"\\"+input("Name of image to be used: "))
    pix = img.load()
    for i in lit:
        for x in i:
            if x == "0":
                print("red")
                pix[count,count1] = (225,0,0,225)
            elif x == "1":
                print("green")
                pix[count,count1] = (0,225,0,225)
            elif x == "2":
                print("yellow")
                pix[count,count1] = (225,225,0,)
            count1 += 1
        count += 1
        count1 = 0
    img.save(os.getcwd()+"\\"+"code2.png")

def decypher():
    string = ""
    listr = []
    stringr = ""
    breaker = False
    code = Image.open(os.path.dirname(os.path.realpath(__file__))+"\\"+input("Name of image to be used: "))
    xip = code.load()
    for x in range(code.size[1]):
            for y in range(4):
                print(xip[x,y])
                if xip[x,y] == (225, 0, 0):
                     stringr = stringr + "0"
                elif xip[x,y] == (0, 225, 0):
                    stringr = stringr + "1"
                elif xip[x,y] == (225, 225, 0):
                    stringr = stringr + "2"
            listr.append(stringr)
            stringr = ""
    for e in listr:
        for z,y in cipher.items():
            if y == e:
               string = string + z
    print(string)

usr_in = input("Encrypt(a) or decrypt(b)?: ")
if usr_in == "a":
    cypher(input("And what is your message?: "))
elif usr_in == "b":
    decypher()
else:
    print("that was not a valid response")
