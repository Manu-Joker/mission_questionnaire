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
import sys
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

        # Transforme les tuple des choix en : choix[1], choix[2] etc...
        choix = [i[0] for i in data['choix']]

        [bonne_reponse] = [i[0] for i in data['choix'] if i[1]]  # bonne réponse lorsque le bool est True
        # Si aucune ou plusieurs bonnes réponses, il y'a anomalie dans les données
        if len([bonne_reponse]) != 1:
            return None

        # i've to know how to identificate the right answer
        q = Question(data['titre'], choix, bonne_reponse)
        return q

    def poser(self, numero_question, nb_questions):    # Afficher le num de la question

        print(f"QUESTION n°{numero_question} / {nb_questions}")
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

    def from_json_data(data):

        if not data.get('questions'):
            return None
        questionnaire_data_question = data['questions']
          # Poser pr toutes les questions

        questions = [Question.FromJsonData(i) for i in questionnaire_data_question]
        # Supprime les questions None (Qui n'ont pas pu être crée)
        questions = [i for i in questions if i]

        # Dans le cas où le fichier json ne contient pas de "catégorie" ou de "difficulté", on la suppose inconnue

        # Par contre si elle ne contient pas de "titre" ou de "questions", on return None
        if not data.get('categorie'):
            data["categorie"]= 'Inconnue'
        if not data.get('difficulte'):
            data["difficulte"] = 'Inconnue'

        if not data.get('titre'):
            return None



        return Questionnaire(data['categorie'], data['titre'], data['difficulte'], questions)

    def from_json_file(file_name):

        try:
            file = open(file_name, "r")
            json_data = file.read()
            file.close()
            questionnaire_data = json.loads(json_data)  # charger en ficher lisible (str)
        except:
            print("Exception lors de l'ouverture du fichier")
            return None
        return Questionnaire.from_json_data(questionnaire_data)

    def lancer(self):
        score = 0
        nb_questions = len(self.questions)
        print(f"CATEGORIE: {self.categorie}")
        print(f"Titre de catégorie: {self.titre_de_categorie}")
        print(f"Difficulté: {self.difficulte}")
        print(f"Nombre de question: {nb_questions}")
        for i in range(nb_questions):
            question = self.questions[i]
            if question.poser(i+1, nb_questions):
                score += 1
        print("Score final :", score, "sur", len(self.questions))
        return score





 # 'questionnaire_data' contains category, title , questions and difficulty level
    # 'questions' contains titles and choices
    # 'choix' contains the choice in question,  and true response

    # Identifier la catégorie, titre et difficulte grace au fichier data

# Faire des fonctions pour gérer le choix de la catégorie,
#    Si possible du titre de catégorie,
#    Et ensuite celle de la difficulté

# First of all select the category, category title and difficulty by user





"""i = 0   # Gérer l'affichage des numéros
for file_name in file_names:
    i += 1     # Implémenter la valeur de i de +1 à chaque boucle
    categorie, titre_de_categorie, difficulte, question_data_question= file_parameter(file_name)
    print(f"{i}) Catégorie: '{categorie}'      ------ Titre: '{titre_de_categorie}'     ------     Difficulté: '{difficulte}'  ")
"""

"""choix_joueur = int(input("Votre préférence:"))

questions = []
file_choice = file_names[choix_joueur-1]     # Choix de fichier du user  """

"""categorie_c, titre_de_categorie_c, difficulte_c, question_data_question_c = file_parameter(file_choice) # Paramètres de catégorie choisie du user"""



#print(titre_de_categorie)

#q.poser()
"""Questionnaire(categorie_c, titre_de_categorie_c, difficulte_c, questions).lancer()"""

"""Questionnaire.from_json_file("cinema_starwars_debutant.json").lancer()
"""

if __name__ == "__main__":   # Ici, le nom du fichier "questionnaire.py" est "main"

    print(sys.argv) # Gérer les noms de fichiers

    if len(sys.argv) < 2:
        print("ERREUR: Veuillez spécifier le nom du fichier json à charger")
        exit(0)
    json_file_name = sys.argv[1]
    questionnaire = Questionnaire.from_json_file(json_file_name).lancer()

    if questionnaire:
        questionnaire.lancer()  # Lancer le questionnaire

else:               # Au cas où on a importé ce fichier dans un autre fichier, son nom ne sera plus 'main'
    print(__name__)  # Donc afficher cet autre nom





