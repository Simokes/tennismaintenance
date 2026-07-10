# Contrôle d’accès du Kalisté

## Principe

Les terrains 7 à 11 utilisent des claviers à code alimentés par piles et des gâches électriques.

```text
clavier sur piles → gâche électrique → ouverture du portillon
```

Le parking est fermé par un cadenas à code indépendant.

## Accès connus

| Repère | Accès | Système | Statut |
|---|---|---|---|
| S2-ACC-T07 | Terrain 7 | Clavier sur piles + gâche électrique | En service, modèle à relever |
| S2-ACC-T08 | Terrain 8 | Clavier sur piles + gâche électrique | En service, modèle à relever |
| S2-ACC-T09 | Terrain 9 | Clavier sur piles + gâche électrique | En service, modèle à relever |
| S2-ACC-T10 | Terrain 10 | Clavier sur piles + gâche électrique | En service, modèle à relever |
| S2-ACC-T11 | Terrain 11 | Clavier sur piles + gâche électrique | En service, modèle à relever |
| S2-ACC-PARK | Parking | Cadenas à code | En service, modèle à relever |

## Actions documentées

- changement générique d’un code ;
- remplacement générique des piles ;
- test de la gâche et du verrouillage ;
- changement générique de la combinaison du cadenas ;
- historique des interventions sans stockage des secrets.

## Sécurité

Les codes et la combinaison du cadenas sont conservés physiquement au bureau. Ils ne doivent jamais apparaître dans Git, une photo, une légende ou un historique.

## À relever

- marque et modèle des claviers ;
- type et nombre de piles ;
- comportement en cas de piles faibles ou déchargées ;
- référence des gâches électriques ;
- présence d’un ferme-porte ;
- marque et modèle du cadenas du parking ;
- notices officielles correspondantes.

<p class="doc-source">📄 <strong>Document source :</strong> <a href="https://github.com/Simokes/tennismaintenance/blob/main/access/ACC-002-controle-acces-kaliste.md">access/ACC-002-controle-acces-kaliste.md</a></p>
