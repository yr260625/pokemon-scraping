"""ポケモン名 値オブジェクト"""
from typing import Final
from dataclasses import dataclass


@dataclass(frozen=True)
class Name:
    """ポケモン名を保持する。
    """
    value: Final[str]

    def __init__(self, value: str):
        """コンストラクタ

        Args:
            value (str): ポケモン名
        """
        self.__validate(value)
        object.__setattr__(self, "value", value)

    def __validate(self, value: str):
        """バリデーション

        Args:
            value (str): ポケモン名

        Raises:
            ValueError: ポケモン名が空白
        """
        if len(value) == 0:
            raise ValueError("不正なポケモン名を検出しました。")
