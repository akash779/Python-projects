import smtplib 

# Replace placeholders with your details
server = "smtp.gmail.com"
port = 587  # For TLS encryption
sender_email = "example@gmail.com   "
password = "password"
recipient_email = "reciver_Email_address"
message = "This is a test email sent with smtplib."

with smtplib.SMTP(server, port) as connection:
  connection.starttls()  # Start TLS for secure communication
  connection.login(sender_email, password)
  connection.sendmail(sender_email, recipient_email, message)

print("Email sent successfully!")
