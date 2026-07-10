# ENGINEERING — Gouvernance du référentiel

**Projet :** TennisMaintenance  
**Statut :** Fondation  
**Version :** 0.2  
**Date :** 2026-07-10

## 1. Rôle du dépôt

Ce dépôt est la mémoire technique versionnée du complexe de tennis.

Il sert à documenter :

- les standards validés ;
- les procédures terrain ;
- les décisions techniques ;
- les équipements réellement installés ;
- les références de pièces ;
- les schémas et photos utiles aux agents.

Le dépôt ne remplace pas les plans officiels, les diagnostics réglementaires ou les documents d'un autre service. Il documente le savoir utile à la maintenance terrain.

## 2. Principe directeur

La documentation doit être :

- fidèle au terrain ;
- compréhensible par un agent qui découvre le site ;
- utile en intervention ;
- mise à jour lorsqu'une installation change ;
- suffisamment simple pour être maintenue dans la durée.

Une documentation fausse ou obsolète est pire qu'une absence de documentation.

## 3. Familles de documents

| Préfixe | Famille | Rôle |
|---|---|---|
| STD | Standard | Décrit une configuration technique conforme. |
| CTRL | Commande | Décrit les programmateurs, canaux, programmes et cycles. |
| ACC | Accès | Décrit les dispositifs d’accès et les procédures non secrètes. |
| PROC | Procédure | Décrit comment réaliser une intervention. |
| FIC | Fiche | Décrit un équipement réel, un terrain ou une zone. |
| ADR | Décision | Explique pourquoi un choix technique a été retenu. |
| STOCK | Inventaire | Liste les pièces, références et quantités utiles. |
| SITE | Site | Décrit l'organisation générale d'un complexe. |

## 4. Cycle de vie d'un standard

Un standard suit le cycle suivant :

```text
Étude → Test terrain → Validé → Déployé → Retiré
```

### Étude

Idée documentée mais non testée.

### Test terrain

Solution installée ou essayée sur une zone pilote.

### Validé

Solution retenue comme standard applicable.

### Déployé

Solution installée sur les équipements concernés.

### Retiré

Ancien standard conservé pour historique, mais à ne plus utiliser.

## 5. Règles de modification

Toute modification importante doit expliquer :

- ce qui change ;
- pourquoi cela change ;
- quels documents sont concernés ;
- si le terrain réel a déjà été modifié ou non.

Une modification technique durable doit être accompagnée d'une ADR.

## 6. Standards

Un fichier `STD` doit au minimum contenir :

- objectif ;
- périmètre ;
- usage ;
- configuration cible ;
- nomenclature ;
- points à confirmer ;
- historique.

Un standard ne doit pas mélanger la théorie et l'inventaire réel. Le standard décrit ce qui est conforme ; les fiches terrain décrivent ce qui existe.

## 7. Procédures

Une procédure doit être utilisable sur le terrain.

Elle doit contenir :

- objectif ;
- matériel nécessaire ;
- sécurité / EPI ;
- étapes ;
- contrôles finaux ;
- erreurs fréquentes ;
- historique.

## 8. Fiches terrain

Une fiche terrain ou équipement doit décrire la réalité installée.

Elle peut contenir :

- localisation ;
- photos ;
- repères ;
- standard applicable ;
- particularités ;
- historique local ;
- points à vérifier.

## 9. ADR

Une ADR documente une décision technique.

Elle doit expliquer :

- le contexte ;
- le problème ;
- les options envisagées ;
- la décision ;
- les conséquences.

Une ADR n'est pas modifiée pour réécrire l'histoire. Si la décision change, une nouvelle ADR est créée et l'ancienne est marquée comme remplacée.

## 10. Photos et schémas

Les photos et schémas doivent avoir un nom explicite.

Exemples :

```text
assets/photos/T01-sortie-eau-2026-07-09.jpg
assets/schemas/STD-001-sortie-terrain.drawio
assets/schemas/STD-001-sortie-terrain.png
```

Les schémas doivent être simples et lisibles imprimés en A4.

## 11. Informations sensibles

Les informations permettant un accès physique ou logique au site ne doivent jamais être stockées dans le dépôt.

Sont notamment interdits :

- codes utilisateurs en vigueur ;
- codes maîtres ou installateur ;
- mots de passe ;
- clés API ;
- séquences confidentielles de programmation ;
- photos ou documents révélant ces informations.

Le dépôt peut contenir :

- la procédure générique de changement d’un code ;
- les liens vers les notices officielles ;
- les références des équipements ;
- la date, le motif et l’accès concerné par une modification ;
- l’emplacement organisationnel du registre sécurisé, sans son contenu.

Les codes d’accès du site sont conservés physiquement au bureau, hors Git.

## 12. Versionnement

Les documents utilisent une version simple :

- `0.x` : brouillon ou test ;
- `1.0` : première version validée ;
- `1.x` : amélioration compatible ;
- `2.0` : changement important de standard.

## 13. Règle finale

Le dépôt doit rester utile. Si une règle rend la documentation trop lourde à maintenir, la règle doit être simplifiée.