"""ポケモン身体値 値オブジェクト"""
from typing import Final
from dataclasses import dataclass


@dataclass(frozen=True)
class BodyMeasurement:
    """ポケモン身体値を保持する。
    """
    height: Final[str]
    weight: Final[str]
    DIMENSION_WEIGHT: Final[str] = 'kg'
    DIMENSION_HEIGHT: Final[str] = 'm'

    def __init__(self, height: str, weight: str):
        """コンストラクタ

        Args:
            height (str): 高さ
            weight (str): 重さ
        """
        self.__validate(height, weight)
        object.__setattr__(self, "height", height + self.DIMENSION_HEIGHT)
        object.__setattr__(self, "weight", weight + self.DIMENSION_WEIGHT)

    def __validate(self, height: str, weight: str):
        """バリデーション

        Args:
            height (str): 高さ
            weight (str): 重さ

        Raises:
            ValueError: 高さ、重さいずれか0以下
        """
        if float(height) <= 0:
            raise ValueError("不正な身体値を検出しました。")

        if float(weight) <= 0:
            raise ValueError("不正な体重値を検出しました。")
