# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This test will initialize the display using displayio and draw a solid green
background, a smaller purple rectangle, and some yellow text.
"""
import time
import board
import terminalio
import digitalio
import displayio
import busio
from adafruit_display_text import label
from adafruit_st7735r import ST7735R
from digitalio import DigitalInOut
from adafruit_apds9960.apds9960 import APDS9960
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
from adafruit_esp32spi import adafruit_esp32spi
import adafruit_requests as requests
from adafruit_io.adafruit_io import IO_HTTP, AdafruitIO_RequestError
from random import randint
led = digitalio.DigitalInOut(board.A1)
led.direction = digitalio.Direction.OUTPUT

esp32_cs =  DigitalInOut(board.D13)
esp32_ready =  DigitalInOut(board.D11)
esp32_reset =  DigitalInOut(board.D12)
# Release any resources currently in use for the displays
displayio.release_displays()

#spi0 = board.SPI()
spi0 = busio.SPI(board.SCK, board.MOSI, board.MISO)
#spi1 = board.SPI()

#tft_clk = board.SCK # SCL pin
tft_mosi = board.MOSI # SDA pin
tft_cs = board.RX
tft_dc = board.D6
tft_rst = board.D9

#wifi_clk = board.A0 # SCL pin
#wifi_mosi = board.A1 # SDA pin
#wifi_miso = board.A2


i2c = board.STEMMA_I2C()
sensor = APDS9960(i2c)
sensor.enable_proximity = True

try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise


display_bus = displayio.FourWire(spi0, command=tft_dc, chip_select=tft_cs, reset=tft_rst)
display = ST7735R(
    display_bus, rotation=270, width=160, height=128, rowstart=0, colstart=0
)


#spi1 = busio.SPI(wifi_clk, wifi_mosi, wifi_miso)
#spi0 = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi0, esp32_cs, esp32_ready, esp32_reset)
requests.set_socket(socket, esp)
print("Connecting to AP...")
while not esp.is_connected:
    try:
        esp.connect_AP(secrets["ssid"], secrets["password"])
    except RuntimeError as e:
        print("could not connect to AP, retrying: ", e)
        continue
print("Connected to", str(esp.ssid, "utf-8"), "\tRSSI:", esp.rssi)

socket.set_interface(esp)
requests.set_socket(socket, esp)

# Set your Adafruit IO Username and Key in secrets.py
# (visit io.adafruit.com if you need to create an account,
# or if you need your Adafruit IO key.)
aio_username = secrets["aio_username"]
aio_key = secrets["aio_key"]

# Initialize an Adafruit IO HTTP API object
io = IO_HTTP(aio_username, aio_key, requests)

try:
    # Get the 'temperature' feed from Adafruit IO
    distance_feed = io.get_feed("distance")
except AdafruitIO_RequestError:
    # If no 'temperature' feed exists, create one
    distance_feed = io.create_new_feed("distance")



# Open the file
with open("/567.bmp", "rb") as bitmap_file1:

    # Setup the file as the bitmap data source
    bitmap1 = displayio.OnDiskBitmap(bitmap_file1)

    # Create a TileGrid to hold the bitmap
    tile_grid1 = displayio.TileGrid(
        bitmap1,
        pixel_shader = getattr(
            bitmap1,
            'pixel_shader',
            displayio.ColorConverter()
        )
    )

    # Create a Group to hold the TileGrid
    group1 = displayio.Group()

    # Add the TileGrid to the Group
    group1.append(tile_grid1)

# Open the file
with open("/456.bmp", "rb") as bitmap_file0:

    # Setup the file as the bitmap data source
    bitmap0 = displayio.OnDiskBitmap(bitmap_file0)

    # Add the Group to the Display
 # Create a TileGrid to hold the bitmap
    tile_grid0 = displayio.TileGrid(
        bitmap0,
        pixel_shader = getattr(
            bitmap0,
            'pixel_shader',
            displayio.ColorConverter()
        )
    )

    # Create a Group to hold the TileGrid
    group0 = displayio.Group()

    # Add the TileGrid to the Group
    group0.append(tile_grid0)

    while True:
        gesture = sensor.proximity
        if gesture < 50:
            display.show(group1)
            print("nobody is there")
            time.sleep(0.5)
            led.value = False
        if gesture > 50:
            random_value = gesture
            display.show(group0)
            led.value = True
            print("Sending {0} to distance feed...".format(random_value))
            io.send_data(distance_feed["key"], random_value)
            print("Data sent!")
            print("Retrieving data from distance feed...")
            received_data = io.receive_data(distance_feed["key"])
            print("Data from distance feed: ", received_data["value"])
            time.sleep(0.01)


