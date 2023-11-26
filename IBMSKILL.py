import cv2
import os

img = cv2.imread("4f95b048-d711-48e8-82a0-b83c65ec8fbc.jpg")

msg = input("Enter secret message: ")
password = input("Enter password: ")

char_to_int = {chr(i): i for i in range(255)}
int_to_char = {i: chr(i) for i in range(255)}

for idx, char in enumerate(msg):
    x, y, z = idx // img.shape[1], idx % img.shape[1], (idx // 3) % 3
    img[x, y, z] = char_to_int[char]

cv2.imwrite("Encryptedmsg.jpg", img)

os.system("start Encryptedmsg.jpg")

decrypted_msg = ""
pas = input("Enter passcode for Decryption: ")

if password == pas:
    for idx in range(len(msg)):
        x, y, z = idx // img.shape[1], idx % img.shape[1], (idx // 3) % 3
        decrypted_msg += int_to_char[img[x, y, z]]
    print("Decrypted message:", decrypted_msg)
else:
    print("Not valid key")
