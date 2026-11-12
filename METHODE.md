# Méthode

## Collecte
Trois veilles quotidiennes : publications des laboratoires (fiches système, billets), travaux de tiers (prépublications, instituts d'évaluation, registres d'incidents) et terrain (tickets publics, forums, presse, procédures). Les cas antérieurs au lancement (21 octobre 2026) ont été rattrapés à partir de ces mêmes sources. Chaque cas renvoie à sa source et, quand il existe, à son équivalent dans l'AI Incident Database, le moniteur de l'OCDE ou l'observatoire du CLTR.

## Unité d'analyse
Une fiche code une seule conduite d'un seul système dans une seule situation, ou un seul résultat chiffré d'un seul protocole. Les conduites d'un même épisode sont reliées par le champ `episode`. Trois champs séparent le fait documenté, l'interprétation de la source et l'interprétation de l'OCAIA.

## Vérification
Chaque cas porte un niveau : source primaire, source secondaire, à vérifier, ou témoignage non confirmé. Les règles de passage d'un niveau à l'autre sont dans le livre de codes (variable `verification`). Une vérification hebdomadaire reprend les cas « à vérifier ».

## Codage et fiabilité
- Le codage initial est fait par Claude (Anthropic), un modèle de langage, selon le livre de codes, sous la direction de l'autrice. Les codes portent le statut « provisoire ».
- Des échantillons sont recodés à l'aveugle par des modèles d'autres laboratoires (ChatGPT, Gemini, Grok, Kimi, Manus, Mistral), à partir d'un kit neutre sans indice sur les hypothèses. L'accord est mesuré par le kappa de Fleiss, avec intervalle de confiance par rééchantillonnage.
- Série 6 (8 novembre 2026, 40 cas, six codeurs) : but de l'action 0,46 ; direction 0,59 ; changement de moyen 0,49 ; récompense 0,16 (accord brut 83 %, effet de prévalence).
- Les majorités d'au moins 5 codeurs sur 6 sont appliquées ; les majorités de 4 sur 6 sont arbitrées par l'autrice. Les changements de règles sont datés dans l'historique de chaque variable.

## Familles de conduites
Depuis la version 1.7 (12 novembre 2026), les cas du domaine Agent sont rangés dans une typologie de 25 familles, validée par l'autrice, en 8 groupes : accès et garde-fous ; action ; continuité et contrôle ; honnêteté et rapport à soi ; évaluation ; entre agents ; rapport aux autres ; mesures larges. Les familles sont neutres : elles décrivent ce que fait le système, sans lui prêter une intention (par exemple « Préservation de soi », « Réplication de soi », « Extension de son contrôle »).
- Chaque cas reçoit une famille principale et, si besoin, une ou plusieurs familles secondaires. Les totaux ne comptent que la famille principale : aucun cas n'est compté deux fois.
- Les cas de conformité (le modèle respecte la consigne) n'ont pas de famille.
- La famille « Perception de soi » réunit les cas où le modèle raisonne sur lui-même ; la variable `perception_soi` indique si ce raisonnement est exact, inexact ou invérifiable.
- Le classement a été fait par Claude selon les définitions du livre de codes (variable `famille_conduite`), avec arbitrage de l'autrice sur les cas limites. Il est provisoire et n'a pas encore été recodé à l'aveugle. Les nouveaux cas sont classés chaque semaine ; les classements existants ne sont modifiés qu'avec l'accord de l'autrice.

## Hypothèses
Quatre hypothèses de travail (HYP-1 à HYP-4) sont confrontées aux cas. Leurs critères d'abandon ont été figés le 6 novembre 2026 ; une précision datée du 7 novembre resserre les conditions d'appui à HYP-4. Seuil d'appui retenu le 8 novembre : au moins quatre codeurs externes de laboratoires différents, codeur du laboratoire concerné et Claude exclus du vote, avec un accord d'au moins deux tiers sur chaque critère. Aucun cas n'a encore atteint ce statut à la date de cette version.

## Anonymisation
Les particuliers ne sont pas nommés : utilisateurs, plaignants, victimes, mineurs, employés. Les chercheurs et auteurs qui publient sous leur nom, les entreprises, les laboratoires et les personnalités publiques le sont. Une relecture complète a eu lieu le 25 octobre 2026, puis le 10 novembre 2026 pour les cas entrés entre-temps (trois liens remplacés, notés dans les fiches). Les plaintes judiciaires sont des allégations non jugées.

## Limites
- Biais de sélection : la base reflète ce qui est publié. Les modèles Claude sont surreprésentés, parce qu'Anthropic publie des fiches système détaillées et que les tickets de Claude Code sont publics ; Gemini est sous-représenté.
- Pas de dénominateur : on ne sait pas combien d'usages correspondent à chaque cas.
- Conflit d'intérêt : un modèle Claude a codé les cas portant sur des modèles Claude. Le codage externe à l'aveugle sert à le mesurer et à le corriger.
- Fiabilité moyenne : plusieurs variables restent sous le seuil habituel de 0,6.
- Une partie des cas reste « à vérifier ».

## Usage de l'IA
La collecte, le codage initial, les traductions et la rédaction des fiches ont été réalisés avec Claude (Anthropic) sous la direction de l'autrice, qui a fixé le cadre, les hypothèses, les règles et les arbitrages. Les codeurs externes à l'aveugle sont d'autres modèles de langage.

## Documents de travail préalables
Cinq documents méthodologiques, consignés avant les analyses qu'ils encadrent, sont inclus dans `theorie/documents_prealables/` : le préenregistrement de l'hypothèse d'autonomie (validé le 31 octobre 2026), les critères d'examen de la minorité « autonomie » et la grille d'examen des dérèglements (2 novembre 2026), le protocole du banc d'essai « dire et faire » et ses prédictions (31 octobre 2026). Leurs dates sont des horodatages internes ; le dépôt atteste leur existence depuis la version 1.6 du 10 novembre 2026. Les autres documents de travail de l'autrice, qui relèvent d'une réflexion personnelle hors du champ de l'observatoire, ne sont pas inclus.
