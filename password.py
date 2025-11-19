def passage(email, password):
    evalidation=False
    pvalidation=False
    if "@" not in email:
        return "INVALID. Retry Email with @ Symbol"
    if type(email) !=str or type(password)!=str:
        return "INVALID. Email and Password Must be Strings"
    if len(password)<8:
        return "INVALID. Password Must be AT LEAST 8 Characters Long"
    for i in password:
        if i.isdigit():
            number=True
        if i.isupper():
            capital=True
print(passage("bi@", "big8"))