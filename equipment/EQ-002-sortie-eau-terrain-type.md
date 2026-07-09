# EQ-002 — Sortie d'eau terrain type

**Statut :** À compléter  
**Version :** 0.1  
**Date :** 2026-07-09  
**Standard lié :** STD-001

## 1. Objectif

Décrire la sortie d'eau type utilisée sur les terrains pour alimenter l'ensemble d'arrosage manuel.

## 2. Usage

La sortie terrain permet d'alimenter un tuyau Ø25 utilisé pour l'arrosage manuel de la terre battue.

Elle privilégie :

- le débit ;
- la robustesse ;
- l'ouverture/fermeture rapide ;
- la simplicité de réparation.

## 3. Configuration fonctionnelle

```text
Sortie réseau femelle 1"
        ↓
Vanne primaire 1/4 tour 1" M/M
        ↓
Raccord 1" femelle → cannelé Ø25
        ↓
Tuyau Ø25 de l'ensemble d'arrosage manuel
```

## 4. Nomenclature

| Repère | Code | Désignation | Quantité | Remarques |
|---|---|---|---:|---|
| SR | — | Sortie réseau femelle 1" | 1 | Élément existant à relever |
| VP | VAN-001 | Vanne 1/4 tour 1" M/M | 1 | Vanne primaire |
| RC1 | RAC-001 | Raccord 1" femelle → cannelé Ø25 | 1 | Liaison vers tuyau |
| COL | COL-001 | Collier inox Ø25 | À confirmer | Selon montage |

## 5. Implantation sur site

| Terrain | Repère | État | Particularités |
|---|---|---|---|
| T1 | T1-SE | À relever | |
| T2 | T2-SE | À relever | |
| T3 | T3-SE | À relever | |
| T4 | T4-SE | À relever | |
| T5 | T5-SE | À relever | |
| T6 | T6-SE | À relever | |

## 6. Points de contrôle

- [ ] La vanne primaire est accessible.
- [ ] La poignée ne gêne pas le passage.
- [ ] Le raccord ne fuit pas.
- [ ] Le tuyau peut être monté sans vrillage excessif.
- [ ] La sortie est protégée des chocs autant que possible.
- [ ] Le montage correspond à STD-001.

## 7. Pannes fréquentes

| Symptôme | Cause probable | Action |
|---|---|---|
| Fuite au filetage | Étanchéité défaillante | Refaire étanchéité |
| Vanne bloquée | Usure / encrassement | Remplacer VAN-001 |
| Raccord cassé | Choc / vieillissement | Remplacer RAC-001 |
| Débit faible | Problème tuyau, buse ou amont | Appliquer PROC-003 |

## 8. Photos à ajouter

- [ ] Sortie type conforme.
- [ ] Exemple de sortie non conforme.
- [ ] Détail de la vanne primaire.
- [ ] Détail du raccord cannelé.

## 9. Documents liés

- STD-001 — Sortie d'eau terrain
- STD-003 — Ensemble d'arrosage manuel
- PROC-001 — Monter une sortie terrain standard
- PROC-003 — Diagnostiquer une sortie d'eau à faible débit
- REF-001 — Raccords, vannes et accessoires d'arrosage
- STOCK-001 — Stock arrosage

## 10. Historique

| Version | Date | Auteur | Description |
|---|---|---|---|
| 0.1 | 2026-07-09 | Peter / ChatGPT | Création de la fiche équipement initiale |
