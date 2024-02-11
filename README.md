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

- Certificate
  - Design a [simple template](template.png) on [Canva](https://www.canva.com/)
- Font
  - A .ttf (True-Type Font) file like [this](/font), can simply be downloaded from [here](https://www.google.com/search?q=download+.ttf+fonts).
- Names
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

- Creating [MIME](https://en.wikipedia.org/wiki/MIME#:~:text=Multipurpose%20Internet%20Mail%20Extensions%20(MIME,%2C%20images%2C%20and%20application%20programs.) object
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




- Placing the name on the certificate and saving to a different directory.

```python
def make_certificates(name):
    '''Function to save certificates as a .png file
    Finding the width and height of the text. 
    Placing it in the center, then making some adjustments.
    Saving the certificates in a different directory.
    '''
    
    image_source = Image.open(r'template.png')
    draw = ImageDraw.Draw(image_source)
    name_width, name_height = draw.textsize(name, font=FONT_FILE)
    draw.text(((WIDTH - name_width) / 2, (HEIGHT - name_height) / 2 - 30), name, fill=FONT_COLOR, font=FONT_FILE)
    
    image_source.save("./out/" + name +".png")
    print('Saving Certificate of:', name)        

```

<br>
