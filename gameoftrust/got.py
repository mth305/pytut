CHEAT = False
COOP  = True

POSDR = 2
NEGDR = 0
LOOSE = -1
WIN   = 3

def get_result(amove, bmove):
    if (amove == COOP) and (bmove == COOP):
        return POSDR, POSDR
    elif (amove == COOP) and (bmove == CHEAT):
        return LOOSE, WIN
    elif (amove == CHEAT) and (bmove == COOP):
        return WIN, LOOSE
    elif (amove == CHEAT) and (bmove == CHEAT):
        return NEGDR, NEGDR

def get_opponent(player, players):
    players = list(players)
    players.remove(player)
    opponent = players[0]
    return opponent

def sanity_check(moves, coins):
    p1, p2 = moves.keys()
    if len(moves[p1]) != len(moves[p2]):
        raise ValueError("The moves lists do not have same lenghts!")
    if len(coins[p1]) != len(coins[p2]):
        raise ValueError("The coins lists do not have same lenghts!")


def cheater(moves, player):
    return moves[player] + [CHEAT,]

def cooperator(moves, player):
    return moves[player] + [COOP,]

def copycat(moves, player):
    opponent = get_opponent(player, moves.keys())
    pmvs = moves[player]
    if len(pmvs) == 0:
        move = COOP
    else:
        move = moves[opponent][-1]
    return pmvs + [move,]

def grudger(moves, player):
    opponent = get_opponent(player, moves.keys())
    pmvs = moves[player]
    move = COOP
    if (len(pmvs) > 1) and (CHEAT in moves[opponent]):
        move = CHEAT
    return pmvs + [move,]

def detective(moves, player):
    opponent = get_opponent(player, moves.keys())
    pmvs = moves[player]
    omvs = moves[opponent]

    if len(pmvs) == 0:
        detective.strategy = "cheater"
    elif len(pmvs) >= 2:
        if (pmvs[-2] == CHEAT) and (omvs[-1] == CHEAT):
            detective.strategy = "copycat"

    if (len(pmvs) == 1):
        move = CHEAT
    elif (len(pmvs) < 4):
        move = COOP
    else:
        if detective.strategy == "cheater":
            move = CHEAT
        elif detective.strategy == "copycat":
            move = omvs[-1]
        else:
            raise ValueError(
                "'{}' is an unkown strategy!".format(detective.strategy))
    return pmvs + [move,]

def play(player1, player2, rounds, p1name=None, p2name=None):
    if p1name is None:
        p1name = player1.__name__
    if p2name is None:
        p2name = player2.__name__
    if p1name == p2name:
        p1name += "1"
        p2name += "2"
    moves = {p1name:[], p2name:[]}
    coins = {p1name:[], p2name:[]}

    for r in range(rounds):
        amoves = player1(moves, p1name)
        sanity_check(moves, coins)
        bmoves = player2(moves, p2name)
        sanity_check(moves, coins)
        moves[p1name] = amoves
        moves[p2name] = bmoves

        ca, cb = get_result(moves[p1name][-1], moves[p2name][-1])
        if len(coins[p1name]) == 0:
            coins[p1name].append(ca)
            coins[p2name].append(cb)
        else:
            coins[p1name].append(coins[p1name][-1] + ca)
            coins[p2name].append(coins[p2name][-1] + cb)

    return moves, coins


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    #from random import randint

    #rounds = randint(5, 10)
    rounds = 10

    player1 = detective
    player2 = copycat

    moves, coins = play(player1, player2, rounds)

    p1name, p2name = list(moves.keys())
    print("Result after {} rounds:".format(rounds))
    print("Player 1 ({:<10}): {:>4}".format(p1name, coins[p1name][-1]))
    print("Player 2 ({:<10}): {:>4}".format(p2name, coins[p2name][-1]))

    fig, ax = plt.subplots(1,2)
    ax[0].plot(moves[p1name], ".-")
    ax[0].plot(moves[p2name], "o-", alpha=0.5)
    ax[1].plot(coins[p1name], ".-", label=p1name)
    ax[1].plot(coins[p2name], "o-", alpha=0.5, label=p2name)
    ax[1].legend()
    plt.show()

