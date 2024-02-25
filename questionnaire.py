# PROJET QUESTIONNAIRE V3 : POO
#
# - Pratiquer sur la POO
# - Travailler sur du code existant
# - Mener un raisonnement
#
# -> Définir les entitées (données, actions)
#
# Question
#    - titre       - str
#    - choix       - (str)
#    - bonne_reponse   - str
#
#    - poser()  -> bool
#
# Questionnaire
#    - questions      - (Question)
#
#    - lancer()
#

import json

# I've first to import json files here
# fichiers json
file_names = ["animaux_leschats_confirme.json", "animaux_leschats_debutant.json", "animaux_leschats_expert.json", "arts_museedulouvre_confirme.json", "arts_museedulouvre_debutant.json", "arts_museedulouvre_expert.json", "cinema_alien_confirme.json", "cinema_alien_debutant.json", "cinema_alien_expert.json", "cinema_starwars_confirme.json", "cinema_starwars_debutant.json", "cinema_starwars_expert.json"]
for file_name in file_names:
    file = open(file_name, "r")
    json_data = file.read()
    questionnaire_data = json.loads(json_data)    #  charger en ficher lisible (str)
    print(questionnaire_data['questions'][2]['choix'])
    # 'questionnaire_data' contains category, title , questions and difficulty level
    # 'questions' contains titles and choices
    # 'choix' contains the choice in question,  and true response

# Choose the category , the title of the category and the difficulty before starting to ask questions
class Head:
    def __init__(self, categorie, titre_de_categorie, difficulte):
        self.categorie = categorie
        self.titre_de_categorie = titre_de_categorie
        self.difficulte = difficulte

    # Identifier la catégorie, titre et difficulte grace au fichier data

    def tirer_parametres_de_data(self):
        parametres = [file_name.replace("_", " ")]  # Tirer les paramètres à travers le nom du fichier



# Faire des fonctions pour gérer le choix de la catégorie,
                #    Si possible du titre de catégorie,
                     #    Et ensuite celle de la difficulté

class Question:
    def __init__(self, titre_de_question, choix, bonne_reponse):
        self.titre = titre_de_question
        self.choix = choix
        self.bonne_reponse = bonne_reponse



    def FromData(data):
        # ....
        for i in data['questions'] :
            data_question = data['questions'][i]
            data_choix = data_question['choix']
            for c in data_choix:
                les_choix = []
                choix = c[0]
                les_choix.append(choix)  # constituer la liste des choix avant de gérer la bonne réponse
                if choix[1] == "True":
                    b_reponse = choix   # identification de la bonne réponse

        # i've to know how to identificate the right answer
        q = Question(data_question['titre'], les_choix, b_reponse)
        return q

    def poser(self):
        print("QUESTION")
        print("  " + self.titre_de_question)
        for i in range(len(self.choix)):
            print("  ", i+1, "-", self.choix[i])

        print()
        resultat_response_correcte = False
        reponse_int = Question.demander_reponse_numerique_utlisateur(1, len(self.choix))
        if self.choix[reponse_int-1].lower() == self.bonne_reponse.lower():
            print("Bonne réponse")
            resultat_response_correcte = True
        else:
            print("Mauvaise réponse")
            
        print()
        return resultat_response_correcte

    def demander_reponse_numerique_utlisateur(min, max):
        reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return Question.demander_reponse_numerique_utlisateur(min, max)
    
class Questionnaire:
    def __init__(self, questions):
        self.questions = questions

    def lancer(self):
        score = 0
        for question in self.questions:
            if question.poser():
                score += 1
        print("Score final :", score, "sur", len(self.questions))
        return score


"""questionnaire = (
    ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
    ("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    ("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
                )

lancer_questionnaire(questionnaire)"""

# q1 = Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris")
# q1.poser()

# data = (("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris", "Quelle est la capitale de la France ?")
# q = Question.FromData(data)
# print(q.__dict__)

"""Questionnaire(
    (
    Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
    Question("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    Question("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
    )
).lancer()"""

