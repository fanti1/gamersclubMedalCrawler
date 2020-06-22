from PIL import Image

def converteImagens(i):
    image = Image.open(f'full_path\\medal{i}.png')
    new_image = image.resize((48, 48))
    new_image.save(f'full_path\\medal{i}.png')
    print(i, new_image.size)


#you probably will get a list size error, because GC have < than 400 icons
for i in range(0, 400):

     converteImagens(i)