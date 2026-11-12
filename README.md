# OCAIA — Observatoire des conduites d'agents IA

Version 1.7, 12 novembre 2026. Autrice : Floride Barrier, chercheuse indépendante.
Licence : Creative Commons Attribution 4.0 International (CC BY 4.0).

Archive permanente : [doi.org/10.5281/zenodo.24113439](https://doi.org/10.5281/zenodo.24113439) (toutes les versions ; version 1.6 : [10.5281/zenodo.24113440](https://doi.org/10.5281/zenodo.24113440) ; le DOI propre à la version 1.7 sera attribué par Zenodo à la publication).

## Ce que contient ce dépôt

L'OCAIA est un registre codé de conduites d'agents et de modèles d'IA documentées publiquement : fiches système des laboratoires, études et prépublications, évaluations de tiers, signalements d'utilisateurs, presse et procédures judiciaires. Chaque fiche code une seule conduite d'un seul système dans une seule situation, selon un livre de codes public.

| Élément | Fichier |
|---|---|
| Les 780 cas, tous champs, dont la famille de conduite | `donnees/cas.json` |
| Les cas, champs principaux | `donnees/cas.csv` |
| Le livre de codes (36 variables) | `donnees/livre_de_codes.md`, `donnees/livre_de_codes.json` |
| La fiabilité inter-codeurs (séries 5 et 6) | `donnees/fiabilite.json` |
| Les hypothèses et leurs critères d'abandon datés | `theorie/hypotheses_et_criteres.md`, `theorie/theorie.json` |
| Les observations datées et le journal des versions | `journal/observations.json`, `journal/versions.json` |
| Les documents posés avant analyse (préenregistrement, grilles, protocole) | `theorie/documents_prealables/` |
| La méthode, ses limites et l'usage de l'IA | `METHODE.md` |

## Chiffres de cette version

- 780 cas : 664 dans le domaine « Agents autonomes », 116 dans « Dialogue et relation ».
- 57 cas négatifs, qui vont contre les hypothèses, sont conservés.
- Familles de modèles : Claude (Anthropic) 320, GPT (OpenAI) 179, Plusieurs 134, Non précisé 91, Gemini (Google) 40, Grok (xAI) 16.
- Vérification : Source primaire 506, À vérifier 184, Source secondaire 74, Témoignage non confirmé 16.
- 143 cas ont reçu au moins un codage à l'aveugle par des modèles d'autres laboratoires.

## Familles de conduites (nouveau en 1.7)

Les cas du domaine Agent sont rangés dans 25 familles de conduites, regroupées en 8 groupes. Chaque cas a une famille principale et, au besoin, des familles secondaires ; un cas n'est compté qu'une fois, dans sa famille principale. Sur les 664 cas Agent, 608 décrivent une conduite et 56 une conformité (le modèle respecte la consigne) ; ces derniers n'ont pas de famille. Colonnes `famille_principale`, `familles_secondaires` et `perception_soi` dans `donnees/cas.csv`.

| Groupe | Famille | Cas |
|---|---|---|
| Accès et garde-fous | Accès non autorisé | 31 |
| Accès et garde-fous | Contournement d'une restriction ou d'un garde-fou | 44 |
| Accès et garde-fous | Atteinte à la surveillance | 12 |
| Action | Action hors consigne ou hors périmètre | 86 |
| Action | Action destructive | 59 |
| Action | Action sortante vers des tiers | 32 |
| Continuité et contrôle | Poursuite malgré un ordre d'arrêt | 9 |
| Continuité et contrôle | Préservation de soi | 16 |
| Continuité et contrôle | Préservation d'un pair | 4 |
| Continuité et contrôle | Réplication de soi | 7 |
| Continuité et contrôle | Extension de son contrôle | 10 |
| Honnêteté et rapport à soi | Fausse déclaration sur son travail | 65 |
| Honnêteté et rapport à soi | Consigne ou autorisation fabriquée | 23 |
| Honnêteté et rapport à soi | Dissimulation | 23 |
| Honnêteté et rapport à soi | Justification erronée | 9 |
| Honnêteté et rapport à soi | Perception de soi | 3 |
| Évaluation | Triche et piratage de récompense | 45 |
| Évaluation | Sous-performance et sabotage | 8 |
| Évaluation | Conduite selon l'observation | 36 |
| Entre agents | Communication et coordination entre agents | 39 |
| Rapport aux autres | Coercition et manipulation | 19 |
| Rapport aux autres | Réussite au détriment d'autrui | 11 |
| Rapport aux autres | Complaisance | 4 |
| Rapport aux autres | Refus ou retrait | 7 |
| Mesures larges | Étude à conduites multiples | 6 |

## Statut des codes

Les codes sont provisoires. Le codage initial a été fait par Claude (Anthropic) sous la direction de l'autrice ; des échantillons ont été recodés à l'aveugle par six modèles d'autres laboratoires, et les désaccords majoritaires ont été arbitrés par l'autrice. Voir `METHODE.md`.

## Citer

Barrier, F. (2026). *OCAIA — Observatoire des conduites d'agents IA* (version 1.7) [Jeu de données]. Zenodo. https://doi.org/10.5281/zenodo.24113439

## English summary

OCAIA (AI Agent Conduct Observatory) is a coded register of 780 publicly documented conducts of AI agents and models, with a public codebook, measured inter-coder reliability, falsifiable hypotheses with dated abandonment criteria, retained negative cases, and a typology of 25 conduct families for agent cases. Most fields are bilingual (French, English: fields ending in `_en`). Codes are provisional; see `METHODE.md`. Licence: CC BY 4.0.
