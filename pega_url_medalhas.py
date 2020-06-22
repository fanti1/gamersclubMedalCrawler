import requests

def puxaURL(i):
    
    URL = f"https://gamersclub.com.br/images/medalhas/{i}.png"
    print (URL)
    try:
        r = requests.head(URL)
        
        if r.status_code == 200:
            with open('imgs_urls.csv', 'a') as csvfile:
                csvfile.write(URL+'\n')

            print(r.status_code)
        else:
            print('404')

    except requests.ConnectionError:
        print("failed to connect")
#you probably will get a list size error, because GC have < than 400 icons
for i in range(0, 400):
    puxaURL(i)