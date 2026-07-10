# ACC-002 — Contrôle d’accès du Kalisté

**Statut :** À compléter  
**Version :** 0.1  
**Date de création :** 2026-07-10  
**Dernière mise à jour :** 2026-07-10

## 1. Objectif

Documenter le fonctionnement général des accès à code du Kalisté, les équipements alimentés par piles, les gâches électriques et le cadenas à code du parking, sans stocker aucun code ou secret dans le dépôt.

## 2. Principe des accès terrains

Les cinq terrains utilisent un système différent de celui de La Pastorale :

```text
clavier à code alimenté par piles → commande locale → gâche électrique → ouverture
```

Le fabricant, le modèle, le type de piles et la présence éventuelle d’un ferme-porte restent à relever.

## 3. Accès équipés

| Repère | Accès | Clavier | Verrouillage | Alimentation | Statut |
|---|---|---|---|---|---|
| S2-ACC-T07 | Terrain 7 | À code, modèle à relever | Gâche électrique | Piles, type à relever | En service |
| S2-ACC-T08 | Terrain 8 | À code, modèle à relever | Gâche électrique | Piles, type à relever | En service |
| S2-ACC-T09 | Terrain 9 | À code, modèle à relever | Gâche électrique | Piles, type à relever | En service |
| S2-ACC-T10 | Terrain 10 | À code, modèle à relever | Gâche électrique | Piles, type à relever | En service |
| S2-ACC-T11 | Terrain 11 | À code, modèle à relever | Gâche électrique | Piles, type à relever | En service |
| S2-ACC-PARK | Parking | Cadenas à code | Mécanique | Sans alimentation | En service |

## 4. Gestion des codes

Les agents autorisés peuvent modifier les codes.

Les codes en vigueur et la combinaison du cadenas sont conservés physiquement au bureau. Le dépôt Git ne contient ni code utilisateur, ni code maître, ni combinaison, ni séquence confidentielle de programmation.

## 5. Procédure générique de changement d’un code terrain

!!! warning "Procédure générique"
    Cette procédure ne remplace pas la notice du fabricant. Les touches et séquences exactes seront ajoutées uniquement après identification fiable du modèle.

1. Vérifier que la modification est autorisée et identifier l’accès concerné.
2. Prévenir les utilisateurs concernés si le changement est immédiat.
3. Contrôler l’état des piles avant toute programmation.
4. Consulter la notice officielle correspondant au modèle réellement installé.
5. Passer le clavier en mode programmation sans noter la séquence secrète dans Git.
6. Ajouter, modifier ou supprimer le code utilisateur concerné.
7. Quitter proprement le mode programmation.
8. Tester que l’ancien code est refusé lorsqu’il doit être remplacé ou supprimé.
9. Tester le nouveau code et vérifier le déverrouillage complet de la gâche.
10. Refermer le portillon et vérifier son verrouillage effectif.
11. Mettre à jour le registre physique conservé au bureau.
12. Tracer dans l’historique Git la date, l’accès concerné et le motif, sans inscrire le code.

## 6. Procédure générique de remplacement des piles

1. Identifier le type et le nombre exacts de piles avant ouverture.
2. Préparer des piles neuves identiques, de même technologie et de même marque si possible.
3. Vérifier la procédure constructeur afin de savoir si la mémoire des codes est conservée sans alimentation.
4. Ouvrir le compartiment sans forcer ni détériorer le joint d’étanchéité.
5. Relever l’état des contacts et rechercher toute trace d’oxydation ou d’humidité.
6. Remplacer toutes les piles du module en même temps.
7. Respecter la polarité indiquée.
8. Refermer correctement le compartiment et son joint.
9. Tester au moins un code autorisé et vérifier la gâche.
10. Vérifier que le portillon se verrouille après fermeture.
11. Inscrire la date de remplacement dans l’historique, sans mentionner de code.

## 7. Procédure générique pour le cadenas du parking

1. Vérifier l’autorisation de modifier la combinaison.
2. Identifier précisément le fabricant et le modèle.
3. Consulter la notice officielle du cadenas.
4. Effectuer la modification hors vue du public.
5. Tester plusieurs fois l’ouverture et la fermeture avec la nouvelle combinaison.
6. Vérifier que l’ancienne combinaison est refusée si elle doit être remplacée.
7. Mettre à jour le registre physique du bureau.
8. Ne jamais inscrire la combinaison dans Git, une photo ou une légende.

## 8. Contrôles de maintenance

Pour les accès terrains :

- clavier lisible, solidement fixé et sans touche bloquée ;
- boîtier fermé et étanche ;
- absence d’oxydation visible ;
- niveau de piles suffisant ou absence d’alerte ;
- déclenchement correct après saisie autorisée ;
- libération complète de la gâche ;
- alignement correct du portillon et de la gâche ;
- verrouillage effectif après fermeture ;
- absence de jeu, frottement ou effort anormal.

Pour le cadenas du parking :

- molettes ou touches libres ;
- anse et corps sans corrosion excessive ;
- fermeture complète ;
- fixation et chaîne en bon état ;
- lubrification adaptée si autorisée par le fabricant.

## 9. Documentation officielle

À compléter après relevé des marques et modèles :

- notice d’installation et de programmation du clavier ;
- fiche technique et références des piles ;
- notice de la gâche électrique ;
- procédure constructeur en cas de piles déchargées ;
- notice du cadenas à code ;
- références de pièces détachées.

## 10. Photos à ajouter

- [ ] Façade d’un clavier représentatif.
- [ ] Plaque signalétique ou référence du clavier.
- [ ] Compartiment à piles, sans révéler de secret.
- [ ] Gâche électrique et alignement du portillon.
- [ ] Ferme-porte éventuel.
- [ ] Cadenas du parking fermé, sans montrer la combinaison.

## 11. Points à confirmer

- [ ] Fabricant et modèle des claviers.
- [ ] Confirmation qu’un seul modèle équipe T7 à T11.
- [ ] Type, nombre et autonomie des piles.
- [ ] Conservation ou perte des codes lors du remplacement des piles.
- [ ] Signalement d’un niveau de pile faible.
- [ ] Fabricant et modèle des gâches électriques.
- [ ] Présence et type de ferme-porte.
- [ ] Fabricant et modèle du cadenas du parking.

## 12. Historique

| Date | Accès concerné | Intervention | Motif | Agent |
|---|---|---|---|---|
| | | | | |

Aucun code ou combinaison ne doit apparaître dans ce tableau.
