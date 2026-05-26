<<<<<<< HEAD
import requests
from PIL import Image
import io

# 1. Tworzymy fałszywy czarny obrazek do testów
dummy_image = Image.new('RGB', (96, 96), color='black')
img_byte_arr = io.BytesIO()
dummy_image.save(img_byte_arr, format='JPEG')
img_byte_arr.seek(0)

# 2. Wysyłamy zapytanie do naszego działającego serwera API
print("Wysyłam zapytanie do serwera...")
resp = requests.post(
    "http://34.116.158.44:3000/predict",
    files={"image": ("test.jpg", img_byte_arr, "image/jpeg")}
)

# 3. Wypisujemy wynik dla prowadzącego
print(f"Status Code: {resp.status_code}")
=======
import requests
from PIL import Image
import io

# 1. Tworzymy fałszywy czarny obrazek do testów
dummy_image = Image.new('RGB', (96, 96), color='black')
img_byte_arr = io.BytesIO()
dummy_image.save(img_byte_arr, format='JPEG')
img_byte_arr.seek(0)

# 2. Wysyłamy zapytanie do naszego działającego serwera API
print("Wysyłam zapytanie do serwera...")
resp = requests.post(
    "http://34.116.158.44:3000/predict",
    files={"image": ("test.jpg", img_byte_arr, "image/jpeg")}
)

# 3. Wypisujemy wynik dla prowadzącego
print(f"Status Code: {resp.status_code}")
>>>>>>> 67c31a867bc2eaf808bf2b9070126c5c0b99d120
print(f"Przewidziana klasa: {resp.text}")