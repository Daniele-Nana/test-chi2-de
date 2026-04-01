# Test du chi² d'adéquation – Vérification de l'équilibre d'un dé

## Contexte

Dans l'industrie statistique, le test du chi² d'adéquation (*goodness‑of‑fit*) permet de comparer une distribution observée à une distribution théorique. Ce projet implémente une fonction R robuste pour réaliser ce test, puis l'applique à un cas concret : vérifier si un dé à six faces est équilibré à partir d'un échantillon de lancers.

## Structure du projet

Le dépôt contient un unique fichier R Markdown (`test-chi2-de.Rmd`) qui regroupe :

- L'implémentation de la fonction `chi.ad(x, p)` avec vérifications des conditions d'application.
- L'application aux données observées du dé.
- Les calculs de la statistique, des degrés de liberté et de la p‑valeur.
- Les visualisations (diagramme en barres comparant effectifs observés et attendus).
- L'interprétation et la conclusion.

## Technologies utilisées

- **R (version ≥ 3.6)** – langage statistique.
- **R Markdown** – pour la création d'un rapport reproductible mêlant code et commentaires.
- **Packages R** :
  - `knitr` – pour la compilation du notebook.
  - `rmarkdown` – pour la production de rapports HTML/PDF.
  - `ggplot2` *(optionnel)* – pour des graphiques plus avancés.

## Prérequis et installation

### 1. Installer R

Téléchargez R depuis [CRAN](https://cran.r-project.org/) et installez‑le sur votre système.

### 2. Installer les packages nécessaires

Ouvrez R et exécutez :
```r
install.packages(c("knitr", "rmarkdown"))
```

Si vous souhaitez utiliser `ggplot2` pour les graphiques :
```r
install.packages("ggplot2")
```

### 3. Récupérer le projet

Clonez ce dépôt ou téléchargez le fichier `chi2_de.Rmd` :
```bash
git clone https://github.com/Daniele-Nana/test-chi2-de.git
```

### 4. Exécution

- Ouvrez `test-chi2-de.Rmd` dans RStudio ou dans un éditeur supportant R Markdown (VS Code avec extension R).
- Exécutez les cellules une à une ou utilisez le bouton **Knit** pour générer un rapport HTML complet.

## Hypothèses du test

- **H₀** : le dé est équilibré → chaque face a une probabilité théorique de 1/6.
- **H₁** : le dé n'est pas équilibré → au moins une face a une probabilité différente.

> **Conditions d'application** : tous les effectifs observés doivent être ≥ 5 (vérifiées par la fonction).

## Résultats obtenus

| Statistique | Degrés de liberté | p‑valeur |
|:-----------:|:-----------------:|:--------:|
| 3.7195      | 5                 | 0.5905   |

- Seuil α = 0,05.
- La p‑valeur (0,5905) est supérieure à α.
- **Conclusion** : on ne rejette pas H₀. Les écarts observés sont compatibles avec un dé équilibré.

## Pistes d'amélioration

1. **Généralisation** : adapter la fonction pour accepter des probabilités théoriques quelconques, pas seulement équiprobables.
2. **Simulation** : ajouter une validation par simulation Monte Carlo pour étudier la puissance du test.
3. **Interface utilisateur** : créer une application Shiny permettant à l'utilisateur de saisir ses propres effectifs et de visualiser le résultat en temps réel.
4. **Rapport dynamique** : générer automatiquement un rapport PDF/HTML avec des commentaires interprétatifs paramétrés.
5. **Intégration continue** : utiliser GitHub Actions pour exécuter le notebook à chaque commit et publier le rapport.

## Auteur

Daniele Nana