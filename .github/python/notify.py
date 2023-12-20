from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import argparse

to = ["21522005@student.uwl.ac.uk"]

parser = argparse.ArgumentParser(
    description=f"Send an automatic GitHub email that there is a website update")
parser.add_argument("-host", type=str, help="Enter the SMTP host")
parser.add_argument("-port", type=int, help="Enter the SMTP port")
parser.add_argument("-username", type=str,
                    help="Enter the SMTP login username")
parser.add_argument("-password", type=str,
                    help="Enter the SMTP login password")

args = parser.parse_args()

message = MIMEMultipart()
message["From"] = "ATAL Society <ataluwl@gmail.com>"
message["To"] = "; ".join(to)
message["Subject"] = f"Film Society"


html = """
    <div class="header">
        <h1>FilmSoc Update</h1>
    </div>
    <div class="content">
        <p>Hello UWL Film Society,</p>
        <p>Your <a href="https://film-uwl.github.io" rel="noopener">website</a> has been updated.
        </p>

        <p>Best Regards,</p>
        <p>ATAL Society</p>
    </div>
"""

message.attach(MIMEText(html, "html"))

server = smtplib.SMTP_SSL(host=args.host, port=args.port)
print(args)
server.login(args.username, args.password)

server.sendmail(message["From"], to, message.as_string())
