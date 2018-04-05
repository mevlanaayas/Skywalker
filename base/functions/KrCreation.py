#def createKrCode():
import pyqrcode

big_code = pyqrcode.create('H A C K L E N D I N I Z') #error='L', version=27, mode='binary'
big_code.png('code.png', scale=6) #module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc]
big_code.show()

#createKrCode()
