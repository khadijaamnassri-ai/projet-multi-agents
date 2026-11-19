# Fiche : `claim`

**Source :** `data/mumin_raw/claim`  
**Projet :** Projet_MultiAgents (SMA / NetLogo)

---

## 1. Présentation du fichier

Ce fichier contient les affirmations vérifiées (fact-checking) du dataset MuMiN.

Un **claim** est une affirmation classée comme `misinformation` ou `factual`.

| Indicateur | Valeur |
|---|---:|
| Lignes | 12 924 |
| Colonnes | 18 |
| Identifiants uniques | 12 924 |
| Valeurs manquantes | 0 |

---

## 2. Colonnes importantes

| Colonne | Signification | Utilité |
|---|---|---|
| `id` | Identifiant du claim | Relier le claim aux tweets |
| `keywords` | Mots-clés associés | Décrire brièvement le claim |
| `date` | Date associée au claim | Ordonner dans le temps |
| `language` | Langue du claim | Filtrer éventuellement |
| `label` | `misinformation` ou `factual` | Type de contenu propagé |
| `reviewers` | Source de vérification | Métadonnée secondaire |

Les autres colonnes (embeddings, clusters, masques train/val/test) ne sont pas nécessaires pour notre simulation.

---

## 3. Résultats de l'analyse

### Labels

| Label | Nombre | % |
|---|---:|---:|
| `misinformation` | 12 252 | 94,80 |
| `factual` | 672 | 5,20 |

### 5 langues principales

| Langue | Nombre |
|---|---:|
| `en` | 5 545 |
| `pt` | 1 418 |
| `es` | 1 067 |
| `hi` | 796 |
| `ar` | 560 |

### Période

Du **2009-09-30** au **2021-12-31**.

### Exemples

| id | keywords | language | label |
|---|---|---|---|
| 325195 | corona virus reaching lungs remains | pt | misinformation |
| 325192 | big dubai airport | pt | misinformation |
| 327883 | sardinia invasion grasshoppers | it | factual |

---

## 4. Utilité pour notre projet SMA

- `id` identifie chaque claim.
- `label` indique si le contenu est trompeur ou factuel.
- La table `tweet_discusses_claim` reliera ces claims aux tweets.

**À conserver :** `id`, `label` ; éventuellement `date`, `language`, `keywords`.
