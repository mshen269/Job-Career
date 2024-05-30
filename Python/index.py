import pygame
from Sudoku import solve_sudoku
import random
import tkinter as tk
from tkinter import messagebox

# Define constants for the game
WINDOW_SIZE = 540
GRID_SIZE = 60
BACKGROUND_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
NUMBER_COLOR = (0, 0, 255)
HIGHLIGHT_COLOR = (173, 216, 230)

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption('Sudoku Solver')

# Load the font
font = pygame.font.SysFont(None, 55)

# Function to draw the grid
def draw_grid():
    for i in range(10):
        line_width = 5 if i % 3 == 0 else 1
        pygame.draw.line(screen, LINE_COLOR, (0, i * GRID_SIZE), (WINDOW_SIZE, i * GRID_SIZE), line_width)
        pygame.draw.line(screen, LINE_COLOR, (i * GRID_SIZE, 0), (i * GRID_SIZE, WINDOW_SIZE), line_width)

# Function to draw the numbers
def draw_numbers(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                number_text = font.render(str(board[i][j]), True, NUMBER_COLOR)
                screen.blit(number_text, (j * GRID_SIZE + 15, i * GRID_SIZE + 15))

# Function to update the display
def update_display(board):
    screen.fill(BACKGROUND_COLOR)
    draw_grid()
    draw_numbers(board)
    pygame.display.flip()

# Sudoku Solver function
def solve_sudoku(board):
    l = [0, 0]
    if not find_empty_location(board, l):
        return True
    row, col = l
    for num in range(1, 10):
        if check_location_is_safe(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

def find_empty_location(board, l):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                l[0] = row
                l[1] = col
                return True
    return False

def used_in_row(board, row, num):
    return any(board[row][col] == num for col in range(9))

def used_in_col(board, col, num):
    return any(board[row][col] == num for row in range(9))

def used_in_box(board, row, col, num):
    return any(board[i][j] == num for i in range(row - row % 3, row - row % 3 + 3) for j in range(col - col % 3, col - col % 3 + 3))

def check_location_is_safe(board, row, col, num):
    return not used_in_row(board, row, num) and not used_in_col(board, col, num) and not used_in_box(board, row, col, num)

def generate_sudoku():
    # Start with an empty board
    board = [[0 for _ in range(9)] for _ in range(9)]
    # Fill the diagonal 3x3 boxes
    for i in range(0, 9, 3):
        fill_diagonal_box(board, i, i)
    # Solve the complete board
    solve_sudoku(board)
    # Remove random elements to create the puzzle
    remove_elements(board, 20)
    return board

def fill_diagonal_box(board, row, col):
    nums = random.sample(range(1, 10), 9)
    k = 0
    for i in range(3):
        for j in range(3):
            board[row + i][col + j] = nums[k]
            k += 1

def remove_elements(board, count):
    while count > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        while board[row][col] == 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
        board[row][col] = 0
        count -= 1

def show_instructions():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    messagebox.showinfo("Instructions", "Press 'S' to solve, 'R' to refresh")
    root.destroy()

def main():
    running = True
    board = generate_sudoku()
    show_instructions()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    solve_sudoku(board)
                if event.key == pygame.K_r:
                    board = generate_sudoku()

        update_display(board)

    pygame.quit()

if __name__ == "__main__":
    main()

