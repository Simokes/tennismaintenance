# EQ-001 — Ensemble d'arrosage manuel

**Statut :** À compléter  
**Version :** 0.1  
**Date :** 2026-07-09  
**Standard lié :** STD-003

## 1. Objectif

Décrire l'ensemble mobile utilisé par les agents pour arroser manuellement les terrains en terre battue.

## 2. Usage

L'ensemble sert à arroser une zone de terrain avec un jet de type pluie, en gardant la possibilité de couper l'eau rapidement depuis la poignée.

Il est utilisé avec les sorties terrain conformes à STD-001.

## 3. Composition fonctionnelle

```text
Sortie terrain STD-001
        ↓
Tuyau souple Ø25
        ↓
Vanne secondaire 1/4 tour 1" M/M
        ↓
Buse cuivre custom Ø25
```

## 4. Nomenclature

| Repère | Code | Désignation | Quantité | Remarques |
|---|---|---|---:|---|
| T25 | TUY-001 | Tuyau souple Ø25 | 1 | Longueur à relever |
| RC2 | RAC-002 | Raccord cannelé Ø25 → femelle 1" | 1 | Liaison tuyau vers VS |
| VS | VAN-001 | Vanne 1/4 tour 1" M/M | 1 | Commande à la poignée |
| RC3 | RAC-001 | Raccord 1" femelle → cannelé Ø25 | 1 | Liaison VS vers buse |
| BC | BUSE-001 | Buse cuivre custom Ø25 | 1 | Jet pluie terre battue |
| COL | COL-001 | Colliers inox Ø25 | À confirmer | Fixation tuyau sur cannelés |

## 5. Points de contrôle

- [ ] Le tuyau n'est pas percé.
- [ ] Le tuyau n'est pas pincé.
- [ ] La vanne secondaire ouvre et ferme correctement.
- [ ] La buse produit un jet pluie correct.
- [ ] Les raccords ne fuient pas.
- [ ] Les colliers sont serrés sans écraser le tuyau.

## 6. Pannes fréquentes

| Symptôme | Cause probable | Action |
|---|---|---|
| Fuite au raccord | Collier desserré / joint / filetage | Resserrer ou remplacer |
| Jet trop concentré | Buse déformée ou bouchée | Nettoyer / reformer / remplacer |
| Débit faible | Tuyau pincé ou buse obstruée | Vérifier tuyau et buse |
| Vanne dure | Usure ou encrassement | Remplacer si nécessaire |

## 7. Affectation

| Ensemble | Terrain / zone | État | Remarques |
|---|---|---|---|
| EA-01 | À relever | À relever | |
| EA-02 | À relever | À relever | |

## 8. Photos à ajouter

- [ ] Vue complète de l'ensemble.
- [ ] Vanne secondaire côté poignée.
- [ ] Buse cuivre.
- [ ] Raccords et colliers.
- [ ] Exemple de jet correct.

## 9. Documents liés

- STD-001 — Sortie d'eau terrain
- STD-003 — Ensemble d'arrosage manuel
- STD-004 — Buse cuivre standard
- PROC-003 — Diagnostiquer une sortie d'eau à faible débit
- PROC-004 — Fabriquer une buse cuivre standard
- REF-001 — Raccords, vannes et accessoires d'arrosage

## 10. Historique

| Version | Date | Auteur | Description |
|---|---|---|---|
| 0.1 | 2026-07-09 | Peter / ChatGPT | Création de la fiche équipement initiale |
