from collections import namedtuple
from os.path import join, dirname, realpath

from recordclass import recordclass

Entity = recordclass("Entity", ["hp", "ad", "ar"])
Item = namedtuple("Item", ["cost", "ad", "ar"])

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    for line in f:
        n = int(line.split(": ")[-1])
        if line.startswith("H"):
            boss_hp = n
        elif line.startswith("D"):
            boss_ad = n
        elif line.startswith("A"):
            boss_ar = n

weapons = {
    "dagger": Item(8, 4, 0),
    "shortsword": Item(10, 5, 0),
    "warhammer": Item(25, 6, 0),
    "longsword": Item(40, 7, 0),
    "greataxe": Item(74, 8, 0)
}
armors = {
    "no_armor": Item(0, 0, 0),
    "leather": Item(13, 0, 1),
    "chainmail": Item(31, 0, 2),
    "splintmail": Item(53, 0, 3),
    "bandedmail": Item(75, 0, 4),
    "platemail": Item(102, 0, 5)
}
rings = {
    "no_ring": Item(0, 0, 0),
    "damage+1": Item(25, 1, 0),
    "damage+2": Item(50, 2, 0),
    "damage+3": Item(100, 3, 0),
    "defense+1": Item(20, 0, 1),
    "defense+2": Item(40, 0, 2),
    "defense+3": Item(80, 0, 3)
}


def player_wins(p: Entity, b: Entity) -> bool:
    players_turn = True
    while p.hp > 0 and b.hp > 0:
        if players_turn:
            b.hp -= max(p.ad - b.ar, 1)
        else:
            p.hp -= max(b.ad - p.ar, 1)
        players_turn = not players_turn
    return p.hp > 0


min_cost = 500
for weapon_name, weapon in weapons.items():
    for armor_name, armor in armors.items():
        for left_ring_name, left_ring in rings.items():
            for right_ring_name, right_ring in rings.items():
                boss = Entity(boss_hp, boss_ad, boss_ar)
                player = Entity(
                    100,
                    weapon.ad + armor.ad + left_ring.ad + right_ring.ad,
                    weapon.ar + armor.ar + left_ring.ar + right_ring.ar
                )
                cost = weapon.cost + armor.cost + left_ring.cost + right_ring.cost
                if player_wins(player, boss) and cost < min_cost:
                    min_cost = cost
                    print("New minimum of {} with {}, {}, {}, and {}".format(cost, weapon_name, armor_name, left_ring_name, right_ring_name))

print("Solution:", min_cost)
