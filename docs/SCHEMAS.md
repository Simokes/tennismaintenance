# Guide de production des schémas

## Objectif

Définir une méthode simple pour produire les schémas du référentiel.

Le but n'est pas de faire du dessin décoratif. Le schéma doit aider à comprendre, monter, diagnostiquer ou réparer.

## 1. Niveaux de schémas

### Niveau 1 — Croquis terrain

Rapide, fait à la main, utile pour capturer l'information.

Stockage :

```text
assets/croquis/
```

### Niveau 2 — Schéma propre

Schéma lisible, réalisé avec draw.io ou équivalent.

Stockage :

```text
assets/schemas/
```

### Niveau 3 — Export image

Image utilisée dans les documents Markdown ou imprimée.

Stockage :

```text
assets/schemas/
```

## 2. Style recommandé

- fond blanc ;
- traits simples ;
- repères courts : VP, VS, RC1, RC2, A1... ;
- flèche indiquant le sens de l'eau ;
- légende sous le schéma ;
- pas de détails inutiles.

## 3. Convention de nommage

```text
SCH-001-sortie-eau-terrain.drawio
SCH-001-sortie-eau-terrain.png
SCH-001-sortie-eau-terrain.md
```

## 4. Règle de vérité terrain

Un schéma peut être générique, mais il ne doit pas contredire le terrain réel.

Si une information est inconnue :

```text
À confirmer
```

## 5. Schémas prioritaires

1. SCH-001 — Sortie d'eau terrain.
2. SCH-002 — Sortie d'entretien GEKA.
3. SCH-003 — Ensemble d'arrosage manuel.
4. SCH-004 — Buse cuivre.
5. SCH-005 — Plan type terrain.

## 6. Validation d'un schéma

Avant validation :

- [ ] le schéma correspond au standard lié ;
- [ ] les repères sont cohérents ;
- [ ] le sens de l'eau est clair ;
- [ ] le schéma reste lisible imprimé ;
- [ ] les incertitudes sont marquées.
