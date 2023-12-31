
#Nombre premiers
#Nombres qui sont uniquement divisibles par eux mêmes et par 1

#Algorithmiquement on peut donc générer une liste qui contient tous les entiers inférieurs à X et tester si X % list[i] == 0
#A noter que l'ordre dans lequel on teste les entiers de la liste a son importance puisque il vaut mieux partir de 2 vers + l'infini
#Que de X vers 2
#A noter que comme tout entier est divisible par 1 on a pas vraiment besoin de tester ça.
#Le processus va donc sans doute ressembler à une suite de tests qui visent à éprouver des cas particuliers de divisibilité euclidienne
#Si l'un des tests est vrai le nombre n'est pas premier et le reste des tests n'est pas exécuté.
#Les tests doivent donc être ordonnés du plus probablement vrai au plus improbablement vrai
#En prenant aussi éventuellement en compte la complexité computationelle du test
#Zbrah
# Test de la /2
#Ah oui et du coup le fait de tester 2 nous dispense de tester tous les multiples de 2 soit les nombres pairs
#Allez on balance le switch
import numpy as np
import time

def is_prime_number(number:int) -> bool:

    if number == 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    elif number % 10 == 0 or number % 10 == 5:
        return False
    else:
        max_divisor = round(number**0.5) + 1 
        for i in range(3, max_divisor, 2):
            if i % 10 == 0 or i % 10 == 5:
                continue
            elif number % i == 0:
                return False
    return True

start_time = time.time()
print(is_prime_number(10000000207))
end_time = time.time()
print(end_time - start_time)
#On commence à ramer un chouilla, quelques secondes autour de 10^6
#A 10^7 on est bien long
#Installer Time ou qqch comme ça pour mesurer le temps d'exécution
#Finalement j'ai juste arrêter de générer une liste de nombres à tester c'était bête
#Avec ce résultat ça va assez vite pour des nombres de 10^8, 10^9
#A 10^10 ça commence à ramer sérieusement
#On est à 400 secondes soit 6 minutes



