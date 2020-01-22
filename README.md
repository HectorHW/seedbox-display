# seedbox-display
simple script which draws my upload speed on sh1106 display
## setup
* enable SPI:

  `sudo raspi-config`
  
  go to Interfacing Options > SPI
  
  `sudo usermod -a -Gspi,gpio pi`
  
  `reboot`
* install required packages with apt:

  `sudo apt install python-dev python-pip libfreetype6-dev libjpeg-dev build-essential libopenjp2-7 libtiff5`
  
* install required packages with pip:

  `sudo -H pip install --upgrade luma.oled`
  
* run the script:

  `python3 draw_speed.py`
  
  
  
  
