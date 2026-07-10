# ACC-001 — Contrôle d’accès du site

**Statut :** À compléter  
**Version :** 0.1  
**Date de création :** 2026-07-10  
**Dernière mise à jour :** 2026-07-10

## 1. Objectif

Documenter le fonctionnement général des accès à code du complexe, les équipements concernés et la méthode générique de changement d’un code, sans stocker aucune information secrète dans le dépôt.

## 2. Principe du système

Les accès concernés utilisent le même principe général :

```text
clavier à code → commande électrique → ventouse électromagnétique → ouverture
                                                     ↓
                                      groom → fermeture automatique
```

Le fabricant, le modèle du clavier et le type de groom restent à relever.

## 3. Accès équipés

| Repère provisoire | Accès | Clavier à code | Ventouse électrique | Groom | Statut |
|---|---|---|---|---|---|
| ACC-T01 | Portillon terrain 1 | Sujet en cours | À confirmer | À confirmer | Cas particulier |
| ACC-T02 | Portillon terrain 2 | Oui | Oui | Oui, type à relever | En service |
| ACC-T03 | Portillon terrain 3 | Oui | Oui | Oui, type à relever | En service |
| ACC-T04 | Portillon terrain 4 | Oui | Oui | Oui, type à relever | En service |
| ACC-T05 | Portillon terrain 5 | Oui | Oui | Oui, type à relever | En service |
| ACC-T06 | Portillon terrain 6 | Oui | Oui | Oui, type à relever | En service |
| ACC-PRIN | Petit portillon d’accès principal | Oui | Oui | Oui, type à relever | En service |
| ACC-VH | Vestiaire hommes | Oui | Oui | Oui, type à relever | En service |
| ACC-VF | Vestiaire femmes | Oui | Oui | Oui, type à relever | En service |

Tous les accès du site sont annoncés comme utilisant le même système, sous réserve de vérification du modèle sur chaque équipement.

## 4. Autorité de modification

Les agents autorisés peuvent changer les codes d’accès.

Les codes en vigueur sont conservés physiquement au bureau. Le dépôt Git ne contient ni code utilisateur, ni code maître, ni séquence secrète de programmation.

## 5. Procédure générique de changement d’un code

!!! warning "Procédure générique"
    Cette procédure ne remplace pas la notice du fabricant. Les touches et séquences exactes ne seront ajoutées qu’après identification fiable du modèle.

1. Vérifier que la modification est autorisée et identifier les accès concernés.
2. Prévenir les utilisateurs concernés si le changement est immédiat.
3. Consulter la notice officielle correspondant au modèle réellement installé.
4. Passer le clavier en mode programmation selon la notice, sans noter la séquence secrète dans Git.
5. Ajouter, modifier ou supprimer le code utilisateur concerné.
6. Quitter proprement le mode programmation.
7. Tester que l’ancien code est refusé lorsqu’il doit être remplacé ou supprimé.
8. Tester le nouveau code et vérifier la libération de la ventouse.
9. Laisser la porte se refermer et vérifier l’action complète du groom.
10. Vérifier que la porte est réellement verrouillée après fermeture.
11. Tester les autres accès uniquement si une programmation commune peut les avoir affectés.
12. Mettre à jour le registre physique conservé au bureau.
13. Tracer dans l’historique Git la date, l’accès concerné et le motif, sans inscrire l’ancien ou le nouveau code.

## 6. Contrôles de maintenance

Pour chaque accès :

- clavier lisible, fixé et sans touche bloquée ;
- déclenchement correct après saisie autorisée ;
- libération complète de la ventouse ;
- absence de maintien ouvert anormal ;
- fermeture régulière par le groom ;
- alignement correct de la porte ;
- verrouillage effectif en fin de course ;
- absence de bruit, frottement ou claquement anormal ;
- état des câbles visibles sans démontage technique.

## 7. Documentation officielle

À compléter après relevé de la marque et du modèle :

- notice d’installation officielle ;
- notice de programmation officielle ;
- fiche technique du clavier ;
- fiche technique de la ventouse ;
- notice et réglage du groom ;
- références de pièces détachées.

## 8. Photos à ajouter

- [ ] Façade d’un clavier représentatif.
- [ ] Plaque signalétique ou référence du clavier.
- [ ] Ventouse électromagnétique.
- [ ] Groom et ses fixations.
- [ ] Porte fermée et alignement.
- [ ] Particularité du terrain 1.

Les photos ne doivent jamais montrer un code, une séquence de programmation ou un document papier contenant des secrets.

## 9. Points à confirmer

- [ ] Fabricant et modèle du clavier.
- [ ] Confirmation qu’un seul modèle équipe tous les accès.
- [ ] Fabricant et modèle de la ventouse.
- [ ] Type et modèle du groom.
- [ ] Fonctionnement exact du terrain 1.
- [ ] Existence éventuelle d’une programmation commune entre plusieurs portes.
- [ ] Responsable de validation du registre papier.

## 10. Historique

| Date | Accès concerné | Modification | Motif | Agent |
|---|---|---|---|---|
| | | | | |

Aucun code ne doit apparaître dans ce tableau.