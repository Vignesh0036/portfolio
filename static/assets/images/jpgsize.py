from PIL import Image

with Image.open('profil.jpg') as image:
    print(image.size)

with Image.open('profile.jpg') as img:
    print(img.size)    
    converted_image = img.crop((200, 800, 1500, 1764))
    converted_image.save('Converted_image.png', 'png')
