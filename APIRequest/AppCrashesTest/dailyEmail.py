import smtplib
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("msmfathih40@gmailcom", "your_password")
server.sendmail("your_email@gmail.com", "receiver@gmail.com", "Hello from Python!")
server.quit()