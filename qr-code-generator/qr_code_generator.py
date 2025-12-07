#!/usr/bin/python3
import qrcode

data = input("Enter the data for the QR code: ")
img = qrcode.make(data)
img.save("qrcode.png")
print("QR code generated and saved as qrcode.png")