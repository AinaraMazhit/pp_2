import pygame
from snake import Snake
from food import Food
from utils import save_game, load_game

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

snake = Snake((100, 100))
food = Food()
food.respawn(snake.body)  # первая генерация еды

score = 0
level = 1
font = pygame.font.SysFont(None, 30)

running = True

while running:
    screen.fill((0, 0, 0))  # очистка экрана

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Управление
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != (0, 20):
                snake.direction = (0, -20)
            elif event.key == pygame.K_DOWN and snake.direction != (0, -20):
                snake.direction = (0, 20)
            elif event.key == pygame.K_LEFT and snake.direction != (20, 0):
                snake.direction = (-20, 0)
            elif event.key == pygame.K_RIGHT and snake.direction != (-20, 0):
                snake.direction = (20, 0)
            elif event.key == pygame.K_s:
                save_game(snake, score, level)
            elif event.key == pygame.K_l:
                score, level = load_game(snake)

    snake.move()

    # Проверка столкновений
    if snake.check_collision():
        print("Game Over!")
        running = False

    # Проверка поедания еды
    if snake.body[0] == food.position:
        snake.grow()
        food.respawn(snake.body)
        score += 10

    
    current_time = pygame.time.get_ticks()
    if current_time - food.spawn_time >= 5000:
        food.respawn(snake.body)


    # Рисуем змею
    for block in snake.body:
        pygame.draw.rect(screen, (0, 255, 0), (*block, 20, 20))

    # Рисуем еду
    pygame.draw.rect(screen, (255, 0, 0), (*food.position, 20, 20))

    # Счёт
    score_text = font.render(f"Score: {score}  Level: {level}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
