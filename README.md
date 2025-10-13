
# Test du Khi-Deux d’adéquation 

# Vérification d’un dé équilibré

## Objectif

Ce projet a pour but d’écrire une fonction `chi_ad(x, p)` qui permet d’effectuer le **test du chi² d’adéquation** afin de vérifier si un dé est équilibré.

### Fonctionnalités principales :

1. Vérifie que `p` est un **vecteur de probabilités** (la somme doit être égale à 1).  
2. Vérifie que **toutes les coordonnées de `x`** (effectifs observés) sont **supérieures à 5**.  
3. Si les conditions sont remplies, effectue le **test du χ² d’adéquation** et renvoie :
   - la statistique du test `chi2_stat`,  
   - le nombre de degrés de liberté `ddl`,  
   - la p-valeur `p_valeur`.

---

## Test du Chi-Deux d'adéquation (χ²) pour un dé équilibré

```python

import numpy as np
import scipy.stats as stat

def chi_ad(x, p) :

    """
    Test du Chi-Deux d'adéquation.

    Paramètres :
    ------------
    x : liste ou array
        Effectifs observés.
    p : liste ou array
        Probabilités théoriques (somme = 1).

    Retour :
    --------
    [chi2_stat, ddl, p_valeur] si les conditions sont respectées.
    Sinon, message d'erreur descriptif.
    """

    # Vérifie que p est un vecteur de probabilités
    if round(np.sum(p), 10) != 1 :    # Pour éviter les erreurs d'imprécisions 
        return "Erreur : p n'est pas un vecteur de probabilités (somme ≠ 1)."

    # Vérifie que les coordonnées de x sont > 5
    if min(x) <= 5 :
        return "Erreur : toutes les coordonnées de x doivent être > 5."

    z = sum(x)    # Effectifs total
    y = np.array(p) * z    # Effectifs attendus 
    ddl = len(x) - 1    # Degrés de liberté
    chi2_stat, chi2_p_valeur = stat.chisquare(x, y)    # Test du chi2 d’adéquation

    # Affichage des résultats du test
    print(f"Statistique du test χ² : {chi2_stat:.4f}")
    print(f"Degrés de liberté : {ddl}")
    print(f"P-valeur : {chi2_p_valeur:.4f}")
    return [chi2_stat, ddl, chi2_p_valeur]

# Données utilisées 

x = [127, 108, 123, 118, 115, 135]    # Effectifs réels 
p = [1/6] * 6    # Probabilités attendues d'un dé équilibré

chi_ad(x, p)
```
---

## Résultats du test

```text
- Statistique du test χ² : 3.7190  
- Degrés de liberté : 5  
- P-valeur : 0.5905

[3.7190, 5, 0.5905]
```

## Interprétation du test

- H0 : le dé est équilibré (toutes les faces ont la même probabilité).  
- H1 : le dé n’est pas équilibré (au moins une face a une probabilité différente).  

### Décision :  
Comme p-valeur = 0.5905 > 0.05, on ne rejette pas H0 au seuil de 5 %.  

### Conclusion :  
Il n’y a pas de différence significative entre les effectifs observés et ceux attendus.    
Le dé paraît équilibré.
