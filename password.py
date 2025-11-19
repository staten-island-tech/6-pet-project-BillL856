def passage(email, password):
    evalidation=False
    pvalidation=False
    if "@" not in email:
        return "INVALID. Retry Email"
    elif "@" in email:
        evalidation=True
    for i in password:
        if password(i) is i.upper():
            capital=True
        elif password(i) is i.digit():
            number=True
    if len(password)>=8 and capital==True and number==True:
        pvalidation=True
