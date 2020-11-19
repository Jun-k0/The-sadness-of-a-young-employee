import pygame
import sys
import time

pygame.init()

box_width=70 #choose box 
box_height=50 #choose box
x1=290 #yes location x
y1=235 #yes location y
x2=375 #no location x
y2=235 #no location y
global ischk # 부당계약인지?

titleImg=pygame.image.load("images/게임표지.png")
selectImg1=pygame.image.load("images/입사.png")
endingImg1=pygame.image.load("images/백수엔딩.png")
Img2=pygame.image.load("images/부당계약.png")
Img3=pygame.image.load("images/업무부여.png")
Img4=pygame.image.load("images/업무처리.png")
Img5=pygame.image.load("images/업무물어봄.png")
Img6=pygame.image.load("images/업무스스로.png")
Img7=pygame.image.load("images/첫월급지급.png")
Img8=pygame.image.load("images/외부업무부여.png")
Img9=pygame.image.load("images/행사고민.png")
Img10=pygame.image.load("images/사고남.png")
Img11=pygame.image.load("images/산재보험.png")
Img12=pygame.image.load("images/산재요청.png")
Img13=pygame.image.load("images/회사산재거절.png")
fffImg=pygame.image.load("images/미완.png")
Img14=pygame.image.load("images/노동청다시요청.png")
Img15=pygame.image.load("images/노동청다음.png")
Img16=pygame.image.load("images/소송고민.png")
Img34=pygame.image.load("images/엔딩2.png")
Img17=pygame.image.load("images/엔딩3전.png")
Img18=pygame.image.load("images/엔딩3.png")
Img19=pygame.image.load("images/엔딩4.png")
Img20=pygame.image.load("images/거짓말들킴.png")
Img21=pygame.image.load("images/엔딩5전.png")
Img22=pygame.image.load("images/엔딩5.png")
Img23=pygame.image.load("images/밥약고민.png")
Img24=pygame.image.load("images/밥먹다현타.png")
Img25=pygame.image.load("images/엔딩6.png")
Img26=pygame.image.load("images/대출전화.png")
Img27=pygame.image.load("images/전화고민.png")
Img28=pygame.image.load("images/가족대출.png")
Img29=pygame.image.load("images/가족대출고민.png")
Img30=pygame.image.load("images/투잡.png")
Img31=pygame.image.load("images/엔딩7.png")
Img32=pygame.image.load("images/집뺏김.png")
Img33=pygame.image.load("images/엔딩8.png")

gameDisplay=pygame.display.set_mode((735,365))
pygame.display.set_caption("젊은 청년씨의 슬픔")

clock=pygame.time.Clock()


#선택지 함수
def choose(action1=None,action2=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x1+box_width>mouse[0]>x1 and y1+box_height>mouse[1]>y1:
        if click[0]:
            time.sleep(1)
            action1()
    elif x2+box_width>mouse[0]>x2 and y2+box_height>mouse[1]>y2:
        if click[0]:
            time.sleep(1)
            action2()

#클릭하면 다음으로
def nexts(action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if click[0]:
        time.sleep(1)
        action()

#게임시작 
def mainmenu():
    menu=True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
          
        titletext=gameDisplay.blit(titleImg,(0,0))
        nexts(select1)
        pygame.display.update()
        clock.tick(15)

#미완
def fff():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen1=gameDisplay.blit(fffImg,(0,0))
        nexts(mainmenu)

        pygame.display.update()
        clock.tick(15)

#입사
def select1():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen1=gameDisplay.blit(selectImg1,(0,0))
        choose(select2,ending1)

        pygame.display.update()
        clock.tick(15)

#백수엔딩
def ending1():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen1=gameDisplay.blit(endingImg1,(0,0))
        nexts(mainmenu)

        pygame.display.update()
        clock.tick(15)

#부당계약
def select2():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen=gameDisplay.blit(Img2,(0,0))
        choose(story1_true,story1_false)

        pygame.display.update()
        clock.tick(15)

#업무부여_부당
def story1_true():
    select = True
    
    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen=gameDisplay.blit(Img3,(0,0))
        global ischk
        ischk=True
        nexts(choose2)

        pygame.display.update()
        clock.tick(15)

#업무부여_노동법
def story1_false():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen=gameDisplay.blit(Img3,(0,0))
        global ischk
        ischk=False
        nexts(choose2)

        pygame.display.update()
        clock.tick(15)

#업무처리
def choose2():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen=gameDisplay.blit(Img4,(0,0))
        choose(story2,story3)

        pygame.display.update()
        clock.tick(15)

#업무물어봄
def story2():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen=gameDisplay.blit(Img5,(0,0))
        nexts(story4)

        pygame.display.update()
        clock.tick(15)

#업무스스로
def story3():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen=gameDisplay.blit(Img6,(0,0))
        nexts(story4)

        pygame.display.update()
        clock.tick(15)

#첫월급지급
def story4():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen=gameDisplay.blit(Img7,(0,0))
        #부당계약 분기
        if ischk==True:
            nexts(story5)
        else:
            nexts(choose6)

        pygame.display.update()
        clock.tick(15)

#외부업무부여8
def story5():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen=gameDisplay.blit(Img8,(0,0))
        nexts(choose3)

        pygame.display.update()
        clock.tick(15)
        
#행사고민9
def choose3():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen=gameDisplay.blit(Img9,(0,0))
        choose(story6,story12)

        pygame.display.update()
        clock.tick(15)

#사고남10
def story6():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen=gameDisplay.blit(Img10,(0,0))
        nexts(story7)

        pygame.display.update()
        clock.tick(15)

#산재보험11
def story7():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen=gameDisplay.blit(Img11,(0,0))
        nexts(choose4)

        pygame.display.update()
        clock.tick(15)

#산재요청12
def choose4():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen=gameDisplay.blit(Img12,(0,0))
        choose(story8,story10)

        pygame.display.update()
        clock.tick(15)

#회사요청거절13
def story8():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen=gameDisplay.blit(Img13,(0,0))
        nexts(story9)

        pygame.display.update()
        clock.tick(15)
#노동청다시요청14
def story9():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen=gameDisplay.blit(Img14,(0,0))
        nexts(ending2)

        pygame.display.update()
        clock.tick(15)
        
#노동청 깨달음 15
def story10():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen=gameDisplay.blit(Img15,(0,0))
        nexts(choose5)

        pygame.display.update()
        clock.tick(15)

#소송고민16
def choose5():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen=gameDisplay.blit(Img16,(0,0))
        choose(ending4,story11)

        pygame.display.update()
        clock.tick(15)

#엔딩2  34
def ending2():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen=gameDisplay.blit(Img34,(0,0))
        nexts(mainmenu)

        pygame.display.update()
        clock.tick(15)

#엔딩3전  17
def story11():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen=gameDisplay.blit(Img17,(0,0))
        nexts(ending3)

        pygame.display.update()
        clock.tick(15)

#엔딩3  18
def ending3():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen=gameDisplay.blit(Img18,(0,0))
        nexts(mainmenu)

        pygame.display.update()
        clock.tick(15)
        

#엔딩4 19
def ending4():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen=gameDisplay.blit(Img19,(0,0))
        nexts(fff)

        pygame.display.update()
        clock.tick(15)
        

#거짓말들킴 20
def story12():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen=gameDisplay.blit(Img20,(0,0))
        nexts(story13)

        pygame.display.update()
        clock.tick(15)


#엔딩5전 21
def story13():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen=gameDisplay.blit(Img21,(0,0))
        nexts(ending5)

        pygame.display.update()
        clock.tick(15)

#엔딩5  22
def ending5():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen=gameDisplay.blit(Img22,(0,0))
        nexts(mainmenu)

        pygame.display.update()
        clock.tick(15)

#밥약고민 23
def choose6():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen=gameDisplay.blit(Img23,(0,0))
        choose(story14,story15)

        pygame.display.update()
        clock.tick(15)

#밥먹다현타 24
def story14():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen=gameDisplay.blit(Img24,(0,0))
        nexts(ending6)

        pygame.display.update()
        clock.tick(15)

#엔딩6 25
def ending6():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen=gameDisplay.blit(Img25,(0,0))
        nexts(mainmenu)

        pygame.display.update()
        clock.tick(15)

#대출전화전 26
def story15():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen=gameDisplay.blit(Img26,(0,0))
        nexts(choose7)

        pygame.display.update()
        clock.tick(15)

#대출전화고민 27
def choose7():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen=gameDisplay.blit(Img27,(0,0))
        choose(story16,story18)

        pygame.display.update()
        clock.tick(15)

#가족대출 28
def story16():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen=gameDisplay.blit(Img28,(0,0))
        nexts(choose8)

        pygame.display.update()
        clock.tick(15)

#가족대출고민 29
def choose8():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen=gameDisplay.blit(Img29,(0,0))
        choose(story17,story18)

        pygame.display.update()
        clock.tick(15)

#투잡 30
def story17():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen=gameDisplay.blit(Img30,(0,0))
        nexts(ending7)

        pygame.display.update()
        clock.tick(15)
        
#엔딩7  31
def ending7():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen=gameDisplay.blit(Img31,(0,0))
        nexts(mainmenu)

        pygame.display.update()
        clock.tick(15)

#집뺏김 32
def story18():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen=gameDisplay.blit(Img32,(0,0))
        nexts(ending8)

        pygame.display.update()
        clock.tick(15)

#엔딩8  33
def ending8():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        selectscreen=gameDisplay.blit(Img33,(0,0))
        nexts(mainmenu)

        pygame.display.update()
        clock.tick(15)
    
mainmenu()
game_loop()
