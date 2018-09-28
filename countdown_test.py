import picamera
import pygame
import time

from constants import SCREEN_W, SCREEN_H, IMAGE_W, IMAGE_H, CANVAS_W, CANVAS_H, WHITE, BLACK

pygame.font.init()

COUNTDOWN_LOCATION = (SCREEN_W/2, SCREEN_H/2)
N_COUNTDOWN = 5
BOTTOM_RESERVE = 50 ## reserved room at bottom for countdown
FONTSIZE = 100 ## countdown fontsize

camera = picamera.PiCamera()
camera.rotation = 180
camera.led = False

camera.preview_alpha = 255
#camera.preview_window = (0, 0, SCREEN_W, SCREEN_H - BOTTOM_RESERVE)
camera.preview_fullscreen = True

pygame.display.init()
# size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
#screen = pygame.display.set_mode((SCREEN_W, SCREEN_H), pygame.FULLSCREEN)
screen = pygame.display.set_mode((CANVAS_W, CANVAS_H), pygame.FULLSCREEN)
screen.fill((0, 0, 0))        
pygame.display.update()

camera.start_preview()

font = pygame.font.Font(None, FONTSIZE)

text_color = WHITE

led_state = False

for i in range(N_COUNTDOWN):
    screen.fill(BLACK)
    text = font.render(str(N_COUNTDOWN - i), 1, text_color)
    textpos = text.get_rect()
    textpos.center = COUNTDOWN_LOCATION
    screen.blit(text, textpos)
    pygame.display.flip()
    if i < N_COUNTDOWN - 2:
        time.sleep(1)
        led_state = not led_state
        camera.led = led_state
    else:
        for j in range(5):
            time.sleep(.2)
            led_state = not led_state
            camera.led = led_state
        
camera.stop_preview()
