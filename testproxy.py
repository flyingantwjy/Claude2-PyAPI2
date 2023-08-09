import requests

proxies = {
  'http': 'http://127.0.0.1:4780',
  'https': 'http://127.0.0.1:4780',
}

response = requests.get('https://www.youtube.com/', proxies=proxies)
print(response.text)
