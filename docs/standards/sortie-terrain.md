# STD-001 — Sortie d'eau terrain

## Usage

Sortie dédiée à l'arrosage manuel des terrains en terre battue.

Priorités :

- débit ;
- robustesse ;
- ouverture / fermeture rapide ;
- réparation simple.

## Configuration existante constatée

Base commune à toutes les sorties d'eau terrain (SET) de La Pastorale :

```text
Sortie réseau filetée femelle 1"
        ↓
Robinet de puisage vissé (fait office de vanne primaire actuellement)
        ↓
Raccord vers tuyau souple Ø25
```

La sortie réseau 1" femelle est **commune au site** : le relevé REL-007 ne
documente que les écarts (modèle du robinet, raccord, état).

- [Photo de référence — SET existante](https://github.com/Simokes/tennismaintenance/blob/main/assets/photos/equipements/S1-SET-reference-existante-2026-07-11.jpg)

## Configuration cible

```text
Sortie réseau femelle 1"
        ↓
Vanne primaire 1/4 tour 1" M/M
        ↓
Raccord 1" femelle → cannelé Ø25
        ↓
Tuyau souple Ø25
```

> Écart principal : le robinet de puisage vissé tient aujourd'hui lieu de vanne
> primaire ; la cible prévoit une vanne primaire 1/4 tour 1" M/M dédiée.

## Repères

| Repère | Désignation |
|---|---|
| SR | Sortie réseau femelle 1" |
| VP | Vanne primaire |
| RC1 | Raccord vers tuyau Ø25 |
| T25 | Tuyau souple Ø25 |

## Documents liés

- [EQ-002 — Sortie d'eau terrain type](https://github.com/Simokes/tennismaintenance/blob/main/equipment/EQ-002-sortie-eau-terrain-type.md)
- [PROC-001 — Monter une sortie terrain standard](https://github.com/Simokes/tennismaintenance/blob/main/procedures/PROC-001-monter-sortie-terrain-standard.md)
- [Source complète STD-001](https://github.com/Simokes/tennismaintenance/blob/main/standards/STD-001-sortie-eau-terrain.md)
