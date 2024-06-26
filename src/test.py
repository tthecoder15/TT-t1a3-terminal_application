import json
import os
from random_card_gen import gen_rand_card
from guess import typo_eval
from guess import guess
from hints_and_score import HintsAndScore
from scoreboard import Scoreboard


def test_json_data():
    # Tests the dictionaries in all files for "Pokemon" supertype then checks if they have flavour text attacks abilities, numbers, types
    set_files_list = os.listdir("card_data/")
    print(set_files_list)
    for set_file in set_files_list:
        file_path = "card_data/" + set_file
        with open(file_path) as f:
            all_cards_in_set = json.load(f)
        for card in all_cards_in_set:
            if card["supertype"] == "Pokémon":
                print(file_path)
                print(card["name"])
                assert card["name"]
                if "flavorText" in card:
                    print(card["flavorText"])
                else:
                    print(f"{card['name']} in {file_path} has no flavour text")
                if "attacks" in card:
                    assert card["attacks"]
                else:
                    print(f"{card['name']} has no attacks")
                if "abilities" in card:
                    assert card["abilities"]
                else:
                    print(f"{card['name']} has no abilities")
                # Checks that attacks exist OR card has an ability
                print(card["subtypes"])
                assert card["subtypes"][0]
                print(card["types"])
                assert card["types"]
                print(card["number"])
                assert card["number"]


def test_every_cards_creation():
    # Tests that every "Pokemon" supertype card can be converted to a local dictionary object. Checks that release data and linking to set name data works successfully
    set_files_list = os.listdir("card_data/")
    with open("set_data/set_data.json") as f:
        all_sets_info = json.load(f)
    for set_file in set_files_list:
        file_path = "card_data/" + set_file
        with open(file_path) as f:
            all_cards_in_set = json.load(f)
        for card in all_cards_in_set:
            for set in all_sets_info:
                if set["id"] == file_path[10:-5]:
                    expansion = set["name"]
                    print(expansion)
                    release_date = set["releaseDate"]
                    print(release_date)
                    break

            print(f"{card['name']} from {file_path} is being assessed")
            if card["supertype"] == "Pokémon" and "flavorText" in card:
                rand_card = card
                if "convertedRetreatCost" not in rand_card:
                    rand_card.update({"convertedRetreatCost": "0"})
                if "attacks" not in rand_card:
                    rand_card.update({"attacks": "This Pokémon has no attacks!"})
                assert {
                    "name": rand_card["name"],
                    "stage": rand_card["subtypes"][0],
                    "card_types": rand_card["types"],
                    "expansion": expansion,
                    "release_date": release_date,
                    "set_number": rand_card["number"],
                    "flavor_text": rand_card["flavorText"],
                    "ret_cost": rand_card["convertedRetreatCost"],
                    "atks": rand_card["attacks"],
                }
            else:
                print(f"{card['name']} is not eligible")


# Automated test for generating cards via hard method
def test_hard_card_gen_access():
    num_of_tests = 10
    while num_of_tests > 0:
        card = gen_rand_card("hard")
        print(card.__dir__)
        num_of_tests -= 1


# # Non automated test for generating cards via standard method
# def test_card_gen_access():
#     num_of_tests = 10
#     while num_of_tests > 0:
#         card = gen_rand_card("standard")
#         print(card.__dir__)
#         num_of_tests -= 1
# test_card_gen_access()


# BELOW TEST IS FOR TYPO CHECKER, NEEDS AUTOMATING
# def test_card_typo():
#     genned_card = gen_rand_card("hard")
#     print("The generated card's name is: \n", genned_card["name"])
#     typo = input(f"Type a typo of {genned_card['name']}: \n")
#     typo_eval(genned_card, typo)

# test_card_typo()


# Non automated test for names with extra characters:
# def test_extra_character_names():
#     print("The next card is Nidoran ♀")
#     guess(
#         {"name": "Nidoran ♀"},
#         HintsAndScore(),
#         Scoreboard().set_current_game_mode("standard"),
#     )
#     print("The next card is Nidoran ♂")
#     guess(
#         {"name": "Nidoran ♂"},
#         HintsAndScore(),
#         Scoreboard().set_current_game_mode("standard"),
#     )
#     print("The next card is Dark Kadabra")
#     guess(
#         {"name": "Dark Kadabra"},
#         HintsAndScore(),
#         Scoreboard().set_current_game_mode("standard"),
#     )
# test_extra_character_names()
