import struct

with open(r'/users/kasanowak/Desktop/pythonALX/giphy.gif','rb') as f:
   img = f.read()
   print(struct.unpack('<HH', img[6:10]))