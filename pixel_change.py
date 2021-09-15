from PIL import Image
#open the image
img = Image.open('bw_yawn.png')
print("Lighten image...")
#loop through the image
for y in range(img.height):
  for x in range(img.width):
    value = img.getpixel((x, y))
    img.putpixel((x,y), value+100)
img.save('output_lighten.png')
print("Lighten image complete")

print('Negative example...')
img = Image.open('bw_leaves.png')
for y in range(img.height):
  for x in range(img.width):
    value = img.getpixel((x,y))
    new_value = 255 - value
    img.putpixel((x,y),new_value)
img.save('output_negative.png')
print("Negative image complete")
