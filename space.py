import curses
import random
import time

def main(stdscr):
    # Clear screen
    stdscr.clear()

    # Get screen dimensions
    rows, columns = stdscr.getmaxyx()
    print(rows, columns)
    # middle of the screen
    x_midle, y_midle = int(columns/2), int(rows/2)
    # ship position
    x0, y0 = x_midle, y_midle+10
    # Initialize asteroids
    stdscr.keypad(True)
    stdscr.nodelay(True)
    asteroids = []
    points = 0
    # asteroids inital position
    for i in range(100):
        x = random.randint(0, columns-1)
        y = random.randint(0, rows-1)
        asteroids.append((x, y))
    ship = "A"
    delta = 0
    result = 0.1
    while True:
        # Clear screen
        stdscr.clear()
        # Move asteroids
        new_asteroids = []
        for x, y in asteroids:
            y += 1
            if y < rows:
                new_asteroids.append((x, y))
        asteroids = new_asteroids

        # Add new asteroids
        if len(asteroids) < 100:
            x = random.randint(0, columns-1)
            y = 0
            asteroids.append((x, y))

        # Draw asteroids
        for x, y in asteroids:
            try:
                stdscr.addstr(y, x, "o")
            except curses.error:
                pass

        # Print points
        try:
            stdscr.addstr(y0, x0, ship)
            points += 1
            stdscr.addstr(0, 0, "Points: " + str(points))
            stdscr.refresh()
        except curses.error:
            pass
        # Get input keys
        key = stdscr.getch()
        if key == curses.KEY_RIGHT:
            x0 += 1
        elif key == curses.KEY_LEFT:
            x0 -= 1
        # game over condition
        for x, y in asteroids:
            if x == x0 and y == y0:
                ship = "X"
                stdscr.addstr(y0, x0, ship)
                stdscr.addstr(y_midle, x_midle, "GAME OVER")
                stdscr.refresh()
                time.sleep(5)
                quit()
        # Acelarate Game
        if result >= 0.01:
            delta += 0.0001
            sleep = 0.1
            result = sleep - delta

        time.sleep(result)

curses.wrapper(main)