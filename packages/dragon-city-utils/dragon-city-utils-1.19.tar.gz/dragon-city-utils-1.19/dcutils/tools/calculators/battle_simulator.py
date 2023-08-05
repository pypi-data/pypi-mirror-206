from pydantic import BaseModel, validate_arguments, validate_model
from pyfilter.tuple_list import FromTupleList
import random

from .dragon import calculate_attack_damage, calculate_status
from .elements import calculate_strongs, calculate_weaknesses

class DragonInBattle:
    def __init__(
        self,
        category: int,
        level: int,
        rank_class: int,
        starts: int,
        hp: int,
        elements: list[str],
        attacks: list[tuple[str, int]]
    ) -> None:
        self.__category = category
        self.__level = level
        self.__rank_class = rank_class
        self.__stars = starts

        attack_elements = list(
            map(lambda attack: attack[0], attacks)
        )

        self.weaknesses = calculate_weaknesses(elements[0])
        self.strongs = calculate_strongs(attack_elements)
        self.attacks = attacks
        self.current_hp = int(hp)

    def attack(self, dragon, attack: tuple[str, int]):
        damage = calculate_attack_damage(
            self.__category,
            self.__level,
            attack[1],
            self.__rank_class,
            self.__stars
        )

        dragon.take_damage(damage)

    def take_damage(self, damage):
        self.current_hp -= damage

        if self.current_hp < 0:
            self.current_hp = 0

    @property
    def is_alive(self) -> bool:
        return self.current_hp > 0

class Dragon(BaseModel):
    category: int
    rarity: str
    level: int = 1
    rank_class: int = 0
    stars: int = 0
    hp_runes: int = 0
    damage_runes: int = 0
    with_tower_bonus: bool = False
    extra_hp_multiplier: float = 0.0
    extra_damage_multiplier: float = 0.0
    elements: list[str]
    attacks: list[tuple[str, int]]

class BattleSimulator:
    @validate_arguments
    def __init__(
        self,
        team_ally: list[dict],
        enemy_team: list[dict]
    ) -> None:
        self.__team_ally = team_ally
        self.__enemy_team = enemy_team

        for allied_dragon, enemy_dragon in zip(team_ally, enemy_team):
            validate_model(Dragon, allied_dragon)
            validate_model(Dragon, enemy_dragon)

        self.who_starts = random.choice(["allies", "enemies"])

        self.__allied_dragons_in_baltte: list[DragonInBattle] = []
        self.__enemy_dragons_in_battle: list[DragonInBattle] = []

        for allied_dragon in self.__team_ally:
            dragon_status_result = calculate_status(
                allied_dragon["category"],
                allied_dragon["rarity"],
                allied_dragon["level"],
                allied_dragon["rank_class"],
                allied_dragon["stars"],
                allied_dragon["hp_runes"],
                allied_dragon["damage_runes"],
                allied_dragon["with_tower_bonus"],
                allied_dragon["extra_hp_multiplier"],
                allied_dragon["extra_damage_multiplier"]
            )["result"]

            allied_dragon_in_baltte = DragonInBattle(
                allied_dragon["category"],
                allied_dragon["level"],
                allied_dragon["rank_class"],
                allied_dragon["stars"],
                dragon_status_result["hp"],
                allied_dragon["elements"],
                allied_dragon["attacks"]
            )

            self.__allied_dragons_in_baltte.append(allied_dragon_in_baltte)

        for enemy_dragon in self.__enemy_team:
            dragon_status_result = calculate_status(
                enemy_dragon["category"],
                enemy_dragon["rarity"],
                enemy_dragon["level"],
                enemy_dragon["rank_class"],
                enemy_dragon["stars"],
                enemy_dragon["hp_runes"],
                enemy_dragon["damage_runes"],
                enemy_dragon["with_tower_bonus"],
                enemy_dragon["extra_hp_multiplier"],
                enemy_dragon["extra_damage_multiplier"]
            )["result"]

            allied_dragon_in_baltte = DragonInBattle(
                enemy_dragon["category"],
                enemy_dragon["level"],
                enemy_dragon["rank_class"],
                enemy_dragon["stars"],
                dragon_status_result["hp"],
                enemy_dragon["elements"],
                enemy_dragon["attacks"]
            )

            self.__enemy_dragons_in_battle.append(allied_dragon_in_baltte)

        print(f"{self.who_starts=}")

    def with_smart_switch(self):
        ...

    def selecting_with_quality_post_defeat(self):
        ...

    def selected_by_order(self):
        current_allied_dragon_index = 0
        current_enemy_dragon_index = 0

        if self.who_starts == "allies":
            for i in range(len(self.__allied_dragons_in_baltte)):


                current_allied_dragon = self.__allied_dragons_in_baltte[current_allied_dragon_index]
                current_enemy_dragon = self.__enemy_dragons_in_battle[current_allied_dragon_index]

                while current_allied_dragon.is_alive:
                    selected_attack: tuple[str, int]

                    selected_attack = FromTupleList(current_allied_dragon.attacks).get_with_value("")

                    current_allied_dragon.attack(current_enemy_dragon, )

        elif self.who_starts == "enemies":
            ...
