# Photos

Cette section contient les photos utiles au référentiel.

## Objectif

Les photos doivent aider un agent à reconnaître rapidement :

- un équipement conforme ;
- un défaut ;
- une localisation ;
- une pièce à remplacer ;
- une intervention réalisée.

## Organisation recommandée

```text
assets/photos/
├── site/
├── terrains/
│   ├── S1-T01/   … S1-T06/   (La Pastorale)
│   └── S2-T01/   … S2-T05/   (Le Kalisté)
├── equipements/
└── defauts/
```

Le **site est inclus** dans le nom du dossier (`S1-T01`, pas `T01`) pour éviter toute collision entre les deux sites.

## Nommage recommandé

Nom complet, avec repère et date (repères locaux au terrain, cf. [checklists](../../checklists/README.md)) :

```text
S1-T01-vue-generale-2026-07-12.jpg
S1-T01-REG-01-ouvert-2026-07-12.jpg
S1-T01-SET-01-2026-07-12.jpg
EQ-001-ensemble-arrosage-manuel-2026-07-09.jpg
DEF-fuite-geka-2026-07-09.jpg
```

## Règles

- Une photo doit avoir un nom explicite.
- Éviter les noms automatiques type `IMG_1234.jpg`.
- Ajouter une photo générale avant les détails.
- Ne pas photographier d'informations sensibles inutiles.
