"""ポケモン能力値 値オブジェクト"""
from typing import Final
from dataclasses import dataclass


@dataclass(frozen=True)
class Stats:
    """ポケモン能力値を保持する。
    """
    attack: Final[int]
    defense: Final[int]
    hit_point: Final[int]
    special_attack: Final[int]
    special_defense: Final[int]
    speed: Final[int]

    def __init__(self, attack: int, defense: int, hit_point: int, special_attack: int, special_defense: int, speed: int):
        """コンストラクタ

        Args:
            attack (int): こうげき
            defense (int): ぼうぎょ
            hit_point (int): HP
            special_attack (int): とっこう
            special_defense (int): とくぼう
            speed (int): すばやさ
        """
        self.__validate(attack, defense, hit_point,
                        special_attack, special_defense, speed)
        object.__setattr__(self, "attack", attack)
        object.__setattr__(self, "defense", defense)
        object.__setattr__(self, "hit_point", hit_point)
        object.__setattr__(self, "special_attack", special_attack)
        object.__setattr__(self, "special_defense", special_defense)
        object.__setattr__(self, "speed", speed)

    def __validate(self, *stats: tuple[int]):
        """バリデーション

        Raises:
            ValueError: 能力値が範囲外の数値
        """
        for ability_score in stats:
            if not 1 <= ability_score <= 15:
                raise ValueError('不正な能力値を検出しました。')
