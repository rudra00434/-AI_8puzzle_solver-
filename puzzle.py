import time
from copy import deepcopy

import pygame

from game.generate_puzzle import GeneratePuzzle
from game.button import Button
from game.highlight_digit import HighlightDigit
from sol.solution import Solution


class Puzzle:
    def __init__(self):
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

        self.dist = 200

        pygame.init()
        pygame.font.init()

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption('### 8 numbers sorting Puzzle ###')
        self.screen.fill(self.black)

        self.generate_puzzle = GeneratePuzzle(self.screen)
        self.highlight = HighlightDigit(self.screen)

    def initialization(self):

        self.puzzle_numbers = self.generate_puzzle.generate_puzzle()
        self.generate_puzzle.draw_puzzle(self.puzzle_numbers)
        solve_button = Button(self.screen, (255, 255, 153), 450, 100, 100, 50, "Solve")
        solve_button.draw((255, 255, 0))

        # self.h_digit_x = 100
        # self.h_digit_y = 100

        self.finish = False
        self.you_win = False

        while not self.finish:
            self.highlight.move_count("8 Puzzle Puzzle", 130, 10)
            solve_button.draw((255, 255, 0))

            for event in pygame.event.get():

                pos = pygame.mouse.get_pos()
                # print(event)
                if event.type == pygame.QUIT:
                    self.finish = True

                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_RIGHT):
                        # print "*** RIGHT ***"
                        self.you_win = self.highlight.highlight_digit_to_be_swapped(100, 0, "RIGHT",
                                                                                    self.puzzle_numbers)
                        self.generate_puzzle.draw_puzzle(self.puzzle_numbers)

                    if (event.key == pygame.K_LEFT):
                        # print "*** LEFT ***"
                        self.you_win = self.highlight.highlight_digit_to_be_swapped(-100, 0, "LEFT",
                                                                                    self.puzzle_numbers)
                        self.generate_puzzle.draw_puzzle(self.puzzle_numbers)

                    if (event.key == pygame.K_DOWN):
                        # print "*** DOWN ***"
                        self.you_win = self.highlight.highlight_digit_to_be_swapped(0, 100, "DOWN",
                                                                                    self.puzzle_numbers)
                        self.generate_puzzle.draw_puzzle(self.puzzle_numbers)

                    if (event.key == pygame.K_UP):
                        # print "*** UP ***"
                        self.you_win = self.highlight.highlight_digit_to_be_swapped(0, -100, "UP",
                                                                                    self.puzzle_numbers)
                        self.generate_puzzle.draw_puzzle(self.puzzle_numbers)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if solve_button.isOver(pos):
                        print("You Clicked Solve button")
                        self.solution = Solution(self.puzzle_numbers)

                        path = self.get_sol()

                        print("BOARD PATH: %s" % deepcopy(self.solution.sol_stack))
                        for i, puzzle in enumerate(reversed(path)):
                            # print puzzle
                            self.screen.fill(self.black)
                            self.highlight.move_count("8 Puzzle Puzzle", 130, 10)
                            solve_button.draw((255, 255, 0))
                            self.generate_puzzle.draw_puzzle(puzzle)
                            self.highlight.move_count("Moves: %s" % str(i))
                            pygame.display.update()
                            # self.clock.tick(30)

                            time.sleep(0.4)
                        self.you_win = True

                if event.type == pygame.MOUSEMOTION:
                    if solve_button.isOver(pos):
                        solve_button.color = (0, 204, 0)
                    else:
                        solve_button.color = (255, 255, 0)

                if self.you_win:
                    self.highlight.move_count("8 Puzzle Puzzle", 130, 10)
                    self.highlight.move_count("You Win !!!", 130, 450)
                    pygame.display.update()
                    self.clock.tick(30)
                    time.sleep(2)
                    self.screen.fill(self.black)
                    self.puzzle_numbers = self.generate_puzzle.generate_puzzle()
                    self.highlight.m_count = 0
                    self.you_win = self.highlight.highlight_digit_to_be_swapped(0, -100, "UP",
                                                                                self.puzzle_numbers)
                    self.generate_puzzle.draw_puzzle(self.puzzle_numbers)

                    self.you_win = False
                    self.finish = False

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
        quit()

    def get_sol(self):
        path = []
        counter = 0
        while (counter < 30):
            self.solution.solution()

            print("SP: %d" % len(self.solution.sol_stack))
            print("SP: %d" % len(path))
            if len(path) == 0 or len(self.solution.sol_stack) < len(path):
                print("IN")
                path = deepcopy(self.solution.sol_stack)
                print(len(path))
                # moves = pygame.draw.rect(self.screen, self.white, [10, 10, 100, 20], 5)
                # self.highlight.move_count("Got solution with moves %d, seeking for better"%len(path), 500, 100)
            if len(self.solution.sol_stack) < 30:
                path = self.solution.sol_stack
                break
            del self.solution.sol_stack[:]
            del self.solution.open_stack[:]
            del self.solution.closed_stack[:]
            del self.solution.sol_stack[:]
            counter += 1
            print(counter)

        print("FINAL PATH: %s" % path)
        print(len(path))
        return path


if __name__ == '__main__':
    puzzle = Puzzle()
    puzzle.initialization()