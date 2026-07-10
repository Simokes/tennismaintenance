# SITE-001 — Site 1

**Statut :** À relever  
**Version :** 0.3  
**Date :** 2026-07-10

## 1. Objectif

Décrire le Site 1 de la structure tennis : six terrains en terre battue, leurs installations d'arrosage, leurs accès et les équipements réellement présents.

Cette fiche est reliée à la vue globale [SITE-000 — Structure tennis](./SITE-000-structure-tennis.md).

## 2. Identification du site

| Champ | Valeur |
|---|---|
| Repère | S1 |
| Nom officiel | À compléter |
| Adresse | À compléter |
| Nombre de terrains | 6 |
| Surface | Terre battue |
| Distance depuis S2 | Environ 5 minutes |
| Responsable terrain | À compléter |
| Service amont réseau eau | À compléter |

## 3. Périmètre documenté

Inclus :

- terrains en terre battue ;
- sorties d'eau terrain et d'entretien ;
- regards utiles au diagnostic ;
- arroseurs fixes et équipements mobiles ;
- programmateur et correspondance des canaux ;
- accès à code, ventouses électromagnétiques et grooms.

Hors périmètre :

- alimentation générale ;
- réseau enterré amont ;
- pompes ;
- conception électrique interne ;
- codes d’accès et autres secrets ;
- travaux relevant d'un autre service.

## 4. Convention de repérage

Les terrains du site sont désormais désignés `S1-T01` à `S1-T06`.

Les fichiers historiques `FIC-T01` à `FIC-T06` sont conservés pendant la migration afin de ne pas casser les liens existants.

## 5. Terrains

| Terrain | Fiche actuelle | Statut | Remarques |
|---|---|---|---|
| S1-T01 | [FIC-T01](./FIC-T01-terrain-1.md) | À relever | Accès : sujet en cours |
| S1-T02 | [FIC-T02](./FIC-T02-terrain-2.md) | À relever | Accès à code |
| S1-T03 | [FIC-T03](./FIC-T03-terrain-3.md) | À relever | Accès à code |
| S1-T04 | [FIC-T04](./FIC-T04-terrain-4.md) | À relever | Accès à code |
| S1-T05 | [FIC-T05](./FIC-T05-terrain-5.md) | À relever | Accès à code |
| S1-T06 | [FIC-T06](./FIC-T06-terrain-6.md) | À relever | Accès à code |

## 6. Accès du site

Les accès concernés utilisent un clavier à code, une ventouse électromagnétique et un groom. Les codes sont conservés physiquement au bureau et ne sont jamais stockés dans Git.

| Repère provisoire | Accès | Système | Statut / remarque |
|---|---|---|---|
| S1-ACC-T01 | S1-T01 | À confirmer | Sujet en cours |
| S1-ACC-T02 | S1-T02 | Clavier + ventouse + groom | En service |
| S1-ACC-T03 | S1-T03 | Clavier + ventouse + groom | En service |
| S1-ACC-T04 | S1-T04 | Clavier + ventouse + groom | En service |
| S1-ACC-T05 | S1-T05 | Clavier + ventouse + groom | En service |
| S1-ACC-T06 | S1-T06 | Clavier + ventouse + groom | En service |
| S1-ACC-PRIN | Petit portillon principal | Clavier + ventouse + groom | En service |
| S1-ACC-VH | Vestiaire hommes | Clavier + ventouse + groom | En service |
| S1-ACC-VF | Vestiaire femmes | Clavier + ventouse + groom | En service |

Document lié : [ACC-001 — Contrôle d’accès du site](../access/ACC-001-controle-acces-site.md).

## 7. Sorties d'eau d'entretien hors terrain

| Repère | Localisation | Standard cible | Statut |
|---|---|---|---|
| S1-SE-01 | À compléter | STD-002 | À relever |
| S1-SE-02 | À compléter | STD-002 | À relever |
| S1-SE-03 | À compléter | STD-002 | À relever |

## 8. Équipements mobiles

| Repère | Désignation | Standard | Affectation | État |
|---|---|---|---|---|
| S1-EA-01 | Ensemble d'arrosage manuel | STD-003 | À compléter | À relever |
| S1-EA-02 | Ensemble d'arrosage manuel | STD-003 | À compléter | À relever |

## 9. Plan et photos à ajouter

- [ ] vue générale du Site 1 ;
- [ ] plan des six terrains ;
- [ ] vestiaires et local technique ;
- [ ] points d'eau et zones de stockage ;
- [ ] accès, claviers, ventouses et grooms ;
- [ ] regards utiles au diagnostic.

## 10. Points à relever en priorité

- [ ] nom officiel et adresse ;
- [ ] plan général ;
- [ ] sorties d'eau et regards ;
- [ ] marque et modèle des contrôles d'accès ;
- [ ] situation définitive de l’accès S1-T01 ;
- [ ] équipements et stocks propres ou partagés avec S2.

## 11. Historique

| Version | Date | Auteur | Description |
|---|---|---|---|
| 0.1 | 2026-07-09 | Peter / ChatGPT | Création de la fiche site initiale |
| 0.2 | 2026-07-10 | Peter / ChatGPT | Ajout du contrôle d’accès |
| 0.3 | 2026-07-10 | Peter / ChatGPT | Identification comme Site 1 et adoption des repères S1-Txx |
