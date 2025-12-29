import smtplib

my_email = "khushboodubey000@gmail.com"
password = "kd592006"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="dd279761@gmail.com",
        msg="Subject: massachussets...✌️\n\nThis is the body of my email."
        )

# connection.close() 
