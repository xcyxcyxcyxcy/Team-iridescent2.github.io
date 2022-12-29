+++
author = []
categories = []
date = 2022-12-22T05:00:00Z
description = ""
image = "/images/screenshot-2022-12-28-at-19-58-14.png"
tags = []
title = "Any Significant Issues to troubleshoot and solving ways"

+++
One of the problems we encountered was how to implement two devices to communicate with the microcontroller at the same time. REPL showed the problem of “SCK in use“, so we tried using two different SPI interfaces but still had the same problem. Finally we used CS to select different devices, the MOSI and MISO of both devices are connected together.

At first when we used the ultrasonic distance detector, we tried to combine it with the camera code in order to realize that we could trigger the camera with distance detection. However, we had a problem with the loop, and it took several days for us to debug it, but sadly we couldn't solve the problem that it could only loop once. Later due to risk reduction, we gave up.