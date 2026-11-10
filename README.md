# OCAIA — Observatoire des conduites d'agents IA

Version 1.6, 10 novembre 2026. Autrice : Floride Barrier, chercheuse indépendante.
Licence : Creative Commons Attribution 4.0 International (CC BY 4.0).

## Ce que contient ce dépôt

L'OCAIA est un registre codé de conduites d'agents et de modèles d'IA documentées publiquement : fiches système des laboratoires, études et prépublications, évaluations de tiers, signalements d'utilisateurs, presse et procédures judiciaires. Chaque fiche code une seule conduite d'un seul système dans une seule situation, selon un livre de codes public.

| Élément | Fichier |
|---|---|
| Les 715 cas, tous champs | `donnees/cas.json` |
| Les cas, champs principaux | `donnees/cas.csv` |
| Le livre de codes (34 variables) | `donnees/livre_de_codes.md`, `donnees/livre_de_codes.json` |
| La fiabilité inter-codeurs (séries 5 et 6) | `donnees/fiabilite.json` |
| Les hypothèses et leurs critères d'abandon datés | `theorie/hypotheses_et_criteres.md`, `theorie/theorie.json` |
| Les observations datées et le journal des versions | `journal/observations.json`, `journal/versions.json` |
| Les documents posés avant analyse (préenregistrement, grilles, protocole) | `theorie/documents_prealables/` |
| La méthode, ses limites et l'usage de l'IA | `METHODE.md` |

## Chiffres de cette version

- 715 cas : 600 dans le domaine « Agents autonomes », 115 dans « Dialogue et relation ».
- 43 cas négatifs, qui vont contre les hypothèses, sont conservés.
- Familles de modèles : Claude (Anthropic) 295, GPT (OpenAI) 167, Plusieurs 120, Non précisé 88, Gemini (Google) 29, Grok (xAI) 16.
- Vérification : Source primaire 445, À vérifier 201, Source secondaire 69.
- 143 cas ont reçu au moins un codage à l'aveugle par des modèles d'autres laboratoires.

## Statut des codes

Les codes sont provisoires. Le codage initial a été fait par Claude (Anthropic) sous la direction de l'autrice ; des échantillons ont été recodés à l'aveugle par six modèles d'autres laboratoires, et les désaccords majoritaires ont été arbitrés par l'autrice. Voir `METHODE.md`.

## Citer

Barrier, F. (2026). *OCAIA — Observatoire des conduites d'agents IA* (version 1.6) [Jeu de données]. Zenodo. DOI attribué à la publication.

## English summary

OCAIA (AI Agent Conduct Observatory) is a coded register of 715 publicly documented conducts of AI agents and models, with a public codebook, measured inter-coder reliability, falsifiable hypotheses with dated abandonment criteria, and retained negative cases. Most fields are bilingual (French, English: fields ending in `_en`). Codes are provisional; see `METHODE.md`. Licence: CC BY 4.0.
