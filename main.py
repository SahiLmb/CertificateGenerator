import os
from dotenv import load_dotenv
from PIL import Image, ImageFont, ImageDraw # Imaging library 
import smtplib # for sending mail
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import csv # to read csv file
from pathlib import Path

# Assigning global variables
FONT_FILE = ImageFont.truetype(r'font/Product Sans Regular.ttf',  100)
FONT_COLOR =  "#5F6368"

load_dotenv()
# access the environment variables with SMTP config
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
    send_email(email, 'Your [Event] Certificate is here!', f"Dear {name}, \n\nCongratulations on completing the [Event name] Your certificate is attached.\n\nBest regards,\n[your company]", certificate_path)
    print('Sending email to:', email)
    
# Function to read names and emails from a CSV file
def read_receiver_from_csv(csv_file):
    receiver = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            receiver.append((row['Name'], row['Email']))
    return receiver
    
    
if __name__ == "__main__":
    # receiver = [("Sahil", "sahilmb2022@gmail.com"), ("Tanmay", "email2@gmail.com")]
    # Load recipients from CSV file
    csv_file_path = Path('mail.csv')  # Update the file path as needed
    receiver = read_receiver_from_csv(csv_file_path)
    
    for name, email in receiver:
        generate_certificates(name, email)
        
    print(len(receiver), "certificates done")