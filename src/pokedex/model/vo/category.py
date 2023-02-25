from typing import Final
from dataclasses import dataclass


@dataclass(frozen=True)
class Category:
    """ポケモン分類を保持する。
    """
    value: Final[str]

    def __init__(self, value: str):
        """コンストラクタ

        Args:
            value (str): 分類
        """
        self.__validate(value)
        object.__setattr__(self, "value", value)

    def __validate(self, value: str):
        """バリデーション

        Args:
            value (str): 分類

        Raises:
            ValueError: 分類が空白
        """
        if len(value) == 0:
            raise ValueError("不正な分類を検出しました。")
