"""起動スクリプト"""
from src.pokedex.collection import Pokedex
from src.pokedex.infrastructure.pokemon_spec import PokemonSpecRepository


if __name__ == '__main__':
    print('処理を開始します。')
    print('ポケモン図鑑収集中...')
    pokedex = Pokedex(PokemonSpecRepository())
    pokedex.release_all()
    print('ポケモン図鑑出力中...')
    print(pokedex.to_json())
    print('処理が完了しました。')
