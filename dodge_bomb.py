import os
import sys
import pygame as pg
import time
import random

WIDTH, HEIGHT = 1600, 900
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def bound (obj_rct)-> tuple[bool,bool]:

    """
    工科トンRectまたは爆弾Rectの画面または爆弾Rect内外反転用の関数
    引数:こうかとん Rect
    も土井r値:横方向判定結果,縦方向判定結果(Ture:画面内/False:画面外)
    """
    yoko,tate =True,True
    if obj_rct.left<0 or obj_rct.right>WIDTH:
        yoko = False
    if obj_rct.top<0 or obj_rct.bottom>HEIGHT:
        tate = False 
    return yoko,tate


def kattoin():
    pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 2.0)
    kattoin_img=pg.Surface((WIDTH,HEIGHT))    
    font = pg.font.Font(None,80)
    kattoin_img.set_alpha(160)  #半透明
    kattoin_rct=kattoin_img.get_rect()
    kattoin_rct.center=WIDTH/2,HEIGHT/2   #位置の設定
    txt=font.render("激熱",True,(255,255,255))    #文字の設定
    Brackout=pg.draw.rect(kattoin_img,(0,0,0),(0,0,WIDTH,HEIGHT))
    clear_img=pg.Surface((WIDTH,HEIGHT))
    clear_rct=clear_img.get_rect()
    clear_rct.center=WIDTH/2,HEIGHT/2
    txt_c=font.render("クリア",True,(255,255,255))
    clear_=pg.draw.rect(clear_img,(0,0,0),(0,0,WIDTH,HEIGHT))

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")    
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 2.0)
    kk_img2=pg.transform.rotozoom(pg.image.load("fig/8.png"), 0, 2.0)    #こうかとんの画像の取得
    kk_rct = kk_img.get_rect()         
    kk_rct2=kk_img2.get_rect()        #こうかとんの位置の取得
    kk_rct.center = 900, 400
    clock = pg.time.Clock()
    tmr = 0
    
    accs = [a for a in range(1,11)]


#ブラックアウトの設定
    Brackout_img=pg.Surface((WIDTH,HEIGHT))    
    font = pg.font.Font(None,80)
    Brackout_img.set_alpha(160)  #半透明
    Brackout_rct=Brackout_img.get_rect()
    Brackout_rct.center=WIDTH/2,HEIGHT/2   #位置の設定
    txt=font.render("GAME OVER",True,(255,255,255))    #文字の設定
    Brackout=pg.draw.rect(Brackout_img,(0,0,0),(0,0,WIDTH,HEIGHT))


    bom_img= pg.Surface((20,20))
    bom_rct=bom_img.get_rect()
    bom_img.set_colorkey((0,0,0))
    bom_rct.center=random.randint(0,WIDTH),random.randint(0,HEIGHT)
    pg.draw.circle(bom_img,(255,0,0),(10,10),10)
    vx,vy =+5,+5
    key_dic={pg.K_UP:(0,-5),pg.K_DOWN:(0,+5),pg.K_LEFT:(-5,0),pg.K_RIGHT:(+5,0)} #移動量辞書
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        if kk_rct.colliderect(bom_rct) ==True:    #こうかとんと爆弾が当たったとき
            screen.blit(Brackout_img,Brackout_rct)
            screen.blit(txt,[WIDTH/2 - 170, HEIGHT/2 - 40])
            pg.display.update()
            screen.blit(kk_img2, kk_rct2)
            pg.display.update()
            pg.time.wait(5000)  
            return 
        key_1=pg.key.get_pressed()
        if key_1[pg.K_SPACE]:    #スペースキーを押した時
            pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 2.0)
            kattoin_img=pg.Surface((WIDTH,HEIGHT))    
            font = pg.font.Font(None,80)
            kattoin_rct=kattoin_img.get_rect()
            kattoin_rct.center=WIDTH/2,HEIGHT/2   #位置の設定
            txt_1=font.render("CLEAR",True,(255,255,255))    #文字の設定
            Brackout=pg.draw.rect(kattoin_img,(0,0,0),(0,0,WIDTH,HEIGHT))
            clear_img=pg.Surface((WIDTH,HEIGHT))
            clear_rct=clear_img.get_rect()
            clear_rct.center=WIDTH/2,HEIGHT/2
            
            screen.blit(kattoin_img,kattoin_rct)
            screen.blit(txt_1,[WIDTH/2 - 170, HEIGHT/2 - 40])
            pg.display.update()
            pg.display.update()
            pg.time.wait(6000) 
            pg.display.update()
            

            return 
        screen.blit(bg_img, [0, 0]) 

        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for k,v in key_dic.items():
            if key_lst[k]:
                sum_mv[0]+=v[0]
                sum_mv[1]+=v[1]
        kk_rct.move_ip(sum_mv)





        if bound(kk_rct) !=(True,True):
            kk_rct.move_ip(-sum_mv[0],-sum_mv[1])

        bom_rct.move_ip(vx,vy)
        yoko,tate=bound(bom_rct)
        screen.blit(kk_img, kk_rct)
        screen.blit(bom_img, bom_rct)
        yoko,tate=bound(bom_rct)
        if not yoko:
            vx*=-1
        if not tate:
            vy*=-1

        pg.display.update()
        tmr += 1
        clock.tick(50)



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
