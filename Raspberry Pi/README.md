## Raspberry Pi

### Requirements

    sudo apt-get install python-smbus


### Functions

The functions of piglow are:

```python
from nunchuck import nunchuck
wii = nunchuck()

wii.raw()                       # Returns all the data in raw
wii.joystick()                  # Returns just the X and Y positions of the joystick
wii.accelerometer()             # Returns X, Y and Z positions of the accelerometer
wii.button_c()                  # Returns True if C button is pressed, False if not
wii.button_z()                  # Returns True if Z button is pressed, False if not

wii.joystick_x()                # Returns just the X position of the joystick
wii.joystick_y()                # Returns just the Y position of the joystick
wii.accelerometer_x()           # Returns just the X position of the accelerometer
wii.accelerometer_y()           # Returns just the Y position of the accelerometer
wii.accelerometer_z()           # Returns just the Z position of the accelerometer

wii.scale(value,min,max,out_min,out_max) # Works the same as Arduino Map, perfect for changing values returned to a different scale, ie -100 - +100
```


### Installation instructions

#### Preparation

First to download and install the required libraries

    sudo apt-get update
    sudo apt-get install python-smbus -y


 - SMBus is required to talk over i2c bus with the Nunchuck


To enable the i2c driver you need to make a few changes

    sudo nano /etc/modules

Then make sure the following is at the end of the file

    i2c-dev
    i2c-bcm2708

So it looks like this:
<p align="center">
<img src="https://raw.github.com/Boeeerb/PiGlow/master/Pictures/etc-modules.jpg" alt="etc-modules"/>
</p>

Ctrl + x and Y to exit save the file, now edit the next

    sudo nano /etc/modprobe.d/raspi-blacklist.conf

And add the #'s to the beginning of each line so it looks like:

<p align="center">
<img src="https://raw.github.com/Boeeerb/PiGlow/master/Pictures/etc-modprobe.jpg" alt="etc-modprobe"/>
</p>

Ctrl + x and Y to exit and save the file, now reboot

    sudo reboot

#### Downloading

To be completed
