import curses
import time
import random

def main(stdscr):
    curses.curs_set(0)
    sh, sw = stdscr.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)

    ball = [sh//2, sw//2]
    ball_velocity = [1, 1]

    paddle_height = 6
    paddle1 = [[sh//2 - paddle_height//2 + i, 1] for i in range(paddle_height)]
    paddle2 = [[sh//2 - paddle_height//2 + i, sw-2] for i in range(paddle_height)]

    def move_paddle(paddle, dy):
        new_paddle = [[y + dy, x] for y, x in paddle]
        if new_paddle[0][0] < 1 or new_paddle[-1][0] >= sh-1:
            return paddle
        return new_paddle

    def move_ball(ball, velocity):
        new_ball = [ball[0] + velocity[0], ball[1] + velocity[1]]
        return new_ball

    for y, x in paddle1 + paddle2:
        w.addch(y, x, '|')

    w.addch(ball[0], ball[1], 'o')
    w.timeout(100)
    w.keypad(1)

    while True:
        key = w.getch()

        # Move the player's paddle
        if key == curses.KEY_UP:
            paddle1 = move_paddle(paddle1, -1)
        elif key == curses.KEY_DOWN:
            paddle1 = move_paddle(paddle1, 1)

        if random.random() < 0.9:  # Occasionally, the AI paddle will not move
            if ball[0] < paddle2[0][0]:
                paddle2 = move_paddle(paddle2, -1)
            elif ball[0] > paddle2[-1][0]:
                paddle2 = move_paddle(paddle2, 1)

        ball = move_ball(ball, ball_velocity)

        if ball[0] in (1, sh - 2):
            ball_velocity[0] *= -1
        if ball[1] in (1, sw - 2):
            ball_velocity[1] *= -1
        if ball in paddle1 or ball in paddle2:
            ball_velocity[1] *= -1

        w.clear()
        for y, x in paddle1 + paddle2:
            w.addch(y, x, '|')
        w.addch(ball[0], ball[1], 'o')
        w.refresh()

# USAGE
# if __name__ == '__main__':
#     curses.wrapper(main)
