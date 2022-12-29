from adafruit_circuitplayground import cp

while True:
    if cp.button_a:
        cp.play_file("567.wav")
    if cp.shake():
        print("Shake detected!")
		 cp.play_file("123.wav")