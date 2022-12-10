import pygame
pygame.init()

#Общее окно
win = pygame.display.set_mode((600, 600))

#Координаты облаков
x_cloud1_1 = 100
x_cloud1_2 = 101
x_cloud1_34 = 55
x_cloud1_56 = 146

x_cloud2_1 = 450
x_cloud2_2 = 451
x_cloud2_34 = 405
x_cloud2_56 = 496

#Скорость облаков
speed_cloud1 = 5
speed_cloud2 = 5

#Координаты капель дождя
y_rain1 = 150
y_rain2 = 190
y_rain3 = 230

head_x = 455
head_y = 355

leg_x1 = 449
leg_x2 = 461
leg_y1 = 368
leg_y2 = 378

eye_x1 = 449
eye_x2 = 461
eye_y = 350

nose_x1 = 453
nose_y1 = 355
nose_y2 = 358

wing_x1 = 464
wing_x2 = 468
wing_x3 = 472
wing_x4 = 437
wing_x5 = 441
wing_x6 = 445
wing_y1 = 355
wing_y2 = 370

wing_up_x1 = 472
wing_up_x2 = 487
wing_up_x3 = 425
wing_up_x4 = 440
wing_up_y1 = 355
wing_up_y2 = 359
wing_up_y3 = 363

speed_bird = 5
clock = pygame.time.Clock()
FPS = 40
run = True
i = 30
sign = 1
wing_speed = 10
flag = 1
flag2 = 20
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    win.fill((255, 255, 255))
    #Облака
    pygame.draw.arc(win, (0,0,255), (x_cloud1_1, 190, 60, 40), 3.14, 6.28)
    pygame.draw.arc(win, (0,0,255), (x_cloud1_2, 121, 60, 40), 0, 3.14)
    pygame.draw.arc(win, (0,0,255), (x_cloud1_34, 171, 60, 40), 2.14, 5.28)
    pygame.draw.arc(win, (0,0,255), (x_cloud1_34, 138, 60, 40), 1, 4.14)
    pygame.draw.arc(win, (0,0,255), (x_cloud1_56, 174, 60, 40), 4.14, 7.28)
    pygame.draw.arc(win, (0,0,255), (x_cloud1_56, 140, 60, 40), 5.28, 2.11)
    
    pygame.draw.arc(win, (0,0,255), (x_cloud2_1, 80, 60, 40), 3.14, 6.28)
    pygame.draw.arc(win, (0,0,255), (x_cloud2_2, 11, 60, 40), 0, 3.14)
    pygame.draw.arc(win, (0,0,255), (x_cloud2_34, 61, 60, 40), 2.14, 5.28)
    pygame.draw.arc(win, (0,0,255), (x_cloud2_34, 28, 60, 40), 1, 4.14)
    pygame.draw.arc(win, (0,0,255), (x_cloud2_56, 64, 60, 40), 4.14, 7.28)
    pygame.draw.arc(win, (0,0,255), (x_cloud2_56, 30, 60, 40), 5.28, 2.11)
    
    if x_cloud2_1 == 450 and x_cloud2_2 == 451 and x_cloud2_34 == 405 and x_cloud2_56 == 496 and speed_cloud2 >= 0:
        
        #Дождик
        pygame.draw.ellipse(win, (0, 0, 255), (435, y_rain1, 5, 10))
        pygame.draw.ellipse(win, (0, 0, 255), (475, y_rain1, 5, 10))
        pygame.draw.ellipse(win, (0, 0, 255), (515, y_rain1, 5, 10))

        pygame.draw.ellipse(win, (0, 0, 255), (435, y_rain2, 5, 10))
        pygame.draw.ellipse(win, (0, 0, 255), (475, y_rain2, 5, 10))
        pygame.draw.ellipse(win, (0, 0, 255), (515, y_rain2, 5, 10))

        pygame.draw.ellipse(win, (0, 0, 255), (435, y_rain3, 5, 10))
        pygame.draw.ellipse(win, (0, 0, 255), (475, y_rain3, 5, 10))
        pygame.draw.ellipse(win, (0, 0, 255), (515, y_rain3, 5, 10))
        if speed_cloud2 == 0:
            y_rain1 += 10
            y_rain2 += 10
            y_rain3 += 10

    #Трава
    pygame.draw.rect(win, (0, 250, 0), (0, 550, 600, 50))

    #Ёлочка
    pygame.draw.rect(win, (139, 69, 19), (130, 560, 20, 20))
    pygame.draw.polygon(win, (0, 150, 0), [[40, 560], [240, 560], [180, 470], [210, 470],
                                           [155, 380], [180, 380], [140, 300], [100, 380], [125, 380], [70, 470], [100, 470]])

    #Дерево
    pygame.draw.ellipse(win, (0, 200, 0), (410, 300, 140, 260))
    pygame.draw.polygon(win, (139, 69, 19), [[470, 580], [490, 580], [480, 340]])

    #Птичка
    #Голова
    pygame.draw.circle(win, (255, 255, 0), (head_x, head_y), 18)

    #Ноги
    pygame.draw.aaline(win, (0, 0, 0), (leg_x1, leg_y1), (leg_x1, leg_y2))
    pygame.draw.aaline(win, (0, 0, 0), (leg_x2, leg_y1), (leg_x2, leg_y2))

    #Глаза
    pygame.draw.circle(win, (0, 0, 0), (eye_x1, eye_y), 3)
    pygame.draw.circle(win, (0, 0, 0), (eye_x2, eye_y), 3)

    #Нос
    pygame.draw.aalines(win, (0, 0, 0), False, [(nose_x1, nose_y1), (nose_x1 + 2, nose_y2), (nose_x1 + 4, nose_y1)])

    #Крылья
    if flag == 0 and flag2 == 20:
        pygame.draw.polygon(win, (205, 133, 63), [[wing_up_x1, wing_up_y1], [wing_up_x2, wing_up_y2], [wing_up_x1, wing_up_y3]])
        pygame.draw.polygon(win, (205, 133, 63), [[wing_up_x4, wing_up_y1], [wing_up_x3, wing_up_y2], [wing_up_x4, wing_up_y3]])
        wing_speed += 1
        if wing_speed == 10:
            flag = 1
    elif flag2 == 20:
        pygame.draw.polygon(win, (205, 133, 63), [[wing_x1, wing_y1], [wing_x2, wing_y2], [wing_x3, wing_y1]])
        pygame.draw.polygon(win, (205, 133, 63), [[wing_x4, wing_y1], [wing_x5, wing_y2], [wing_x6, wing_y1]])
        wing_speed -= 1
        if wing_speed == 0:
            flag = 0
    if flag2 == 20:
        #Изменение координат птички
        head_x -= speed_bird
        head_y += sign

        leg_x1 -= speed_bird
        leg_x2 -= speed_bird
        leg_y1 += sign
        leg_y2 += sign

        eye_x1 -= speed_bird
        eye_x2 -= speed_bird
        eye_y += sign

        nose_x1 -= speed_bird
        nose_y1 += sign
        nose_y2 += sign
        
        wing_x1 -= speed_bird
        wing_x2 -= speed_bird
        wing_x3 -= speed_bird
        wing_x4 -= speed_bird
        wing_x5 -= speed_bird
        wing_x6 -= speed_bird
        wing_y1 += sign
        wing_y2 += sign
        
        
        wing_up_x1 -= speed_bird
        wing_up_x2 -= speed_bird
        wing_up_x3 -= speed_bird
        wing_up_x4 -= speed_bird
        wing_up_y1 += sign
        wing_up_y2 += sign
        wing_up_y3 += sign
    if head_x == 455 or head_x == 180:
        speed_bird *= -1
        sign *= -1
        flag2 -= 1
        pygame.draw.polygon(win, (205, 133, 63), [[wing_x1, wing_y1], [wing_x2, wing_y2], [wing_x3, wing_y1]])
        pygame.draw.polygon(win, (205, 133, 63), [[wing_x4, wing_y1], [wing_x5, wing_y2], [wing_x6, wing_y1]])
    if flag2 == 0:
        flag2 = 20
        speed_bird *= -1
        sign *= -1
    #Изменение координат облаков
    x_cloud1_1 -= speed_cloud1
    x_cloud1_2 -= speed_cloud1
    x_cloud1_34 -= speed_cloud1
    x_cloud1_56 -= speed_cloud1

    x_cloud2_1 += speed_cloud2
    x_cloud2_2 += speed_cloud2
    x_cloud2_34 += speed_cloud2
    x_cloud2_56 += speed_cloud2
    
    if x_cloud1_34 < 0 or x_cloud1_56 > 540:
        speed_cloud1 *= -1
        x_cloud1_1 -= 2*speed_cloud1
        x_cloud1_2 -= 2*speed_cloud1
        x_cloud1_34 -= 2*speed_cloud1
        x_cloud1_56 -= 2*speed_cloud1
        
    if x_cloud2_34 < 0 or x_cloud2_56 > 540:
        speed_cloud2 *= -1
        x_cloud2_1 += 2*speed_cloud2
        x_cloud2_2 += 2*speed_cloud2
        x_cloud2_34 += 2*speed_cloud2
        x_cloud2_56 += 2*speed_cloud2
        
    #Остановка облака
    if x_cloud2_1 == 450 and x_cloud2_2 == 451 and x_cloud2_34 == 405 and x_cloud2_56 == 496 and i != 0 and speed_cloud2 >= 0:
        speed_cloud2 = 0
        i -= 1
    if i == 0:
        i = 30
        speed_cloud2 = 5
        x_cloud2_1 += speed_cloud2
        x_cloud2_2 += speed_cloud2
        x_cloud2_34 += speed_cloud2
        x_cloud2_56 += speed_cloud2
        y_rain1 = 150
        y_rain2 = 190
        y_rain3 = 230
        
    
    pygame.display.update()
    clock.tick(FPS)
            
pygame.quit()
