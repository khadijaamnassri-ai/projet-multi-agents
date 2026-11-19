# Fiche : `tweet`

**Source :** `data/mumin_raw/tweet`  
**Projet :** Projet_MultiAgents (SMA / NetLogo)

---

## 1. Présentation du fichier

Ce fichier liste les tweets du dataset MuMiN sous forme d’identifiants.

| Indicateur | Valeur |
|---|---:|
| Lignes (tweets) | 21 565 018 |
| Colonnes | 2 |
| Identifiants uniques | 21 565 018 |
| Valeurs manquantes | 0 |

---

## 2. Colonnes importantes

| Colonne | Type | Signification | Utilité |
|---|---|---|---|
| `tweet_id` | `int64` | Identifiant Twitter du tweet | Relier tweets ↔ claims / retweets |
| `relevance` | `float64` | Score de pertinence (≈ 0,70 à 1) | Filtrage optionnel |

### Point important

**Le texte des tweets n’est pas présent** dans ce fichier.  
Colonnes trouvées : uniquement `tweet_id` et `relevance`. Aucune colonne `text`, `content`, etc.

---

## 3. Résultats de l'analyse

### Exemples (5 premières lignes)

| tweet_id | relevance |
|---|---:|
| 1244112949385605120 | 0,805 |
| 1248919207728664578 | 0,805 |
| 1242754302189416453 | 0,707 |
| 1245990540190945280 | 0,805 |
| 1283781136704036865 | 0,971 |

### Score `relevance`

| Stat | Valeur |
|---|---:|
| Min | ≈ 0,70 |
| Max | ≈ 1,00 |
| Moyenne | ≈ 0,78 |

---

## 4. Utilité pour notre projet SMA

- Les tweets sont des **nœuds** du réseau, identifiés par `tweet_id`.
- Ils se relient aux claims via `tweet_discusses_claim` (`src` = tweet).
- Ils se relient aux utilisateurs via `user_retweeted_tweet` (`tgt` = tweet).

**Limite :** sans texte, on ne peut pas analyser le contenu des messages. On travaille avec les **identifiants** et les **relations**.

**À conserver :** `tweet_id` (et éventuellement `relevance`).
