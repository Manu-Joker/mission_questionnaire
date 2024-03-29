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


class Question:
    def __init__(self, titre_de_question, choix, bonne_reponse):
        self.titre_de_question = titre_de_question
        self.choix = choix
        self.bonne_reponse = bonne_reponse



    def FromJsonData(data):
        # ....


        choix = [i[0] for i in data['choix']]

        [bonne_reponse] = [i[0] for i in data['choix'] if i[1]]  # bonne réponse lorsque il y'a True
        if len([bonne_reponse]) != 1:
            return None

        # i've to know how to identificate the right answer
        q = Question(data['titre'], choix, bonne_reponse)
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


# Choose the category , the title of the category and the difficulty before starting to ask questions

class Questionnaire:  # Reconstituer la classe Questionnaire

    def __init__(self, categorie, titre_de_categorie, difficulte, questions):
        self.categorie = categorie
        self.titre_de_categorie = titre_de_categorie
        self.difficulte = difficulte
        self.questions = questions


    def lancer(self):
        score = 0
        print(f"CATEGORIE: {self.categorie}")
        print(f"Titre de catégorie: {self.titre_de_categorie}")
        print(f"Difficulté: {self.difficulte}")
        for question in self.questions:
            if question.poser():
                score += 1
        print("Score final :", score, "sur", len(self.questions))
        return score


def file_parameter(file_name):
    file = open(file_name, "r")
    json_data = file.read()
    file.close()
    questionnaire_data = json.loads(json_data)  # charger en ficher lisible (str)
    categorie = questionnaire_data['categorie']
    titre_de_categorie = questionnaire_data['titre']
    difficulte = questionnaire_data['difficulte']
    question_data_question = questionnaire_data['questions']
    return categorie, titre_de_categorie, difficulte, question_data_question


 # 'questionnaire_data' contains category, title , questions and difficulty level
    # 'questions' contains titles and choices
    # 'choix' contains the choice in question,  and true response

    # Identifier la catégorie, titre et difficulte grace au fichier data

# Faire des fonctions pour gérer le choix de la catégorie,
#    Si possible du titre de catégorie,
#    Et ensuite celle de la difficulté

# First of all select the category, category title and difficulty by user


file_names = ["animaux_leschats_confirme.json", "animaux_leschats_debutant.json", "animaux_leschats_expert.json",
              "arts_museedulouvre_confirme.json", "arts_museedulouvre_debutant.json", "arts_museedulouvre_expert.json",
              "cinema_alien_confirme.json", "cinema_alien_debutant.json", "cinema_alien_expert.json",
              "cinema_starwars_confirme.json", "cinema_starwars_debutant.json", "cinema_starwars_expert.json"]


print("Voulez-vous que votre questionnaire soit de :")

i = 0   # Gérer l'affichage des numéros
for file_name in file_names:
    i += 1     # Implémenter la valeur de i de +1 à chaque boucle
    categorie, titre_de_categorie, difficulte, question_data_question= file_parameter(file_name)
    print(f"{i}) Catégorie: '{categorie}'      ------ Titre: '{titre_de_categorie}'     ------     Difficulté: '{difficulte}'  ")


choix_joueur = int(input("Votre préférence:"))

questions = []
file_choice = file_names[choix_joueur-1]     # Choix de fichier du user

categorie_c, titre_de_categorie_c, difficulte_c, question_data_question_c = file_parameter(file_choice) # Paramètres de catégorie choisie du user



#print(titre_de_categorie)
for i in range(0, len(question_data_question_c)):   # Poser pr toutes les questions
    q = Question.FromJsonData(question_data_question_c[i])
    questions.append(q)
#q.poser()
Questionnaire(categorie_c, titre_de_categorie_c, difficulte_c, questions).lancer()













