import collections
from tournament import tournament, sorted_results, make_players
from got import cheater, cooperator, copycat, detective, grudger

def get_id(name):
    return int(name.split("#")[-1])

def set_id(name, newid):
    oldid = get_id(name)
    return name.replace(str(oldid), str(newid))

def get_func(name):
    func_name = name.split("#")[0]
    if func_name == "cheater":
        return cheater
    elif func_name == "cooperator":
        return cooperator
    elif func_name == "copycat":
        return copycat
    elif func_name == "detective":
        return detective
    elif func_name == "grudger":
        return grudger
    else:
        raise ValueError("Unkown player type: {}".format(func_name))

def next_players(results, nr_kick=5):
    maxid = max([get_id(name) for name, _ in results])
    best = [name for name, _ in results[:nr_kick]]
    best = [set_id(name, i+maxid+1) for i, name in enumerate(best)]
    rest = [name for name, _ in results[:-nr_kick]]
    pnames = best + rest
    return {name:get_func(name) for name in pnames}

def count_types(result, types):
    ptypes = [name.split("#")[0] for name, _ in result]
    ptypes = collections.Counter(ptypes)
    for t in types:
        if t not in ptypes:
            ptypes[t] = 0
    return ptypes


def simulation(init_players, rounds, steps, nr_kick):
    players = init_players
    results = []
    player_types = {name.split("#")[0] for name in players}
    evolution = {t:[] for t in player_types}
    results = []

    for s in range(steps):

        total_coins, _ = tournament(players, rounds)
        res = sorted_results(total_coins)
        players = next_players(res, nr_kick=nr_kick)

        ptypes = count_types(res, player_types)
        for t, cnt in ptypes.items():
            evolution[t].append(cnt)
        results.append(ptypes)
        print("Step: {:>3}".format(s), ptypes)
    return results, evolution

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    players = make_players(
        [copycat]*10 +\
        [cheater]*10 +\
        [grudger]*10 +\
        [detective]*10 +\
        [cooperator]*10
    )

    players = make_players(
        [cooperator]*18 + \
        [cheater] + \
        [copycat]
    )

    players = make_players(
        [cheater]*9 + \
        [cooperator]*9 + \
        [copycat]*3
    )


    rounds  = 20
    steps   = 50
    nr_kick = 5

    results, evolution = simulation(players, rounds, steps, nr_kick)

    for t, cnt in evolution.items():
        plt.plot(cnt, label=t)
    plt.legend()
    plt.show()
