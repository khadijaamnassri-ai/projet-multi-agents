# Fiche : `tweet_discusses_claim`

**Source :** `data/mumin_raw/tweet_discusses_claim`  
**Projet :** Projet_MultiAgents (SMA / NetLogo)

---

## 1. Présentation du fichier

Cette table relie les **tweets** aux **claims** qu’ils discutent.

| Indicateur | Valeur |
|---|---:|
| Lignes (relations) | 42 913 |
| Colonnes | 3 |
| Valeurs manquantes | 0 |

---

## 2. Colonnes importantes

| Colonne | Signification | Utilité |
|---|---|---|
| `src` | Identifiant du **tweet** | Point de départ du lien |
| `tgt` | Identifiant du **claim** | Claim discuté |
| `relevance` | Score de pertinence | Filtrage optionnel |

En résumé : **`src` = tweet**, **`tgt` = claim**.

---

## 3. Résultats de l'analyse

| Statistique | Valeur |
|---|---:|
| Nombre de relations | 42 913 |
| Tweets distincts (`src`) | 26 190 |
| Claims distincts (`tgt`) | 13 196 |

### Exemples

| src (tweet) | tgt (claim) | relevance |
|---|---|---:|
| 1243046281326534661 | 325195 | 0,705 |
| 1243148522209161217 | 325195 | 0,709 |
| 1238795119572049920 | 325195 | 0,772 |

### Vérification d’intégrité

| Contrôle | Résultat |
|---|---:|
| Tweets présents dans `tweet` | 25 645 / 26 190 |
| Tweets absents de `tweet` | **545** |
| Claims présents dans `claim` | 12 914 / 13 196 |
| Claims absents de `claim` | **282** |

Certaines relations pointent vers des identifiants introuvables dans les tables `tweet` ou `claim`.

---

## 4. Utilité pour notre projet SMA

Cette table est le **lien central** entre contenu social et verdict fact-checké :

- un tweet (`src`) discute un claim (`tgt`) ;
- via `claim.label`, on sait si ce claim est `misinformation` ou `factual`.

**À conserver :** `src`, `tgt` (et éventuellement `relevance`).  
Pour la simulation, on pourra filtrer les relations dont les IDs existent bien dans `tweet` et `claim`.
