# Relevé terrain — checklists vivantes

Cette section pilote la **collecte des données terrain** des 11 terrains : préparer une mission ciblée, cocher ce qui est obtenu, distinguer le confirmé du reste, et générer la liste des éléments manquants.

Chaque terrain a une **checklist vivante** (famille `CHK`) maintenue dans le dépôt. Trois états, sans pourcentage : **Obtenu** / **À confirmer** / **À relever**.

<p class="doc-source">📄 <strong>Procédure générale et règles :</strong> <a href="https://github.com/Simokes/tennismaintenance/blob/main/checklists/README.md">checklists/README.md</a> — workflow de mission, nommage des photos, gabarit.</p>

## Workflow de mission

```text
Checklist du terrain
→ préparation d'une mission ciblée (éléments « À relever »)
→ prise de photos et relevés sur site
→ classement et renommage des fichiers
→ mise à jour des fiches terrain (FIC)
→ mise à jour de la checklist
→ nouvelle liste des éléments manquants
```

Règle : **ne pas deviner.** Une information non vérifiée est marquée `À confirmer` ; une fonction hydraulique ne se déduit pas d'une photo.

## Tableau de bord

--8<-- "checklists/tableau-de-bord.md"

## Checklists par terrain

- [CHK-S1-T01 — La Pastorale, terrain 1](CHK-S1-T01.md)
- [CHK-S1-T02 — La Pastorale, terrain 2](CHK-S1-T02.md)

Les autres terrains sont créés à partir du gabarit une fois le modèle S1-T01 validé.

## Issues de relevé liées

| Issue | Sujet | Priorité |
|---|---|---|
| [#7](https://github.com/Simokes/tennismaintenance/issues/7) | Sorties d'eau S1-T01 à S1-T06 | Haute |
| [#8](https://github.com/Simokes/tennismaintenance/issues/8) | Sorties d'entretien hors terrain | Haute |
| [#9](https://github.com/Simokes/tennismaintenance/issues/9) | Regards utiles au diagnostic | Haute |
| [#10](https://github.com/Simokes/tennismaintenance/issues/10) | Stock réel arrosage | Moyenne |
| [#11](https://github.com/Simokes/tennismaintenance/issues/11) | Photos prioritaires | Haute |
| [#12](https://github.com/Simokes/tennismaintenance/issues/12) | Références fournisseurs | Moyenne |

Ces fiches se remplissent aussi sur papier via les [fiches de relevé A4](../releves/index.md) (famille `REL`), puis se transcrivent dans les fiches terrain.
