#!/usr/bin/env python
import numpy as np
from urllib.request import urlopen

def random_grid(size):
    return np.random.randint(low=0, high=2, size=size)

def line_to_binary(line):
    line = line.replace(".", "0")
    line = line.replace("*", "1")
    return list(line)

def load_pattern(url):
    with urlopen(url) as page:
        string = page.read()
    grid = string.splitlines()
    grid = [line for line in grid if not line.startswith(b"#")]
    width = max([len(line) for line in grid])
    grid = [line.decode("utf-8")+"."*(width-len(line)) for line in grid]
    grid = [line_to_binary(line) for line in grid]
    return np.array(grid, dtype=int)

def evolve(grid):

    # boundary conditions
    pgrid = np.pad(grid, mode="wrap", pad_width=1)
    neighbors = pgrid[:-2,  :-2] + pgrid[1:-1, :-2] + pgrid[2:,  :-2] \
              + pgrid[:-2, 1:-1] +                  + pgrid[2:, 1:-1] \
              + pgrid[:-2, 2:  ] + pgrid[1:-1, 2:]  + pgrid[2:, 2:  ]

    alive = grid.astype(bool)

    # lonely
    grid[np.logical_and(alive, neighbors < 2)] = 0

    # alright & unnecessary
    # grid[np.logical_and(alive, np.logical_and(neighbors == 2, neighbors == 3))] = 1

    # overpopulation
    grid[np.logical_and(alive, neighbors > 3)] = 0

    # new life
    grid[np.logical_and(~alive, neighbors == 3)] = 1

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from utils import animate_imshow
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--pattern", type=str, default="",
                        help="Starting pattern. Available patterns:\
                        'gun', 'reflector' or 'spaceship'")
    parser.add_argument("--steps", "-s", type=int, default=200,
                        help="Number of steps to run.")
    args = parser.parse_args()

    if args.pattern == "gun":
        grid = load_pattern(
            "http://www.radicaleye.com/lifepage/patterns/p24gun/pic3.life")
    elif args.pattern == "reflector":
        grid = load_pattern(
            "http://www.radicaleye.com/lifepage/patterns/ssrefl/rle10.life")
    elif args.pattern == "spaceship":
        grid = load_pattern(
            "http://www.radicaleye.com/lifepage/patterns/newc5/rle3.life")
        grid = np.vstack((np.zeros(grid.shape), grid))
    else:
        size = (200,200)
        grid = random_grid(size)

    frames = []
    for s in range(args.steps):
        evolve(grid)
        frames.append(grid.copy())
    
    anim = animate_imshow(frames, cmap_name="viridis")
    plt.show()
