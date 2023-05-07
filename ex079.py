#79

def maiortamanho(s1,s2):

    if s1>s2:
        print(s1)
    elif s2>s1:
        print(s2)
    else:
        print(s1,s2)

string1 = str(input("Primeira string"))
string2 = str(input("Segunda string"))

maiortamanho(string1,string2)