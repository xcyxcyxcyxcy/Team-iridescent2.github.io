---
title: A project showcase
date: 2022-12-25T05:40:24-05:00
image: images/2020-three-quarters-1.png
author:
- Admin
categories:
- Working days
tags:
- work
- day
description: This is meta description

---
In this project, we aim to create an interesting Doorbell system. We use the Adafruit Feather RP2040 as the main microcontroller. This system can provide remote control, visual information, audio information with users.

In our desired scenes, there would be a door to distinguish the home and outside.

On the outside, there is a sensor, a Circuit playground microcontroller has been installed. When the sensor APDS9960 detects something below 40 cm, the system will start to work and send the distance and warning messages to the owners via the WIFI, provided by the Airlift wifi mode, the user can read the messages from the websites on the phone.

In the home, there would be a ST7735R LCD screen, Adafruit STEMMA speaker installed. If some people want to visit the home, the speaker will power on when the sensor detects something, the visitor will shake the Playground as the doorbell, then the speaker will begin to play some audio and the LCD will display some pictures to give some messages to the owner.