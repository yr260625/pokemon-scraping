import json
from typing import Final
from dataclasses import dataclass


@dataclass(frozen=True)
class Ability:
    """ポケモン特性を保持する。
    """
    id: Final[int]
    name: Final[str]

    def __init__(self, id: int, name: str):
        """コンストラクタ

        Args:
            id (int): 特性ID
            name (str): 特性名
        """
        self.__validate(name)
        object.__setattr__(self, "id", id)
        object.__setattr__(self, "name", name)

    def __validate(self, name: str):
        """バリデーション

        Args:
            id (int): 特性ID
            name (str): 特性名

        Raises:
            ValueError: 特性名が空白
        """
        if len(name) == 0:
            raise ValueError("不正な特性名を検出しました。")


@dataclass(frozen=True)
class Abilities:
    """ポケモンの特性一覧を保持する。
    """
    abilities: Final[tuple[Ability]]

    def to_json(self) -> str:
        """特性一覧をJSONに変換

        Returns:
            str: JSON文字列
        """
        _mapping: Final[dict] = {}
        for ability in self.abilities:
            _mapping.setdefault(ability.id, ability.name)
        return json.dumps(_mapping, ensure_ascii=False)

    @staticmethod
    def create(abilities: list[dict]):
        """特性一覧ファクトリー

        Args:
            abilities (list[dict]): 特性一覧(辞書配列形式)

        Returns:
            Abilities: 特性一覧オブジェクト
        """
        _abilities = []
        for ability in abilities:
            _abilities.append(Ability(ability["id"], ability["name"]))
        return Abilities(tuple(_abilities))
