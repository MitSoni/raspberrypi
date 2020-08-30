import time

import board
import busio
import digitalio
import adafruit_max31865
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.D5)  # Chip select of the MAX31865 board.
sensor = adafruit_max31865.MAX31865(spi, cs, wires=3)
temp = sensor.temperature
relay=digitalio.DigitalInOut(board.D18)
relay1=digitalio.DigitalInOut(board.D13)
relay1.direction=digitalio.Direction.OUTPUT
relay.direction=digitalio.Direction.OUTPUT
while 1:
  print("temp: {0:0.3f}C".format(temp))
  relay.value=False
  time.sleep(1)
  relay.value = True
  time.sleep(1)
  relay1.value=False
  time.sleep(1)
  relay1.value = True
  time.sleep(1)

