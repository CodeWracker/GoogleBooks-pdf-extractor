import requests
import json
pages = []
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'x-client-data': 'CKG1yQEIkbbJAQijtskBCMS2yQEIqZ3KAQjWocoBCJm1ygEI+MfKAQjnyMoBCOnIygEItMvKAQiW1soBCLvXygE=',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'content-type': 'application/json; charset=UTF-8'
}
request = requests.get(
    'https://books.google.com.br/books',
    headers=headers,
    params=[
        ('id','xxoXcuh0oS0C'),
        ('hl','pt-BR'),
        ('pg','PA3'),
        ('jscmd','click3')])
print(request.text)
print()
for req_page in request.json()['page']:
    print(req_page)



