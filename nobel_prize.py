import requests
import pprint
from api import *

# Tips: använd sidan nedan för att se vilken data vi får tillbaks och hur apiet fungerar
# vi använder oss enbart av /nobelPrizes
# Dokumentation, hjälp samt verktyg för att testa apiet fins här: https://app.swaggerhub.com/apis/NobelMedia/NobelMasterData/2.1



cat = {"fysik": "phy",
       "kemi": "che",
       "litteratur": "lit",
       "ekonomi": "eco",
       "fred": "pea",
       "medicin": "med"}



# TODO 10p programmet skall ge en hjälpsam utskrift istället för en krasch om användaren skriver in fel input

def main():
    """
    Menu with alternatives for Nobel prize information
    :return:
    """
    HELP_STRING = """
    Ange ett år och fält
    Exempelvis 1965 fysik.
    Följande ämnen finns att välja på:
    fysik, kemi, litteratur, ekonomi, fred och medicin
    
    q) Avsluta programmet
    h) Visa hjälptext
    """
    print(HELP_STRING)

    while True:
        choice = input("> ").lower()
        if choice == "q":
            choice_quit()
            break
        elif choice == "h":
            show_help_text()
        else:
            list_input = choice.split()
            if len(list_input) == 1:   # bara året
                year = list_input[0]
                category = ""
            elif len(list_input) == 2:
                year, subject = choice.split()
                category = cat[subject]

            search_param = {"nobelPrizeYear": int(year), "nobelPrizeCategory": category}

            result = requests.get("http://api.nobelprize.org/2.1/nobelPrizes", params=search_param).json()  # result = dict
            # pprint.pprint(result)
            nobel_prizes(result)



        # TODO 20p Skriv ut hur mycket pengar varje pristagare fick, tänk på att en del priser delas mellan flera mottagare,
        #   skriv ut både i dåtidens pengar och dagens värde
        #   Skriv ut med tre decimalers precision. exempel 534515.123
        #   Skapa en funktion som hanterar uträkningen av prispengar och skapa minst ett enhetestest för den funktionen
        #   Tips, titta på variabeln andel
        # Feynman fick exempelvis 1/3 av priset i fysik 1965, vilket borde gett ungefär 282000/3 kronor i dåtidens penningvärde


def nobel_prizes(nobel_info):
    """
    Extracted information on Nobel prizes
    :param nobel_info: info from API
    """
    for prize in nobel_info['nobelPrizes']:
        prize_amount = prize['prizeAmount']
        adj_prize_amount = round((prize['prizeAmountAdjusted']), 3)
        print(f"{prize['categoryFullName']['se']} prissumma {prize_amount} SEK (nuvarande penningvärde (SEK): "
              f"{adj_prize_amount}) tilldelades:\n")
        amt_of_winners = len(prize['laureates'])
        winner_amount = round((prize_amount / amt_of_winners), 3)

        for winner in prize['laureates']:
            print(winner['knownName']['en'])
            print(winner['motivation']['en'])
            print(f"Amount of prize money: {winner_amount} ")
            print(f"Prize money in today's money value: {adj_prize_amount}")
            print("---"*30)
            winner_share = winner['portion']


def calculate_prize_amount():
    pass


def show_help_text():
    """
    Info on how to use the menu
    """
    print("""
    Ange ett år och fält
    Exempelvis 1965 fysik.
    Följande ämnen finns att välja på:
    fysik, kemi, litteratur, ekonomi, fred och medicin
    
    q) Avsluta programmet
    """)

def choice_quit():
    """
    Quits application
    """
    print("Hej då!")



if __name__ == '__main__':
    main()