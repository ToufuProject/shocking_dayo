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