import sys

def somme_valeurs_etalonnage(chemin_fichier):
    somme_totale = 0
    try:
        with open(chemin_fichier, "r", encoding="utf-8") as fichier:
            for ligne in fichier:
                l = len(ligne)
                p, s = 0, 0
                for i in range(l):
                    if ligne[i].isdigit() and not p:
                        p = ligne[i]
                    if ligne[l - i - 1].isdigit() and not s:
                        s = ligne[l - i - 1]
                    if p and s: # si p != 0 et s != 0 
                        break 
                somme_totale += int(p + s)
        return somme_totale
    except FileNotFoundError:
        print(f"Le fichier {chemin_fichier} n'a pas été trouvé.")
        return -1
    

def main():
    # Vérifier si un argument a été passé
    if len(sys.argv) != 2:
        print("Usage: python somme_valeurs_etalonnage.py <fichier_d'entrée>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    # Appeler la fonction somme_valeurs_etalonnage avec le fichier passé en argument
    total = somme_valeurs_etalonnage(input_file)
    if total != -1:
        print(f"Somme des valeurs d'étalonnage : {total}")

if __name__ == '__main__':
    main()
