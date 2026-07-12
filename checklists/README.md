# Checklists de relevé terrain (famille `CHK`)

**Checklists vivantes** d'avancement du relevé, **une par terrain**, maintenues dans le dépôt (pas sur papier). Elles pilotent la collecte : préparer une mission ciblée, cocher ce qui est obtenu, distinguer le confirmé du reste, et générer la liste des éléments manquants.

## Rôle dans l'architecture

Trois familles se complètent, chacune avec un rôle distinct :

| Famille | Rôle | Support |
|---|---|---|
| `REL` (`releves/`) | **Saisie** sur site, par *sujet* (sorties d'eau, regards…) | Papier A4 imprimé |
| `CHK` (ce dossier) | **Pilotage vivant** de la collecte, par *terrain* | Fichier suivi dans Git |
| `FIC` (`sites/`) | **Donnée de référence validée** | Document numéroté |

Une `CHK` n'est ni le support de saisie ni la donnée finale : c'est l'**état d'avancement** entre les deux. Elle est éditable depuis un téléphone après une mission.

## Nomenclature

`CHK-<site>-<terrain>.md` — un fichier par terrain, numéro suivant le terrain (pas l'issue) :

```text
checklists/CHK-S1-T01.md … checklists/CHK-S1-T06.md   (La Pastorale)
checklists/CHK-S2-T01.md … checklists/CHK-S2-T05.md   (Le Kalisté)
```

Les identifiants d'éléments restent **locaux au terrain**, en forme complète si ambiguïté : `S1-T01-REG-01`, `SET-01`, `AR-01`.

## Trois états (pas de pourcentage)

Chaque élément prend l'un de trois états, sans score calculé :

| État | Sens |
|---|---|
| **Obtenu** | Photo ou information relevée et fiable. |
| **À confirmer** | Vu, mais la fonction/identification n'est pas vérifiée sur site. |
| **À relever** | Pas encore obtenu. |

Un pourcentage automatique imposerait une pondération à maintenir et donnerait une fausse précision : l'information utile est « telle photo manque », pas « 62 % ». La progression globale se lit dans le [tableau de bord](./tableau-de-bord.md), qui agrège ces états sans calcul.

## Workflow de mission

```text
Checklist du terrain
→ préparation d'une mission ciblée (liste des éléments « À relever »)
→ prise de photos et relevés sur site
→ classement et renommage des fichiers (voir ci-dessous)
→ mise à jour des fiches terrain (FIC) et documents de référence
→ mise à jour de la checklist (états)
→ nouvelle liste des éléments manquants pour la mission suivante
```

## Procédure générale de relevé

**Première passe recommandée** (ne pas chercher la perfection) :

1. Photo générale de chaque terrain.
2. Photographier chaque sortie d'eau.
3. Repérer et photographier les regards accessibles.
4. Photographier l'ensemble d'arrosage manuel.
5. Ne noter que les informations **certaines** ; sinon `À confirmer` / `À relever`.

**Éléments de site (hors terrain)**, à relever une seule fois pour La Pastorale : nom officiel, adresse, position des vestiaires, du local technique, des sorties d'entretien (`SEM`) et des zones de stockage (voir `SITE-001`).

**Équipements mobiles** (inventaire, hors checklist par terrain) : tuyaux Ø25, buses cuivre, accessoires — suivis dans `STOCK-001` / `REL-010`.

## Classement et nommage des photos

Un dossier par terrain, **site inclus** dans le chemin pour éviter toute collision entre les deux sites :

```text
assets/photos/terrains/S1-T01/
assets/photos/terrains/S2-T01/
```

Nom complet, avec repère et date :

```text
S1-T01-vue-generale-2026-07-12.jpg
S1-T01-REG-01-ouvert-2026-07-12.jpg
S1-T01-SET-01-2026-07-12.jpg
```

## Règles

- **Ne pas deviner** : `À confirmer` / `À relever` si l'information n'est pas certaine. En particulier, les **fonctions hydrauliques ne se déduisent pas des photos** : elles restent `À confirmer` tant qu'elles ne sont pas vérifiées sur site.
- **Aucune donnée sensible** (codes, mots de passe, séquences d'accès).
- Identifiants **locaux au terrain**, forme complète en cas d'ambiguïté.

## Fichiers

- [Gabarit `CHK-template.md`](./CHK-template.md) — modèle réutilisable pour les 11 terrains.
- [Tableau de bord](./tableau-de-bord.md) — complétude globale des 11 terrains.

| Checklist | Terrain | État |
|---|---|---|
| [CHK-S1-T01](./CHK-S1-T01.md) | S1-T01 (La Pastorale) | En cours |
| [CHK-S1-T02](./CHK-S1-T02.md) | S1-T02 (La Pastorale) | Amorcé |
| [CHK-S1-T03](./CHK-S1-T03.md) | S1-T03 (La Pastorale) | À démarrer |
| [CHK-S1-T04](./CHK-S1-T04.md) | S1-T04 (La Pastorale) | À démarrer |
| [CHK-S1-T05](./CHK-S1-T05.md) | S1-T05 (La Pastorale) | À démarrer |
| [CHK-S1-T06](./CHK-S1-T06.md) | S1-T06 (La Pastorale) | À démarrer |
