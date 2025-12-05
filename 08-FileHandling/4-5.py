import re

file_name = 'email.txt'

with open(file_name, 'r') as file:
    email = file.read()

# regular expression pattern
# for amounts
pattern_sender = 'From:\s\w+\s\w+\s<(.+)>'
pattern_recipient = 'To:\s\w+\s\w+\s<(.+)>'
pattern_subject = 'Subject:\s(.+)'

# extract numbers from email
# tip: findall() method returns an array
email_sender = re.findall(pattern_sender, email)
email_recipient = re.findall(pattern_recipient, email)
email_subject = re.findall(pattern_subject, email)
# email_body = re.findall(pattern_body, email)

print(email_sender, email_recipient, email_subject)