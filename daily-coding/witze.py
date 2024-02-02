witze = [
    {"witz": "Warum hat der Teddybär keinen Kuchen gegessen? Weil er schon gestopft ist!"},

    {"witz": "Warum können Geister so gut lügen? Weil man durch sie hindurchsehen kann!"},

    {"witz": "Was sagt ein Null zu einer Acht? Schicker Gürtel!"},

    {"witz": "Warum hat der Besen den Job verloren? Weil er immer nur rumstand!"},

    {"witz": "Warum hat der Computer Angst vorm Essen? Weil er fürchtet, dass er sich einen Virus holt!" },
]

import random

def witz_erzaehlen(witze):
    witz = random.shuffle(witze)

    for witze_data in witze:
        jokes = witze_data["witz"]

    user_answer = input(f"Möchtest du einen Witz hören?: ")
    
    if user_answer == "Ja":
        print(jokes)
    elif user_answer == "Nein":
        print("Okay, schade.")
        return(user_answer)
    else:
        print("Ich habe das nicht verstanden.")
        return(user_answer)

witz_erzaehlen(witze)

                        
