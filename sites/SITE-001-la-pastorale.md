# SITE-001 — La Pastorale

**Statut :** À relever  
**Version :** 0.5  
**Date :** 2026-07-12

## 1. Objectif

Décrire La Pastorale : six terrains en terre battue, leurs installations d'arrosage, leurs accès et les équipements réellement présents.

Cette fiche est reliée à la vue globale [SITE-000 — Structure tennis](./SITE-000-structure-tennis.md).

## 2. Identification du site

| Champ | Valeur |
|---|---|
| Repère | S1 |
| Nom officiel | La Pastorale |
| Adresse | À compléter |
| Nombre de terrains | 6 |
| Terrains | T1 à T6 |
| Surface | Terre battue |
| Distance depuis Le Kalisté | Environ 5 minutes |
| Responsable terrain | À compléter |
| Service amont réseau eau | À compléter |

## 3. Périmètre documenté

Inclus : terrains en terre battue, sorties d'eau, regards utiles au diagnostic, arroseurs fixes, équipements mobiles, programmateur et contrôle d'accès.

Hors périmètre : réseau enterré amont, conception électrique interne, codes d'accès et autres secrets.

## 4. Convention de repérage

Les terrains de La Pastorale sont désignés `S1-T01` à `S1-T06`. Les fichiers historiques `FIC-T01` à `FIC-T06` sont conservés pendant la migration afin de ne pas casser les liens existants.

## 5. Terrains

| Terrain | Numéro réel | Fiche actuelle | Surface | Remarque |
|---|---:|---|---|---|
| S1-T01 | 1 | [FIC-T01](./FIC-T01-terrain-1.md) | Terre battue | Accès : sujet en cours |
| S1-T02 | 2 | [FIC-T02](./FIC-T02-terrain-2.md) | Terre battue | Accès à code |
| S1-T03 | 3 | [FIC-T03](./FIC-T03-terrain-3.md) | Terre battue | Accès à code |
| S1-T04 | 4 | [FIC-T04](./FIC-T04-terrain-4.md) | Terre battue | Accès à code |
| S1-T05 | 5 | [FIC-T05](./FIC-T05-terrain-5.md) | Terre battue | Accès à code |
| S1-T06 | 6 | [FIC-T06](./FIC-T06-terrain-6.md) | Terre battue | Accès à code |

### Sorties d'eau par terrain (SET)

Répartition confirmée par le relevé REL-007 (issue #71) : **10 sorties** (`SET-01` à `SET-10`). Architecture de base commune (robinet de puisage vissé = vanne primaire actuelle, raccord **Écrou femelle 1" → cannelé Ø25**, tuyau **Tricoflex Jaune Ø25**), avec des **variations de robinets** (tête, maintenance). La conformité n'est pas évaluée : aucun standard n'est encore déployé.

| Terrain | Sorties (SET) | Nombre | Remarque |
|---|---|---:|---|
| S1-T01 | SET-01 | 1 | |
| S1-T02 | SET-02, SET-03 | 2 | `SET-03` : repère SET, **usage actuel SEM** (maintenance) |
| S1-T03 | SET-04, SET-05, SET-06 | 3 | |
| S1-T04 | SET-07, SET-08 | 2 | `SET-08` : raccordement à vérifier (photo à fournir) |
| S1-T05 | SET-09 | 1 | |
| S1-T06 | SET-10 | 1 | |
| **Total** | | **10** | |

## 6. Accès du site

À La Pastorale, les accès concernés utilisent un clavier à code, une ventouse électromagnétique et un groom. Ce système est différent de celui du Kalisté.

| Repère provisoire | Accès | Système | Statut / remarque |
|---|---|---|---|
| S1-ACC-T01 | Terrain 1 | À confirmer | Sujet en cours |
| S1-ACC-T02 | Terrain 2 | Clavier + ventouse + groom | En service |
| S1-ACC-T03 | Terrain 3 | Clavier + ventouse + groom | En service |
| S1-ACC-T04 | Terrain 4 | Clavier + ventouse + groom | En service |
| S1-ACC-T05 | Terrain 5 | Clavier + ventouse + groom | En service |
| S1-ACC-T06 | Terrain 6 | Clavier + ventouse + groom | En service |
| S1-ACC-PRIN | Petit portillon principal | Clavier + ventouse + groom | En service |
| S1-ACC-VH | Vestiaire hommes | Clavier + ventouse + groom | En service |
| S1-ACC-VF | Vestiaire femmes | Clavier + ventouse + groom | En service |

Les codes sont conservés physiquement au bureau et ne sont jamais stockés dans Git.

## 7. Points à relever

- adresse et plan général ;
- sorties d'eau, regards et arroseurs ;
- correspondance complète des canaux ;
- marque et modèle des claviers, ventouses et grooms ;
- situation définitive de l'accès T1 ;
- photos et historique local.

## 8. Historique

| Version | Date | Description |
|---|---|---|
| 0.1 | 2026-07-09 | Création de la fiche site |
| 0.2 | 2026-07-10 | Ajout du contrôle d'accès |
| 0.3 | 2026-07-10 | Identification comme Site 1 |
| 0.4 | 2026-07-10 | Nom officiel La Pastorale et distinction avec Le Kalisté |
| 0.5 | 2026-07-12 | Sorties d'eau : répartition confirmée (10 SET, `SET-01`→`SET-10`), base commune avec variations de robinets, `SET-03` en usage SEM, `SET-08` à vérifier ; retrait de la notion de conformité (aucun standard déployé) — issue #71 |
