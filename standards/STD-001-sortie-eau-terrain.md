# STD-001 — Sortie d'eau terrain

**Statut :** Brouillon  
**Version :** 0.3  
**Date :** 2026-07-12  
**Famille :** Point d'eau terrain

## 1. Objectif

Standardiser les sorties d'eau utilisées pour l'arrosage manuel des terrains en terre battue.

L'objectif est d'obtenir une sortie robuste, simple, réparable et adaptée à un usage intensif sur terrain.

## 2. Usage

Cette sortie est dédiée à l'arrosage manuel des terrains.

Elle doit permettre :

- un débit important ;
- une ouverture et fermeture rapides ;
- une maintenance simple ;
- une compatibilité avec l'ensemble d'arrosage manuel standard ;
- une réduction des pertes de charge inutiles.

## 3. Configuration existante constatée sur site

> Cette section décrit l'installation **actuellement en place** sur les terrains
> de La Pastorale, distincte de la configuration cible standardisée (§ 4).
> Elle sert de **modèle de référence** aux relevés : la fiche REL-007 ne
> documente que les écarts par rapport à cette base commune.

Architecture commune à toutes les sorties d'eau terrain (SET) :

```text
Sortie réseau filetée femelle 1"
        ↓
Robinet de puisage vissé  (fait actuellement office de vanne primaire)
        ↓
Raccord Écrou femelle 1" → cannelé Ø25
        ↓
Tuyau souple Ø25
```

La sortie réseau filetée femelle 1" est une **caractéristique commune du site** :
elle n'a pas à être relevée sortie par sortie. Seuls varient le modèle du robinet
de puisage, le raccord vers le tuyau et leur état.

Le raccord type est désigné **Écrou femelle 1" → cannelé Ø25**. Il s'agit d'une
**architecture commune**, non de sorties identiques ni conformes à un standard
(aucun standard n'est encore déployé). Le détail du réel — variations de robinets,
diamètre de tête, contraintes de maintenance — figure dans les fiches terrain et
`EQ-002`, pas dans ce standard.

**Photo de référence — SET existante conforme à cette base :**

![Sortie d'eau terrain existante : robinet de puisage vissé sur remontée en tube galvanisé de la sortie réseau, avec sortie filetée pour le raccord tuyau](../assets/photos/equipements/S1-SET-reference-existante-2026-07-11.jpg)

## 4. Configuration cible

```text
Sortie réseau femelle 1"
        ↓
Vanne primaire 1/4 tour 1" mâle/mâle
        ↓
Raccord 1" femelle → embout cannelé Ø25
        ↓
Tuyau souple Ø25
        ↓
Raccord 1" cannelé → femelle
        ↓
Vanne secondaire 1/4 tour 1" mâle/mâle
        ↓
Raccord 1" femelle → cannelé
        ↓
Buse cuivre custom Ø25
```

> **Écart principal existant → cible :** le robinet de puisage vissé tient
> aujourd'hui lieu de vanne primaire. La cible prévoit une vanne primaire
> 1/4 tour 1" M/M dédiée.

## 5. Repères

| Repère | Désignation | Fonction |
|---|---|---|
| SR | Sortie réseau femelle 1" | Point de départ disponible sur le terrain |
| VP | Vanne primaire 1/4 tour 1" M/M | Isolement rapide côté réseau |
| RC1 | Écrou femelle 1" → cannelé Ø25 | Liaison entre VP et tuyau |
| T25 | Tuyau souple Ø25 | Transport de l'eau jusqu'à la poignée |
| RC2 | Raccord 1" cannelé → femelle | Liaison entre tuyau et VS |
| VS | Vanne secondaire 1/4 tour 1" M/M | Commande à la poignée |
| RC3 | Raccord 1" femelle → cannelé | Liaison entre VS et buse cuivre |
| BC | Buse cuivre custom Ø25 | Jet de type pluie pour terre battue |

## 6. Rôle des deux vannes

### Vanne primaire — VP

La vanne primaire sert à isoler la sortie d'eau côté réseau.

Elle est utilisée pour :

- ouvrir l'alimentation du tuyau ;
- fermer la sortie après utilisation ;
- isoler la sortie en cas de fuite ou démontage.

### Vanne secondaire — VS

La vanne secondaire est placée côté poignée, près de la buse.

Elle est conservée car elle permet à l'agent de couper immédiatement l'eau sans revenir à la sortie réseau.

Elle est utile lorsque :

- une zone commence à flaquer ;
- l'agent est loin de la sortie ;
- il faut déplacer le tuyau ;
- il faut interrompre rapidement l'arrosage.

## 7. Philosophie du standard

Ce standard privilégie :

- les pièces laiton ou métalliques ;
- les raccords vissés et cannelés ;
- la robustesse ;
- le débit ;
- la réparation simple ;
- l'absence de raccord rapide sur la partie terrain.

## 8. Points à confirmer sur le terrain

- Longueur standard du tuyau Ø25 : ............ m
- Type exact de tuyau : ........................................
- Référence de la vanne 1" M/M : ........................................
- Référence du raccord 1" femelle/cannelé Ø25 : ........................................
- Méthode exacte de fixation du tuyau sur cannelé : collier / autre : ........................................

## 9. Historique

| Version | Date | Auteur | Description |
|---|---|---|---|
| 0.1 | 2026-07-09 | Peter / ChatGPT | Création du brouillon initial |
| 0.2 | 2026-07-11 | Peter / Claude | Ajout de la configuration existante constatée + photo de référence (issue #69) |
| 0.3 | 2026-07-12 | Peter / Claude | Vocabulaire normalisé du raccord (Écrou femelle 1" → cannelé Ø25) ; note sur les variations de robinets ; architecture commune ≠ conformité (issue #71) |
