# FIC-T01 — Terrain 1

**Statut :** À relever  
**Date de création :** 2026-07-09  
**Dernière mise à jour :** 2026-07-12

## 1. Identification

| Champ | Valeur |
|---|---|
| Terrain | T1 |
| Surface | Terre battue |
| Standard sortie eau | STD-001 |
| Nombre d'arroseurs fixes | 6 |
| Ensemble d'arrosage associé | À relever |
| Programmateur associé | CTRL-001 — Hunter ICC |

## 2. Plan simplifié

```text
Fond nord

      AR-01      AR-02


AR-03                  AR-04


      AR-05      AR-06

Fond sud
```

Les positions et repères définitifs doivent être confirmés sur place. Le schéma doit ensuite afficher les paires reliées au même canal.

## 3. Sorties d'eau terrain

Architecture de base commune à toutes les sorties (voir EQ-002 § 3.1 / STD-001 § 3) : sortie réseau filetée femelle 1" + robinet de puisage vissé (vanne primaire actuelle) + raccord **Écrou femelle 1" → cannelé Ø25** + tuyau **Tricoflex Jaune Ø25**. Les sorties partagent cette base mais **ne sont pas identiques** (modèle / tête de robinet, maintenance). La conformité n'est pas évaluée tant qu'aucun standard n'est déployé.

**Sorties confirmées (relevé REL-007 / issue #71) : 1 — `SET-01`.**

| Repère | Usage actuel | Type / modèle du robinet | Fonctionnelle | État / observation |
|---|---|---|---|---|
| SET-01 | SET | À relever | À confirmer | À relever |

## 4. Regards utiles au diagnostic

Cette section ne décrit pas le contenu technique interne des regards. Elle indique uniquement quels équipements ils commandent ou isolent lorsque cette information est utile au diagnostic terrain.

| Regard | Localisation | Dessert / impacte | Éléments accessibles | Remarques |
|---|---|---|---|---|
| REG-01 | À relever | À relever | Vanne / électrovanne / autre | |
| REG-02 | À relever | À relever | Vanne / électrovanne / autre | |

## 5. Arroseurs fixes

Chaque arroseur est un équipement physique. Le canal indique la sortie du programmateur qui le déclenche. Deux arroseurs reliés au même canal fonctionnent simultanément.

| Repère | Position réelle | Canal | Arroseur associé | Modèle | État | Vérifié |
|---|---|---|---|---|---|---|
| AR-01 | À relever | À relever | À relever | Commun site | À relever | Non |
| AR-02 | À relever | À relever | À relever | Commun site | À relever | Non |
| AR-03 | À relever | À relever | À relever | Commun site | À relever | Non |
| AR-04 | À relever | À relever | À relever | Commun site | À relever | Non |
| AR-05 | À relever | À relever | À relever | Commun site | À relever | Non |
| AR-06 | À relever | À relever | À relever | Commun site | À relever | Non |

## 6. Correspondance programmateur

Exemple de principe à vérifier : un canal commande deux arroseurs opposés, comme le fond sud-ouest et le fond nord-ouest.

| Canal | Arroseur 1 | Arroseur 2 | Zone couverte | Regard / électrovanne utile | Vérifié le | Remarques |
|---|---|---|---|---|---|---|
| CAN-01 | À relever | À relever | À relever | À relever | | |
| CAN-02 | À relever | À relever | À relever | À relever | | |
| CAN-03 | À relever | À relever | À relever | À relever | | |

Voir [CTRL-001 — Programmateur Hunter ICC](../control/CTRL-001-programmateur-hunter-icc.md) pour la correspondance générale, les programmes et les cycles.

## 7. Particularités du terrain

- À relever.

## 8. Photos à ajouter

- [ ] Vue générale
- [ ] Sortie d'eau
- [ ] Regards
- [ ] Arroseurs
- [ ] Défauts connus

## 9. Historique local

| Date | Intervention | Agent | Observation |
|---|---|---|---|
| | | | |
