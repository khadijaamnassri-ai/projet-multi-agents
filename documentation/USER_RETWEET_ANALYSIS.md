# Fiche : `user_retweeted_tweet`

**Source :** `data/mumin_raw/user_retweeted_tweet`  
**Projet :** Projet_MultiAgents (SMA / NetLogo)

---

## 1. Présentation du fichier

Cette table décrit les **partages (retweets)** : quel utilisateur a retweeté quel tweet.

| Indicateur | Valeur |
|---|---:|
| Lignes (relations) | 472 972 |
| Colonnes | 3 |
| Valeurs manquantes | 0 |

---

## 2. Colonnes importantes

| Colonne | Signification | Utilité |
|---|---|---|
| `src` | Utilisateur qui **retweete** | Agent qui partage |
| `tgt` | Tweet **partagé** | Contenu diffusé |
| `relevance` | Score de pertinence | Filtrage optionnel |

En résumé : **`src` (user) a retweeté `tgt` (tweet)**.

---

## 3. Résultats de l'analyse

| Statistique | Valeur |
|---|---:|
| Nombre de relations | 472 972 |
| Utilisateurs distincts (`src`) | 325 919 |
| Tweets distincts partagés (`tgt`) | 25 600 |

### Exemples

| src (user) | tgt (tweet) | relevance |
|---|---|---:|
| 2854398267 | 1243046281326534661 | 0,705 |
| 1342694810 | 1243046281326534661 | 0,705 |
| 1127665416266895360 | 1243046281326534661 | 0,705 |

### Vérification d’intégrité

| Contrôle | Résultat |
|---|---:|
| Utilisateurs présents dans `user` | 325 919 / 325 919 |
| Utilisateurs absents | **0** |
| Tweets présents dans `tweet` | 25 205 / 25 600 |
| Tweets absents de `tweet` | **395** |

Tous les utilisateurs de cette table existent dans `user`.  
En revanche, 395 tweets partagés sont absents de la table `tweet`.

---

## 4. Utilité pour notre projet SMA

Cette table modélise la **propagation par partage** :

- un utilisateur (`src`) diffuse un tweet (`tgt`) ;
- si ce tweet discute un claim via `tweet_discusses_claim`, on peut relier le partage à un label `misinformation` / `factual`.

**À conserver :** `src`, `tgt` (et éventuellement `relevance`).
