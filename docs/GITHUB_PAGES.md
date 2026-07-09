# GitHub Pages — activation

## Objectif

Rendre le référentiel consultable comme un site documentaire.

## Configuration recommandée

Le dépôt utilise MkDocs Material et un workflow GitHub Actions.

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

## Workflow

Le workflow est :

```text
Deploy documentation site
```

Il effectue :

1. installation de Python ;
2. installation de MkDocs Material ;
3. construction du site ;
4. publication sur GitHub Pages.

## Adresse attendue

```text
https://simokes.github.io/tennismaintenance/
```

## Limite actuelle

L'outil ChatGPT/GitHub dispose des droits `pull`, `push` et `triage`, mais pas des droits `admin`. L'activation de GitHub Pages doit donc être faite manuellement par le propriétaire du dépôt.

## Règle

Les documents doivent rester lisibles directement dans GitHub, même sans GitHub Pages.
