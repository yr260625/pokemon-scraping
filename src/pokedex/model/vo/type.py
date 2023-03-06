"""ポケモンタイプ 値オブジェクト"""
import json
from typing import Final, List, Dict
from dataclasses import dataclass


@dataclass(frozen=True)
class Type:
    """ポケモンタイプを保持する。
    """
    type_id: Final[int]
    name: Final[str]

    def __init__(self, type_id: int):
        """コンストラクタ

        Args:
            type_id (int): タイプID
        """
        self.__validate(type_id)
        object.__setattr__(self, "type_id", type_id)
        object.__setattr__(self, "name", self.getName(type_id))

    def __validate(self, type_id: int):
        if type_id < 0:
            raise ValueError("不正なタイプIDを検出しました。")

    def getName(self, type_id: int) -> str:
        """タイプ名取得

        Args:
            type_id (int): タイプID

        Returns:
            str: タイプ名
        """
        _type_definition: Final[Dict[int, str]] = {
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
        if type_id not in _type_definition:
            raise ValueError("不正なタイプIDを検出しました。")

        return _type_definition[type_id]


@dataclass(frozen=True)
class Types:
    """ポケモンのタイプ一覧を保持する。
    """
    types: Final[List[Type]]

    def to_json(self) -> str:
        """タイプ一覧をJSONに変換

        Returns:
            str: JSON文字列
        """
        type_map: Dict[int, str] = {}
        for index, type_obj in enumerate(self.types, 1):
            type_map.setdefault(index, type_obj.name)
        return json.dumps(type_map, ensure_ascii=False)

    @staticmethod
    def create(type_id1: int, type_id2: int):
        """タイプ一覧ファクトリー

        Args:
            type_id1 (int): タイプID1
            type_id2 (int): タイプID2

        Returns:
            Types: タイプ一覧オブジェクト
        """
        return Types([
            Type(type_id1),
            Type(type_id2),
        ])
