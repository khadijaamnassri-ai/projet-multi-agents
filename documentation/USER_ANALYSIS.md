# Fiche : `user`

**Source :** `data/mumin_raw/user`  
**Projet :** Projet_MultiAgents (SMA / NetLogo)

---

## 1. Présentation du fichier

Ce fichier liste les utilisateurs du dataset MuMiN sous forme d’identifiants.

| Indicateur | Valeur |
|---|---:|
| Lignes | 1 986 354 |
| Colonnes | 2 |
| Identifiants uniques (`user_id`) | 1 947 444 |
| Doublons (lignes en plus) | 38 910 |
| Valeurs manquantes | 0 |

---

## 2. Colonnes importantes

| Colonne | Type | Signification | Utilité |
|---|---|---|---|
| `user_id` | `int64` | Identifiant Twitter de l’utilisateur | Nœud agent / compte |
| `relevance` | `float64` | Score de pertinence (≈ 0,70 à 1) | Filtrage optionnel |

### Point important

**Aucun profil utilisateur n’est présent** (pas de nom, bio, description, etc.).  
Colonnes trouvées : uniquement `user_id` et `relevance`.

---

## 3. Résultats de l'analyse

### Exemples (5 premières lignes)

| user_id | relevance |
|---|---:|
| 2854398267 | 0,705 |
| 1342694810 | 0,705 |
| 1127665416266895360 | 0,705 |
| 3396877671 | 0,705 |
| 490642460 | 0,705 |

### Score `relevance`

| Stat | Valeur |
|---|---:|
| Min | ≈ 0,70 |
| Max | ≈ 1,00 |
| Moyenne | ≈ 0,78 |

### Attention

Il y a plus de lignes (1 986 354) que d’`user_id` uniques (1 947 444).  
Certains utilisateurs apparaissent plusieurs fois. Pour le réseau, on utilisera les **identifiants uniques**.

---

## 4. Utilité pour notre projet SMA

- Les utilisateurs sont les **agents / comptes** du réseau.
- Ils se relient entre eux via `user_follows_user`.
- Ils se relient aux tweets via `user_retweeted_tweet`.

**Limite :** sans profil, on ne connaît ni le nom ni les attributs sociaux détaillés. On travaille avec les **identifiants** et les **liens**.

**À conserver :** `user_id` (et éventuellement `relevance`).
