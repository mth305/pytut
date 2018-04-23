import itertools
from got import cheater, cooperator, copycat, detective, grudger, play

def get_unique_games(players):
    perms = itertools.permutations(players, r=2)
    games = {tuple(sorted(p)) for p in perms}
    return games

def tournament(players, rounds, verbose=False):
    total_coins = {p:0 for p in players}
    all_coins   = {p:[] for p in players}
    
    games = get_unique_games(players)
    
    for match, (p1name, p2name) in enumerate(games):
    
        p1func = players[p1name]
        p2func = players[p2name]
        moves, coins = play(
            p1func, p2func, rounds, p1name=p1name, p2name=p2name)
    
        total_coins[p1name] += coins[p1name][-1]
        total_coins[p2name] += coins[p2name][-1]
    
        all_coins[p1name].append(coins[p1name][-1])
        all_coins[p2name].append(coins[p2name][-1])
    
        if verbose:
            msg = "#{:0>3} {:<10}/{:>10} {}".format(
                match, p1name, p2name, total_coins)
            print(msg)
    return total_coins, all_coins

def make_players(players):
    return {p.__name__+"#"+str(i):p for i,p in enumerate(players)}

def sorted_results(total_coins):
    res = sorted(total_coins.items(), key=lambda x:x[1])
    return res[::-1]

if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt

    rounds = 50
    players = make_players([copycat, cheater, cooperator, grudger, detective])

    total_coins, all_coins = tournament(players, rounds, verbose=True)

    results = sorted_results(total_coins)
    for player, coins in results:
        print(player, coins)
    
    for player, coins in all_coins.items():
        plt.plot(np.cumsum(coins), label=player)
    plt.legend()
    plt.show()
