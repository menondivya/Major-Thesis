#sudo apt-get install python-smbus i2c-tools
#sudo raspi-config
#sudo nano /etc/mo
#Add these two lines to the above mentiones location
#   i2c-bcm2708
#   i2c-dev


#sudo reboot
#sudo i2cdetect -y 1

#mkdir hd44780 && cd hd44780
#wget http://tutorials-raspberrypi.de/wp-content/uploads/scripts/hd44780_i2c.zip
#unzip hd44780_i2c.zip

import lcddriver
from time import *
 
lcd = lcddriver.lcd()
lcd.lcd_clear()
 
lcd.lcd_display_string("Tutorials-", 1)
lcd.lcd_display_string("      RaspberryPi.de", 2)
lcd.lcd_display_string("", 3)
lcd.lcd_display_string("HD44780 I2C Tutorial", 4)
