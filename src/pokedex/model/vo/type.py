import json
from typing import Final
from dataclasses import dataclass


@dataclass(frozen=True)
class Type:
    """ポケモンのタイプを保持する。
    """
    id: Final[int]
    name: Final[str]

    def __init__(self, id: int):
        """コンストラクタ

        Args:
            id (int): タイプID
        """
        self.__validate(id)
        object.__setattr__(self, "id", id)
        object.__setattr__(self, "name", self.getName(id))

    def __validate(self, id: int):
        if id < 0:
            raise ValueError("不正なタイプIDを検出しました。")

    def getName(self, id: int) -> str:
        """タイプ名取得

        Args:
            id (int): タイプID

        Returns:
            str: タイプ名
        """
        _type_definition: Final[dict] = {
            0:  "なし",
            1:  "ノーマル",
            2:  "ほのお",
            3:  "みず",
            4:  "くさ",
            5:  "でんき",
            6:  "こおり",
            7:  "かくとう",
            8:  "どく",
            9:  "じめん",
            10:  "ひこう",
            11:  "エスパー",
            12:  "むし",
            13:  "いわ",
            14:  "ゴースト",
            15:  "ドラゴン",
            16:  "あく",
            17:  "はがね",
            18:  "フェアリー",
        }
        if id not in _type_definition.keys():
            raise ValueError("不正なタイプIDを検出しました。")

        return _type_definition[id]


@dataclass(frozen=True)
class Types:
    """ポケモンのタイプ一覧を保持する。
    """
    types: Final[tuple[Type]]

    def to_json(self) -> str:
        """タイプ一覧をJSONに変換

        Returns:
            str: JSON文字列
        """
        _mapping: Final[dict] = {}
        for index, type in enumerate(self.types, 1):
            _mapping.setdefault(index, type.name)
        return json.dumps(_mapping, ensure_ascii=False)

    @staticmethod
    def create(id1: int, id2: int):
        """タイプ一覧ファクトリー

        Args:
            id1 (int): タイプID
            id2 (int): タイプID

        Returns:
            Types: タイプ一覧オブジェクト
        """
        return Types((
            Type(id1),
            Type(id2)
        ))
