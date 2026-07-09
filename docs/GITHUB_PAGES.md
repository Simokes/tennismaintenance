# GitHub Pages — notes d'activation

## Objectif

Rendre le référentiel consultable comme un mini-site documentaire.

## Activation manuelle

L'activation de GitHub Pages se fait dans les paramètres du dépôt.

Chemin recommandé :

```text
Settings → Pages → Build and deployment
```

Configuration simple :

```text
Source : Deploy from a branch
Branch : main
Folder : /docs
```

Après activation, `docs/index.md` devient la page d'accueil du site.

## Limite actuelle

L'outil ChatGPT/GitHub dispose des droits `pull`, `push` et `triage`, mais pas des droits `admin`. L'activation de GitHub Pages doit donc être faite manuellement par le propriétaire du dépôt.

## Règle

Les documents doivent rester lisibles directement dans GitHub, même sans GitHub Pages.
