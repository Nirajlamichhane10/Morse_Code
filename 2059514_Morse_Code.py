# Coding Challenge 2
# Name:Niraj Lamichhane
# Student No: 2059514
def intro():
    name=input("Please enter your name:")
    print("Welcome to Wolmorse,",name)
    print("This progarm encodes and Decodes Morse Code")

# A Morse code encoder/decoder

MORSE_CODE = (
    ("-...", "B"), (".-", "A"), ("-.-.", "C"), ("-..", "D"), (".", "E"), ("..-.", "F"), ("--.", "G"),
    ("....", "H"), ("..", "I"), (".---", "J"), ("-.-", "K"), (".-..", "L"), ("--", "M"), ("-.", "N"),
    ("---", "O"), (".--.", "P"), ("--.-", "Q"), (".-.", "R"), ("...", "S"), ("-", "T"), ("..-", "U"),
    ("...-", "V"), (".--", "W"), ("-..-", "X"), ("-.--", "Y"), ("--..", "Z"), (".-.-.-", "."),
    ("-----", "0"), (".----", "1"), ("..---", "2"), ("...--", "3"), ("....-", "4"), (".....", "5"), 
    ("-....", "6"), ("--...", "7"), ("---..", "8"), ("----.", "9"), ("-.--.", "("), ("-.--.-", ")"),
    (".-...", "&"), ("---...", ":"), ("-.-.-.", ";"), ("-...-", "="), (".-.-.", "+"), ("-....-", "-"),
    ("..--.-", "_"), (".-..-.", '"'), ("...-..-", "$"), (".--.-.", "@"), ("..--..", "?"), ("-.-.--", "!")
)
data=dict(MORSE_CODE)
key=list(data.keys())
value=list(data.values())
def main():
    intro()
    get_input()
def again():
    print("Would you like to run the program again?")
    d=input("Enter yes for (Y) or no for (N):").upper()
    if d=="Y":
        get_input()
    else:
        print("Thank You !!!!!  for using this program")
def get_input():
    a=input(" Now what would you like to do , Enter(D) to decode or Enter(E) to encode: ").upper()
    while a!="E" and a!="D":
        print("Your choice is invalid")
        a=input("Enter(D) to decode or Enter(E) to encode: ").upper()
    if a=="E":
        b=input("Would you like to read file(F) or console(C): ").upper()
        while b!="F" and b!="C":
            print("Invalid Choice")
            b=input("Would you like to read file(F) or console(C): ").upper()
        if b=="C":
            print(encode())
        else:
            encoding()        
    else:
        b=input("Would you like to read file(F) or console(C): ").upper()
        while b!="F" and b!="C":
            print("Invalid Choice")
            b=input("Would you like to read file(F) or console(C): ").upper()
        if b=="C":
            print(decode())
        else:
            file=input("insert a file to convert")
            print(decoding(file))
    again()        
def encode():
    text=input("Enter text to encode: ").upper()
    code=""
    for x in text:
        if x!=" ":
            code=code+key[value.index(x)]+" "
        else:
            code=code+"  "
    return code
def decode():
    z=input("Enter a text to decode: ").upper()+" "

    code=""
    word=""
    for x in z:
        if x!=" ":
            word=word+x
            i=0
        else:
            i=i+1
            if i==3:
                code=code+" "
            elif i==2:
                code=code+""
            else:
                code=code+value[key.index(word)]
                word=""
    return code
# Now File Handling :
def encoding():
    file = input("insert a file to convert")
    text=open(file,"r")
    e=text.readlines()
    f="".join(e)                        # This is used to convert list into string
    g=f.upper()
    code=""
    for x in g:
        if x!=" ":
            code=code+key[value.index(x)]+" "
        else:
            code+="  "
    h=open("output.txt","w")
    h.write(code)
    h.close()
    print("Your output is in output.txt")
def decoding(file):
    text=open(file,"r")
    j=text.readlines()
    k="".join(j)
    word=""
    code=""
    for x in k:
        if x!=" ":
            word=word+x
            i=0
        else:
            i=i+1
            if i==3:
                code=code+" "
            elif i==2:
                code=code+""
            else:
                code=code+value[key.index(word)]
                word=""
    return code
main()
                
    

    
