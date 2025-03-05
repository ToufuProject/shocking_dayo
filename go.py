if game_over:
        font = pygame.font.SysFont(None, 74)
        text = font.render('GAME OVER', True, (255, 255, 255))
        text_rect = text.get_rect(center=(YOKO / 2, TATE / 2))
        screen.blit(text, text_rect)
        font_small = pygame.font.SysFont(None, 24)
        restart_text = font_small.render('Press Space to Restart', True, (255, 255, 255))
        restart_rect = restart_text.get_rect(center=(YOKO / 2, TATE / 2 + 70))
        screen.blit(restart_text, restart_rect)
    else:
        # 背景を真っ黒に塗りつぶす
        screen.fill((0, 0, 0))
        # 星を描画する
        draw_stars(screen, 2)
        hako.update()
        hako.draw(screen)
        teki_hako.update()
        teki_hako.draw(screen)


class Fireball(pygame.sprite.Sprite):
    """
    02-S06
    """
    def __init__(self, start_x, start_y, charged=False):
        pygame.sprite.Sprite.__init__(self)
        self.charged = charged
        self.speedx = -1
        self.speedy = 0
        if charged:
            """
            02-S05
            """
            size = (100, 100)  # チャージショットのサイズ
            self.image = pygame.image.load(MABUTA_DIR)  # 画像をロード
            self.image = pygame.transform.scale(self.image, size)  # 画像のサイズ調整
        else:
            size = (20, 20)  # 通常のファイヤーボールのサイズ
            self.image = pygame.Surface(size)
            self.image.fill((255, 165, 0))  # オレンジ色のファイヤーボール

        player.fireball_charge_start = None  # チャージ時間をリセット
        self.rect = self.image.get_rect(center=(start_x, start_y))

    def update(self):
        # ファイヤーボールを移動
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # 画面外に出たら消去
        if self.rect.right < 0 or self.rect.left > YOKO or self.rect.bottom < 0 or self.rect.top > TATE:
            self.kill()

        # 敵に当たったら消去
        enemy_hit_list = pygame.sprite.spritecollide(self, teki_hako, True)
        if enemy_hit_list:
            if not self.charged:
                self.kill()

