Project Title: Secure Email Sender with smtplib

Description

This Python script facilitates sending emails using the smtplib library and TLS encryption for security. It provides a template to guide you through the configuration process.

Features

Sends emails from a Gmail account using SMTP.
Implements TLS encryption for secure communication.
Instructions

Prerequisites:

Python 3.x
Configuration:

Replace placeholders: Edit the code at the beginning of the script, replacing the following placeholders with your own details:
server: Replace with "smtp.gmail.com" (default for Gmail).
port: Replace with 587 (default port for TLS).
sender_email: Replace with your full Gmail address (including "@gmail.com").
password: Replace with your Gmail application-specific password (generated from your Google account settings for enhanced security).
recipient_email: Replace with the email address of the intended recipient.
message: Replace with the email body content you wish to send.
Usage:

Save the script as a Python file (e.g., email_sender.py).
Open a terminal or command prompt and navigate to the directory containing the script.
Run the script using python email_sender.py (replace with the actual script filename).
Success Message:

If the email is sent successfully, the script will print "Email sent successfully!

