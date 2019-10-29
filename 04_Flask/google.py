import requests

api_url='https://translation.googleapis.com/language/translate/v2'
key = 'AIzaSyB5r2yDfhjsaWqHJs2pUwTZKGBnCt1eCVk'
data = {
    'q':'엄마 판다는 새끼가 있네',
    'source':'ko',
    'target':'en'
}

result = requests.post(f'{api_url}?key={key}',data).json()
print(result)
