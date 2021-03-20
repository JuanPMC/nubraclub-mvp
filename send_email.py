import smtplib, ssl


def send_email(message):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "nibra.dev@gmail.com"  # Enter your address
    receiver_email = "nibraclub@gmail.com"  # Enter receiver address
    password = "pasticontrasena-bananera"
    # message = """\
    # Subject: Hi there
    #
    # This message is sent from Python.
    # De nibra.dev a nibraclub."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    return 0
