from os.path import join, dirname, realpath

PLAYER_HP = 50
PLAYER_MANA = 500
with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    for line in f:
        n = int(line.split(": ")[-1])
        if line.startswith("H"):
            BOSS_HP = n
        elif line.startswith("D"):
            BOSS_AD = n

COSTS = [53, 73, 113, 173, 229]


def get_min(boss_hp, player_hp, player_mana, timer_shield=0, timer_poison=0, timer_recharge=0, cost=0,
            players_turn=True):
    # Handle active effects
    player_armor = 0
    if timer_shield > 0:
        player_armor = 7
        timer_shield -= 1
    if timer_poison > 0:
        boss_hp -= 3
        timer_poison -= 1
    if timer_recharge > 0:
        player_mana += 101
        timer_recharge -= 1

    if players_turn:
        player_hp -= 1
        if player_hp <= 0:
            return float("inf")

    if boss_hp <= 0:
        return cost

    if players_turn:
        min_cost = float("inf")
        for i in range(5):
            if player_mana < COSTS[i]:
                continue
            new_player_mana = player_mana - COSTS[i]
            new_boss_hp = boss_hp
            new_player_hp = player_hp
            new_cost = cost + COSTS[i]
            new_timer_shield = timer_shield
            new_timer_poison = timer_poison
            new_timer_recharge = timer_recharge

            if i == 0:
                new_boss_hp -= 4
            elif i == 1:
                new_boss_hp -= 2
                new_player_hp += 2
            elif i == 2 and timer_shield == 0:
                new_timer_shield = 6
            elif i == 3 and timer_poison == 0:
                new_timer_poison = 6
            elif i == 4 and timer_recharge == 0:
                new_timer_recharge = 5

            if boss_hp > 0:
                new_cost = get_min(new_boss_hp, new_player_hp, new_player_mana, new_timer_shield, new_timer_poison,
                                   new_timer_recharge, new_cost, not players_turn)

            if new_cost < min_cost:
                min_cost = new_cost

        return min_cost
    else:
        player_hp -= max(BOSS_AD - player_armor, 1)
        if player_hp <= 0:
            return float("inf")
        return get_min(boss_hp, player_hp, player_mana, timer_shield, timer_poison, timer_recharge, cost,
                       not players_turn)


print(get_min(BOSS_HP, PLAYER_HP, PLAYER_MANA))
