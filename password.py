e=input("Email")
p=input("Password")
def passage(email, password):
    if "@" not in e:
        return "INVALID. Retry Email with @ Symbol"
    if type(e) !=str or type(p)!=str:
        return "INVALID. Email and Password Must be Strings"
    if len(p)<8:
        return "INVALID. Password Must be AT LEAST 8 Characters Long"
    for i in p():
        if i.isdigit():
            number=True
        if i.isupper():
            capital=True
    if "@" in e and type(e)==str:
        print("Valid Email")
    if type(p)==str and number==True and capital==True and len(p)>=8:
        print("Valid Password")
passage(e, p)