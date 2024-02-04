import os
from dotenv import load_dotenv
from PIL import Image, ImageFont, ImageDraw # Imaging library 
import smtplib # for sending mail
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import pandas # to read csv file

# Assigning global variables
FONT_FILE = ImageFont.truetype(r'font/SwanseaBoldItalic-p3Dv.ttf',  100)
FONT_COLOR =  "#000000"

load_dotenv()
# access the environment variables
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = os.getenv('SMTP_PORT')
SMTP_USERNAME = os.getenv('SMTP_USERNAME')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')

def send_email(to_email, subject, body, attachment_path):
  # Creating MIME object
  msg = MIMEMultipart()
  msg['From'] = SMTP_USERNAME
  msg['To'] = to_email # receiver
  msg['Subject'] = subject 
  
  # Attach body
  msg.attach(MIMEText(body, 'plain'))
  
  # Attaching Certificate
  with open(attachment_path, 'rb') as attachment:
      attachment_part = MIMEBase('application', 'octet-stream')
      attachment_part.set_payload(attachment.read())
      encoders.encode_base64(attachment_part)
      attachment_part.add_header('Content-Disposition', f'attachment; filename={attachment_path}')
      msg.attach(attachment_part)
      
      # Connecting to the SMTP server and sending email
      server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
      server.starttls()
      server.login(SMTP_USERNAME, SMTP_PASSWORD)
      server.sendmail(SMTP_USERNAME, to_email, msg.as_string())


template = Image.open(r'CERT 1.png')
WIDTH, HEIGHT = template.size

# Name Placing on the certificate
def generate_certificates(name, email):
    
    # to save as a .png file
    image_source = Image.open(r'CERT 1.png')
    draw = ImageDraw.Draw(image_source)
    name_width, name_height = draw.textsize(name, font=FONT_FILE)
    
    # ((WIDTH - name_width)/2, (HEIGHT - name_height)/2 - 50): These are the coordinates where the text will be drawn. 
    # The (WIDTH - name_width)/2 calculates the horizontal position, centering the text on the X-axis,
    # and (HEIGHT - name_height)/2 - 30 calculates the vertical position, 
    # centering the text on the Y-axis with an additional offset of 50 pixels towards the top.
    draw.text(((WIDTH - name_width)/2, (HEIGHT - name_height)/2 + 30), name, fill=FONT_COLOR, font=FONT_FILE)
   
   # Saving certificates in a different directory
    certificate_path = "./out/" + name + ".png" 
    image_source.save(certificate_path)
    print('Saving Certificate of:', name)
    
    # Send email
    send_email(email, 'Certificate', 'Congratulations! Your certificate is attached below.', certificate_path)
    print('Sending email to:', email)
    
if __name__ == "__main__":
    names_and_emails = [("Sahil Bodke", "sahilmb2022@gmail.com"), ("Tanmay", "bodkesahil26@gmail.com")]
    for name, email in names_and_emails:
        generate_certificates(name, email)
        print(len(names_and_emails), "certificates done")