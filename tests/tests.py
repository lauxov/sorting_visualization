import random
import pygame
import sys
import argparse
from typing import List

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--sort', default='bubble', help='sorting algorithm (bubble, selection, insertion, quick)')
args = parser.parse_args()

# Initialize Pygame and load sounds
pygame.init()
pygame.mixer.init()
swap_sound = pygame.mixer.Sound('swap.wav')
success_sound = pygame.mixer.Sound('success.mp3')

# Config
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = (255, 255, 255)
BAR_COLOR = (0, 0, 255)
SORTED_COLOR = (0, 255, 0)
BAR_WIDTH = 5
BAR_SPACING = 1

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Sort')

NUM_BARS = (SCREEN_WIDTH - BAR_SPACING) // (BAR_WIDTH + BAR_SPACING)
BAR_HEIGHTS = [random.randint(1, SCREEN_HEIGHT) for i in range(NUM_BARS)]

def is_sorted(arr: List[int]) -> bool:
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def draw_bars(arr: List[int], sorted: bool = False) -> None:
    SCREEN.fill(BG_COLOR)
    for i, height in enumerate(arr):
        x = i * (BAR_WIDTH + BAR_SPACING) + BAR_SPACING
        y = SCREEN_HEIGHT - height
        color = SORTED_COLOR if sorted else BAR_COLOR
        rect = pygame.Rect(x, y, BAR_WIDTH, height)
        pygame.draw.rect(SCREEN, color, rect)
    pygame.display.update()

def bubble_sort(arr: List[int]) -> None:
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
        if not swapped:
            break
    draw_bars(arr, sorted=True)
    success_sound.play()

def selection_sort(arr: List[int]) -> None:
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            draw_bars(arr)
            pygame.time.Clock().tick(60)
    draw_bars(arr, sorted=True)
    success_sound.play()

def insertion_sort(arr: List[int]) -> None:
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        left = 0
        right = i - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < key:
                left = mid + 1
            else:
                right = mid - 1
        for j in range(i-1, left-1, -1):
            arr[j+1] = arr[j]
        arr[left] = key
        draw_bars(arr)
        pygame.time.Clock().tick(60)
    draw_bars(arr, sorted=True)
    success_sound.play()

def quick_sort(arr: List[int], low: int, high: int) -> None:
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)

def partition(arr: List[int], low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            draw_bars(arr)
            pygame.time.Clock().tick(60)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    draw_bars(arr)
    pygame.time.Clock().tick(60)
    return i + 1

# It's part of parser (line 7)
if args.sort == 'bubble':
    bubble_sort(BAR_HEIGHTS)
elif args.sort == 'selection':
    selection_sort(BAR_HEIGHTS)
elif args.sort == 'insertion':
    insertion_sort(BAR_HEIGHTS)
elif args.sort == 'quick':
    quick_sort(BAR_HEIGHTS, 0, len(BAR_HEIGHTS) - 1)

draw_bars(BAR_HEIGHTS)

success_sound.play()
draw_bars(BAR_HEIGHTS, sorted=True)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
