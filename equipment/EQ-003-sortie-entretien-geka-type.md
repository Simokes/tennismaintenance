# EQ-003 — Sortie d'entretien GEKA type

**Statut :** À compléter  
**Version :** 0.1  
**Date :** 2026-07-09  
**Standard lié :** STD-002

## 1. Objectif

Décrire la sortie d'eau d'entretien type utilisée hors terrain pour les usages polyvalents.

## 2. Usage

La sortie d'entretien sert aux besoins généraux des agents :

- Kärcher ;
- nettoyage ;
- arrosage hors terrain ;
- remplissage de seaux ;
- entretien divers.

Elle doit permettre un réglage progressif du débit et une connexion rapide des équipements mobiles.

## 3. Configuration fonctionnelle

```text
Sortie réseau
        ↓
Robinet de puisage standard
        ↓
Raccord GEKA vissé
        ↓
Tuyau / équipement mobile compatible GEKA
```

## 4. Nomenclature

| Repère | Code | Désignation | Quantité | Remarques |
|---|---|---|---:|---|
| SR | — | Sortie réseau | 1 | À relever |
| ROB | ROB-001 | Robinet de puisage standard | 1 | Débit réglable |
| GKF | GEKA-001 | Raccord GEKA fixe | 1 | Interface commune |
| JGK | JOINT-001 | Joint GEKA EPDM | 1 | Pièce d'usure remplaçable |

## 5. Compatibilités mobiles

| Équipement | Code | Interface | Usage |
|---|---|---|---|
| Tuyau Ø19 | GEKA-002 | GEKA → cannelé Ø19 | Kärcher / entretien léger |
| Tuyau Ø25 | GEKA-003 | GEKA → cannelé Ø25 | Entretien gros débit |
| Accessoire Kärcher | À définir | GEKA ou adaptateur | Nettoyage |

## 6. Implantation sur site

| Sortie | Localisation | État | Particularités |
|---|---|---|---|
| SE-01 | À relever | À relever | |
| SE-02 | À relever | À relever | |
| SE-03 | À relever | À relever | |

## 7. Points de contrôle

- [ ] Le robinet permet un réglage progressif.
- [ ] Le GEKA est bien fixé.
- [ ] Le joint GEKA est en bon état.
- [ ] Le raccord ne fuit pas en pression.
- [ ] Les tuyaux mobiles se connectent sans forcer.
- [ ] Le robinet est accessible et protégé des chocs.

## 8. Pannes fréquentes

| Symptôme | Cause probable | Action |
|---|---|---|
| Fuite au GEKA | Joint usé | Appliquer PROC-002 |
| Débit insuffisant | Robinet partiellement bouché / amont | Diagnostic puis transmission si amont |
| Connexion difficile | Saleté ou usure GEKA | Nettoyer / remplacer joint ou raccord |
| Robinet dur | Vieillissement | Remplacer ROB-001 si nécessaire |

## 9. Photos à ajouter

- [ ] Sortie entretien conforme.
- [ ] Raccord GEKA fixe.
- [ ] Joint GEKA.
- [ ] Tuyaux compatibles.

## 10. Documents liés

- STD-002 — Sortie d'eau d'entretien
- PROC-002 — Remplacer un joint GEKA
- PROC-003 — Diagnostiquer une sortie d'eau à faible débit
- REF-001 — Raccords, vannes et accessoires d'arrosage
- STOCK-001 — Stock arrosage

## 11. Historique

| Version | Date | Auteur | Description |
|---|---|---|---|
| 0.1 | 2026-07-09 | Peter / ChatGPT | Création de la fiche équipement initiale |
