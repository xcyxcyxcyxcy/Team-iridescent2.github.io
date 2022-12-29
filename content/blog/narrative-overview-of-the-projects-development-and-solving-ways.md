+++
author = []
categories = []
date = 2022-12-22T05:00:00Z
description = ""
image = "/images/wechatimg961.jpeg"
tags = []
title = "Narrative overview of the projects development and solving ways"

+++
At the beginning we intend to make an anti-theft system. The specific function is to turn on the camera and perform face recognition when an object is detected close to the camera, and if the recognition result is judged to be a person, an alarm is issued and a screenshot is uploaded to the Internet. But we are stuck on how to capture images and upload them.

The main idea is using the Pico4ML’s camera to provide the face recognition. Unfortunately, we meet some problems when using the Pico4ML and the wifi model. We can’t capture the photos, store photos and then upload the photos to users via wifi. Because the Pico4ML only have 264KB on-chip SRAM and 2MB on board flash. It means we need additional storage devices to store the photos.

  
![](/images/screenshot-2022-12-28-at-16-21-08.png)

After the midpoint checkpoint, we swapped out the camera function with the expectation that we could implement a recording and replay function for an interactive effect. However, due to time constraints, we did not complete the recording function with the microphone, so we finally discarded this feature. We should have talked more with the teacher in advance.

Now we implement the function of a multifunctional doorbell. The speaker and the display will only respond if some requirements set are met. At the same time the time to trigger the distance sensor will be uploaded to the Internet through the wifi module to stay to see when someone has come to play.

![](/images/screenshot-2022-12-28-at-16-27-12.png)