import curses
import time
import random

def main(stdscr):
    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Snake Game by Jaseunda")
        stdscr.refresh()
        time.sleep(2)

        curses.curs_set(0)
        sh, sw = 20, 60
        w = curses.newwin(sh, sw, 0, 0)

        snake = [[sh // 2, sw // 2]]
        snake_direction = (0, 1)

        food = [random.randint(1, sh - 2), random.randint(1, sw - 2)]

        w.timeout(100)
        w.keypad(1)

        while True:
            key = w.getch()

            if key == curses.KEY_UP and snake_direction[0] != 1:
                snake_direction = (-1, 0)
            elif key == curses.KEY_DOWN and snake_direction[0] != -1:
                snake_direction = (1, 0)
            elif key == curses.KEY_LEFT and snake_direction[1] != 1:
                snake_direction = (0, -1)
            elif key == curses.KEY_RIGHT and snake_direction[1] != -1:
                snake_direction = (0, 1)

            new_head = [snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1]]

            if new_head in snake or new_head[0] in (0, sh - 1) or new_head[1] in (0, sw - 1):
                break

            snake.insert(0, new_head)

            if new_head == food:
                food = [random.randint(1, sh - 2), random.randint(1, sw - 2)]
            else:
                snake.pop() 


            w.clear()
            for y, x in snake:
                w.addch(y, x, '■')
            w.addch(food[0], food[1], '*')
            w.refresh()

# USAGE
# if __name__ == '__main__':
#     curses.wrapper(main)
