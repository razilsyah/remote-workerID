import requests

url = 'https://detik.com'
respone = requests.get(url)
try:
    print (f'respone = {respone.status_code}')

except Exception as e:
    print("ini error",e)

# print("langsung di jalankan")