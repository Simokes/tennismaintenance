# Tennis Maintenance

Référentiel technique de maintenance pour une structure tennis municipale répartie sur deux sites.

Le dépôt conserve une trace claire, versionnée et transmissible des sites, terrains, standards, procédures, inventaires, interventions, équipements de commande, dispositifs d’accès et décisions techniques.

## Structure gérée

| Site | Terrains | Surfaces |
|---|---:|---|
| Site 1 (`S1`) | 6 | Terre battue |
| Site 2 (`S2`) | 5 | 3 durs et 2 gazons synthétiques |

Les deux sites se trouvent à environ cinq minutes l’un de l’autre. La structure gère donc **11 terrains**.

Les terrains sont repérés avec leur site :

```text
S1-T01 à S1-T06
S2-T01 à S2-T05
```

Les anciens repères `T01` à `T06` restent compatibles pendant la migration et désignent le Site 1.

## Objectif

Le but n'est pas de remplacer les plans officiels du service technique ni les notices constructeur, mais de documenter le périmètre réel de maintenance :

- organisation des deux sites ;
- surfaces et équipements de chaque terrain ;
- sorties d'eau et équipements d'arrosage ;
- programmateurs, canaux et cycles utiles aux agents ;
- contrôle d’accès, portes, ventouses et grooms ;
- équipements, pièces et stocks ;
- procédures adaptées aux différentes surfaces ;
- historiques d'intervention ;
- décisions techniques.

## Périmètre

Inclus :

- maintenance des terrains et équipements accessibles aux agents ;
- documentation des installations réellement présentes sur chaque site ;
- procédures communes ou propres à la terre battue, au dur et au gazon synthétique ;
- arrosage, accès, clôtures, filets, éclairage et drainage lorsqu'ils relèvent du périmètre terrain ;
- références, photos et documents constructeur utiles.

Hors périmètre :

- alimentation générale ;
- réseaux enterrés amont ;
- conception électrique interne ;
- secrets d’accès : codes utilisateurs, codes maîtres, mots de passe et séquences confidentielles ;
- éléments gérés par un autre service, sauf information utile au diagnostic.

## Organisation du dépôt

```text
sites/          Structure globale, fiches des deux sites et terrains réels.
standards/      Standards techniques communs ou propres à une surface.
equipment/      Fiches d'équipements types.
control/        Programmateurs, canaux, programmes et cycles.
access/         Contrôle d’accès et procédures non secrètes.
procedures/     Procédures terrain.
inventory/      Stocks, références, fournisseurs et nomenclature.
interventions/  Historique des interventions importantes.
decisions/      Décisions techniques sous forme d'ADR.
assets/         Schémas, photos et supports visuels.
```

## Types de documents

| Préfixe | Type | Rôle |
|---|---|---|
| SITE | Site | Décrit la structure globale ou un site réel. |
| STD | Standard | Définit une configuration technique officielle. |
| EQ | Équipement | Décrit un ensemble fonctionnel utilisé ou maintenu. |
| CTRL | Commande | Décrit un programmateur, ses canaux, programmes et cycles. |
| ACC | Accès | Décrit le contrôle d’accès et ses procédures non secrètes. |
| PROC | Procédure | Explique comment réaliser une intervention. |
| FIC | Fiche terrain | Décrit un équipement réel ou une zone réelle du site. |
| INT | Intervention | Trace une intervention importante ou utile pour l'historique. |
| ADR | Décision | Explique pourquoi une décision technique a été prise. |
| STOCK | Inventaire | Liste les pièces, références et quantités utiles. |

## Règles de base

La documentation doit toujours indiquer le site concerné et refléter le terrain réel. Une information non vérifiée est marquée `À confirmer` ou `À relever`.

Aucun secret permettant un accès physique ou logique à un site ne doit être stocké dans le dépôt.
