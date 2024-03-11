import json
import unittest
from unittest.mock import patch
import questionnaire
import os
import questionnaire_import

def additionner(a, b):
    return a+b


def conversion_nombre():
    num_str = input("Rentrez un nombre : ")
    return int(num_str)


class TestsUnitaireDemo(unittest.TestCase):
    def setUp(self):   # Permet de tester avant le début de l'exécution
        print("setUp")

    def tearDown(self):   # Tester à la fin de l'exécution
        print("tearDown")

    def test_additionner_nombres_positifs(self):
        print("test_additionner1")
        self.assertEqual(additionner(5, 10), 15)
        self.assertEqual(additionner(6, 10), 16)
        self.assertEqual(additionner(6000, 5), 6005)

    def test_additionner_nombres_negatifs(self):
        print("test_additionner2")
        self.assertEqual(additionner(-6, -10), -16)

    def test_conversion_nombre_valide(self):
        with patch("builtins.input", return_value="10"):
            self.assertEqual(conversion_nombre(), 10)
        with patch("builtins.input", return_value="100"):
            self.assertEqual(conversion_nombre(), 100)
   
    def test_conversion_entree_invalide(self):       
        with patch("builtins.input", return_value="abcd"):
            self.assertRaises(ValueError, conversion_nombre)

class TestsQuestion(unittest.TestCase):
    def test_question_bonne_mauvaise_reponse(self):
        choix = ("choix1", "choix2", "choix3")
        q = questionnaire.Question("titre_question", choix, "choix2")
        with patch("builtins.input", return_value="1"):
            self.assertFalse(q.poser(1, 1))
        with patch("builtins.input", return_value="2"):
            self.assertTrue(q.poser(1, 1))
        with patch("builtins.input", return_value="3"):
            self.assertFalse(q.poser(1, 1))

class TestQuestionnaire(unittest.TestCase):
    def test_questionnaire_cinema_starwars_debutant(self):
        filename = os.path.join("test_data", "cinema_starwars_debutant.json")
        q = questionnaire.Questionnaire.from_json_file(filename)
        self.assertIsNotNone(q)  # tester si q ne retourne pas de None
        # Maintenant tester si le nombre de questions est correct
        # le titre, La catégorie, la difficulté
        # patcher le input --> forcer de répondre tjrs à 1 --> Score c'est 4
        # lancer

        self.assertEqual(len(q.questions), 10)
        self.assertEqual(q.titre_de_categorie, "Star wars")
        self.assertEqual(q.categorie, "Cinéma")
        self.assertEqual(q.difficulte, "débutant")
        with patch("builtins.input", return_value="1"):
            self.assertEqual(q.lancer(), 1)    #Tester si le score donne tjrs 1/10 si on répond tjrs 1 aux questions


    def test_invalide_code(self):
    # Fichier ne contenant pas de catégorie, ni de "difficulté"
        filename = os.path.join("test_data", "format_invalide1.json")
        q = questionnaire.Questionnaire.from_json_file(filename)
        self.assertIsNotNone(q)
        self.assertEqual(q.categorie, "Inconnue")
        self.assertEqual(q.difficulte, "Inconnue")
        self.assertIsNotNone(q.questions)

    # Fichier ne contenant que  "question" (aucun autre paramètre)
        filename = os.path.join("test_data", "format_invalide2.json")
        q = questionnaire.Questionnaire.from_json_file(filename)
        self.assertIsNone(q)

    # Fichier ne contenant "titre" (aucun autre paramètre)
        filename = os.path.join("test_data", "format_invalide3.json")
        q = questionnaire.Questionnaire.from_json_file(filename)
        self.assertIsNone(q)


class TestsImportQuestionnaire(unittest.TestCase):
    def test_import_format_json(self):
        questionnaire_import.generate_json_file("Arts", "Musée du Louvre", "https://www.codeavecjonathan.com/res/mission/openquizzdb_86.json")
        filenames = "animaux_leschats_confirme.json", "animaux_leschats_debutant.json", "animaux_leschats_expert.json"
        for filename in filenames:
    # Vérifier si le fichier existe
            self.assertTrue(os.path.isfile(filename))
            file = open(filename)
            json_data = file.read()
            file.close()
            try:
                data = json.loads(json_data)
            except:
    # Si on arrive pas à charger les données, on fait échouer le test
                self.fail(f"Problème de décérialisation de données pour le fichier {filename}")

    #  titre, questions, difficulté, catégorie
    # Questions --> titre, choix
    # Choix  --> longueur du titre > 0
    # ...... --> 2è champ est bien un bool (isinstance(...., bool))
    #  --> il y'a une seule bonne réponse

            self.assertIsNotNone(data.get("titre"))
            self.assertIsNotNone(data.get("questions"))
            self.assertIsNotNone(data.get("difficulte"))
            self.assertIsNotNone(data.get("categorie"))

            questions = data.get("questions")

            for question in questions:
                self.assertIsNotNone(question.get("titre"))
                self.assertIsNotNone(question.get("choix"))

                for choix in question.get("choix"):

                    self.assertGreater(len(choix[0]), 0)
                    # ou ça self.assertTrue(len(choix[0]) > 0)
                    self.assertTrue(isinstance(choix[1], bool))

                bonnes_reponses = [i[0] for i in question.get("choix") if i[1]]
                # print(bonnes_reponses)
                self.assertEqual(len(bonnes_reponses), 1)







unittest.main()