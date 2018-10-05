import pygame
import math
pygame.init()
a=pygame.mixer.Sound("a2.wav")
#ang_vel=math.pi/4
ang_vel=math.pi/4
frame_rate=60
pygame.mixer.Channel(0).play(a)
clock=pygame.time.Clock()
theta=0
amplitude=0.7
R=50
r=11
while True:
    r_vol=amplitude/(R-r*math.cos(theta))**2
    l_vol=amplitude/(R+r*math.cos(theta))**2
    print("volume : " + str(l_vol*10**3) + " " + str(r_vol*10**3))
    pygame.mixer.Channel(0).set_volume(l_vol*10**3, r_vol*10**3)
    print("theta : " + str(theta))
    theta=theta+ang_vel/frame_rate
    theta=theta%(2*math.pi)
    clock.tick(frame_rate)
