import requests


def download(i):
    
    with open('imgs_urls.csv') as fp:
        line = fp.readlines()
    url = line[i].rstrip()
    
    r = requests.get(url)
    if r.status_code == 200:
        
        open(f'full_path', 'wb').write(r.content)
    

#you probably will get a list size error, because GC have < than 400 icons
for i in range(0, 400):
    download(i)