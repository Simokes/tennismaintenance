# Tennis Maintenance

Référentiel technique de maintenance pour un complexe municipal de tennis.

Ce dépôt sert à conserver une trace claire, versionnée et transmissible des standards, procédures, inventaires, interventions, équipements de commande et décisions techniques liés à la maintenance courante des terrains et points d'eau.

## Objectif

Le but n'est pas de remplacer les plans officiels du service technique ni les notices constructeur, mais de documenter le périmètre réel de maintenance terrain :

- sorties d'eau des terrains ;
- sorties d'entretien hors terrain ;
- équipements mobiles d'arrosage ;
- programmateur, canaux et cycles utiles aux agents ;
- pièces standards ;
- procédures de maintenance courante ;
- historiques d'intervention utiles ;
- historique des décisions techniques.

## Périmètre

Inclus :

- maintenance limitée aux terrains ;
- équipements accessibles aux agents terrain ;
- sorties d'eau à partir de la sortie réseau utilisable ;
- arrosage manuel ;
- correspondance entre canaux du programmateur et arroseurs ;
- réglages et cycles réellement utilisés sur le site ;
- raccords, tuyaux, vannes, buses et points d'entretien.

Hors périmètre :

- alimentation générale ;
- réseau enterré amont ;
- pompes ;
- conception électrique interne du programmateur ;
- électrovannes ou éléments gérés par un autre service, sauf information utile au diagnostic.

## Organisation du dépôt

```text
standards/      Standards techniques : ce que doit être une installation conforme.
equipment/      Fiches équipements : ensembles fonctionnels utilisés ou maintenus.
control/        Programmateurs, canaux, programmes et cycles réellement utilisés.
procedures/     Procédures terrain : comment réaliser une intervention.
sites/          Description du site réel et des terrains.
inventory/      Stocks, références, fournisseurs et nomenclature.
interventions/  Historique des interventions importantes.
decisions/      Décisions techniques structurées sous forme d'ADR.
assets/         Schémas, photos et supports visuels.
```

## Types de documents

| Préfixe | Type | Rôle |
|---|---|---|
| STD | Standard | Définit une configuration technique officielle. |
| EQ | Équipement | Décrit un ensemble fonctionnel utilisé ou maintenu. |
| CTRL | Commande | Décrit un programmateur, ses canaux, programmes et cycles. |
| PROC | Procédure | Explique comment réaliser une intervention. |
| FIC | Fiche terrain | Décrit un équipement réel ou une zone réelle du site. |
| INT | Intervention | Trace une intervention importante ou utile pour l'historique. |
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

La documentation doit refléter le terrain réel. Si une installation ou un réglage change, le document correspondant doit être mis à jour.
