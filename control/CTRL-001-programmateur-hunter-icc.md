# CTRL-001 — Programmateur Hunter ICC

**Statut :** Partiel — modèle et coffret confirmés sur plaque ; programmes, cycles et correspondance des canaux à relever  
**Version :** 0.2  
**Date de création :** 2026-07-10  
**Dernière mise à jour :** 2026-07-12

## 1. Objectif

Documenter le programmateur réellement installé, son fonctionnement utile aux agents, ses programmes, ses cycles et la correspondance entre ses canaux et les arroseurs des terrains.

Cette fiche ne remplace ni la notice constructeur ni les plans électriques officiels.

## 2. Identification

| Champ | Valeur |
|---|---|
| Fabricant | Hunter Industries |
| Gamme indiquée sur site | ICC |
| Modèle exact | **ICC-800PL** (confirmé sur plaque signalétique) |
| Génération | **ICC d'origine** (pas ICC2) — confirmé |
| Type de coffret | **Plastique**, pour extérieur (suffixe « PL ») — confirmé |
| Emplacement | À relever |
| Nombre de stations disponibles | Base 8 stations (ICC-800) + modules d'extension visibles — total à confirmer en comptant les borniers |
| Nombre de stations utilisées | À relever |
| Alimentation | Entrée 230 VAC → sortie 24 VAC (transformateur interne, d'après la plaque) — raccordement par le service compétent |
| Capteur pluie raccordé | À confirmer |

!!! note "Modèle confirmé sur plaque (2026-07-11)"
    Programmateur **Hunter ICC-800PL**, coffret plastique extérieur, génération ICC d'origine. Le manuel ICC (§ 9) et la liste de pièces du coffret plastique sont donc les bonnes références. Photos § 10.

## 3. Principe de commande du site

Un canal du programmateur commande généralement **deux arroseurs simultanément**. Les arroseurs associés forment habituellement une paire opposée sur un même côté du terrain.

Exemple constaté à confirmer terrain par terrain :

```text
CAN-01 → arroseur fond sud-ouest + arroseur fond nord-ouest
```

Il faut distinguer :

- l'arroseur physique et sa position ;
- le canal du programmateur ;
- la paire d'arroseurs déclenchée par ce canal ;
- le programme et le cycle qui activent le canal.

## 4. Correspondance générale des canaux

Ne renseigner une ligne qu'après un essai manuel ou une vérification fiable.

| Canal | Terrain | Arroseur 1 | Arroseur 2 | Électrovanne / regard utile | Vérifié le | Remarques |
|---|---|---|---|---|---|---|
| CAN-01 | À relever | À relever | À relever | À relever | | |
| CAN-02 | À relever | À relever | À relever | À relever | | |
| CAN-03 | À relever | À relever | À relever | À relever | | |
| CAN-04 | À relever | À relever | À relever | À relever | | |

Ajouter autant de lignes que nécessaire après relevé du nombre réel de stations.

## 5. Programmes

| Programme | Usage réel | Jours actifs | Heures de départ | Ajustement saisonnier | Statut |
|---|---|---|---|---|---|
| A | À relever | À relever | À relever | À relever | À confirmer |
| B | À relever | À relever | À relever | À relever | À confirmer |
| C | À relever | À relever | À relever | À relever | À confirmer |

## 6. Cycles et durées par station

| Programme | Canal | Terrain / paire | Durée | Ordre de passage | Remarques |
|---|---|---|---|---|---|
| À relever | À relever | À relever | À relever | À relever | |

## 7. Commandes utiles aux agents

À compléter après identification exacte du modèle :

- lancer manuellement une station ;
- lancer un programme complet ;
- interrompre un arrosage ;
- neutraliser temporairement un canal ;
- modifier une durée sans dérégler les autres programmes ;
- contrôler la date et l'heure ;
- lire les messages ou défauts affichés ;
- restaurer les réglages du site après une intervention.

## 8. Méthode de relevé canal par canal

1. Prévenir les personnes présentes sur les terrains.
2. Placer le programmateur en commande manuelle.
3. Activer un seul canal pendant une durée courte.
4. Identifier les deux arroseurs réellement déclenchés.
5. Noter leur terrain et leur position.
6. Repérer, sans démontage technique, le regard ou l'électrovanne utile au diagnostic si cela est vérifiable.
7. Arrêter le canal et vérifier l'absence de fuite ou de maintien en eau anormal.
8. Reporter le résultat dans cette fiche et dans la fiche du terrain concerné.

## 9. Documentation officielle

### Manuel d'utilisation et de programmation

- [Hunter ICC — Manuel utilisateur en français (PDF)](https://www.hunterirrigation.com/sites/default/files/OM_ICC_FR.PDF)

Ce manuel est la référence constructeur pour le fonctionnement, la programmation, les départs manuels, les durées de station, les programmes et les réglages du programmateur ICC.

### Pièces détachées

- [Hunter ICC — Liste des pièces du coffret plastique (PDF)](https://www.hunterirrigation.com/sites/default/files/replacementpartslist_icc-plasticcabinet.pdf)

Cette liste sert à identifier les composants remplaçables et leurs références. Vérifier que le programmateur installé possède bien un coffret plastique avant d'utiliser ces références pour une commande.

### Portails constructeur

- [Portail officiel Hunter — manuels utilisateur](https://www.hunterirrigation.com/support/owner-manuals)
- [Support officiel Hunter](https://www.hunterirrigation.com/support)
- [Page officielle Hunter ICC2](https://www.hunterirrigation.com/irrigation-product/controllers/icc2) — uniquement si la génération ICC2 est confirmée

## 10. Photos

Relevé du 2026-07-11 :

- [x] Façade et commandes — [CTRL-001-hunter-icc-facade-2026-07-11.jpg](https://github.com/Simokes/tennismaintenance/blob/main/assets/photos/equipements/CTRL-001-hunter-icc-facade-2026-07-11.jpg)
- [x] Plaque signalétique (ICC-800PL) — [CTRL-001-hunter-icc-plaque-2026-07-11.jpg](https://github.com/Simokes/tennismaintenance/blob/main/assets/photos/equipements/CTRL-001-hunter-icc-plaque-2026-07-11.jpg)
- [x] Coffret plastique et modules de stations — [CTRL-001-hunter-icc-interieur-2026-07-11.jpg](https://github.com/Simokes/tennismaintenance/blob/main/assets/photos/equipements/CTRL-001-hunter-icc-interieur-2026-07-11.jpg)
- [x] Notice de programmation affichée sur site — [CTRL-001-hunter-icc-notice-programmation-2026-07-11.jpg](https://github.com/Simokes/tennismaintenance/blob/main/assets/photos/equipements/CTRL-001-hunter-icc-notice-programmation-2026-07-11.jpg)
- [ ] Vue générale du programmateur fermé.
- [ ] Écran affichant les programmes et durées utiles en fonctionnement.

## 11. Historique des réglages

| Date | Modification | Valeur précédente | Nouvelle valeur | Motif | Agent |
|---|---|---|---|---|---|
| | | | | | |

## 12. Points à confirmer

- [x] Modèle et génération exacts — **ICC-800PL**, génération ICC (confirmé plaque, 2026-07-11).
- [x] Type de coffret : **plastique** extérieur (confirmé).
- [ ] Nombre total de stations.
- [ ] Correspondance complète canal → paire d'arroseurs.
- [ ] Programmes réellement utilisés.
- [ ] Heures de départ et durées actuelles.
- [ ] Usage des capteurs éventuels.
- [ ] Responsabilité de modification entre agents terrain et service technique.
