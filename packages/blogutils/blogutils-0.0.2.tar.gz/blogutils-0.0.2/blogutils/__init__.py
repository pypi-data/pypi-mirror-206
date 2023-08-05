import datetime
import re
import smtplib
import markdown


def read_file(filename):
    with open(filename, 'r') as f:
        contents = f.read()
    return contents

def write_file(filename, contents):
    with open(filename, 'w') as f:
        f.write(contents)

def generate_slug(title):
    slug = re.sub(r'\W+', '-', title.lower())
    return slug

def get_datetime():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def send_email(to, subject, body):
    from_address = 'your-email-address'
    password = 'your-email-password'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_address, password)
    message = f'Subject: {subject}\n\n{body}'
    server.sendmail(from_address, to, message)
    server.quit()
    
def create_post(title, author, tags):
    now = get_datetime()
    slug = generate_slug(title)
    filename = f"{slug}.md"
    content = f"""---
TITLE:- {title},
Written by {author} on {now}.
Tagged with {tags}.
---

Write your post here.
"""
    html_content = markdown.markdown(content)

    write_file(filename, html_content)
    return filename


