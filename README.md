# Interesting Doorbell System


[Live Preview](https://8wx1f4-f6ckyda.instant.forestry.io//)




## Local development

```bash
# clone your imported repository
# cd in the project directory
# Start local dev server
hugo server
```

## Deployment and hosting

### Vercel

[![Deploy to Vercel](https://zeit.co/button)](https://zeit.co/new/project?template=https://github.com/forestryio/kross-hugo-starter)

<div align=center><img width="1200" height="600" src="https://github.com/xcyxcyxcyxcy/Team-iridescent.github.io/blob/main/image/Arlo-video-doorbell-best-video-doorbells-crop-6d815f7.jpg"/></div>

## Project showcase

In this project, we aim to create an interesting Doorbell system. We use the Adafruit Feather RP2040 as the main microcontroller. This system can provide remote control, visual information, audio information with users.

In our desired scenes, there would be a door to distinguish the home and outside. On the outside, there is a sensor, a Circuit playground microcontroller has been installed.  When the sensor APDS9960 detects something below 40 cm, the system will start to work and send the distance and warning messages to the owners via the WIFI, provided by the Airlift wifi mode, the user can read the messages from the websites on the phone. 

In the home, there would be a ST7735R LCD screen, Adafruit STEMMA speaker installed. If some people want to visit the home, the speaker will power on when the sensor detects something, the visitor will shake the Playground as the doorbell, then the speaker will begin to play some audio and the LCD will display some pictures to give some messages to the owner.

There are some images and video of our whole system:
<div align=center><img width="600" height="400" src="https://github.com/xcyxcyxcyxcy/Team-iridescent.github.io/blob/main/image/system.png"/></div>
<div align=center><img width="600" height="400" src="https://github.com/xcyxcyxcyxcy/Team-iridescent.github.io/blob/main/image/system2.png"/></div>
<div align=center><img width="600" height="400" src="https://github.com/xcyxcyxcyxcy/Team-iridescent.github.io/blob/main/image/ezgif.com-gif-maker.gif"/></div>

## Project instructions
### Components used
* Adafruit Feather  RP2040 
* Airlift wifi module
* APDS 9960 sensor
* ST7735R
* Adafruit STEMMA Speaker
* Relay
* Circuit Playground Express
* Several cables
### Assembly details
<div align=center><img width="600" height="400" src="https://github.com/xcyxcyxcyxcy/Team-iridescent.github.io/blob/main/image/5031671205774_.pic.jpg"/></div>
<div align=center><img width="500" height="300" src="https://github.com/xcyxcyxcyxcy/Team-iridescent.github.io/blob/main/image/截屏2022-12-28%20下午4.48.25.png"/></div>
Because the speaker is controlled by Circuit Playground express, in this way we can use Microcontroller to control the speaker. 
### Block diagrams
<div align=center><img width="800" height="400" src="https://github.com/xcyxcyxcyxcy/Team-iridescent.github.io/blob/main/image/图片%201.png"/></div>
### Description of your RP2040 dev environment:
We use Circuit Python language and Mu editor to finish our code. It is easier to make some functions code working together on the same microcontroller.

## Narrative overview of project development process
At the beginning we intend to make an anti-theft system. The specific function is to turn on the camera and perform face recognition when an object is detected close to the camera, and if the recognition result is judged to be a person, an alarm is issued and a screenshot is uploaded to the Internet. But we are stuck on how to capture images and upload them.

The main idea is using the Pico4ML’s camera to provide the face recognition. Unfortunately, we meet some problems when using the Pico4ML and the wifi model. We can’t capture the photos, store photos and then upload the photos to users via wifi. Because the Pico4ML only has 264KB on-chip SRAM and 2MB on board flash. It means we need additional storage devices to store the photos.
<div align=center><img width="700" height="400" src="https://github.com/xcyxcyxcyxcy/Team-iridescent.github.io/blob/main/image/ezgif.com-gif-maker的副本.gif"/></div>
<div align=center><img width="700" height="400" src="https://github.com/xcyxcyxcyxcy/Team-iridescent.github.io/blob/main/image/ezgif.com-gif-maker的副本2.gif"/></div>
After the midpoint checkpoint, we swapped out the camera function with the expectation that we could implement a recording and replay function for an interactive effect. However, due to time constraints, we did not complete the recording function with the microphone, so we finally discarded this feature. We should have talked more with the teacher in advance.

Now we implement the function of a multifunctional doorbell. The speaker and the display will only respond if some requirements set are met. At the same time the time to trigger the distance sensor will be uploaded to the Internet through the wifi module to stay to see when someone has come to play.
<div align=center><img width="600" height="400" src="https://github.com/xcyxcyxcyxcy/Team-iridescent.github.io/blob/main/image/ezgif.com-gif-maker.gif"/></div>

## Troubleshooting
One of the problems we encountered was how to implement two devices to communicate with the microcontroller at the same time. REPL showed the problem of “SCK in use“, so we tried using two different SPI interfaces but still had the same problem. Finally we used CS to select different devices, the MOSI and MISO of both devices are connected together.

At first when we used the ultrasonic distance detector, we tried to combine it with the camera code in order to realize that we could trigger the camera with distance detection. However, we had a problem with the loop, and it took several days for us to debug it, but sadly we couldn't solve the problem that it could only loop once. Later due to risk reduction, we gave up.

## Reflections on design and components
### Our design:
We made a safe doorbell system.
- Pros: 
1. It can keep kids safe and it can use cute pictures and songs as a sign to remind kids whether they can open the door when they stay at home alone. 

1. It also can upload some information like time, distance and so on to a website as a record for parents. 

1. The Circuit Python playground have more functions like the temperature sensors, and it can play some individually designed audios, we can develop more functions to the system with it in the future 

- Cons:
1. We couldn’t upload images to the website.
1. We couldn’t upload any audio to the website.
1. The distance sensor can be more accurate.
1. We couldn’t use the wifi model with the Pico4ML at the same time.

### Some components we want to recommend to other teams:
#### Adafruit feather RP2040:
- Pros: 
1. It is suitable for the Adafruit Airlift Wifi module.
1. It has 2 SPI so it can control two components at the same time.
- Cons:
1. Its code would be hard to edit if you want to use it to control 2 components.
 
#### Circuit playground express:
- Pros:
1. It is really interesting and simple for you to have a try.
1. You can use it to play lots of music you want.
1. Its LED lights can be edited to flash different colors.
- Cons:
1. You should add a filter to improve its sound.

### Other design we want to use next time:
We want to use the camera module in the Pico4ML microcontroller to achieve people detection. This function may contain some machine learning knowledge. Then the system will capture the image automatically, then store it and also, we want to record audio and replay or upload online somewhere. To make it possible, the main task is trying to make the wifi model can upload the image data or audio data directly.

## A bit more detail about some feature or accomplishment we found particularly satisfying
Just a few days before the demo day, we discovered that the Circuit Playground has interesting features and there are many extensions that can be changed to make the features interesting. Because it has lots of different sensors. It’s like a multimedia device. We can personalize the music playback and image display. And you can shake or tap the playground, or other custom interactions to increase the fun of the project.

## Team Overview:
[Yixuan Wang](https://github.com/Sharonun)

[Chenye Xiong](https://github.com/xcyxcyxcyxcy)

[Zhuoling Li](https://github.com/Zhuoling11)
