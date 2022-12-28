---
title: Narrative Overview of the Project's Development
date: 2022-12-22T05:40:24-05:00
image: ''
author:
- Group8
categories: []
tage:
- tags
description: This is meta description

---
At the beginning we intend to make an anti-theft system. The specific function is to turn on the camera and perform face recognition when an object is detected close to the camera, and if the recognition result is judged to be a person, an alarm is issued and a screenshot is uploaded to the Internet. But we are stuck on how to capture images and upload them.

The main idea is using the Pico4ML’s camera to provide the face recognition. Unfortunately, we meet some problems when using the Pico4ML and the wifi model. We can’t capture the photos, store photos and then upload the photos to users via wifi. Because the Pico4ML only have 264KB on-chip SRAM and 2MB on board flash. It means we need additional storage devices to store the photos.