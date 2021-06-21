import requests #permet de faire des requêtes HTTP
import json
import random
import time

def get_quote():
  responseQuote = requests.get("https://animechan.vercel.app/api/random")
  quote = json.loads(responseQuote.text)
  
  return(quote)


def get_joke():
  reponseJoke = requests.get(
  'https://www.blagues-api.fr/api/random',
  headers = {
    'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMjMxMDgwNzkzMDMwNTI0OTI4IiwibGltaXQiOjEwMCwia2V5IjoiUE5rZmpSZGlIdmdYQ1lLeGY4NWRudW1xTWNMMkRZWlJRT0xnVFkwenZ2SEJUbEJDd3QiLCJjcmVhdGVkX2F0IjoiMjAyMS0wNi0xOFQyMjowNDowOSswMDowMCIsImlhdCI6MTYyNDA1Mzg0OX0.29WM9oKQQYBx7ulT1hnX6HKeqCaIiDXufn8aTMleph0'
    }
  )

  joke = json.loads(reponseJoke.text)

  return(joke)


def get_Equipe():
  listEquipe = ["Equipe 1 = Dylan, Alexis / Equipe 2 = Loris, Clément","Equipe 1 = Dylan, Loris / Equipe 2 = Alexis, Clément", "Equipe 1 = Dylan, Clément / Equipe 2 = Loris, Alexis"]

  i = random.randint(0,2)

  equipe = listEquipe[i]

  return equipe




def get_mode_de_jeux():

  listMdj = ["FootCar","Rumble","Gidage Thermique","Panier"]
  i = random.randint(0,3)
  
  modeDeJeux = listMdj[i]

  return modeDeJeux


def get_Mutateur():

  listMutateur = ["Basic", "Ballon lunaire", "Démoliton", "Saut dans le temps", "Flipper", "Cubique", "Ballon de plage", "Jour de neige", "Ruée de Crampons"]

  i = random.randint(0,8)

  mutateur = listMutateur[i]

  return mutateur

def get_Game():
  message = "``" + "Voiture à utiliser : " + get_car() +"\n"+ "Les équipes seront : " + get_Equipe() +"\n"+ "Mutateur : " + get_Mutateur () +"\n"+  "ou" +"\n"+ get_Mutateur_Complet() +"\n"+ "Sur le mode de jeux : " + get_mode_de_jeux()  +"``"

  return message
  
def get_Mutateur_Complet():

  i = 0 #va être génerer aléatoirement par la suite
  
  listScoreMax = ["1", "3", "5", "7", "illimité"]

  i = random.randint(0,3)
  scoreMax = listScoreMax[i]

  listProlongation = ["Par défaut", "MAX +5, MORT SUBITE", "MAX +5, EQUIPE ALEATOIRE"]

  i = random.randint(0,2)
  prolongation = listProlongation[i]

  listSerie = ["ILLIMITE", "3 MANCHES", "5 MANCHES", "7 MANCHES"]

  i = random.randint(0,3)
  serie = listSerie[i]
  
  listVitesseDeJeux = ["STANDARD", "RALENTI", "SAUT DANS LE TEMPS"]

  i = random.randint(0,2)
  vitesseJeux = listVitesseDeJeux[i]

  listVitesseMaxBallon = ["STANDARD", "LENTE", "RAPIDE", "SUPER RAPIDE"]

  i = random.randint(0,3)
  vitesseBallon = listVitesseMaxBallon[i]

  listTypeDeBallon = ["STANDARD", "CUBE", "PALET", "BASKETBALL", "BALLON DE PLAGE", "ANNIVERSAIRE"]

  i = random.randint(0,5)
  ballon = listTypeDeBallon[i]

  listPoidDuBallon = ["STANDARD", "FAIBLE", "FORT", "TRES FAIBLE", "BALLE COURBE", "COURBE BALLON DE PLAGE"]

  i = random.randint(0,5)
  poid = listPoidDuBallon[i]

  listTailleDuBallon = ["STANDARD", "PETITE", "MOYENNE", "GRANDE", "GEANTE"]

  i = random.randint(0,4)
  taille = listTailleDuBallon[i]

  listRebondissement  = ["STANDARD", "FAIBLE", "FORT", "SUPER FORT"]

  i = random.randint(0,3)
  rebondissement = listRebondissement[i]

  listNbTurbo = ["STANDARD", "SANS TURBO", "ILLIMITE", "RECHARCHE (LENTE)", "RECHARCHE (RAPIDE)"]

  i = random.randint(0,4)
  turbo = listNbTurbo[i]

  listRumble = ["AUCUN", "DEFAUT", "LENT", "CIVILISE", "DEMOLITION", "RESSORTS CHARGES", "CRAMPONS SEULEMENT", "RUEE DE CRAMPONS"]

  i = random.randint(0,7)
  rumble = listRumble[i]

  listPuissanceTurbo = ["X1", "X1.5", "X2", "X10"]
  i = random.randint(0,3)
  turbo = listPuissanceTurbo[i]

  listGravite = ["STANDARD", "BASSE", "FORTE", "SUPER FORTE"]

  i = random.randint(0,3)
  gravite = listGravite[i]

  listDestruction = ["STANDARD", "AUCUNE", "TIRS AMIS", "EN CONTACT", "EN CONTACT (TA)"]

  i = random.randint(0,4)
  destruction = listDestruction[i]

  listTempsDeReprise = ["3 SECONDES", "2 SECONDES", "1 SECONDE", "DESACTIVE"]

  i = random.randint(0,3)
  tempsReprise = listTempsDeReprise[i]

  regle = "RULES ARE : " +"\n"+ "Score max = " + scoreMax +"\n"+ "Prolongation = " + prolongation +"\n"+"Serie = " + serie +"\n"+ "Vitesse de jeux = " + vitesseJeux +"\n"+ "Vitesse du ballon = " + vitesseBallon +"\n"+ "Type de ballon = " + ballon +"\n"+ "Poid du ballon = " + poid +"\n"+ "Taille du ballon = " + taille +"\n"+ "Rembondissement = " + rebondissement +"\n"+ "Turbo = " + turbo +"\n"+ "Rumble (si vous souhaitez vous en servir) = " + rumble +"\n"+ "Turbo = " + turbo +"\n"+ "Gravite = " + gravite +"\n"+ "Destruction = " + destruction +"\n"+ "Temps de reprise = " + tempsReprise
  
  return regle



def get_car():

  car = "octane"

  listCar = ["octane / fennec", "Dominus", "breakout", "gizmo", "backfire", "merc", "paladin", "hotshot", "road hog", "venom", "X-devil"]

  i = random.randint(0,10)

  car = listCar[i]

  return car

  #end Function