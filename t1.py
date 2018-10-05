import pygame
import math
pygame.init()
a=pygame.mixer.Sound("a3.wav")
#ang_vel=math.pi/4
ang_vel=math.pi/4
frame_rate=60
pygame.mixer.Channel(0).play(a, loops=-1)
clock=pygame.time.Clock()
theta=0
amplitude=14
R=15
r=11
R_sq=R**2
r_sq=r**2
tw_rr=2*(R)*(r)
a=150
b=100
while True:
    r_vol=amplitude/((R-r*math.cos(theta))**2)
    l_vol=amplitude/((R+r*math.cos(theta))**2)
    #r_vol=amplitude/((R_sq + r_sq - tw_rr*math.cos(theta)))
    #l_vol=amplitude/((R_sq + r_sq + tw_rr*math.cos(theta)))
    #r_vol=amplitude/((b**2)*((math.cos(theta))**2) + (r**2) + (a*math.sin(theta))**2 - 2*b*r*math.cos(theta))
    #l_vol=amplitude/((b**2)*((math.cos(theta))**2) + (r**2) + (a*math.sin(theta))**2 + 2*b*r*math.cos(theta))

    print("volume : " + str(l_vol) + " " + str(r_vol))
    pygame.mixer.Channel(0).set_volume(l_vol, r_vol)
    theta=theta+ang_vel/frame_rate
    theta=theta%(2*math.pi)
    clock.tick(frame_rate)
