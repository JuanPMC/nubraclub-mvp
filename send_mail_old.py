import yagmail


def send_yag():
    receiver = "nibraclub@gmail.com"
    sender = "nibra.dev@gmail.com"
    subject = "Yagmail test without attachment"
    body = "Hello there from Yagmail"
    # filename = "document.pdf"

    yag = yagmail.SMTP(sender)
    yag.send(
        to=receiver,
        subject=subject,
        contents=body,
        # attachments=filename,
    )
    return 0