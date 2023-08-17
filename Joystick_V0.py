import pygame
import mouse
import time
import pyautogui

pygame.display.init()
pygame.joystick.init()
joys=pygame.joystick.Joystick(0)
joystick_number=pygame.joystick.get_count()
joys.init()

mouse_speed=4.0
scroll_speed=0.35
time.sleep(2)

while True:
    pygame.event.pump()
    
    x_value = joys.get_axis(0)
    y_value = joys.get_axis(1)
    scroll_value = joys.get_axis(3)


    if x_value<0.05 and x_value>-0.05:
        x_value=0
    if y_value<0.05 and y_value>-0.05:
        y_value=0
    if scroll_value<0.05 and scroll_value>-0.05:
        scroll_value=0

    mouse_pos=mouse.get_position()
    mouse_next_pos = (mouse_pos[0] + x_value * mouse_speed, mouse_pos[1] + y_value * mouse_speed)

    event=pygame.event.get(eventtype= pygame.JOYBUTTONDOWN)
    if len(event)!=0:
        button=event[0].dict.get("button")
        if button==0:
            mouse.click()
        if button==1:
            mouse.right_click()
    mouse.move(mouse_next_pos[0],mouse_next_pos[1])
    mouse.wheel(-scroll_value*scroll_speed)
    time.sleep(0.005)

    
#mouse_next_pos = (mouse_pos[0] + x_value * mouse_speed, mouse_pos[1] + y_value * mouse_speed) #mouse_next_pos = (mouse_pos[0] + x_value * mouse_speed, mouse_pos[1] + y_value * mouse_speed) #mouse_next_pos = (mouse_pos[0] + x_value * mouse_speed, mouse_pos[1] + y_value * mouse_speed) #mouse_next_pos = (mouse_pos[0] + x_value * mouse_speed, mouse_pos[1] + y_value * mouse_speed) #mouse_next_pos = (mouse_pos[0] + x_value * mouse_speed, mouse_pos[1] + y_value * mouse_speed) #mouse_next_pos = (mouse_pos[0] + x_value * mouse_speed, mouse_pos[1] + y_value * mouse_speed) #mouse_next_pos = (mouse_pos[0] + x_value * mouse_speed, mouse_pos[1] + y_value * mouse_speed) #mouse_next_pos = (mouse_pos[0] + x_value * mouse_speed, mouse_pos[1] + y_value * mouse_speed) 


"""
joybutton
0:a
1:b
2:x
3:y
4:lb
5:rb
6:back
7:start
8:sol düğme bas
9:sağ düğme bas
"""
"""
joyaxis
sağ:1
sol:-1
alt:1
üst:-1
sol teker sağ-sol eksen 0
sol teker alt-üst eksen 1
sağ teker sağ-sol eksen 2
sağ teker alt-üst eksen 3
"""
# for event in pygame.event.get():
    #     if event.type == pygame.JOYBUTTONDOWN:
    #         button_number=event.dict.get("button")
    #         if button_number==0:
    #             mouse.click()
    #     if event.type == pygame.JOYAXISMOTION:
    #         # print(event)
    #         # axis_1=event.dict.get("axis")
    #         if event.dict.get("axis")==0:
    #             value=(event.dict.get("value"))
    #             mouse_x,mouse_y=mouse.get_position()
    #             mouse.move(mouse_x,mouse_y+value)
    #     if event.type==pygame.JOYHATMOTION:
    #         print(event)