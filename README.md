# Tennis Maintenance

Référentiel technique de maintenance pour un complexe municipal de tennis.

Ce dépôt sert à conserver une trace claire, versionnée et transmissible des standards, procédures, inventaires et décisions techniques liés à la maintenance courante des terrains et points d'eau.

## Objectif

Le but n'est pas de remplacer les plans officiels du service technique, mais de documenter le périmètre réel de maintenance terrain :

- sorties d'eau des terrains ;
- sorties d'entretien hors terrain ;
- équipements mobiles d'arrosage ;
- pièces standards ;
- procédures de maintenance courante ;
- historique des décisions techniques.

## Périmètre

Inclus :

- maintenance limitée aux terrains ;
- équipements accessibles aux agents terrain ;
- sorties d'eau à partir de la sortie réseau utilisable ;
- arrosage manuel ;
- raccords, tuyaux, vannes, buses et points d'entretien.

Hors périmètre :

- alimentation générale ;
- réseau enterré amont ;
- pompes ;
- programmation centrale ;
- électrovannes ou éléments gérés par un autre service, sauf information utile au diagnostic.

## Organisation du dépôt

```text
standards/    Standards techniques : ce que doit être une installation conforme.
equipment/    Fiches équipements : ensembles fonctionnels utilisés ou maintenus.
procedures/   Procédures terrain : comment réaliser une intervention.
sites/        Description du site réel et des terrains.
inventory/    Stocks, références, fournisseurs et nomenclature.
decisions/    Décisions techniques structurées sous forme d'ADR.
assets/       Schémas, photos et supports visuels.
```

## Types de documents

| Préfixe | Type | Rôle |
|---|---|---|
| STD | Standard | Définit une configuration technique officielle. |
| EQ | Équipement | Décrit un ensemble fonctionnel utilisé ou maintenu. |
| PROC | Procédure | Explique comment réaliser une intervention. |
| FIC | Fiche terrain | Décrit un équipement réel ou une zone réelle du site. |
| ADR | Décision | Explique pourquoi une décision technique a été prise. |
| STOCK | Inventaire | Liste les pièces, références et quantités utiles. |

## Statuts recommandés

| Statut | Sens |
|---|---|
| Étude | Idée non testée. |
| Test | Installé ou essayé sur une zone pilote. |
| Validé | Standard officiel applicable. |
| Abandonné | Ancien choix conservé pour historique. |

## Règle de base

La documentation doit refléter le terrain réel. Si une installation change, le document correspondant doit être mis à jour.
