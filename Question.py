class Question:
    def __init__(self, prompt, anwser):
        self.prompt = prompt
        self.answer = anwser

    def getPrompt(self):
        return self.prompt

    def getAnswer(self):
        return self.answer


class Questions:
    prompts_Pokemon = [
        "W jakiego pokemona evouluje pikachu?\n\nA) Jolteon \n\nB) Pichu \n\nC) Electrive \n\nD) Raichu",
        "Jaki Poke Ball jest najskuteczniejszy?\n\nA) Great Ball \n\nB) Master Ball \n\nC) Ultra Ball \n\nD) Nest Ball",
        "Ile trzeba posiadać odznak aby wziąć udział w lidze Pokemon?\n\nA) 6 \n\nB) 7 \n\nC) 8 \n\nD) 9",
        "Jakie urządzenie pozwala na sprawdzenie informacji o pokemonie?\n\nA) Pokecounter \n\nB) Pokedex \n\n"
        "C) Pokefinder \n\n""D) Pokeinfo",
        "Jakie są trzy typy pokemonów startowych?\n\nA) Trawiasty,Ognisty i Wodny \n\nB) Elektryczny,Ziemny i Trujący\n\n"
        "C) Smoczy,Latający i Normalny \n\nD) Psychiczny,Walczący i Duch",
        "Jak nazywa się głowny rywal Asha w podróży po regionie Kanto?\n\nA) Lance \n\nB) Giovanni \n\nC) Gary \n\nD) James",
        "Który z pokemonów nie jest evolucją Evee?\n\nA) Vaporeon \n\nB) Sylveon \n\nC) Leafeon \n\nD) Flygon",
        "Jak nazywa się pokemon uznawany za Boga?\n\nA) Arceus \n\nB) Mew \n\nC) Jirachi \nD) Celebi",
        "Jak brzmią imiona dwóch członków zespołu R?\n\nA) Jessie i James \n\nB) Joanie i James\n\n"
        "C) Jenny i John\n\nD)Jessie i John",
        "Kto użyczył głosu tytułowemu bohaterowi w filmie Detektyw Pikachu?\n\nA) Justice Smith\n\nB) Omar Chaparro\n\n"
        "C) Bill Nighy\n\nD) Ryan Reynolds",
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
    ]

    def getQuestion(self, index):
        return self.questions[index]


prompts_Games = [

]

prompts_Music = [

]


