# Relevés terrain (famille `REL`)

Fiches de **relevé terrain A4** à imprimer, remplir à la main sur site, puis transcrire dans les documents de référence.

## Rôle dans l'architecture

- **Issue GitHub** (`releve:`) = pilotage, périmètre et suivi.
- **Fiche `REL-<issue>`** (ce dossier) = **source unique** du support papier, à la racine.
- **Documents de référence** (`FIC`, `SITE`, `EQ`, `STOCK`, …) = données validées, mises à jour **après** transcription.

## Impression

La source `REL-xxx.md` est **incluse** (sans duplication) dans la page publiée `docs/releves/REL-xxx.md`, qui ajoute un bouton « Imprimer ». Le rendu A4 réutilise le CSS d'impression existant (`docs/stylesheets/print.css`).

## Nomenclature

`REL-<numéro d'issue>-<sujet-court>.md` — le numéro reprend l'issue source (ex. `REL-007` ↔ issue #7).

## Règles

- Aucune donnée sensible (codes, mots de passe, séquences d'accès) sur les fiches.
- Ne pas deviner : `À confirmer` / `À relever` si l'information n'est pas certaine.

## Fiches

| Fiche | Issue | Sujet |
|---|---|---|
| [REL-007](./REL-007-sorties-eau-la-pastorale.md) | #7 | Sorties d'eau — La Pastorale (S1-T01 à T06) |
