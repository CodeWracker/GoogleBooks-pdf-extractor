import json
import urllib.request
lk = input('Link do Google Books: ')
book_id = (lk.split("?")[1].split("id=")[1].split('&')[0])
pages = []
cont = 1
request = urllib.request.urlopen("https://books.google.com.br/books?id="+(book_id)+"&hl=pt-BR&pg=PR"+str(cont)+"&jscmd=click3")
request_json = json.loads(request.read())['page']
print()
i = 0;
for req_page in request_json :
    pages.append([{req_page['pid']}])
    try:
        print(req_page['src'])
        pages[i].append({req_page['src']})
    except:
        pages
    i = i+1
print()
cont = int(str(pages[len(pages)-1][0]).split("'")[1].split('PA')[1])
print(cont)

pages_url = []
for inc in range(1,cont+1):
    print(inc)
    request = urllib.request.urlopen("https://books.google.com.br/books?id="+(book_id)+"&lpg=PR3&hl=pt-BR&pg=PA"+str(inc)+"&jscmd=click3")
    request_json = json.loads(request.read())['page']
    req_page = request_json[0] 
    print(req_page) 
    try:
        
        pages_url.append([{req_page['pid']},{req_page['src']}])
    except:
        print(inc)
    
print()
for page in pages_url:
    print(page)
'''
print()
for req_page in request_json :
    if([{req_page['pid']}] in pages):
        print('aaa')

'''

