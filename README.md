# Parser de Document d'Étalonnage

Ce projet résout le problème d'extraction des valeurs d'étalonnage à partir d'un document composé de lignes contenant des caractères alphanumériques. La valeur d'étalonnage sur chaque ligne est formée en combinant le premier chiffre et le dernier chiffre dans cet ordre.

## Description du Problème

L'objectif est d'extraire la valeur d'étalonnage de chaque ligne d'un document donné. La valeur d'étalonnage est déterminée selon la règle suivante :

- Trouver le premier et le dernier chiffre de chaque ligne.
- Les combiner (premier chiffre + dernier chiffre) pour former un nombre à deux chiffres.

### Exemple :

Pour les lignes d'entrée suivantes :

- `1abc2` → Valeur d'étalonnage : `12`
- `pqr3stu8vwx` → Valeur d'étalonnage : `38`
- `a1b2c3d4e5f` → Valeur d'étalonnage : `15`
- `treb7uchet` → Valeur d'étalonnage : `77`

En additionnant ces valeurs d'étalonnage, on obtient : `12 + 38 + 15 + 77 = 142`

## Solution

La solution suit ces étapes :

1. **Analyse de l'Entrée** : Lire le document d'entrée (ou les lignes de texte).
2. **Extraction des Chiffres** : Pour chaque ligne, extraire le premier et le dernier chiffre.
3. **Combinaison** : Former le nombre d'étalonnage en concaténant le premier et le dernier chiffre.
4. **Somme** : Additionner toutes les valeurs d'étalonnage.

## Utilisation

1. Clonez ce répertoire :

   ```bash
   git clone https://github.com/abirsouissi/etalonnage.git

Allez dans le répertoire du projet :

cd etalonnage

Exécutez le programme pour calculer la somme des valeurs d'étalonnage :

    Usage: python somme_valeurs_etalonnage.py <fichier_d'entrée>

Technologies Utilisées

    Python 3.x
