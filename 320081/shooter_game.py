from models import *

display.set_caption("пау пау ева онлайн для нищих")
background = transform.scale(image.load("galaxy.jpg"), WINDOW_SIZE)

mixer.music.load("space.ogg")
mixer.music.set_volume(0.05)
mixer.music.play()

player = Player("rocket.png", 250, WINDOW_SIZE[1] - SPSize[1], 10)

enemies = sprite.Group()
for i in range(5):
    enemies.add(Enemy("ufo.png", randint(0, WINDOW_SIZE[1] - SPSize[1]), 
    randint(-100, 100), randint(1, 4)))

clock = time.Clock()

game_over = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not game_over:
        window.blit(background, (0, 0))
        player.update_position()
        player.reset()
        player.fire()

        enemies.draw(window)
        enemies.update()

        bullets.draw(window)
        bullets.update()

        counter.show() 
        clock.tick(FPS)
        display.update()











понял