import numpy as np
import collections
import matplotlib.pyplot as plt
import seaborn as sns
 
COLORS = sns.color_palette("muted")

def total_count(counter):
    cnt = 0
    for _, c in counter.items():
        cnt += c
    return cnt

def plot_counter(counter, ax_label):
    cnt = total_count(counter)
    phi = np.linspace(0., 2*np.pi, cnt)

    ax = plt.subplot(111, polar=True, label=ax_label)
    ax.set_rmax(2)

    i = 0
    for color, (key, value) in zip(COLORS, sorted(counter.items())):
        for _ in range(value):
            ax.plot(phi[i], 1, "o", color=color, markersize=10, label=key)
            i += 1
    ax.legend()
    return (ax,)

if __name__ == "__main__":
    from simulation import simulation
    from tournament import make_players
    from got import copycat, cheater, grudger, detective, cooperator

    players = make_players(
        [copycat]*10 +\
        [cheater]*10 +\
        [grudger]*10 +\
        [detective]*10 +\
        [cooperator]*10
    )

    player_types = {name.split("#")[0] for name in players}

    rounds  = 20
    steps   = 50
    nr_kick = 5

    results, _ = simulation(players, rounds, steps, nr_kick)
    for i, cntr in enumerate(results):
        ax = plot_counter(cntr, i)
        fname = "{:0>4}.png".format(i)
        plt.savefig(fname)
        print("Saved result as:", fname)


