from random import sample
import numpy as np


class Question:
    def __init__(self, prompt, anwser):
        self.prompt = prompt
        self.answer = anwser

    def getPrompt(self):
        return self.prompt

    def getAnswer(self):
        return self.answer


class Questions:

    def __init__(self, category):
        if category == "Pokemon":
            sequence = [i for i in range(10)]
        elif category == "Games":
            sequence = [i for i in range(10, 20)]
        elif category == "Music":
            sequence = [i for i in range(20, 30)]
        else:
            sequence = [i for i in range(30)]
        self.subset = sample(sequence, 10)
        print(self.subset)
        self.questions = np.take(questions, np.array(self.subset))

    def getQuestion(self, index):
        return self.questions[index]


prompts_Pokemon = [
    "W jakiego pokemona evouluje pikachu?\n\nA) Jolteon \n\nB) Pichu \n\nC) Electrive \n\nD) Raichu",
    "Jaki Poke Ball jest najskuteczniejszy?\n\nA) Great Ball \n\nB) Master Ball \n\nC) Ultra Ball \n\nD) Nest Ball",
    "Ile trzeba posiadać odznak aby wziąć udział w lidze Pokemon?\n\nA) 6 \n\nB) 7 \n\nC) 8 \n\nD) 9",
    "Jakie urządzenie pozwala na sprawdzenie informacji o pokemonie?\n\nA) Pokecounter \n\nB) Pokedex\n\n"
    "C) Pokefinder \n\n""D) Pokeinfo",
    "Jakie są trzy typy pokemonów startowych?\n\nA) Trawiasty,Ognisty i Wodny \n\nB) Elektryczny,Ziemny i Trujący\n\n"
    "C) Smoczy,Latający i Normalny \n\nD) Psychiczny,Walczący i Duch",
    "Jak nazywa się głowny rywal Asha w podróży po regionie Kanto?\n\nA) Lance \n\nB) Giovanni \n\nC) Gary \n\nD) James",
    "Który z pokemonów nie jest evolucją Evee?\n\nA) Vaporeon \n\nB) Sylveon \n\nC) Leafeon \n\nD) Flygon",
    "Jak nazywa się pokemon uznawany za Boga?\n\nA) Arceus \n\nB) Mew \n\nC) Jirachi \n\nD) Celebi",
    "Jak brzmią imiona dwóch członków zespołu R?\n\nA) Jessie i James \n\nB) Joanie i James\n\n"
    "C) Jenny i John\n\nD)Jessie i John",
    "Kto użyczył głosu tytułowemu bohaterowi w filmie Detektyw Pikachu?\n\nA) Justice Smith\n\nB) Omar Chaparro\n\n"
    "C) Bill Nighy\n\nD) Ryan Reynolds",
]

prompts_Games = [
    "W jakiego bohatera wcielamy sie w grze GTA San Andreas?\n\nA) Carl 'C.J' Johnson\n\nB) Lance 'Ryder' Wilson\n\n"
    "C) Sean 'Sweet' Johnson\n\nD) Melvin 'Big Smoke' Harris",
    "Który ze skrótów nie jest gatunkiem gry komputerowej?\n\nA) RTS\n\nB) RPG\n\nC) MMO\n\nD) SJP",
    "Do jakiej wioski docieramy na początku gry Gothic 3?\n\nA) Do Montery\n\n"
    "B) Do Adrei\n\nC) Do Reddock\n\nD) Do Vengardu",
    "Które miasto nie wystąpiło w grze Heroes of Might & Magic III?\n\nA) Nekropolis\n\nB) Bastion\n\n"
    "C) Twierdza\n\nD) Przystań",
    "Jakie studio odpowiada za produkcję gier z serii Diablo?\n\nA) Bethesda Game studio\n\nB) Ubisoft Montreal"
    "\n\nC) Blizzard Entertainment\n\nD) BioWare",
    "Jakiej wielkości jest rzeczywisty teren gry the Elder Scrolls II: Daggerfall?\n\n"
    "A) Czech\n\nB) Chin\n\nC) Wielkiej Brytanii\n\nD) Belgii",
    "W jakim przedziale czasowym dzieje się Europa Universalis IV?\n\nA) 782-1524\n\nB) 1444-1821\n\n"
    "C) 999-1999\n\nD) 0-2001",
    "W którym roku została wydana gra quake I?\n\nA) 1995\n\nB) 1996\n\nC) 1997\n\nD) 1998",
    "W którym roku zaprezentowano grę Tetris?\n\nA) 1984\n\nB) 1980\n\nC) 1987\n\nD) 1985",
    "Kim można zagrać w grze Dragon Age II?\n\nA) Tylko Krasnoludem\n\nB) Tylko Człowiekiem\n\n"
    "C) Elfem,Krasnoludem i Człowiekiem\n\nD) Tylko Elfem",
]

prompts_Music = [
    "Jak nazywa się utwór zespołu ABBA, dzięki któremu grupa wygrała Eurowizję w 1974 roku?\n\n"
    "A) Money,Money,Money\n\nB) Waterloo\n\nC) Mamma Mia\n\nD) Gimme! Gimme! Gimme!",
    "Który zespół jest autorem utworu 'The show must go on'?\n\nA) Queen\n\nB) Pink Floyd\n\n"
    "C) The Beatles\n\nD) The Rolling Stones",
    "Jak w muzyce nazywa się najwyższy głos żeński ?\n\nA) Tenor\n\nB) Alt\n\n"
    "C) Sopran\n\nD) Kontralt",
    "Który zespół wykonuje utwór 'Stairway to Heaven' ?\n\nA) Scorpions\n\nB) The Doors\n\n"
    "C) R.E.M\n\nD) Led Zeppelin",
    "Określenie w partyturze mówiące, że poszczególne nuty należy grać z wyraźnymi przerwami to?\n\n"
    "A) Staccato\n\nB) Kantato\n\nC) Rasgueado\n\nD) Vibrato",
    "Która z piosenek NIE jest utorstwa braci FIGO FAGOT ?\n\nA) Wędkarz miłości\n\nB) Wóda zryje banie\n\n"
    "C) Hot Dog\n\nD) Biała mewa",
    "Ile dźwięków występuje w skali chromatycznej ?\n\nA) 8\n\nB) 12\n\nC) 15\n\nD) 7",
    "Jak nazywa się 5 dźwięk?\n\nA) Septyma\n\nB) Kwarta\n\nC) Kwinta\n\nD) Oktawa",
    "Dokończ fragment piosenki: 'Trudno tak razem być nam zesobą'\n\nA) Z whiskey nie jest lżej\n\n"
    "B) Bez siebie nie jest lżej\n\nC) Bo mnie denerwujesz\n\nD) Bo studiuję na WAT",
    "Skąd wywodzi się muzyka country ?\n\nA) Z Czech\n\nB) Z Argentyny\n\nC) Z Polski\n\nD) Ze Stanów Zjednoczonych",
]

questions = [
    Question(prompts_Pokemon[0], "D"),
    Question(prompts_Pokemon[1], "B"),
    Question(prompts_Pokemon[2], "C"),
    Question(prompts_Pokemon[3], "B"),
    Question(prompts_Pokemon[4], "A"),
    Question(prompts_Pokemon[5], "C"),
    Question(prompts_Pokemon[6], "D"),
    Question(prompts_Pokemon[7], "A"),
    Question(prompts_Pokemon[8], "A"),
    Question(prompts_Pokemon[9], "D"),
    Question(prompts_Games[0], "A"),
    Question(prompts_Games[1], "D"),
    Question(prompts_Games[2], "B"),
    Question(prompts_Games[3], "D"),
    Question(prompts_Games[4], "C"),
    Question(prompts_Games[5], "C"),
    Question(prompts_Games[6], "B"),
    Question(prompts_Games[7], "B"),
    Question(prompts_Games[8], "A"),
    Question(prompts_Games[9], "B"),
    Question(prompts_Music[0], "B"),
    Question(prompts_Music[1], "A"),
    Question(prompts_Music[2], "C"),
    Question(prompts_Music[3], "D"),
    Question(prompts_Music[4], "A"),
    Question(prompts_Music[5], "D"),
    Question(prompts_Music[6], "B"),
    Question(prompts_Music[7], "C"),
    Question(prompts_Music[8], "B"),
    Question(prompts_Music[9], "D"),
]
