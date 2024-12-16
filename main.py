#### Imports et définition des variables globales


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici
    carac = [s[0]]
    occurence = [1]
    i = 1
    while(i<len(s)):
        if s[i] == s[i-1]:
            occurence[-1] += 1
        else:
            carac.insert(s[i])
            occurence.insert(1)           
    fin = zip(carac,occurence)                 
    return fin


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    
    # votre code ici
    # cas de base
    lettre_courante = s[0]
    occurence = 0
    # recherche nombre de caractères identiques au premier
    for lettre in s:
        if lettre_courante == lettre:
            occurence += 1
        else:
            break

    return [('lettre_courante,occurence')+artcode_r(s[occurence::])]
    

#### Fonction principale


def main():
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
