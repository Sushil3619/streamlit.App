
import streamlit as st
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the display
win = pygame.display.set_mode((WIDTH, HEIGHT))

class SnakeGame:
    def __init__(self):
        self.snake = [(200, 200), (220, 200), (240, 200)]
        self.direction = 'RIGHT'
        self.apple = self.generate_apple()

    def generate_apple(self):
        return (random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
                random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)

    def play(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != 'DOWN':
                        self.direction = 'UP'
                    elif event.key == pygame.K_DOWN and self.direction != 'UP':
                        self.direction = 'DOWN'
                    elif event.key == pygame.K_LEFT and self.direction != 'RIGHT':
                        self.direction = 'LEFT'
                    elif event.key == pygame.K_RIGHT and self.direction != 'LEFT':
                        self.direction = 'RIGHT'

            # Move the snake
            head = self.snake[-1]
            if self.direction == 'UP':
                new_head = (head[0], head[1] - BLOCK_SIZE)
            elif self.direction == 'DOWN':
                new_head = (head[0], head[1] + BLOCK_SIZE)
            elif self.direction == 'LEFT':
                new_head = (head[0] - BLOCK_SIZE, head[1])
            elif self.direction == 'RIGHT':
                new_head = (head[0] + BLOCK_SIZE, head[1])

            self.snake.append(new_head)

            # Check for collision with apple
            if self.snake[-1] == self.apple:
                self.apple = self.generate_apple()
            else:
                self.snake.pop(0)

            # Check for collision with wall or self
            if (self.snake[-1][0] < 0 or self.snake[-1][0] >= WIDTH or
                    self.snake[-1][1] < 0 or self.snake[-1][1] >= HEIGHT or
                    self.snake[-1] in self.snake[:-1]):
                break

            # Draw everything
            win.fill((0, 0, 0))
            for pos in self.snake:
                pygame.draw.rect(win, GREEN, (pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(win, RED, (self.apple[0], self.apple[1], BLOCK_SIZE, BLOCK_SIZE))
            pygame.display.update()

            clock.tick(10)

def main():
    st.title("Snake Game")
    if st.button("Play"):
        game = SnakeGame()
        game.play()

if __name__ == "__main__":
    main()
