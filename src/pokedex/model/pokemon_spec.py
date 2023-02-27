"""ポケモン諸元"""
import json
from dataclasses import dataclass
from src.pokedex.model.vo.ability import Abilities
from src.pokedex.model.vo.number import Number
from src.pokedex.model.vo.name import Name
from src.pokedex.model.vo.category import Category
from src.pokedex.model.vo.type import Types
from src.pokedex.model.vo.body_measurement import BodyMeasurement
from src.pokedex.model.vo.stats import Stats


@dataclass(frozen=False)
class PokemonSpec:
    """ポケモンの各種諸元値を保持するエンティティクラス。
    """

    def __init__(
        self,
        pokemon_id: Number,
        name: Name,
        category: Category,
        types: Types,
        body_measurement: BodyMeasurement,
        abilities: Abilities,
        stats: Stats
    ):
        """コンストラクタ

        Args:
            pokemon_id (Number): 図鑑No.
            name (Name): ポケモン名
            category (Category): ポケモン分類
            types (Types): ポケモンタイプ
            body_measurement (BodyMeasurement): ポケモン身体値
            abilities (Abilities): ポケモン特性
            stats (Stats): ポケモン能力値
        """
        self.pokemon_id = pokemon_id
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
        types_map = json.loads(self.types.to_json())
        abilities_map = json.loads(self.abilities.to_json())

        return json.dumps({
            'ずかんNo.': self.pokemon_id.value,
            '名前': self.name.value,
            '分類': self.category.value,
            'タイプ': types_map,
            '高さ': self.body_measurement.height,
            '重さ': self.body_measurement.weight,
            '特性': abilities_map,
            'HP': self.stats.hit_point,
            'こうげき': self.stats.attack,
            'ぼうぎょ': self.stats.defense,
            'とくこう': self.stats.special_attack,
            'とくぼう': self.stats.special_defense,
            'すばやさ': self.stats.speed,
        }, ensure_ascii=False)

    @staticmethod
    def create(raw_spec: str):
        """ポケモン諸元値ファクトリー

        Args:
            raw_spec (str): ポケモン諸元値(raw)

        Returns:
            PokemonSpec: ポケモン諸元値オブジェクト
        """
        spec_map = json.loads(raw_spec)
        pokemon = spec_map["pokemon"]

        number = Number(pokemon['zukan_no'])
        name = Name(pokemon['name'])
        category = Category(pokemon['bunrui'])
        types = Types.create(pokemon['type_1'], pokemon['type_2'])
        body = BodyMeasurement(pokemon['takasa'], pokemon['omosa'])
        abilities = Abilities.create(spec_map['abilities'])
        stats = Stats(
            pokemon['spec_hp'],
            pokemon['spec_kougeki'],
            pokemon['spec_bougyo'],
            pokemon['spec_tokukou'],
            pokemon['spec_tokubou'],
            pokemon['spec_subayasa']
        )
        return PokemonSpec(
            number,
            name,
            category,
            types,
            body,
            abilities,
            stats
        )
