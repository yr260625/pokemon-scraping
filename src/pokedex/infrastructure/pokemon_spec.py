"""ポケモン諸元値リポジトリー"""
from typing import Final
import bs4
import requests
from src.pokedex.model.pokemon_spec import PokemonSpec
from src.pokedex.repository.pokemon_spec import IPokemonSpecRepository


class PokemonSpecRepository(IPokemonSpecRepository):
    """ポケモン諸元値リポジトリクラス

    Args:
        IPokemonSpecRepository (_type_): ポケモン諸元値リポジトリインターフェース
    """

    BASE_URL: Final[str] = 'https://zukan.pokemon.co.jp/detail'
    TIME_OUT: Final[int] = 5

    def find_by_id(self, pokemon_id: int) -> PokemonSpec:
        """ポケモン諸元値取得

        Args:
            id (int): 図鑑No.

        Returns:
            PokemonSpec: ポケモン諸元値オブジェクト

        Raises:
            HTTPError: ステータスコードが400系 or 500系
        """
        res = requests.get(f'{self.BASE_URL}/{pokemon_id}', timeout=self.TIME_OUT)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        raw_spec = soup.select_one('#json-data').text
        return PokemonSpec.create(raw_spec)
