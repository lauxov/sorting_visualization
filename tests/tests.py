import random
import pygame
import sys

pygame.mixer.init()
swap_sound = pygame.mixer.Sound('swap.wav')
success_sound = pygame.mixer.Sound('success.mp3')

screen_width = 800
screen_height = 600
bg_color = (255, 255, 255)
bar_color = (0, 0, 255)
sorted_color = (0, 255, 0)

bar_width = 5
bar_spacing = 1

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Sort')

num_bars = (screen_width - bar_spacing) // (bar_width + bar_spacing)
bar_heights = [random.randint(1, screen_height) for i in range(num_bars)]

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                draw_bars(arr)
                pygame.time.Clock().tick(60)
        if swapped:
            swap_sound.play()
    draw_bars(arr, sorted=True)
    success_sound.play()

def draw_bars(arr, sorted=False):
    screen.fill(bg_color)
    for i, height in enumerate(arr):
        x = i * (bar_width + bar_spacing) + bar_spacing
        y = screen_height - height
        color = sorted_color if sorted else bar_color
        rect = pygame.Rect(x, y, bar_width, height)
        pygame.draw.rect(screen, color, rect)
    pygame.display.update()

draw_bars(bar_heights)
bubble_sort(bar_heights)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
