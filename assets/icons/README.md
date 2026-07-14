# Bibliothèque TennisMaintenance — symboles

Langage graphique **commun** à tous les plans (arrosage, éclairage, accès…).
Style **d'inspiration ISO** (ce ne sont pas des symboles normalisés officiels) :
module 48 px, trait 2 px, rayons et police uniformes.
Un même symbole = un même dessin sur tous les plans.

## Fichier

- `bibliotheque-tennismaintenance.svg` — planche complète, **A4 paysage exact
  (297 × 210 mm)**, imprimable à 100 % et éditable sous Inkscape.

## Réutilisation dans les plans

Chaque pictogramme est exposé dans le bloc `<defs>` sous **deux variantes** :

- `tm-{code}` — **dessin seul** (48 × 48). À utiliser quand tu poses ta propre
  étiquette numérotée sur le plan.
- `tm-{code}-lbl` — **dessin + texte** (48 × 78), étiquette embarquée : `CODE-XX`
  pour les équipements numérotés, nom en clair pour le reste. Un seul `<use>`
  amène le picto et son texte.

(États : `tm-etat-confirme`, `tm-etat-hs`, …)

Pour placer un symbole sur un plan **sans le redessiner** :

1. copier le bloc `<defs>…</defs>` de la bibliothèque dans le plan (une fois) ;
2. instancier autant de fois que voulu :

```xml
<use href="#tm-ar"     x="520" y="300" width="48" height="48"/>   <!-- dessin seul -->
<use href="#tm-ar-lbl" x="520" y="300" width="48" height="78"/>   <!-- dessin + AR-XX -->
```

Ainsi tous les plans partagent la même source graphique : corriger un symbole
dans la bibliothèque met tout le monde à jour, pas de copier-coller divergent.

### Sous Inkscape

- Chaque `<symbol>` est **nommé** (`inkscape:label` + `<title>`) : il apparaît
  dans **Objet ▸ Symboles**, prêt à être glissé-déposé sur un plan.
- Sur la planche, chaque pictogramme est enveloppé dans un **groupe nommé**
  (visible dans le panneau *Objets*) : un clic sélectionne le symbole entier,
  facile à déplacer, dupliquer ou copier vers un autre fichier.
- Le groupe **embarque son étiquette texte** : équipements numérotés au format
  `CODE-XX` (ex. `AR-XX`, `REG-XX` — remplacer `XX` par le numéro sur le plan),
  mobilier et repères en nom clair (`Banc`, `Poubelle`, `Portillon`…). En
  copiant le symbole, l'étiquette suit ; le plan reste lisible.

## Symboles (23)

| Domaine | Codes |
|---------|-------|
| Hydraulique | AR arroseur · REG regard · SET sortie d'eau · GK raccord Geka · EV électrovanne · VM vanne de réglage · VI vanne d'isolement · FIL filtre · CAR clapet anti-retour · PRG purge/vidange · CPT compteur · canalisation (simple trait) |
| Électricité & éclairage | PROG programmateur · CE coffret électrique · LED mât LED · HAL projecteur halogène · MON monnayeur |
| Mobilier | BAN banc · CHA chaise d'arbitre · POU poubelle |
| Accès & repères | ACC portillon · N nord · échelle |

Domaines à compléter au fil des relevés : **Clôtures · Sols · Signalisation**.

## Convention d'états

Marqueur apposé à côté d'un symbole pour indiquer son statut, sans surcharger le dessin :

| Marqueur | Sens |
|----------|------|
| ✔ (vert) | Confirmé sur site |
| ◐ (orange) | À vérifier |
| ✖ (rouge) | Hors service |
| 🔧 (bleu) | En intervention |
| 📷 (noir) | Photo disponible |

## Charte couleur — verrouillée

Aucune couleur en dehors de ces cinq :

- 🔵 `#1a4b9e` — Eau
- 🟢 `#1a7a3a` — Regards
- 🟠 `#d97a1a` — Surface / terrain
- 🔴 `#c0392b` — Électricité
- ⚫ `#2b2b2b` — Structure

Palette identique à `assets/plans/Template_plan-arrosage.svg`.

## Règle

Version 1.0 — première version canonique de la bibliothèque.

Bibliothèque compacte (≈ 20-25 symboles) : plus facile à mémoriser pour les
agents, plus homogène, plus durable qu'une collection riche de pictogrammes
rarement utilisés.
