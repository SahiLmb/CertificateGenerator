<p align="center">
  <b>Certificate Generator</b>
</p> 
<p align="center"> A mass certificate generator with direct email functionality python script </p>
<p align="center">
  <br>
  <a href="main.py">Source Code</a> &nbsp; · &nbsp; 
   <a href="#docs">Docs</a> &nbsp; · &nbsp;
   <br>

   ### Docs

All you need

1. Certificate
  - Design a [simple template](template.png) on [Canva](https://www.canva.com/)
2. Font
  - A .ttf (True-Type Font) file like [this](/font), can simply be downloaded from [here](https://www.google.com/search?q=download+.ttf+fonts).
3. Names
  - Finally, a list of names in a .txt format or a .csv format.

### Import Necessary modules
```python
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
```
Using the [pillow module](https://pypi.org/project/Pillow/) to make changes.
<br>
- Calculating and declaring default values.
```python
from PIL import Image, ImageFont, ImageDraw

'''Global Variables'''
FONT_FILE = ImageFont.truetype(r'font/GreatVibes-Regular.ttf', 180)
FONT_COLOR = "#FFFFFF"

template = Image.open(r'template.png')
WIDTH, HEIGHT = template.size
```
<br>

- Loading environment variables set in .env file
```python
load_dotenv()
# access the environment variables 
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = os.getenv('SMTP_PORT')
SMTP_USERNAME = os.getenv('SMTP_USERNAME')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
```

<br>

- Creating [MIME](https://en.wikipedia.org/wiki/MIME#:~:text=Multipurpose%20Internet%20Mail%20Extensions%20MIME,%2C%20images%2C%20and%20application%20programs.) object
```python
def send_email(to_email, subject, body, attachment_path):
  # Creating MIME object
  msg = MIMEMultipart()
  msg['From'] = SMTP_USERNAME
  msg['To'] = to_email # receiver
  msg['Subject'] = subject 
  
  # Attach body
  msg.attach(MIMEText(body, 'plain'))
```
<br>

- Attaching certificate
```python
 with open(attachment_path, 'rb') as attachment:
      attachment_part = MIMEBase('application', 'octet-stream')
      attachment_part.set_payload(attachment.read())
      encoders.encode_base64(attachment_part)
      attachment_part.add_header('Content-Disposition', f'attachment; filename={attachment_path}')
      msg.attach(attachment_part)
```
<br>

- Connecting the script to [SMTP](https://www.geeksforgeeks.org/simple-mail-transfer-protocol-smtp/) server to send the mail
```python
 server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
      server.starttls()
      server.login(SMTP_USERNAME, SMTP_PASSWORD)
      server.sendmail(SMTP_USERNAME, to_email, msg.as_string())
```
<br>

- Placing the name on the certificate
```python
template = Image.open(r'CERT 1.png')
WIDTH, HEIGHT = template.size

def generate_certificates(name, email):
```
<br>

- Saving the certificate in .png file
```python
image_source = Image.open(r'CERT 1.png') 
    draw = ImageDraw.Draw(image_source)
    name_width, name_height = draw.textsize(name, font=FONT_FILE)
```
<br>

- Adjusting the name to be in the middle of certificate
```python
'''((WIDTH - name_width)/2, (HEIGHT - name_height)/2 - 50): These are the coordinates where
the text will be drawn. The (WIDTH - name_width)/2 calculates the horizontal position,centering
the text on the X-axis, and (HEIGHT - name_height)/2 - 30 calculates the vertical position,
centering the text on the Y-axis with an additional offset of 50 pixels towards the top.'''

draw.text(((WIDTH - name_width)/2, (HEIGHT - name_height)/2 + 30), name, fill=FONT_COLOR, font=FONT_FILE)
```
<br>

- Saving certficates in a different directory
```python
certificate_path = "./out/" + name + ".png" 
    image_source.save(certificate_path)
    print('Saving Certificate of:', name)
```
<br>

- Function to read names and emails from a [CSV](/mail.csv) file
```python
def read_receiver_from_csv(csv_file):
    receiver = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            receiver.append((row['Name'], row['Email']))
    return receiver
```
<br>

- Loading recipients from [csv](/mail.csv) file
```python
if __name__ == "__main__":
    # receiver = [("Sahil", "sahilmb2022@gmail.com"), ("Tanmay", "email2@gmail.com")]
    # Load recipients from CSV file
    csv_file_path = Path('mail.csv')  # Update the file path as needed
    receiver = read_receiver_from_csv(csv_file_path)
    
    for name, email in receiver:
        generate_certificates(name, email)
        
    print(len(receiver), "certificates done")
```
