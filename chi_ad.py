
import numpy as np
import scipy.stats as stat

def chi_ad(x, p) :
    
    if round(np.sum(p), 10) != 1 :     # Pour éviter les erreurs d'imprécisions 
        return "p n'est pas un vecteur de probabilités (somme différente de 1)."
    
    if min(x) <= 5 :
            return "Toutes les coordonnées de x ne sont pas supérieurs à 5."
    
    z = sum(x)     # Effectifs total
    y = np.array(p) * z     # Effectifs attendus 
    ddl = len(x) - 1     # Degrés de liberté
    chi2_stat, chi2_p_valeur = stat.chisquare(x, y)     # Test du chi2 d’adéquation
    
    print(f"La statistique du test chi2 est égale à {chi2_stat}.")
    print(f"Le degré de liberté est égal à {ddl}.")
    print(f"La p_valeur est égale à {chi2_p_valeur}.")
    return [chi2_stat, ddl, chi2_p_valeur]

x = [127, 108, 123, 118, 115, 135]     # Effectifs réels 
p = [1/6] * 6     # Probabilités attendues d'un dé équilibré

chi_ad(x, p)
