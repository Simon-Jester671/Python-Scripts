import requests

domain = 'example.com'
file = open('/path/to/file', 'r')
body = file.read()
subs = body.splitlines()

for sub in subs:
    url = f'http://{sub}.{domain}'
    try:
        request.get(url)
    except requests.ConnectionError:
        pass
    else:
        print('Found Subdomain: ', url)
