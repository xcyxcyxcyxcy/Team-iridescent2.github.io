---
title: Significant Issues to trouble shoot and solving ways
date: 2022-12-22T05:40:24-05:00
image: ''
author: []
categories:
- lifestyle
tags: []
description: This is meta description

---
One of the problems we encountered was how to implement two devices to communicate with the microcontroller at the same time. REPL showed the problem of “SCK in use“, so we tried using two different SPI interfaces but still had the same problem. Finally we used CS to select different devices, the MOSI and MISO of both devices are connected together.

At first when we used the ultrasonic distance detector, we tried to combine it with the camera code in order to realize that we could trigger the camera with distance detection. However, we had a problem with the loop, and it took several days for us to debug it, but sadly we couldn't solve the problem that it could only loop once. Later due to risk reduction, we gave up.