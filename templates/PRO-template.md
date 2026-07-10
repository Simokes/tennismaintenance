<!--
====================================================================
MODÈLE DE DOSSIER PROJET « PRO-xxx »
====================================================================
Mode d'emploi :
1. Copier ce fichier vers  docs/projects/PRO-xxx-slug.md
   (xxx = numéro à 3 chiffres, slug = titre court en minuscules).
2. Remplacer tous les champs entre chevrons  < ... >.
3. Ajouter la page à la navigation dans  mkdocs.yml, sous « Projets » :
       - PRO-xxx — <Titre court> : projects/PRO-xxx-slug.md
4. Vérifier :  mkdocs build --strict   (doit être vert).

Convention technique (NE PAS MODIFIER la structure des conteneurs) :
- Le H1 (# …) reste EN DEHORS du conteneur : il sert de titre de page
  et il est réaffiché à l'impression via la règle
  .md-content__inner:has(.project-report) > h1  (print.css).
- Le bloc  <div class="print-actions no-print"> … </div>  porte le
  bouton d'impression (classe .print-button) ; il est masqué à l'impression.
- Le corps du dossier est enveloppé dans
      <div class="project-report" markdown="1"> … </div>
  L'attribut  markdown="1"  est OBLIGATOIRE : sans lui, l'extension
  md_in_html n'interprète pas le Markdown interne et tout s'affiche en
  texte brut. Laisser une ligne vide après la balise ouvrante et avant
  la balise fermante.
- Classes CSS stables utilisées : .print-actions, .print-button,
  .project-report (définies dans docs/stylesheets/print.css).
====================================================================
-->

# PRO-xxx — <Titre du projet>

<div class="print-actions no-print">
  <button type="button" class="md-button md-button--primary print-button" onclick="window.print()">🖨️ Imprimer le dossier</button>
  <p>Format conseillé : A4 portrait, échelle 100 %. La navigation et ce bouton seront masqués à l'impression.</p>
</div>

<div class="project-report" markdown="1">

**Site :** <site>  
**Statut :** <Étude | Test | Validé | Abandonné>  
**Version :** <0.1>  
**Date :** <AAAA-MM-JJ>  
**Porteur :** <nom / fonction>

## 1. Objet du projet

<Décrire en une à trois phrases le besoin et le résultat attendu.>

## 2. Contexte

<Rappeler la situation actuelle, les usages, les contraintes d'exploitation.>

| Élément | Donnée actuelle |
|---|---|
| Site | <…> |
| … | <…> |

## 3. Problématique

### <Axe 1 — ex. Sécurité>

- <point> ;
- <point>.

### <Axe 2 — ex. Durabilité>

- <point> ;
- <point>.

## 4. Objectifs

- <objectif> ;
- <objectif>.

## 5. Contraintes techniques

- <contrainte> ;
- <contrainte>.

## 6. Solutions étudiées

### A — <Solution A>

**Avantages :** <…>  
**Limites :** <…>

### B — <Solution B>

**Avantages :** <…>  
**Limites :** <…>

## 7. Comparatif

Notation indicative : 1 = défavorable, 5 = très favorable.

| Critère | Solution A | Solution B |
|---|---:|---:|
| <critère> | <1-5> | <1-5> |
| <critère> | <1-5> | <1-5> |

## 8. Recommandation

<Recommandation argumentée : quelle option, sur quel périmètre, avec quelles réserves.>

## 9. Budget à compléter

| Poste | Solution A | Solution B |
|---|---:|---:|
| <poste> | À chiffrer | À chiffrer |
| **Total** | **À chiffrer** | **À chiffrer** |

## 10. Risques et mesures

| Risque | Mesure proposée |
|---|---|
| <risque> | <mesure> |

## 11. Décision demandée

- [ ] <Option de décision 1>
- [ ] <Option de décision 2>
- [ ] Demander un complément d'étude.
- [ ] Ne pas poursuivre le projet.

**Décision retenue :** ______________________________

**Nom / fonction :** ______________________________

**Date :** ____________________    **Signature :** ____________________

</div>

<p class="no-print"><a href="https://github.com/Simokes/tennismaintenance/blob/main/projects/PRO-xxx-slug.md">Consulter le document source complet</a></p>
