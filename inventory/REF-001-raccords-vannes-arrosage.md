# REF-001 — Raccords, vannes et accessoires d'arrosage

**Statut :** À compléter  
**Version :** 0.2  
**Date :** 2026-07-12

## 1. Objectif

Créer une nomenclature commune pour les pièces utilisées sur les sorties d'eau terrain et les sorties d'entretien.

Cette fiche sert à éviter les désignations ambiguës lors des commandes, réparations et échanges entre agents.

## 2. Codification proposée

| Préfixe | Famille | Exemple |
|---|---|---|
| VAN | Vanne / robinet | VAN-001 |
| RAC | Raccord | RAC-001 |
| TUY | Tuyau | TUY-001 |
| GEKA | Raccord GEKA | GEKA-001 |
| BUSE | Buse / lance | BUSE-001 |
| JOINT | Joint | JOINT-001 |
| COL | Collier | COL-001 |
| ARR | Arroseur fixe | ARR-001 |

## 3. Vannes et robinets

| Code | Désignation | Filetage / diamètre | Usage | Standard lié | Référence fournisseur |
|---|---|---|---|---|---|
| VAN-001 | Vanne 1/4 tour mâle/mâle | 1" M/M | Sortie terrain / poignée | STD-001, STD-003 | À compléter |
| ROB-001 | Robinet de puisage standard | À confirmer | Sortie entretien | STD-002 | À compléter |

## 4. Raccords cannelés et filetés

| Code | Désignation | Côté A | Côté B | Usage | Standard lié | Référence fournisseur |
|---|---|---|---|---|---|---|
| RAC-001 | Raccord femelle → cannelé | 1" femelle | Cannelé Ø25 | VP vers tuyau / VS vers buse | STD-001, STD-003 | À compléter |
| RAC-002 | Raccord cannelé → femelle | Cannelé Ø25 | 1" femelle | Tuyau vers VS | STD-001, STD-003 | À compléter |
| RAC-003 | Mamelon mâle/mâle | 1" mâle | 1" mâle | Adaptation éventuelle | À définir | À compléter |
| RAC-004 | Manchon femelle/femelle | 1" femelle | 1" femelle | Adaptation éventuelle | À définir | À compléter |

## 5. GEKA

| Code | Désignation | Interface | Côté tuyau / sortie | Usage | Standard lié | Référence fournisseur |
|---|---|---|---|---|---|---|
| GEKA-001 | Raccord GEKA fileté | GEKA | À confirmer | Sortie entretien fixe | STD-002 | À compléter |
| GEKA-002 | Raccord GEKA cannelé Ø19 | GEKA | Cannelé Ø19 | Tuyau Kärcher / entretien | STD-002 | À compléter |
| GEKA-003 | Raccord GEKA cannelé Ø25 | GEKA | Cannelé Ø25 | Tuyau entretien gros débit | STD-002 | À compléter |
| JOINT-001 | Joint GEKA EPDM | GEKA | Joint remplaçable | Maintenance GEKA | STD-002 | À compléter |

## 6. Tuyaux

| Code | Désignation | Diamètre | Usage | Standard lié | Référence fournisseur |
|---|---|---:|---|---|---|
| TUY-001 | Tuyau souple terrain (Tricoflex Jaune) | Ø25 | Arrosage manuel terre battue | STD-003 | **Tricoflex Jaune Ø25 — art. 048273**, couronne 25 m, Made in France ([photo](https://github.com/Simokes/tennismaintenance/blob/main/assets/photos/equipements/TUY-001-tricoflex-jaune-25-art-048273.jpg)) |
| TUY-002 | Tuyau entretien | Ø19 | Kärcher / entretien | STD-002 | À compléter |
| TUY-003 | Tuyau entretien gros débit | Ø25 | Entretien hors terrain | STD-002 | À compléter |

## 7. Arroseurs

Arroseurs fixes escamotables des terrains (repères `AR-xx` des fiches terrain, commandés par les canaux `CAN-xx` du programmateur `CTRL-001`).

| Code | Désignation | Marque | Usage | Référence / observation |
|---|---|---|---|---|
| ARR-001 | Arroseur fixe escamotable | **Rain Bird** (marque confirmée sur la pièce) | Arrosage automatique terre battue | Modèle **Falcon 6504** selon relevé terrain — à confirmer sur l'arroseur ([photo](https://github.com/Simokes/tennismaintenance/blob/main/assets/photos/equipements/ARR-001-rainbird-falcon-6504.jpg)) |

## 8. Buses

| Code | Désignation | Matière | Usage | Standard lié | Référence fournisseur |
|---|---|---|---|---|---|
| BUSE-001 | Buse cuivre custom Ø25 | Cuivre | Jet pluie terre battue | STD-004 | Fabrication interne |

## 9. Colliers et consommables

| Code | Désignation | Diamètre | Usage | Référence fournisseur |
|---|---|---:|---|---|
| COL-001 | Collier inox pour tuyau Ø25 | À confirmer | Fixation tuyau sur cannelé | À compléter |
| CONS-001 | Ruban PTFE | Standard | Étanchéité filetages | À compléter |
| CONS-002 | Filasse / pâte | Standard | Étanchéité filetages selon usage | À compléter |

## 10. Points à confirmer

- [ ] Références exactes des vannes 1" M/M.
- [ ] Références exactes des raccords cannelés Ø25.
- [ ] Type exact de robinet de puisage pour STD-002.
- [ ] Type exact de raccord GEKA fixe.
- [ ] Matière retenue pour les joints GEKA.
- [ ] Diamètre intérieur / extérieur réel des tuyaux.
- [ ] Modèle exact de l'arroseur `ARR-001` (marque Rain Bird confirmée ; « Falcon 6504 » à vérifier sur l'arroseur).

## 11. Historique

| Version | Date | Auteur | Description |
|---|---|---|---|
| 0.1 | 2026-07-09 | Peter / ChatGPT | Création de la nomenclature initiale |
| 0.2 | 2026-07-12 | Peter / Claude | Référence tuyau TUY-001 (Tricoflex art. 048273) et arroseur ARR-001 (Rain Bird) d'après photos |
