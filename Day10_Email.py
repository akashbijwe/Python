import smtplib

host = "smtp.mail.yahoo.com"
port = 465
username = "akash_bijwe@yahoo.com"
password = "master482455"
from_email = username
to_list = ["mr.akashbijwe@gmail.com"]
message = "Hello there!"

email_conn = smtplib.SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username, password)
email_conn.sendmail(from_email, to_list, message)
email_conn.quit()


# OR this Method 

from smtplib import SMTP

host = "smtp.mail.yahoo.com"
port = 465
username = "akash_bijwe@yahoo.com"
password = "master482455"
from_email = username
to_list = ["mr.akashbijwe@gmail.com"]
message = "Hello there!"

email_conn = SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username, password)
email_conn.sendmail(from_email, to_list, message)
email_conn.quit()