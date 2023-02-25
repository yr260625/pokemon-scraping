from typing import Final
from dataclasses import dataclass


@dataclass(frozen=True)
class Number:
    """図鑑No.を保持する。
    """
    value: Final[str]

    def __init__(self, value: str):
        """コンストラクタ

        Args:
            value (str): 図鑑No.
        """
        self.__validate(value)
        object.__setattr__(self, "value", value)

    def __validate(self, value: str):
        """バリデーション

        Args:
            value (str): 図鑑No.

        Raises:
            ValueError: 図鑑No.が非数値
        """
        if not value.isdigit():
            raise ValueError("不正な図鑑No.を検出しました。:" + value)
