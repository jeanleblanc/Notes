from importlib.abc import Traversable
from math import *

# Free code camp : python in 4h

    # Hello World & draw a shape

print("Hello World") #print va "imprimer" ce que l'on va ecrire"

print("   /|")
print("  / |")
print(" /  |")
print("/___|")
# Python execute les lignes dans l'ordre
print("___________________________________________________________________")

    # variable & data type

print("There once was a man named George, ")
print("he was 70 years old. ")
print("He really liked the name George, ")
print("but didn't like being 70.")
#une variable est un conteneur de donées
#changeons le nom et l'age du personnage -->
print("------------------------------------------")
name = "John"
age = "35"
print("There once was a man named "+ name+ ", ") # ajouter une variable entre deux "+"
print("he was "+age+ " years old. ") # attention de bien remmetre des guillemets
print("He really liked the name "+ name+" , ") #attention aux espaces
print("but didn't like being "+age+".")#pour changer le nom du personnage il 
#faut juste changer ce qui se trouve apres la variable ("john" --> "tom")
print("------------------------------------------")
name = "John"
age = "35"
print("There once was a man named "+ name+ ", ") 
print("he was "+age+" years old. ")
age = "78"
name = "tom"
print("He really liked the name "+ name+" , ") 
print("but didn't like being "+age+".")

#autres types de données
name = "tom" #chaine de charactere toujours entre "xx"
age = 50.5 #nombre
isMale = True  #boolean repondre True or False  

print("___________________________________________________________________")

    #Working with strings 

#string sont des chaine de caractere
print("giraffe academy")
print("giraffe \nacademy") #\n va passer dans la string à la ligne 
print("giraffe \"academy") # \" va litteralement ecire le guillemet
phrase = "Giraffe Academy"
print(phrase) 
print(phrase +" is cool")# concaténation : prend une chaine et en 
#ajoute une autre
print("------------------------------------------")
print(phrase.lower())#on peut ajouter une fonction à une string
# en locurence lower met tout en minuscule
print(phrase.upper()) #a l'inverse met tout en maj
print(phrase.isupper()) #verifie si la phrase est en majuscule
print(phrase.upper().isupper()) #on peut mettre une fonction apres une autre
print(len(phrase)) #pour savoir cb il y a de characteres
print(phrase[0]) #pour savoir quel est le caractere x de la phrase (ici 0)
#en python on commence a compter par 0
print(phrase.index("i")) #pour savoir en quelle position se trouve la lettre x
print(phrase.index("Aca")) #nous dis en quelle position commence xxx
#si on met dans index qq chose qui n'existe pas --> message d'erreur
print(phrase.replace("Giraffe", "Elephant")) #on remplace giraffe par (,) elephant

print("___________________________________________________________________")

# Working with numbers

print(2)#pour imprimer un nbrs 
print(3.643)#pour imprimer un nbrs decimal 
print(-535)#pour imprimer un nbrs negatif

print("------------------------------------------")
#on peut aussi faie des operations
print(4 + 4 - 7 * 2 / 2) #plus moins fois diviser
print(3 * (4 + 5))#PEMIMDAS
print(10 % 3)#10 mode 3 premier nbrs / deuxieme et renvoie le reste
print("------------------------------------------")
Num = 45
print (Num)#variable avec un num
print (str(Num) + " it's my age")#pour convertir num en 
#une string (pour pouvoir ajouter apres une string) ==> erreur si on le fait pas
Num = -5
print (abs(Num))#donne la valeure absolue
print (pow(5, 3))#x^y
print (max(5, 13))#renvoie le numero le plus grand
print (min(5, 13))#renvoie le numero le plus petit
print (round(3.7)) #arrondis ton nombre
#pour utiliser plus de fonction math il faut declarer <<from math import *>> en haut
print(floor(6.795139))#arrondi au nbrs le plus bas
print(ceil(1.2))#arrondi au plus grand
print(sqrt(9))#fait la racine carré

    #Getting input from users 

print("___________________________________________________________________")

#permetre à un utilisateur d'entrer des infos dans notre porgramme
#input("Enter your name : ") #input dis qu'on demande a l'user une info ("info: ")
#name = input("Enter your name : ")
#age = input("Enter your age : ")
#print ("Hello my name is "+name+" and i have "+age+" years old.") #pour 
#utiliser les données reçus

    #Building a basic calculator
    
print("___________________________________________________________________")

#premiere chose à faire est crée deux variable dans lequels on veut stocker
#les deux nombres que l'user veut additioner
#num1 = input("Enter a number : ") 
#num2 = input("Enter another number : ") 
#result_badexemle = num1 + num2 # ici il va faire comme si les var. etaient des 
#string donc va afficher 58 au lieu de 13
#result_int = int(num1) + int(num2) #int()va transformer ce qu'il y a dans la parenthese
# en nombre entier, on ne peut pas avoir de decimales...
#result = float(num1) + float(num2)
#print("Result : " +str(result))

    #Mad libs game
    
print("___________________________________________________________________")
#crée une mad libs en python (txt a trous remplis avec des mots aleatoires)
#color = input("Enter a color : ")
#plural_noun= input("Enter a plural noun : ")
#celebrity = input("Enter a celebrity : ")


#print("Rose are " + color)
#print(plural_noun+" are blue ")
#print("I love "+celebrity )

        #LIST
# structure utilisable a l'interieur de python
# on crée une liste pour mettre un tas de valeures liées   
friends = ["Kevin", "Karen", "Jim"] #[]pour dire qu'on va entrer des valeurs
#a notre liste
# variable = 1 value / List = xValue
friends = ["Kevin", 2, False] # on peut aussi mettre nbrs et bolean
friends = ["Kevin", "Karen", "Jim"] 
print(friends)
# pour avoir acces a un seul ca marche comme un index (0, 1, 2...)
print(friends[1]) #ca marche avec des nbrs negatif
print(friends[-1])#va renvoyer vers le dernier > ici le 2e
# [-2] l'avant dernier etc.
print(friends[1:]) #va donner l'element 1 et tout ce qu'il y a apres
friends = ["Kevin", "Karen", "Jim", "Oscar", "Jean", "Toby"]
print(friends[2:4]) # de l'element 2 a (:) 4 exclu
print(friends[:3]) # jusqu'a 3
friends[1] = "Mike" # pour changer la valeur de l'index 1
print(friends[1]) #ce sera mis a jour 
print("______________________________________________________________________")

# List function

lucky_nbrs = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

friends.extend(lucky_nbrs)#fonction extension :  prend une liste et 
#ajoute une autre liste a la fin
friends.append("Creed") # ajoute qq a la fin de la liste
friends.insert(1, "Kelly") # ajoute en position 1 kelly
friends.remove("Jim") #suprimme un element de la liste
friends.pop() #enleve  le dernier element de la liste
friends.clear() #efface tout ce qu'il y a dans la liste

lucky_nbrs = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
#on veut savoir si qq est dans cette liste
print(friends.index("Kevin")) #nous renvoi l'index (pos) de Kevin dans la liste
#si on met un nom qui n'est pas dans la liste > erreur
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
#on veut savoir si qq est dans cette liste
print(friends.count("Jim")) #nous renvoi le nbrs de Jim dans la liste
#si on met un nom qui n'est pas dans la liste > erreur

friends.sort() #va trier "" ordre alphabetique, 4 ordre croissant.
print(friends)

friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
friends.reverse() #va donner la liste dans le sens inverse
print(friends)

friends2 = friends.copy() #crée une copy de la liste 

print("______________________________________________________________________")


    # Tuples
#type de data structur containeur ou on peut stocker differente valeurs
#ressemble a une liste
coordinates = (4, 5) #pour crée un tuple on utilise () et on met les values qu'on veut stock
#particularité il est immuable : on pt pas le modif
print(coordinates[0]) #index ici est entre []
# on utilise les tuples pour des données qui ne vont jamais changer
coordinates = [(1, 5), (265,4), (2,3)] #on peut aussi crée des listes de tuple

print("______________________________________________________________________")

    #Fonctions
#collection de code qui acompli une tache particuliere

def say_hi(): #ça dit que tout le code qui va venir après c'est notre fonction
    #il faut forcement l'indenté (tab)
    print("Hello User") # mais en mettant jusque ça il ne le fait pas

say_hi() # il faut appeler la fonction
# python execute la fonction là ou elle est appelée

def sayhi(name):
    print("Hello " + name)
    
sayhi("Mike")
sayhi("Steve")

def SayHi(name, age):
    print("Hello " + name + " you are " + age) #si on veut mettre un int il faut 
    #rajouter str(age) et il va convertir en nbrs
    
    
SayHi("Tom", "45")
SayHi("John", "90")

print("______________________________________________________________________")

    #return statement 

def cube(num):
   return num*num*num #return va renvoyer tout les valeur inseré après
    #sans le return la fonction renvoi "none"
    
print(cube(3)) #si on ne print pas rien ne se passe

def cube(num):
   return num*num*num   
   print("code") 
    
#on peut crée une variable qui va stocker la valeur retourné par la fonction cube
result = cube(4)   
print(result) #comme on imprime la fonction ça ne va pas executer le "print"


print("______________________________________________________________________")

    #if statements
#c'est une structure special en python où on peut aider notre programme a 
#prendre des desisons, en utilisant if on peut utiliser un certain code quand
#certaine conditions sont vraies et inversement.
#ça permet à notre programme de repondre à ce qu'on peut lui envoyer
   
is_male = True
if is_male:
    print("you are a male") #ce qui est indenté va etre executé si la c'est est vraie
    
is_male = False
if is_male:
    print("you are a male") #Ne va rien faire quand c'est faux
else: # quand le if est faux alors il va executer le else
    print("you are not a male")
    
    #FAISONS PLUS COMPLEXE
    
is_male = False
is_tall = False

if is_male and is_tall: # si les deux sont vrais
    print("you are a big man")
elif is_male and not(is_tall): #si le 1e est vrai et pas le 2e
    print("your are a short male")
elif not(is_male) and is_tall: #si le 2e est vrai mais pas le 1e
    print("You are a big girl")
else: # seulement si aucun des deux est vrai
    print("you are a short girl")
    


print("______________________________________________________________________")

    #if statement & comparaisons

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3: #ici on compare deux nbrs maison peut aussi le faire avec des strings
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(35, 5, 4)) #va renvoyer 35 car il est le plus grand

def test_num(num1, num2):
    if num1 == num2: # est egale a 
        return True
    if num1 != num2: #n'est pas egal a
        return False
    if num1 > num2: # est plus grand que
        return big
    if num1 < num2: # est plus petit que 
        return small    #avec un seul egale ça fera plus petit ou egal

print("______________________________________________________________________")

    #test calculator (better)

#num1 = float (input("Enter first number: ")) #rappelle > converti en un nbrs  
#op = input("Enter operator: ")
#num2 = float (input("Enter second number: ")) #rappelle > converti en un nbrs  

#if op == "+": #on verifie si "op" est egal a la string "+"
 #   print(num1 + num2) #dans ce cas on additionne les input num1 et num2
#elif op == "-":
 #   print(num1 - num2)
#elif op == "/":
#    print(num1 / num2)
#elif op == "*":
#    print(num1 * num2)
#else:
 #   print("Invalid operator")

print("______________________________________________________________________")

    #DICTIONARIES
#structure special qui permet de stocker des infos dans ce qu'on apelle
#the keys value pair. On peut crée plein de clef de valeur pair et quand on 
# veut acceder a un element specifique du dic on peut s'y referé par sa clefs 

monthConversions = { #a droite valeur / a gauche la clef (le clefs doit etre UNIQUE)
    "Jan": "January",
    "Feb": "Februari",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "Augustus",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    #on peut aussi mettre des nbrs en tant que clefs (a la place des strings)
}
print(monthConversions["Jan"]) # ici va renvoyer la valeur associé  a la clef entre []

print(monthConversions.get("Dec"))# autre manniere de faire > avantage si valeur fausse
# il va renvoyer "none" au lieu d'un message d'erreur
print(monthConversions.get("Loc", "Not a default value")) #quand on est dans la 
# situation où la clefs n'est associé a aucune valeur, on peut luis passer une valeur par default
# qu'il va renvoyer seulement si la premiere n'est pas inscite dans le dic.
 
print("______________________________________________________________________")

    #While Loop

#structur en python qui nous permet de parcourir et executer un block de 
#code plusieur fois. 

i = 1
while i <= 10: #tant que c'est vrai on execute la loop
    print(i) #on imrpime "i"
    i += 1 #on ajoute 1 a "i" et on recommence pour voir si i <=

print("Done with loop") #quand "i" sera = ou > que 10 alors il va faire la suite >


print("______________________________________________________________________")

    # Building a guessing game

# on veut faire deviner au joueur un mot secret

#secret_word = "giraffe" #stock le mot secret
#guess = "" #stock les supposition du joueur
#guess_count = 0 # stock le nbrs d'essai qu'aura fait le joueur
#guess_limit = 3 #dit au programme la limite d'essai du joueur
#out_of_guesses = False

#while guess != secret_word and not(out_of_guesses): #on execute que si le mot entrer n'est pas le mot secret
    #et si la loop n'est pas out of guesses (False)
#    if guess_count < guess_limit: # a chaque loop on check si limite est plus grande que le compte
     #   guess = input("Enter a supposition: ")
    #    guess_count += 1 # a chaque fois que l'on fait un soposition le nbrs d'essai augmente
 #   else: #si ce n'est pas le cas
   #     out_of_guesses =True #on change out of guesses pour vrai
        
#if out_of_guesses: #si out of guess est vrai alors >
#    print("You lose...")
#else: # si non
#    print("You Win !!")

print("______________________________________________________________________")

    # For Loop
# Special type de loop pour loop sur defferentes collection d'elements
for letter in "Giraffe Academy":
    print(letter) # va imprimer toute les differentes lettres de la string

friends = ["Jim", "Karen", "Kevin"] 
for friend in friends: #pour chaque friend dans friends
    print(friend) #on imprime un friend
    
for index in range(10):
    print(index) #va imprimer tout les nombres de 0 à 10 exclu
    
print("-------------------------------------------------------------")
    
for index in range(3, 10): #2e position ne sera pas inclu
    print(index) #imprime les nombres entre 3 et 10

friends = ["Jim", "Karen", "Kevin"] 
len(friends) #va donner le nbrs d'elements dans la variable

for index in range(len(friends)): 
    print(friends[index]) #va imprimer les ami du nombre auxquelles ils sont
    #friends  [0], puis [1] et enfin [2] parce qu'on a trois amis 
    
for num in range(5) :
    if num == 0:
         print("first interaction")        
    else:
        print("not first")
       
       
print("______________________________________________________________________")

    # exponant fonction 
print(2**3) # 2 puissance 3 (** = puissance)

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num #va faire cet operation pow_num fois
    return result

print(raise_to_power(3, 4)) 

print("______________________________________________________________________")

    #2D lists & nested loops

number_grid = [
 [1, 2, 3], #au lieu de lister des elements on liste des listes
 [4, 5, 6],
 [7, 8, 9],
 [0]
]

#pour acceder a chaque elements individuellements
print(number_grid[2][1]) # [1ere = row] [2e = colone]


for row in number_grid :
    for col in row:
        print(col)


print("______________________________________________________________________")
     #Build a translator

#def translate(phrase):
 #   translation = ""
  #  for letter in phrase:
   #     if letter.lower() in "aeiou" :
    #       if letter.isupper():
     #           translation = translation + "G"
      #      else: 
       #         translation = translation + "g"
        #else:
         #   translation = translation + letter
 #   return translation

#print(translate(input("Enter a Phrase : ")))

print("______________________________________________________________________")

    # Try / Except
    
# number = int(input("Enter a num: "))
# print(number)
#ici si l'utilisateur entre autre chose qu'un entier le programme bug et arrete tout

#try:
  #  number = int(input("Enter a num: "))
 #   print(number)
#except: #pour toutes els erreurs dans try va renvoyer >
 #   print("Invalid input")

#on peut preciser les exeption

#try:
#    value = 10/0
#    number = int(input("Enter a num: "))
#    print(number)
#except ZeroDivisionError as err: 
#   print(err)
#except ValueError:
#    print("Invalid Input")

print("______________________________________________________________________")
    #Reading Files
    
#permet de lire un ficher externe
animal_file = open("/home/jean_a/Notes/python/.animal.txt", "r") # r dit qu'on va juste lire les info  dans le fichier
                        #w tu peux modifier le fichier
                        #r+ lire et ecrire

print(animal_file.readable()) #demande si le fichier est lisible

print(animal_file.readline()) #lis la premiere ligne
print(animal_file.readline()) #lis la ligne suivante

#print(animal_file.readlines() [1]) #lis ligne position index 1

print(animal_file.readlines() ) #lis chaque ligne > tableau


for animal in animal_file.readlines():
    print(animal)

animal_file.close() 

print("______________________________________________________________________")
    #Writing Files
    
animal_file = open("/home/jean_a/Notes/python/.animal.txt", "a")#ajoute du txt a la fin du fichier

animal_file.write("Foque") 
#poblemes ne passe pas a la ligne et si on execute 2x rajoute encore le mm
animal_file.write("\nMama") #pour passer a la ligne 

animal_file.close() 

animal_file = open("/home/jean_a/Notes/python/.animal-2.txt", "w")#va remplacer tout

animal_file.write("Mama") 

animal_file.close() 

animal_file = open("/home/jean_a/Notes/python/.animal-2.txt", "w")#va créer nouveau fichier$

animal_file.close() 


print("______________________________________________________________________")
    #Module and pip
 
#import useful_tools #on va importer le fichier et l'utiliser
#print(useful_tools.name) #on peut utiliser tout ce qu'il y a a l'interieur


print("______________________________________________________________________")
    #Classe and object
#aide a organiser son programme
#permet de crée sa propre data type (x string > Student)

#dans un autre fichier on a crée un classe "students" qui defini ce qu'est un etudiant
#ici on va créer un students, un objet
        
from student import Student

student1 = Student("Jim", "Buissness", 3.1, False) #on crée un etudiant
student2 = Student("Pam", "Art", 5.3, True) #on crée un etudiant

print(student1.name)#on peut avoir des information quant a notre etudiant
print(student1.gpa)
print(student2.name)








































































