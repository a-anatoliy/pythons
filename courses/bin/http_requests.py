import requests

url = 'https://www.google.com/afadf'
response = requests.get(url)
print(f'Request to {url}. Status code is {response.status_code}.')
print(response.text)