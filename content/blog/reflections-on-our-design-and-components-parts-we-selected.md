+++
author = []
categories = []
date = 2022-12-22T05:00:00Z
description = ""
image = ""
tags = []
title = "Reflections on our design and components/parts we selected"

+++
**Our design:**

We made a safe doorbell system.

Pros:

1: It can keep kids safe and it can use cute pictures and songs as a sign to remind kids whether they can open the door when they stay at home alone.

2:It also can upload some information like time, distance and so on to a website as a record for parents.

3\. The Circuit Python playground have more functions like the temperature sensors, and it can play some individually designed audios, we can develop more functions to the system with it in the future

Cons:

1: We couldn’t upload images to the website.

2: We couldn’t upload any audio to the website.

3: The distance sensor can be more accurate.

4\. We couldn’t use the wifi model with the Pico4ML at the same time.

**Some components we want to recommend to other teams:**

Adafruit feather RP2040:  
Pros:

1:It is suitable for the Adafruit Airlift Wifi module.

2:It has 2 SPI so it can control two components at the same time.

Cons:  
1: Its code would be hard to edit if you want to use it to control 2 components.

Circuit playground express:

Pros:

1:It is really interesting and simple for you to have a try.

2:You can use it to play lots of music you want.

3: Its LED lights can be edited to flash different colors.

Cons:

1: You should add a filter to improve its sound.

**Other design we want to use next time:**

We want to use the camera module in the Pico4ML microcontroller to achieve people detection. This function may contain some machine learning knowledge. Then the system will capture the image automatically, then store it and also, we want to record audio and replay or upload online somewhere. To make it possible, the main task is trying to make the wifi model can upload the image data or audio data directly.