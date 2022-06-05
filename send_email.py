import yagmail  # https://pypi.org/project/yagmail/


def sendEmail():

    receiver = "email@email.com"
    subject="Hello world"
    body = ["Dear world"]

    # Initializing yagmail.SMTP (params are email and pass for email)
    yag = yagmail.SMTP("email", "password")

    yag.send(to=receiver, subject=subject, contents=body,)


# Call to function
sendEmail() 
