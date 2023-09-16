
import string 

def encode_rotation(plainText):
    shift = 25
    shift %= 26

    alphabet = string.ascii_lowercase 

    shiftedalphabet = alphabet [shift:] + alphabet [:shift]

    table = str.maketrans(alphabet,shiftedalphabet)

    encripted = plainText.translate(table)

    print(encripted) 

def decode_rotation_brut(cipher):
    # every letter as a numnber
    letter_dict= {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}    
    number_dict = {}
    for leter, num in letter_dict.items():
        number_dict[num] = leter
 
    for shift in range (-26, 27):
        result=""
        for letter in cipher:
            if ' '== letter:
                result=result + ' '
            else: 
                cypherNum=letter_dict[letter]
                cypherNum=cypherNum+shift 
                if cypherNum>26:
                    cypherNum=cypherNum-26
                elif cypherNum<1:
                    cypherNum=cypherNum+26

                result=result+ number_dict[cypherNum]  
        print(shift, " " , result)
    
cipher = 'nzyrclofwletzyd jzf qtrfcpo zfe esp njaspc'
decode_rotation_brut(cipher)
plainText = "code"
encode_rotation(plainText)