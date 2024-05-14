# Virtual Drums
This project creates a Virtual Drumset Window. In the window there are two drums(snare, kick) shown in a small boxes. When one hits the boxes with the defined colour it gerates a sound. This project is unique as compared to other Virtual Drums because It uses MultiThreading to generate sound and the sound is only played once every hit and makes the drum set more realistic.

## Installation
clone the project and then navigate to VirtualDrums
```
pip install -r requirements.txt 
```

### Select the correct color mask
You can Then select The colour of the object you want use with ```colordetection.py```, you have to choose the object you want to use to play the drums and then run the command below, it will open three windows, mask, hsv videocapture, and the HSV bars, move the bars and select the hsv values with the best mask. Default colur is green with hsv values [ 32 , 78 , 90 ,  79  ,  255 , 255 ] 

```
python colordetection.py
```
![Screenshot 2024-05-14 181006](https://github.com/mishra-18/Virtual-Drums/assets/155224614/677a57e3-285e-49c2-a812-802d1c97d60b)

### Run the python file 🐍
Finally you can use the VirtualDrums by typing the command

```
python VirtualDrums.py
```
![Screenshot 2024-05-14 175633](https://github.com/mishra-18/Virtual-Drums/assets/155224614/d156e2af-e2e7-46ee-9422-8e6cbe5caa85)
