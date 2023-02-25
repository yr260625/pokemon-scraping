import json
from src.pokedex.model.vo.ability import Abilities
from src.pokedex.model.vo.number import Number
from src.pokedex.model.vo.name import Name
from src.pokedex.model.vo.category import Category
from src.pokedex.model.vo.type import Types
from src.pokedex.model.vo.body_measurement import BodyMeasurement
from src.pokedex.model.vo.stats import Stats
from dataclasses import dataclass


@dataclass(frozen=False)
class PokemonSpec:
    """ポケモンの各種諸元値を保持するエンティティクラス。
    """

    def __init__(
        self,
        id: Number,
        name: Name,
        category: Category,
        types: Types,
        body_measurement: BodyMeasurement,
        abilities: Abilities,
        stats: Stats
    ):
        """コンストラクタ

        Args:
            id (Number): 図鑑No.
            name (Name): ポケモン名
            category (Category): ポケモン分類
            types (Types): ポケモンタイプ
            body_measurement (BodyMeasurement): ポケモン身体値
            abilities (Abilities): ポケモン特性
            stats (Stats): ポケモン能力値
        """
        self.id = id
        self.name = name
        self.category = category
        self.types = types
        self.body_measurement = body_measurement
        self.abilities = abilities
        self.stats = stats

    def to_json(self) -> str:
        """ポケモン諸元値をJSONに変換

        Returns:
            str: JSON文字列
        """
        _types_dict = json.loads(self.types.to_json())
        _abilities_dict = json.loads(self.abilities.to_json())

        return json.dumps({
            'ずかんNo.': self.id.value,
            '名前': self.name.value,
            '分類': self.category.value,
            'タイプ': _types_dict,
            '高さ': self.body_measurement.height,
            '重さ': self.body_measurement.weight,
            '特性': _abilities_dict,
            'HP': self.stats.hit_point,
            'こうげき': self.stats.attack,
            'ぼうぎょ': self.stats.defense,
            'とくこう': self.stats.special_attack,
            'とくぼう': self.stats.special_defense,
            'すばやさ': self.stats.speed,
        }, ensure_ascii=False)

    @staticmethod
    def createFromRawSpec(raw_spec: str):
        """ポケモン諸元値(raw)からポケモン諸元値オブジェクトを生成

        Args:
            raw_spec (str): ポケモン諸元値(raw)

        Returns:
            PokemonSpec: ポケモン諸元値オブジェクト
        """
        _dict = json.loads(raw_spec)
        _pokemon = _dict["pokemon"]

        _number = Number(_pokemon['zukan_no'])
        _name = Name(_pokemon['name'])
        _category = Category(_pokemon['bunrui'])
        _types = Types.create(_pokemon['type_1'], _pokemon['type_2'])
        _body = BodyMeasurement(_pokemon['takasa'], _pokemon['omosa'])
        _abilities = Abilities.create(_dict['abilities'])
        _stats = Stats(
            _pokemon['spec_hp'],
            _pokemon['spec_kougeki'],
            _pokemon['spec_bougyo'],
            _pokemon['spec_tokukou'],
            _pokemon['spec_tokubou'],
            _pokemon['spec_subayasa']
        )
        return PokemonSpec(
            _number,
            _name,
            _category,
            _types,
            _body,
            _abilities,
            _stats
        )
