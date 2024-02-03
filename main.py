from PIL import Image, ImageFont, ImageDraw # Imaging library 

FONT_FILE = ImageFont.truetype(r'font/SwanseaBoldItalic-p3Dv.ttf',  100)
FONT_COLOR =  "#000000"

template = Image.open(r'CERT 1.png')
WIDTH, HEIGHT = template.size

# Name Placing on the certificate
def generate_certificates(name):
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
    image_source.save("./out/" + name + ".png")
    print('Saving Certificate of:', name)
    
if __name__ == "__main__":
    names = ["Sahil Bodke", "Long names wont work"]
    # with open('names.txt') as f:
    #     generated_certificates = f.readlines()
    #     for item in generated_certificates:
            #  Removes leading and trailing whitespaces and converts each name to title case 
            # (capitalizes the first letter of each word). The processed names are then added to the names list.
            # names.append(item.strip().title())
    for name in names:
        generate_certificates(name)
        print(len(names), "certificates done")