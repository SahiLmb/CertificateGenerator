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

### Pillow module

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
