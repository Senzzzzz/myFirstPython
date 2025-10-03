from PIL import Image
import pytesseract


file_path = "C:/Users/Sen/Desktop/mesheal.PNG"

image = Image.open(file_path)
Image._show(image)

numbers_list = []
total = 0
numbers = pytesseract.image_to_string(image)
numbers = numbers.split()
for number in numbers:
    number = number.replace(",", "")
    if number.isdigit():
        total += int(number)
print(total)
