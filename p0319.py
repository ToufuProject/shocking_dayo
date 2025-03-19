""""
今日のにゅめー

その０：デバッグ
その１：ちょっとしたコツ
teki_detekuru_kankaku
saigo_teki_detekara_keika_jikan
game_over
の位置について
その２：ファイヤーボールを修正(押しっぱなし問題の解決) ← これがむずいmemo.txtを見てみよう！
その３：リスタート
"""


import pygame
import os
import random

TATE = 900
YOKO = 1200
TITLE = "TAKOYAKI OISHI"
BASE_DIR = os.path.dirname(__file__)
IMG_DIR = os.path.join(BASE_DIR, "imgs")
PLAYER_DIR = os.path.join(IMG_DIR, "resized_ningen2025.png")
BOSS_DIR = os.path.join(IMG_DIR, "mabuta.png")
# ゲーム上の物体をしまう箱
all_sprites = pygame.sprite.Group()
# てきをしまう箱
teki_hako = pygame.sprite.Group()

pygame.init()
screen = pygame.display.set_mode((YOKO, TATE))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32, 32))
        self.gazou = pygame.image.load(PLAYER_DIR).convert()
        self.image.blit(self.gazou, (0,0),(0,0,32,32))
        iro = self.image.get_at((0,0))
        self.image.set_colorkey(iro)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.vx = 0
        self.vy = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] == True:
            self.vx = 1
        elif keys[pygame.K_LEFT] == True:
            self.vx = -1
        elif keys[pygame.K_UP] == True:
            self.vy = -1
        elif keys[pygame.K_DOWN] == True:
            self.vy = 1
        else:
            self.vx = 0
            self.vy = 0
        self.rect.x += self.vx
        self.rect.y += self.vy
        # もしもスペースを押したらファイヤーボールを出す
        # ファイヤーボールを初期化して、それをall_spritesにしまう



class Teki(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32, 32))
        self.gazou = pygame.image.load(PLAYER_DIR).convert()
        self.image.blit(self.gazou, (0, 0), (0, 0, 32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = random.randint(0, 300)
        self.vx = 1
        self.vy = 0

    def update(self):
        self.rect.x += self.vx


class Fireball(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        size = (16,16)
        self.image = pygame.Surface(size)
        self.image.fill((255,0,0))
        self.vx = -1
        self.rect = self.image.get_rect(center=(x,y))

    def update(self):
        self.rect.x += self.vx
        pygame.sprite.spritecollide(self, teki_hako, dokill=True)



# ボスを作ろう
# ボスの画像はBOSS_DIR
# ボスのパラメーター：サイズ、速さ、ライフ、

player = Player()
all_sprites.add(player)
teki_detekuru_kankaku = 0
saigo_teki_detekara_keika_jikan = 0

game_over = False

kurikaeshi = True
while kurikaeshi:
    current_time = pygame.time.get_ticks() / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            kurikaeshi = False

    teki_detekuru_kankaku = 1.5
    if current_time - saigo_teki_detekara_keika_jikan > teki_detekuru_kankaku:
        teki = Teki()
        teki_hako.add(teki)
        saigo_teki_detekara_keika_jikan = current_time
    atari = pygame.sprite.spritecollide(player, teki_hako, dokill=True)
    if atari:
        game_over = True

    if game_over:
        font = pygame.font.SysFont(None, 74)
        text = font.render('IKEMEN TAKAHASHI', True, (255, 255, 255))
        text_rect = text.get_rect(center=(YOKO / 2, TATE / 2))
        screen.blit(text, text_rect)
        font_small = pygame.font.SysFont(None, 24)
        restart_text = font_small.render('Press Space to Restart', True, (255, 255, 255))
        restart_rect = restart_text.get_rect(center=(YOKO / 2, TATE / 2 + 70))
        screen.blit(restart_text, restart_rect)
        # その３：リスタートモード
        # リスタート判定
        # pygame.key.get_pressed()でボタンの状態チェック
        # もしもスペースが押されていたら敵の箱とキャラクターを入れる箱を空っぽにする(箱.empty())
        # プレイヤーを初期化する
        # プレイヤーを箱に追加する
        # ゲームオーバーのフラッグをFalseにする
    else:
        screen.fill((0, 0, 0))
        all_sprites.update()
        all_sprites.draw(screen)
        teki_hako.update()
        teki_hako.draw(screen)
    pygame.display.flip()
pygame.quit()
