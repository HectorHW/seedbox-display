from time import sleep, strftime, localtime
from luma.core.interface.serial import  spi
from luma.oled.device import sh1106
from luma.core.render import canvas
from PIL import ImageFont
import requests

COMICSANS_BOLD_FONT = ImageFont.truetype("Comic_Sans_MS_Bold.ttf", 15, encoding='UTF-8')
LOCALHOST = 'http://localhost:8080'

def init_display():
    serial = spi(device=0, port=0)
    device = sh1106(serial)
    return device

def get_upspeed(session, addr=LOCALHOST):
    info = session.get(f"{addr}/api/v2/transfer/info",  )
    speed = info.json()['up_info_speed']/(2**10)
    return speed

def close_session(session, addr=LOCALHOST):
    session.get(f"{addr}/api/v2/auth/logout")

if __name__ == '__main__':
    session = requests.Session()
    display = init_display()
    while True:

        speed = get_upspeed(session)
        speed_s = f"Up:{speed:.1f}Kb/s"

        time_str = strftime("%H:%M:%S", localtime())

        with canvas(display) as draw:
            draw.rectangle(display.bounding_box, outline="white", fill="black")
            draw.text((5, 10), time_str, fill="white", font=COMICSANS_BOLD_FONT)
            draw.text((5, 36), speed_s, fill="white", font=COMICSANS_BOLD_FONT)

        sleep(0.5)