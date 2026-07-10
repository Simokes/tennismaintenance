# SITE-001 — Complexe de tennis

**Statut :** À relever  
**Version :** 0.2  
**Date :** 2026-07-10

## 1. Objectif

Décrire l'organisation générale du complexe afin de relier les standards techniques aux équipements réellement présents sur site.

Cette fiche sert de point d'entrée pour les fiches terrain, les sorties d'eau, les regards utiles au diagnostic, les zones d'entretien et les accès.

## 2. Identification du site

| Champ | Valeur |
|---|---|
| Nom du site | À compléter |
| Adresse | À compléter |
| Nombre de terrains | 6 |
| Surface principale | Terre battue |
| Responsable terrain | À compléter |
| Service amont réseau eau | À compléter |

## 3. Périmètre documenté

Inclus :

- terrains ;
- sorties d'eau terrain ;
- sorties d'eau d'entretien accessibles aux agents ;
- regards utiles au diagnostic terrain ;
- arroseurs fixes ;
- équipements mobiles d'arrosage ;
- programmateur et correspondance des canaux ;
- accès à code, ventouses électromagnétiques et grooms.

Hors périmètre :

- alimentation générale ;
- réseau enterré amont ;
- pompes ;
- conception électrique interne ;
- codes d’accès et autres secrets ;
- travaux relevant d'un autre service.

## 4. Plan général simplifié

À compléter après relevé terrain.

```text
À dessiner :

- position des 6 terrains ;
- vestiaires ;
- local technique ;
- points d'eau d'entretien ;
- accès ;
- zones de stockage ;
- regards utiles au diagnostic.
```

## 5. Terrains

| Terrain | Fiche | Statut | Remarques |
|---|---|---|---|
| T1 | [FIC-T01](./FIC-T01-terrain-1.md) | À relever | Accès : sujet en cours |
| T2 | [FIC-T02](./FIC-T02-terrain-2.md) | À relever | Accès à code |
| T3 | [FIC-T03](./FIC-T03-terrain-3.md) | À relever | Accès à code |
| T4 | [FIC-T04](./FIC-T04-terrain-4.md) | À relever | Accès à code |
| T5 | [FIC-T05](./FIC-T05-terrain-5.md) | À relever | Accès à code |
| T6 | [FIC-T06](./FIC-T06-terrain-6.md) | À relever | Accès à code |

## 6. Accès du site

Les accès concernés utilisent un clavier à code, une ventouse électromagnétique et un groom assurant la fermeture automatique. Les codes sont conservés physiquement au bureau et ne sont jamais stockés dans Git.

| Repère provisoire | Accès | Système | Statut / remarque |
|---|---|---|---|
| ACC-T01 | Terrain 1 | À confirmer | Sujet en cours |
| ACC-T02 | Terrain 2 | Clavier + ventouse + groom | En service |
| ACC-T03 | Terrain 3 | Clavier + ventouse + groom | En service |
| ACC-T04 | Terrain 4 | Clavier + ventouse + groom | En service |
| ACC-T05 | Terrain 5 | Clavier + ventouse + groom | En service |
| ACC-T06 | Terrain 6 | Clavier + ventouse + groom | En service |
| ACC-PRIN | Petit portillon principal | Clavier + ventouse + groom | En service |
| ACC-VH | Vestiaire hommes | Clavier + ventouse + groom | En service |
| ACC-VF | Vestiaire femmes | Clavier + ventouse + groom | En service |

Document lié : [ACC-001 — Contrôle d’accès du site](../access/ACC-001-controle-acces-site.md).

## 7. Sorties d'eau d'entretien hors terrain

| Repère | Localisation | Standard cible | Statut | Remarques |
|---|---|---|---|---|
| SE-01 | À compléter | STD-002 | À relever | |
| SE-02 | À compléter | STD-002 | À relever | |
| SE-03 | À compléter | STD-002 | À relever | |

## 8. Équipements mobiles

| Repère | Désignation | Standard | Affectation | État |
|---|---|---|---|---|
| EA-01 | Ensemble d'arrosage manuel | STD-003 | À compléter | À relever |
| EA-02 | Ensemble d'arrosage manuel | STD-003 | À compléter | À relever |

## 9. Photos à ajouter

- [ ] Vue générale du complexe
- [ ] Plan ou croquis global
- [ ] Sorties d'eau terrain
- [ ] Sorties d'entretien
- [ ] Zone de stockage tuyaux / buses
- [ ] Localisation des regards utiles au diagnostic
- [ ] Portillon principal
- [ ] Clavier à code représentatif
- [ ] Ventouse électromagnétique
- [ ] Groom

## 10. Points à relever en priorité

- [ ] Nom exact du site
- [ ] Plan général des terrains
- [ ] Position des sorties d'eau terrain
- [ ] Position des sorties d'entretien hors terrain
- [ ] Longueur réelle des tuyaux utilisés
- [ ] Nombre d'ensembles mobiles disponibles
- [ ] Repérage des regards utiles au diagnostic
- [ ] Marque et modèle des claviers à code
- [ ] Référence des ventouses
- [ ] Type et référence des grooms
- [ ] Situation définitive de l’accès T1

## 11. Historique

| Version | Date | Auteur | Description |
|---|---|---|---|
| 0.1 | 2026-07-09 | Peter / ChatGPT | Création de la fiche site initiale |
| 0.2 | 2026-07-10 | Peter / ChatGPT | Ajout du contrôle d’accès et de la règle de conservation des codes hors Git |