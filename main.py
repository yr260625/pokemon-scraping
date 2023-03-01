"""起動スクリプト"""
import traceback
from src.pokedex.pokemon_specifications import PokemonSpecifications
from src.pokedex.infrastructure.pokemon_spec import PokemonSpecRepository

if __name__ == '__main__':
    try:
        print('処理を開始します。')
        pokemon_specifications = PokemonSpecifications(PokemonSpecRepository())
        print('ポケモン図鑑収集中...')
        pokemon_specifications.release_all()
        print('ポケモン図鑑出力中...')
        print(pokemon_specifications.to_json())
        print('処理が完了しました。')
    except Exception as error:
        print(error)
        print(traceback.format_exc())
