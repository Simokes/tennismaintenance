# PROJECT_STATUS

> Point d'entrée pour toute nouvelle conversation IA (Claude / ChatGPT).
> Fichier **vivant** : résume l'état du projet, pas la documentation complète.
> Dernière mise à jour : **2026-07-12**.

## 🚀 Conversation Starter — procédure de reprise

1. Lire ce fichier (`PROJECT_STATUS.md`).
2. Lire `README.md` (référentiel, périmètre, nomenclature).
3. Lire les ADR (`decisions/`) et `docs/gouvernance.md` pertinents.
4. Vérifier les **PR et issues récentes** avant toute proposition (`gh pr list`, `gh issue list`).
5. Ne **jamais refaire un audit déjà clôturé**.
6. Ne **jamais reproposer une décision déjà validée** (voir « Décisions validées »).
7. Reprendre exactement depuis la section « **Prochaines priorités** ».

## 🎯 Objectif du projet

Référentiel technique de maintenance d'une structure tennis municipale : **2 sites** (La Pastorale = terre battue, Le Kalisté = dur + gazon synthétique), **11 terrains**. Voir `README.md` pour le périmètre exact.

## 🏛️ Architecture (Option 3 — validée, issue #34)

- **Racine du dépôt = référentiel de référence** (source de vérité, fichiers numérotés, templates, ADR).
- **`docs/` = site publié** (MkDocs Material, mobile-first) qui **résume et renvoie** vers la source.
- Détail et règles : `README.md` § « Architecture documentaire » et `docs/gouvernance.md`.

## 🔁 Workflow GitHub (réellement utilisé)

```text
Issue → Étude → Commentaire d'analyse → Validation humaine explicite
→ PR ciblée → Review → CI verte → Squash merge → Commentaire de clôture → Issue fermée
```

Rôles :
- **Claude** : étude et implémentation.
- **ChatGPT (GPTReviewer)** : revue, validation, suivi GitHub.
- **Humain** : décision explicite avant tout changement structurant.

## ✅ Décisions validées (clôturées — ne pas rouvrir)

| Sujet | Réf | Résultat |
|---|---|---|
| Audit MkDocs initial | #28 | Clôturé ; 6 lots correctifs livrés |
| Architecture documentaire | #34 | **Option 3** (racine = référentiel, `docs/` = publication) |
| Durcissement CI | #31 | Lien cassé / page orpheline **font échouer** `mkdocs build --strict` |
| Contrôle CI des liens source | #42 | `scripts/check_source_links.py` (câblé dans les 2 workflows) |
| Bandeau « Document source » | #41 | Standardisé (classe `.doc-source`) sur les pages `docs/` |
| Patron de projet | #33 | `templates/PRO-template.md` (convention `.project-report`) |
| Collision `EQ-004` | #43 | Porte renommée **`EQ-005`** |
| Slugs sites | #43 | `SITE-001-la-pastorale`, `SITE-002-le-kaliste` |
| Modèle d'intervention | #43 / #49 | `INT-000` = fiche papier ; gabarit unique = `templates/INT-template.md` |
| UX du site | #28 | Nav 4 onglets + thème « Terre battue » clair/sombre |
| Checklists de relevé | #73 / #74 | Famille **`CHK`** : pilotage vivant de la collecte, par terrain, 3 états (`Obtenu` / `À confirmer` / `À relever`), sans pourcentage. Pilote validé sur `S1-T01`. |

## 📊 État des chantiers

- **Socle documentaire & technique : stabilisé.** CI verte (build `--strict` + liens source), architecture et nomenclature en place, site habillé.
- **Contenu terrain : à collecter.** La plupart des fiches sont marquées `À relever` / `À confirmer` — c'est le principal travail restant. Trois familles outillent la collecte, avec des rôles distincts : **`REL`** (saisie papier A4, cf. `docs/releves/`, toutes créées), **`CHK`** (pilotage vivant par terrain, cf. `docs/checklists/`, pilote `S1-T01` livré) et **`FIC`** (donnée de référence validée).

## ⏭️ Prochaines priorités

1. **Relevés terrain** : les fiches papier A4 à remplir sur site sont **toutes créées** (famille `REL`, cf. `docs/releves/`).
   - La Pastorale : `REL-007` (#7), `REL-008` (#8), `REL-009` (#9), `REL-010` (#10), `REL-012` (#12).
   - Le Kalisté : `REL-017` (cartographie, #17), `REL-020` (revêtements, #20).
   - **Travail restant = collecte physique sur site**, puis transcription dans les documents de référence (`SITE-002`, `ACC-002`, `PROC-005/006`, `FIC-S2-*`, `STOCK-001`, `REF-001`, `FOURN-001`…). Les issues correspondantes **restent ouvertes** jusqu'à cette transcription.
   - Sans fiche dédiée : **photos prioritaires #11** (à prendre sur les deux sites).
   - **Généraliser les checklists `CHK`** (#73) aux terrains restants (`S1-T03` à `S1-T06`, `S2-T01` à `S2-T05`) à partir du gabarit `checklists/CHK-template.md`, au fil des missions. Le [tableau de bord](https://simokes.github.io/tennismaintenance/checklists/) suit la complétude.
2. Améliorations UX optionnelles (non tranchées) : remplacer les emojis d'interface par des icônes Material (nécessite `pymdownx.emoji`) ; clarifier certains libellés de catégories.

## 🚫 À ne jamais oublier (garde-fous)

- **Aucun secret d'accès** (codes, mots de passe, séquences) ne doit être stocké dans le dépôt.
- Toute **donnée de référence naît/évolue d'abord à la racine** ; `docs/` ne duplique pas, il renvoie.
- **Nomenclature numérotée unique** (un préfixe-numéro = un seul document).
- Garder **`mkdocs build --strict` et `scripts/check_source_links.py` verts** (tout renommage de source impose de corriger ses liens dans la même PR).
- **Décision humaine explicite** obligatoire avant renumérotation, suppression ou migration massive.
- **Modifications de `.github/workflows/*`** : vérifier les permissions disponibles avant d'agir ; si l'écriture est refusée (selon l'agent/token utilisé), demander une intervention humaine plutôt que de contourner.

## 📎 Références canoniques

- `README.md` — périmètre, structure, nomenclature.
- `docs/gouvernance.md` — principes et architecture (version publiée).
- `decisions/` — ADR (décisions techniques).
- `templates/` — gabarits (`PRO-template.md`, `INT-template.md`, `STD/PROC/FIC/ADR`).
- `scripts/check_source_links.py` — contrôle CI des liens source.
- Site publié : <https://simokes.github.io/tennismaintenance/>

## 🔧 Maintenance de ce fichier

Mettre à jour `PROJECT_STATUS.md` **uniquement** lors d'un changement d'état macro :
- après le merge d'un lot ou la clôture d'une issue importante → ajuster « Décisions validées » / « Prochaines priorités » ;
- après une décision structurante → l'ajouter aux décisions et garde-fous ;
- **ne pas** en faire un journal exhaustif : préférer des **liens** vers les sources canoniques.

> Format réutilisable pour d'autres projets DevOS : *Conversation Starter* + *Décisions validées* + *Workflow* + *Prochaines priorités* + *Garde-fous*, en liant les sources plutôt qu'en les recopiant.
