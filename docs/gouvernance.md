# Gouvernance

Le référentiel doit rester utile, simple et fidèle au terrain.

## Architecture documentaire

Deux arborescences complémentaires coexistent (architecture validée en [issue #34](https://github.com/Simokes/tennismaintenance/issues/34)) :

- **Racine du dépôt** — **référentiel technique de référence** : fichiers numérotés, exhaustifs, templates et ADR. C'est la **source de vérité**, l'endroit où l'on modifie une donnée technique.
- **`docs/` (ce site)** — **vue opérationnelle publiée**, synthétique et orientée terrain, qui **renvoie vers** le document source racine.

Règles :

1. La donnée de référence **naît et évolue d'abord à la racine**.
2. Ce site **ne duplique pas** le détail : il résume et **renvoie** au document source (« Document source complet »).
3. Une page citant un document source **inexistant est interdite** (contrôle CI).
4. La **nomenclature numérotée est unique**.

## Documents sources

- [ENGINEERING.md](https://github.com/Simokes/tennismaintenance/blob/main/ENGINEERING.md)
- [README.md](https://github.com/Simokes/tennismaintenance/blob/main/README.md)
- [Roadmap](ROADMAP.md)

## Principes

1. La documentation reflète le terrain réel.
2. Les standards décrivent une configuration conforme.
3. Les fiches terrain décrivent ce qui existe réellement.
4. Une décision durable doit être documentée en ADR.
5. Une information incertaine reste marquée `À confirmer`.

## Cycle d'un standard

```text
Étude → Test terrain → Validé → Déployé → Retiré
```

## Règle de simplicité

Si une règle rend la documentation trop lourde à maintenir, la règle doit être simplifiée.