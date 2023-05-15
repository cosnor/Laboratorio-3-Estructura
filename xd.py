menu_button = Button(screen, 10, 10, 33, 33, "x", (255,0,0), 0)
        menu_button.draw()
        play_button = Button(screen, 620, 405, 200, 50, "JUGAR", (255,0,0), 20) #150
        play_button.draw()
        manual_button = Button(screen, 180, 405, 200, 50, "MANUAL", (255,0,0), 20)
        manual_button.draw()
        font1 = pygame.font.Font("Laboratorio-3-Estructura/src/font/Pixeled.ttf", 20)
        text_surface = font1.render("AJUSTE DE BOMBA", True, (255, 255, 255))
        screen.blit(text_surface, (150, 135))
        ##### 350
        atras1_button = Button(screen, 580, 150, 40, 40, "<", (255, 0, 0), 20) #300, 150
        adelante1_button = Button(screen, 820, 150, 40, 40, ">", (255, 0, 0), 20) #650, 150
        adelante1_button.draw()
        atras1_button.draw()
        atras2_button = Button(screen, 580, 290, 40, 40, "<", (255, 0, 0), 20)
        adelante2_button = Button(screen, 820, 290, 40, 40, ">", (255, 0, 0), 20)
        adelante2_button.draw()
        atras2_button.draw()
       #listica de errores
        textE = font1.render("ERRORES", True, (0, 0, 0))
        screen.blit(textE, (655, 90))  
        text_1 = font1.render(str(a1.data), True, (0, 0, 0))
        screen.blit(text_1, (710, 135)) #495
        if a1.prev == None:
            text11 = font2.render("", True, (0, 0, 0))
            screen.blit(text11, (690, 150)) #20
        else:
            text11 = font2.render(str(a1.prev.data), True, (0, 0, 0))
            screen.blit(text11, (690, 150))
        if a1.next == None:
            text21 = font2.render("", True, (0, 0, 0))
            screen.blit(text21, (740, 150)) #30
        else:
            text21 = font2.render(str(a1.next.data), True, (0, 0, 0))
            screen.blit(text21, (740, 150))

        #listica de modulos
        textM = font1.render("MODULOS", True, (0, 0, 0))
        screen.blit(textM, (655, 230))
        text_2 = font1.render(str(a2.data), True, (0, 0, 0))
        screen.blit(text_2, (710, 280))
        if a2.prev == None:
            text12 = font2.render("", True, (0, 0, 0))
            screen.blit(text12, (690, 295))
        else:
            text12 = font2.render(str(a2.prev.data), True, (0, 0, 0))
            screen.blit(text12, (690, 295))
        if a2.next == None:
            text22 = font2.render("", True, (0, 0, 0))
            screen.blit(text22, (740, 295))
        else:
            text22 = font2.render(str(a2.next.data), True, (0, 0, 0))
            screen.blit(text22, (740, 295))