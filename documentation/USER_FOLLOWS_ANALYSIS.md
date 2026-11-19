# Fiche : `user_follows_user`

**Source :** `data/mumin_raw/user_follows_user`  
**Projet :** Projet_MultiAgents (SMA / NetLogo)

---

## 1. Présentation du fichier

Cette table décrit le **réseau de suivi** entre utilisateurs : qui suit qui.

| Indicateur | Valeur |
|---|---:|
| Lignes (relations) | 2 482 238 |
| Colonnes | 3 |
| Valeurs manquantes | 0 |

---

## 2. Colonnes importantes

| Colonne | Signification | Utilité |
|---|---|---|
| `src` | Utilisateur qui **suit** | Agent suiveur |
| `tgt` | Utilisateur **suivi** | Agent suivi |
| `relevance` | Score de pertinence | Filtrage optionnel |

En résumé : **`src` suit `tgt`**.

---

## 3. Résultats de l'analyse

| Statistique | Valeur |
|---|---:|
| Nombre de relations | 2 482 238 |
| Utilisateurs distincts dans `src` | 1 182 675 |
| Utilisateurs distincts dans `tgt` | 669 450 |
| Utilisateurs distincts au total | 1 668 820 |

### Exemples

| src (suit) | tgt (est suivi) | relevance |
|---|---|---:|
| 1197841132522287104 | 368883443 | 0,705 |
| 1440520162759741448 | 368883443 | 0,705 |
| 2334883345 | 368883443 | 0,705 |

### Vérification d’intégrité

| Contrôle | Résultat |
|---|---:|
| Utilisateurs de la relation présents dans `user` | 1 667 537 / 1 668 820 |
| Utilisateurs absents de `user` | **1 283** |

Une petite partie des IDs de suivi n’apparaît pas dans la table `user`.

---

## 4. Utilité pour notre projet SMA

Cette table construit le **graphe social** :

- les liens `src → tgt` représentent le suivi ;
- la désinformation peut se propager le long de ces liens.

**À conserver :** `src`, `tgt` (et éventuellement `relevance`).  
Pour NetLogo, on pourra ne garder que les liens dont `src` et `tgt` existent dans `user`.
