"""
Filename: SudokuSolver.py
Author: James Shih
"""

import time


def main():
    start = time.time()
    game_board, unsolved, maybe_d = init_game()
    zones = define_zone(game_board)
    print_game(game_board)
    game_solver(game_board, zones, maybe_d)
    end = time.time()
    print('Spent:', end-start, 'seconds')


def game_solver(gb, zones, maybe_d):
    while check_unsolved(gb):
        for i in range(len(gb)):
            for j in range(len(gb[i])):
                if (i, j) in maybe_d:
                    search(i, j, gb, zones, maybe_d)
            # print(maybe_d)
    print_game(gb)


def check_unsolved(gb):
    for row in gb:
        for col in row:
            if col == '-':
                return True
    return False


def search(i, j, gb, zones, maybe_d):
    for num in gb[i]:
        if num.isdigit():
            if num in maybe_d[(i, j)]['maybe']:
                maybe_d[(i, j)]['maybe'].remove(num)
    for row in range(len(gb)):
        num = gb[row][j]
        if num.isdigit():
            if num in maybe_d[(i, j)]['maybe']:
                maybe_d[(i, j)]['maybe'].remove(num)
    cur_zone = zones[(i, j)]
    for coord in zones:
        if zones[coord] == cur_zone:
            new_i, new_j = coord
            num = gb[new_i][new_j]
            if num.isdigit():
                if num in maybe_d[(i, j)]['maybe']:
                    maybe_d[(i, j)]['maybe'].remove(num)
    if len(maybe_d[(i, j)]['maybe']) == 1:
        gb[i][j] = str(maybe_d[(i, j)]['maybe'][0])


def define_zone(gb):
    zones = {}
    for i in range(len(gb)):
        for j in range(len(gb[i])):
            if i < 3 and j < 3:
                zones[(i, j)] = 'upper_l'
            elif i < 3 and 3 <= j < 6:
                zones[(i, j)] = 'upper_m'
            elif i < 3 and 6 <= j < 9:
                zones[(i, j)] = 'upper_r'
            elif 3 <= i < 6 and j < 3:
                zones[(i, j)] = 'mid_l'
            elif 3 <= i < 6 and 3 <= j < 6:
                zones[(i, j)] = 'mid_m'
            elif 3 <= i < 6 and 6 <= j < 9:
                zones[(i, j)] = 'mid_r'
            elif 6 <= i < 9 and j < 3:
                zones[(i, j)] = 'lower_l'
            elif 6 <= i < 9 and 3 <= j < 6:
                zones[(i, j)] = 'lower_m'
            else:
                zones[(i, j)] = 'lower_r'
    return zones


def print_game(game_board):
    print('  ==============SUDOKU SOLVER==============')
    for row in game_board:
        print(row)


def init_game():
    maybe_d = {}
    game_board = [[], [], [], [], [], [], [], [], []]
    row = 0
    unsolved = 0
    with open('test.txt') as f:
        for line in f:
            line = line.strip()
            col = 0
            for ele in line:
                game_board[row].append(ele)
                if ele == '-':
                    unsolved += 1
                    maybe_d[(row, col)] = {'maybe': ['1', '2', '3', '4', '5', '6', '7', '8', '9']}
                col += 1
            row += 1
    return game_board, unsolved, maybe_d


def show_sol():
    sol_board = [[], [], [], [], [], [], [], [], []]
    row = 0
    with open('solution.txt') as f:
        for line in f:
            line = line.strip()
            for ele in line:
                sol_board[row].append(ele)
            row += 1
    print(' ==============SUDOKU SOLUTION==============')
    for row in sol_board:
        print(row)


if __name__ == '__main__':
    main()
