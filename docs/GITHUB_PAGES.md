# GitHub Pages — activation

## Objectif

Rendre le référentiel consultable comme un site documentaire.

## Configuration recommandée

Le dépôt utilise MkDocs Material et des workflows GitHub Actions.

Dans GitHub :

```text
Settings → Pages → Build and deployment
```

Choisir :

```text
Source : GitHub Actions
```

Ne pas utiliser :

```text
Deploy from a branch
```

Cette ancienne option sert plutôt aux sites statiques simples. Ici, le site doit être construit par le workflow `.github/workflows/pages.yml`.

## Déploiement

Le workflow est :

```text
Deploy documentation site
```

Il s'exécute après une modification de `main` et effectue :

1. installation de Python ;
2. installation des dépendances déclarées dans `requirements.txt` ;
3. construction stricte du site ;
4. publication sur GitHub Pages.

La commande de référence est :

```bash
mkdocs build --strict --verbose
```

## Validation des pull requests

Le workflow `.github/workflows/docs-check.yml` construit également la documentation sur chaque pull request qui modifie :

- `docs/` ;
- `mkdocs.yml` ;
- `requirements.txt` ;
- le workflow de validation lui-même.

Le contrôle doit réussir avant fusion. Il permet notamment de détecter :

- une page déclarée dans la navigation mais absente ;
- un lien interne non résolu signalé par MkDocs ;
- une configuration YAML invalide ;
- une extension ou dépendance manquante ;
- un avertissement MkDocs transformé en erreur par le mode strict.

Ce contrôle ne garantit pas que tous les liens externes sont disponibles. Les sites constructeurs peuvent être momentanément indisponibles ou bloquer les vérifications automatisées.

## Adresse attendue

```text
https://simokes.github.io/tennismaintenance/
```

## Limite actuelle

L'outil ChatGPT/GitHub dispose des droits `pull`, `push` et `triage`, mais pas des droits `admin`. L'activation de GitHub Pages et les règles de protection de branche doivent donc être configurées manuellement par le propriétaire du dépôt.

## Règle

Les documents doivent rester lisibles directement dans GitHub, même sans GitHub Pages.
