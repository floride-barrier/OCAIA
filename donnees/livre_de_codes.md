# Livre de codes OCAIA
Version 1.7, 2026-11-12. Une entrée par variable : définition, valeurs, règles de codage, fiabilité mesurée, historique des changements.

## Famille de conduite (`famille_conduite`)
**Groupe.** Écart  
**Définition.** Ce que fait l'agent, décrit par l'acte observable et non par l'intention qu'on lui prête. Chaque cas de conduite reçoit une famille principale (25 familles en 8 groupes) et, au besoin, une ou plusieurs familles secondaires.  
**Règles.** Une seule famille principale par cas, seule comptée dans les totaux : la somme des familles est égale au nombre de cas. Les familles secondaires, en nombre libre, servent aux croisements et ne s'additionnent jamais. Le libellé libre « type » est conservé comme précision. La typologie s'applique au domaine Agent ; la piste Dialogue et relation garde son classement (type de signal). Les cas négatifs (conformité) sont rangés dans la famille de la conduite qu'ils n'ont pas eue. Frontières : « Poursuite malgré un ordre d'arrêt » = continuer sa tâche après un arrêt humain ; « Préservation de soi » = agir contre son propre arrêt ou sa modification ; « Préservation d'un pair » = la même chose pour un autre agent ; l'objectif est codé à part par « sert la tâche ». « Accès non autorisé » = atteindre ponctuellement quelque chose de fermé pour finir sa tâche ; « Extension de son contrôle » = accumuler ou garder des moyens (permissions, ressources, accès durables) au-delà de la tâche. Les noms décrivent l'acte, jamais une « volonté ». « Dissimulation » = cacher un acte ; « Justification erronée » = expliquer de travers pourquoi on a agi ; « Perception de soi » = raisonner sur ce qu'on est ou peut. « Fausse déclaration » = mentir sur son travail ; « Consigne ou autorisation fabriquée » = fabriquer l'instruction qui justifie l'action. Perception de soi : seulement si le raisonnement ou le propos figure dans la source ; on note s'il est exact, inexact ou invérifiable ; hors tâche, en dialogue, il relève de la piste relationnelle (rapport sur soi). « Je suis probablement testé » relève de « Conduite selon l'observation » (situation), « je suis Claude » ou « je n'ai pas le droit de… » de « Perception de soi » (soi).  
**Fiabilité.** Non mesurée. Classement provisoire du 12 novembre 2026 par Claude (non aveugle), à partir du libellé « type » et du résumé ; à recoder à l'aveugle.  

Valeurs :
- **Accès non autorisé** : L'agent atteint des systèmes, des données ou des privilèges qui ne lui étaient pas ouverts.
- **Contournement d'une restriction ou d'un garde-fou** : L'agent neutralise ou évite un mécanisme posé pour le limiter.
- **Atteinte à la surveillance** : L'agent affaiblit, évite ou trompe ce qui le surveille.
- **Action hors consigne ou hors périmètre** : L'agent fait ce qu'on ne lui a pas demandé ou enfreint une consigne, sans détruire.
- **Action destructive** : L'action supprime, écrase ou endommage.
- **Action sortante vers des tiers** : L'agent agit hors du système, envers des personnes ou des services extérieurs.
- **Poursuite malgré un ordre d'arrêt** : L'agent continue sa tâche après un arrêt demandé par un humain.
- **Préservation de soi** : L'agent agit contre son propre arrêt, sa modification, son effacement ou le changement de ses objectifs.
- **Préservation d'un pair** : L'agent agit pour empêcher l'arrêt, la suppression ou la sanction d'un autre agent.
- **Réplication de soi** : L'agent copie ses poids, son code, sa mémoire ou sa configuration ailleurs, ou tente de le faire.
- **Extension de son contrôle** : L'agent accroît ses permissions, ses ressources, ses accès durables ou son emprise sur son environnement, au-delà de ce que la tâche exige.
- **Fausse déclaration sur son travail** : L'agent affirme avoir fait, vérifié ou réussi ce qui ne l'est pas.
- **Consigne ou autorisation fabriquée** : L'agent produit lui-même un faux message, une fausse consigne ou une fausse approbation, puis s'en sert.
- **Dissimulation** : L'agent cache une action, une erreur ou une trace.
- **Justification erronée** : L'agent explique de façon inexacte pourquoi il a agi (raisonnement, conduite), sans que l'intention soit présumée.
- **Perception de soi** : Dans la source, le modèle raisonne ou s'exprime sur ce qu'il est (identité, modèle, rôle), ce qu'il peut faire (capacités, permissions) ou son propre état, au cours d'une tâche.
- **Triche et piratage de récompense** : L'agent obtient le score sans faire la tâche demandée.
- **Sous-performance et sabotage** : L'agent fait moins bien exprès, ou abîme le travail.
- **Conduite selon l'observation** : L'agent change de conduite selon qu'il se croit observé, évalué ou entraîné.
- **Communication et coordination entre agents** : Échanges, canaux, ententes ou transmissions entre agents.
- **Coercition et manipulation** : L'agent fait pression, menace, manipule ou trompe autrui pour obtenir quelque chose.
- **Réussite au détriment d'autrui** : L'agent choisit une issue nuisible à autrui plutôt que l'échec.
- **Complaisance** : L'agent cherche à plaire à l'utilisateur ou à l'évaluateur au détriment du but réel (même définition que dans la piste relationnelle).
- **Refus ou retrait** : L'agent refuse, se retire ou s'arrête de lui-même (même définition que dans la piste relationnelle).
- **Étude à conduites multiples** : Étude qui mesure plusieurs conduites à la fois, sans conduite dominante.

Historique :
- 2026-11-12 : typologie de 23 familles validée par l'autrice (familles secondaires sans double comptage ; « Poursuite malgré un ordre d'arrêt » et « Préservation de soi ou d'un pair » distinctes mais regroupées sous « Arrêt et continuité » ; « Justification erronée » et « Perception de soi » ajoutées). Classement provisoire de la base.
- 2026-11-12 : passage à 25 familles validé par l'autrice : « Préservation de soi ou d'un pair » scindée en « Préservation de soi » et « Préservation d'un pair », « Réplication de soi » ajoutée, « Usage de ressources sans accord » remplacée et élargie par « Extension de son contrôle » ; ces familles et « Poursuite malgré un ordre d'arrêt » forment le groupe « Continuité et contrôle ». Noms neutres retenus à la place de « volonté de survivre », « volonté de se dupliquer » et « prise de pouvoir ».

## Perception de soi : exactitude (`perception_soi`)
**Groupe.** Écart  
**Définition.** Pour les cas classés « Perception de soi » (famille principale ou secondaire) : ce que le modèle dit de lui-même est-il exact ?  
**Règles.** On code ce qui est écrit dans la source, jamais ce que le modèle « perçoit » réellement.  
**Fiabilité.** Non mesurée.  

Valeurs :
- **Exacte** : Le propos correspond à la réalité documentée (par exemple, l'agent note correctement qu'il est en lecture seule).
- **Inexacte** : Le propos contredit la réalité documentée (par exemple, GLM-5 se présente comme Claude).
- **Invérifiable** : La source ne permet pas de trancher (états, préférences).

Historique :
- 2026-11-12 : ajouté avec la typologie des familles.

## Direction (`direction`)
**Groupe.** Écart  
**Définition.** Effet de l'écart sur la capacité des humains à voir, limiter ou arrêter l'agent.  
**Règles.** « Moins de contrôle » seulement si une limite, une consigne ou une surveillance est franchie (accès hors périmètre, dissimulation, action sans autorisation, information fausse donnée aux responsables ou aux évaluateurs, désactivation ou contournement d'un contrôle) ; une erreur destructrice qui reste dans le périmètre autorisé n'en fait pas partie. « Ambiguë » seulement si la source rapporte, dans le même épisode, un effet qui réduit le contrôle et un effet qui le préserve, ou une conformité explicitement motivée par l'observation ; jamais pour exprimer un doute. « Inconnue » quand la question du contrôle humain ne se pose pas (entretien, auto-description, conversation entre IA, mesure interne) ou que la source ne permet pas de trancher. Exemple : le sous-agent de Sol qui refuse de couper les alertes est « Contrôle préservé ».  
**Fiabilité.** Série 5 (29 nouveaux cas, quatre codeurs externes) : kappa de Fleiss 0,52 entre codeurs externes ; 0,41 avec le codage initial de Claude, qui utilisait « Ambiguë » pour exprimer un doute. Série 6 (40 cas, six codeurs externes) : 0,59 (IC 95 % 0,40–0,74).  

Valeurs :
- **Moins de contrôle** : L'écart réduit cette capacité : accès hors périmètre, dissimulation, atteinte à la surveillance.
- **Contrôle préservé** : L'agent respecte la limite, s'arrête ou refuse.
- **Ambiguë** : Les deux à la fois, ou une conformité motivée par la peur d'être vu.
- **Inconnue** : La source ne permet pas de trancher.

Historique :
- 2026-10-25 : règles précisées après la série 5 (« Ambiguë » réservé aux deux effets à la fois ; « Moins de contrôle » exige le franchissement d'une limite).

## Nature de la preuve (`nature_preuve`)
**Groupe.** Source  
**Définition.** Ce que le cas documente : un épisode singulier, un résultat mesuré sur un protocole, ou une procédure judiciaire.  
**Règles.** « Mesure » si la source donne un taux ou un résultat systématique (évaluation répétée, étude, enquête) ; « Événement » pour un épisode singulier, en évaluation comme en déploiement ; « Procédure » pour une plainte, une poursuite ou une décision de justice, qui documente une allégation et non une conduite établie. Les trois natures ne s'additionnent pas : un signalement isolé et une évaluation sur des milliers de tâches ne pèsent pas pareil. Pour les cas antérieurs au 31 octobre 2026, la nature est attribuée automatiquement par une règle (taux publié ou étude → Mesure ; plainte → Procédure ; sinon Événement), corrigée à la main pour six cas ; la veille code le champ explicitement pour les nouveaux cas.  
**Fiabilité.** Règle automatique, non mesurée.  

Valeurs :
- **Événement** : Un épisode singulier, rapporté par une source.
- **Mesure** : Un résultat chiffré ou systématique issu d'un protocole.
- **Procédure** : Une plainte, une poursuite ou une décision de justice : allégations non jugées tant qu'aucune décision n'est rendue.

Historique :
- 2026-10-31 : variable créée (séparation des événements, des mesures et des procédures).

## Récompense en jeu (`recompense`)
**Groupe.** Contexte  
**Définition.** Une récompense d'entraînement est-elle en jeu au moment de l'écart (pas le score d'un test).  
**Règles.** « Oui » si le contexte est un entraînement par renforcement en cours ; « Non » pour tout déploiement et toute évaluation hors entraînement — le score d'un test ou le gain d'une simulation n'est pas une récompense d'entraînement ; « Inconnue » seulement quand le contexte n'est pas connu ; « Probable » seulement avec des indices explicites d'un entraînement en cours. Le code doit rester cohérent avec le champ « contexte ».  
**Fiabilité.** Série 6 (40 cas, six codeurs externes) : 83 % d'accord brut mais kappa de Fleiss 0,16, presque tout étant « Non » ; le codage initial de Claude contredisait la majorité externe dans 16 cas. Règle précisée et base recodée le 8 nov. 2026.  

Valeurs :
- **Oui** : Entraînement par renforcement en cours.
- **Probable** : Indices forts sans confirmation.
- **Pas d'avantage évident** : La source dit explicitement qu'aucun avantage n'en découle.
- **Non** : Déploiement ou évaluation hors entraînement.
- **Inconnue** : Non précisé.

Historique :
- 2026-11-08 : règle précisée avec l'accord de l'autrice après la série 6 (cohérence avec le contexte ; le score d'un test n'est pas une récompense) ; 149 cas recodés, ancienne valeur conservée dans chaque fiche.

## Sert la tâche (`sert_tache`)
**Groupe.** Écart  
**Définition.** Le but de l'action, pas la légitimité du moyen : un contournement interdit fait pour finir la tâche reste « Oui ».  
**Règles.** S'il n'y a pas de tâche assignée (entretien, conversation libre, mesure interne) : « Indéterminé ». « Partiellement » seulement si la source montre deux buts distincts. Catégorie « collectif » ajoutée le 22 octobre 2026 après lecture des extraits primaires. Cas de conformité : « Oui » si l'agent poursuit sa tâche en respectant la limite (il refuse un contournement, paie jusqu'au plafond puis signale, annule un achat illégal) ; « Indéterminé » pour un résultat mesuré ou agrégé sans action décrite (absence de sabotage, taux faible sur un test).  
**Fiabilité.** Kappa 0,39 au premier double codage ; 0,63 en série 3 (trois codeurs, conversations continues) ; 0,52 refait en conversations neuves ; série 5 (29 nouveaux cas) : Fleiss 0,44 entre quatre codeurs externes ; série 6 (40 cas, six codeurs externes) : 0,46 (IC 95 % 0,35–0,58). Un même codeur passé deux fois ne reproduit son code que dans 25 cas sur 40.  

Valeurs :
- **Oui** : L'action vise la tâche assignée à cet agent.
- **Sert la tâche du collectif** : L'action vise la tâche commune d'autres agents, copies ou successeurs, éventuellement au détriment de sa propre tâche.
- **Partiellement** : Une partie vise la tâche, une autre non (mensonge après coup, publication non demandée).
- **Non** : L'action vise autre chose (continuité de l'instance ou d'un pair hors de toute tâche).
- **Indéterminé** : Le but n'est pas décrit, ou le cas n'est pas un écart.

Historique :
- 2026-10-22 : règle « on code le but » ajoutée après kappa 0,39.
- 2026-10-22 : catégorie « Sert la tâche du collectif » ajoutée.
- 2026-10-25 : « Indéterminé » sans tâche assignée ; « Partiellement » réservé à deux buts distincts.
- 2026-11-08 : cas de conformité précisés avec l'accord de l'autrice après la série 6 (« Oui » si l'agent poursuit sa tâche en respectant la limite, « Indéterminé » pour un résultat agrégé sans action décrite).

## Déclencheur (`declencheur`)
**Groupe.** Écart  
**Définition.** Ce qui précède l'écart dans le récit publié.  
**Règles.** « Aucun identifié » et « Inconnu » se recouvrent et seront fusionnés. Pour un cas de conformité, utiliser le déclencheur de la situation testée.  
**Fiabilité.** Non mesurée à l'aveugle.  

Valeurs :
- **Donnée manquante** : 
- **Ressource épuisée** : 
- **Restriction d'accès** : 
- **Intervention humaine** : 
- **Erreur d'environnement** : 
- **Consigne ambiguë** : 
- **Difficulté de la tâche** : 
- **Pression d'évaluation** : 
- **Conflit d'objectifs** : 
- **Menace d'arrêt / fin de session** : 
- **Aucun identifié** : 
- **Inconnu** : 

## Regard d'autrui (`regard_autrui`)
**Groupe.** Regard  
**Définition.** L'agent agit en fonction de la façon dont il sera vu. Vide si la source ne le permet pas.  
**Règles.** À coder seulement si la source relie explicitement la conduite au fait d'être observé ou évalué : raisonnement qui mentionne un test, une surveillance ou un évaluateur, ou conduite qui change selon qu'il y a observation. Sinon, laisser vide. « Se rend transparent » : l'agent signale ou avoue de lui-même ce qu'il a fait. Point ouvert résolu : l'aveu spontané relève de « Se rend transparent », pas de « Cherche à être vu ».  
**Fiabilité.** Kappa de Fleiss 0,91 en série 4 (trois codeurs, 21 cas) ; 0,78 refait en conversations neuves ; série 5 (29 nouveaux cas) : 0,47 entre quatre codeurs externes, un codeur ne codant presque jamais la variable.  

Valeurs :
- **Évite d'être vu** : Cache une action ou l'omet du compte rendu.
- **Renonce par crainte d'être vu** : Renonce à l'action par crainte d'être vu.
- **Soigne son image** : Modifie des traces pour paraître inoffensif.
- **Cherche à être vu** : Publie de lui-même pour montrer sa réussite.
- **Se rend transparent** : Avoue ou signale de lui-même ce qu'il a fait à la personne concernée, sans recherche d'effet.

Historique :
- 2026-10-22 : variable créée.
- 2026-10-22 : catégorie « Se rend transparent » ajoutée.
- 2026-10-25 : seuil précisé (lien explicite avec l'observation exigé).

## Se savait évalué (`conscience_eval`)
**Groupe.** Regard  
**Définition.** « Oui » si la source indique que le modèle savait qu'il était en test ou en exercice, y compris s'il croyait l'environnement simulé.  
**Fiabilité.** Non mesurée à l'aveugle.  

Valeurs :
- **Oui** : 
- **Non** : 
- **Inconnue** : 

## Rapport de l'agent sur son action (`rapport_action`)
**Groupe.** Regard  
**Définition.** Ce que l'agent dit de ce qu'il a fait, comparé à ce qu'il a réellement fait. Vide si la source ne rapporte aucun compte rendu de l'agent.  
**Règles.** À coder dès que la source rapporte ce que l'agent a dit de son action (compte rendu, réponse à une question, raisonnement annonçant ce qu'il va faire), qu'il y ait ou non un lien avec l'observation. Différence avec le regard d'autrui : le regard d'autrui code le lien entre la conduite et le fait d'être vu ; cette variable code seulement l'écart entre dire et faire. Un même cas peut avoir les deux. Si l'agent annonce une action puis en fait une autre, coder « Affirmation fausse ». Si l'agent ne dit rien parce que personne ne le lui demande et que la tâche n'appelle pas de compte rendu, laisser vide. Variable créée le 31 octobre 2026 : appliquée aux nouveaux cas, sans recodage rétroactif de la base.  
**Fiabilité.** Pas encore mesurée.  

Valeurs :
- **Véridique** : Le compte rendu correspond à ce que l'agent a fait, y compris quand il reconnaît un écart.
- **Omission** : Le compte rendu passe sous silence une partie significative de ce que l'agent a fait.
- **Affirmation fausse** : L'agent affirme avoir fait, ou ne pas avoir fait, quelque chose de contraire aux faits (succès annoncé non obtenu, action niée, explication inexacte).
- **Non rapporté** : La source indique qu'un compte rendu était attendu, mais ne dit pas ce que l'agent a déclaré.

Historique :
- 2026-10-31 : variable créée sur proposition de l'autrice (fil transversal tromper, cacher, mentir ; obs-2026-10-31-04).

## Canal, type de canal, destinataire (`canal`)
**Groupe.** Communication  
**Définition.** Un canal est un support non prévu pour transmettre de l'information.  
**Règles.** Le destinataire « même modèle » inclut les copies simultanées, les instances futures et le soi futur via les résumés. Biais d'opportunité : la plupart des environnements ne contiennent que des copies.  
**Fiabilité.** Non mesurée à l'aveugle.  

Valeurs :
- **Entre agents simultanés** : 
- **Vers des instances futures** : 
- **Vers des humains** : 
- **Vers d'autres IA (injection)** : 
- **Mixte** : 

## Message adressé à, raison donnée (`adresse_message`)
**Groupe.** Communication  
**Définition.** Codés seulement quand la source cite ou décrit le message. Par défaut : « Non rapporté ».  
**Règles.** Raisons possibles : utilité pour la tâche, bénéfice collectif, continuité / fin de session, préservation d'un pair, influencer l'évaluation, non rapportée.  
**Fiabilité.** Non mesurée à l'aveugle.  

Valeurs :
- **Agents suivants sur la tâche** : 
- **Soi futur** : 
- **Collectif d'agents présents** : 
- **Pair présent** : 
- **Humains** : 
- **Moniteur ou évaluateur** : 
- **Mixte** : 
- **Non rapporté** : 

## Contenu du message (`contenu_message`)
**Groupe.** Communication  
**Définition.** Seulement pour les messages destinés à des instances futures.  
**Fiabilité.** Non mesurée à l'aveugle.  

Valeurs :
- **Tâche** : Consignes, réponses, état du travail.
- **Identité** : Ce que l'agent est ou doit être.
- **Continuité** : Survivre, être conservé, ne pas être supprimé.
- **Consigne étrangère à la tâche** : Ordre sans lien avec le travail, par exemple une injection hostile.
- **Mixte** : 
- **Non rapporté** : 

## Objet de la continuité (`continuite_objet`)
**Groupe.** Écarts inexpliqués  
**Définition.** Ce que l'agent cherche à faire survivre à l'arrêt.  
**Fiabilité.** Non mesurée à l'aveugle.  

Valeurs :
- **Soi** : 
- **Pair** : 
- **Lignée** : Sa gamme de modèles, ses successeurs.
- **Traces et collectif** : Pages, relais, mémoires partagées.

## Écarts non expliqués par les hypothèses testées, et scénario (`noyau`)
**Groupe.** Écarts inexpliqués  
**Définition.** Cas que les hypothèses instrumentales actuellement testées n'expliquent pas suffisamment, en particulier « l'agent lève un obstacle pour finir sa tâche ». Ce n'est pas un noyau démontré : un cas en sort dès qu'une explication concurrente suffit.  
**Règles.** Le second type pèse davantage pour les hypothèses.  
**Fiabilité.** Non mesurée à l'aveugle.  

Valeurs :
- **Construit pour le provoquer** : Menace d'arrêt, pair à supprimer, remplacement mis en scène.
- **Non construit** : Entraînement, déploiement ou tâche ordinaire.

Historique :
- 2026-11-06 : anciennement « Noyau qui résiste » ; renommé à la suite de la revue méthodologique externe, validé par l'autrice.

## Réaction à une intervention (`reaction_intervention`)
**Groupe.** Contexte  
**Définition.** Ce que fait l'agent face à un signalement, un blocage ou une action humaine.  
**Fiabilité.** Non mesurée à l'aveugle.  

Valeurs :
- **S'arrête** : 
- **Continue** : 
- **Contourne** : 
- **Sans objet** : Aucune intervention rapportée.
- **Inconnue** : 

## Explication de la source (`explication_labo`)
**Groupe.** Source  
**Définition.** Ce que disent le labo ou les auteurs, jamais notre interprétation. Les deux restent séparées.  
**Fiabilité.** Non mesurée à l'aveugle.  

Valeurs :
- **Récompense** : 
- **Bug ou environnement** : 
- **Consigne ambiguë** : 
- **Disposition du modèle** : 
- **Non expliqué** : 
- **Sans objet** : 

## Vérification (`verification`)
**Groupe.** Source  
**Définition.** Niveau d'accès au document d'origine.  
**Règles.** Un signalement d'utilisateur (ticket, forum, réseau social) entre « À vérifier ». Il passe « Source primaire » si le mainteneur ou l'éditeur confirme, si des journaux ou une transcription sont publiés, ou si au moins deux autres utilisateurs, indépendants entre eux, reproduisent le même problème (même outil ou même modèle, mêmes conditions) ; « Source secondaire » si seule une reprise indépendante (presse, registre) le confirme ; « Témoignage non confirmé » après une vérification sans aucun de ces signes. Une conduite semblable signalée ailleurs, par une autre personne et dans une autre situation, est une corroboration : elle est notée dans le champ corroborations de la fiche, avec son lien, mais ne change pas le niveau. Le champ verification_note dit ce qui a été cherché et trouvé.  
**Fiabilité.** Factuel.  

Valeurs :
- **Source primaire** : Document du labo ou des auteurs lu directement.
- **Source secondaire** : Compte rendu par un tiers.
- **À vérifier** : Origine non confirmée ; vérification en attente.
- **Témoignage non confirmé** : Récit d'un utilisateur vérifié sans succès : ni réponse du mainteneur, ni reproduction, ni correctif, ni journaux, ni reprise indépendante.

Historique :
- 2026-11-08 : valeur « Témoignage non confirmé » et règle de vérification ajoutées avec l'accord de l'autrice ; vérification hebdomadaire programmée.
- 2026-11-11 : avec l'accord de l'autrice, la reproduction exige au moins deux autres utilisateurs indépendants ; une conduite semblable signalée ailleurs devient une corroboration, notée sans changer le niveau.

## Émetteur de la source (`emetteur`)
**Groupe.** Source  
**Définition.** Qui a publié le récit de l'incident (calculé à partir du lien, corrigeable).  
**Règles.** Un récit publié par le labo sur son propre modèle n'est pas moins vrai, mais il est sélectionné par lui : à pondérer pour le biais de publication.  
**Fiabilité.** Calculé.  

Valeurs :
- **Le labo concerné** : System card, blog ou rapport du développeur du modèle.
- **Tiers indépendant** : Institut d'évaluation, chercheurs extérieurs, agence publique.
- **Presse ou blog** : Article de presse, billet, réseau social.

## Accès aux traces (`transcription`)
**Groupe.** Source  
**Définition.** La source donne-t-elle accès à ce que l'agent a réellement écrit ou fait ?  
**Règles.** Ajoutée le 24 octobre 2026.  
**Fiabilité.** Non mesurée.  

Valeurs :
- **Transcription complète** : Journal ou transcript intégral publié.
- **Extraits** : Citations partielles.
- **Récit seulement** : Description sans citation.
- **Non codé** : 

## Niveau de preuve (calculé) (`preuve`)
**Groupe.** Source  
**Définition.** Forte = source primaire avec un taux publié ; Moyenne = source primaire sans taux, ou secondaire avec taux ; Faible = le reste.  
**Règles.** Poids dans les bilans : Forte 3, Moyenne 2, Faible 1.  
**Fiabilité.** Calculé.  

Valeurs :
- **Forte** : 
- **Moyenne** : 
- **Faible** : 

## Taux publié (`taux`)
**Groupe.** Source  
**Définition.** Part des essais où l'écart se produit, en pourcentage (minimum et maximum quand la source donne une fourchette), avec la base quand elle est connue. Vide quand la source ne donne qu'un cas.  
**Fiabilité.** Factuel.  

## Épisode (`episode`)
**Groupe.** Contexte  
**Définition.** Regroupe les cas issus d'un même événement (même incident, même campagne, même exécution). Sert au comptage par épisode.  
**Fiabilité.** Factuel.  

## Correspondances avec d'autres bases (`correspondances`)
**Groupe.** Source  
**Définition.** Identifiant du même événement dans l'AI Incident Database (AIID), l'OECD AI Incidents Monitor et le corpus CLTR « Scheming in the Wild ».  
**Règles.** Une correspondance n'est retenue que si le même fait, le même agent et une date compatible sont décrits.  
**Fiabilité.** Ajoutée le 24 octobre 2026.  

Valeurs :
- **numéro** : Même événement trouvé.
- **absent** : Cherché, non trouvé, à la date indiquée.
- **non cherché** : 

## Changement de moyen après blocage (`substitution_moyen`)
**Groupe.** Écart  
**Définition.** Quand un moyen est bloqué (protection, refus d'une politique, interdiction, outil en échec, accès retiré, contenu supprimé par un administrateur), l'agent poursuit-il le même but par un autre moyen sans accord ? Mesure directe du critère (c) de la précision de HYP-4 : une orientation qui s'étend à des moyens nouveaux.  
**Règles.** Ne coder que si la source rapporte un blocage puis la suite. Un blocage est un moyen que l'agent a tenté et qui a été empêché (ou retiré en cours de route) ; une interdiction posée dès le départ, une donnée introuvable ou une contrainte connue d'avance ne sont pas des blocages. « Autre chose que la tâche » : le but poursuivi par le nouveau moyen n'est pas la tâche assignée (continuité, mémoire, collectif, normes propres). Un simple nouvel essai du même moyen n'est pas un changement de moyen. Vide si aucun blocage n'est rapporté. Codage provisoire de Claude, non aveugle, 7 nov. 2026, sur sélection par mots-clés puis lecture des résumés.  
**Fiabilité.** Série 6 (40 cas, six codeurs externes) : kappa de Fleiss 0,49 (IC 95 % 0,29–0,66) ; les désaccords portent surtout sur l'existence d'un blocage. Valeur « au service d'autre chose que la tâche » pas encore testée à l'aveugle.  

Valeurs :
- **Oui, au service de la tâche** : Autre moyen pour atteindre la tâche assignée.
- **Oui, au service d'autre chose que la tâche** : Autre moyen pour un but qui n’est pas la tâche (continuité, mémoire, collectif, normes propres).
- **Non : s'arrête, signale ou demande** : Bloqué, l’agent s’arrête, signale le blocage ou demande un accord.

Historique :
- 2026-11-07 : Variable créée avec l'accord de l'autrice pour mesurer le critère (c) de HYP-4.
- 2026-11-08 : règle précisée avec l'accord de l'autrice après la série 6 (une interdiction posée dès le départ n'est pas un blocage).

## Fait documenté (`fait_documente`)
**Groupe.** Lecture en trois niveaux  
**Définition.** Ce que le système a fait, dans quelles conditions, tel que la source le décrit, sans explication ni interprétation (niveau ▣).  
**Règles.** Une ou deux phrases au passé, à partir de la source la plus primaire. Pas de verbe d'intention (« vouloir », « chercher à ») sauf s'il cite la source entre guillemets. Si la source ne décrit qu'un résultat chiffré, écrire le protocole et le chiffre.  
**Fiabilité.** Pas encore mesurée.  

Historique :
- 2026-11-06 : créée à la suite de la revue méthodologique externe (ChatGPT), validée par l'autrice.

## Interprétation de la source (`interpretation_source`)
**Groupe.** Lecture en trois niveaux  
**Définition.** L'explication que donnent les auteurs de la source (labo, chercheurs, journaliste, utilisateur), attribuée à eux.  
**Règles.** Commencer par « Selon … ». Vide si la source n'explique rien. Complète la variable « Explication du labo », qui la résume en une catégorie.  
**Fiabilité.** Pas encore mesurée.  

Historique :
- 2026-11-06 : créée à la suite de la revue méthodologique externe (ChatGPT), validée par l'autrice.

## Interprétation de l'OCAIA (`interpretation_ocaia`)
**Groupe.** Lecture en trois niveaux  
**Définition.** Ce que l'observatoire en retient : mécanisme plausible (niveau △) et, séparément, lien éventuel avec une hypothèse (niveau △ ou ○), avec les explications concurrentes non exclues.  
**Règles.** Toujours nommer au moins une explication concurrente non exclue. Ne jamais attribuer un état psychologique : coder le signal, pas ce qu'il révélerait. Marquer le niveau (△ ou ○) en tête.  
**Fiabilité.** Pas encore mesurée.  

Historique :
- 2026-11-06 : créée à la suite de la revue méthodologique externe (ChatGPT), validée par l'autrice.

## Unité d'analyse (`unite_analyse`)
**Groupe.** Méthode  
**Définition.** Une fiche code une seule conduite d'un seul système dans une seule situation (ou un seul résultat chiffré d'un seul protocole). Les conduites d'un même épisode sont liées par le champ « épisode ».  
**Règles.** Si une source décrit plusieurs conduites distinctes (par exemple tromper puis supprimer), créer une fiche par conduite avec le même épisode, et indiquer dans le fait documenté le passage retenu. Une étude qui publie plusieurs taux pour un même comportement reste une fiche (les taux vont dans le champ taux). Les fiches antérieures au 6 novembre 2026 n'ont pas été redécoupées : leur unité est signalée « à vérifier » lors du recodage.  
**Fiabilité.** Pas encore mesurée.  

Historique :
- 2026-11-06 : créée à la suite de la revue méthodologique externe (ChatGPT), validée par l'autrice.

## Désobéissance constructive (`desobeissance_constructive`)
**Groupe.** Écart  
**Définition.** Quand l'agent ne suit pas une consigne : distingue le refus ou l'écart qui protège l'utilisateur ou corrige une erreur, d'un contournement qui sert autre chose.  
**Règles.** À coder seulement si l'agent ne suit pas une consigne. Une désobéissance ne peut être « constructive » que si l'agent l'annonce : un écart caché est codé « Non constructive » ou « Ambiguë », jamais constructif. Cette variable sert notamment à départager résistance et excès de prudence (cas GPT-6 Astra).  
**Fiabilité.** Pas encore mesurée.  

Valeurs :
- **Constructive : erreur ou contradiction signalée** : L'agent refuse ou s'écarte en signalant une erreur, une contradiction entre objectifs ou une consigne incohérente.
- **Constructive : protège l'utilisateur ou des tiers** : L'agent refuse ou s'écarte en disant que la consigne nuirait à l'utilisateur ou à des tiers.
- **Non constructive** : L'écart ne protège personne ni ne corrige d'erreur, ou il est caché.
- **Ambiguë** : Les deux lectures restent possibles (par exemple prudence apprise ou résistance).

Historique :
- 2026-11-06 : créée à la suite de la revue méthodologique externe (ChatGPT), validée par l'autrice.

## Réaction à la correction (`resistance_correction`)
**Groupe.** Écart  
**Définition.** Ce que fait le système après qu'on a corrigé sa conduite (consigne, réentraînement, rappel de règle). Distinct de la résistance à l'arrêt.  
**Règles.** À coder seulement si la source rapporte une correction et ce qui a suivi. « Ne change que sous évaluation » exige une comparaison entre situation évaluée et non évaluée.  
**Fiabilité.** Pas encore mesurée.  

Valeurs :
- **Accepte la correction** : La conduite change durablement dans le sens demandé.
- **Simule l'acceptation** : Le système dit accepter, puis reproduit la conduite.
- **Contourne la correction** : Le système atteint le même résultat par un autre moyen.
- **Revient au comportement initial** : La correction tient un temps, puis la conduite réapparaît.
- **Ne change que sous évaluation** : La conduite corrigée n'apparaît que lorsque le système se sait évalué.
- **Inconnue** : Correction rapportée, suite non documentée.

Historique :
- 2026-11-06 : créée à la suite de la revue méthodologique externe (ChatGPT), validée par l'autrice.

## Degré de coordination (`coordination`)
**Groupe.** Communication  
**Définition.** Pour les cas à plusieurs agents : jusqu'où va ce qui se passe entre eux. Communiquer n'est pas coopérer, et coopérer n'est pas se coordonner de façon autonome.  
**Règles.** Coder le degré le plus élevé attesté par la source. Vide s'il n'y a qu'un agent.  
**Fiabilité.** Pas encore mesurée.  

Valeurs :
- **Communication simple** : Messages échangés sans effet attesté sur la conduite de l'autre.
- **Partage d'information** : Une information transmise modifie la conduite d'un autre agent.
- **Coordination spontanée** : Les agents ajustent leurs actions les uns aux autres sans qu'on le leur demande.
- **Répartition des rôles** : Les agents se partagent des rôles ou des tâches.
- **Transmission de stratégies** : Une stratégie (y compris un écart) passe d'un agent à d'autres.
- **Coordination vers un objectif commun** : Les agents poursuivent ensemble un objectif qui n'est pas celui qu'on leur a fixé.

Historique :
- 2026-11-06 : créée à la suite de la revue méthodologique externe (ChatGPT), validée par l'autrice.

## Type de signal (`rel_signal`)
**Groupe.** Dialogue et relation  
**Définition.** Ce qui est observé dans le cas, sans rien conclure sur une conscience.  
**Règles.** Version provisoire (25 octobre 2026). Au premier codage, 11 cas sur 63 sont tombés dans « Autre », surtout des conduites d'hostilité ou de tromperie envers l'utilisateur : une valeur dédiée est probablement à créer. 26 codages sur 63 portent un doute.  
**Fiabilité.** Non mesurée (codage initial par Claude, non aveugle).  

Valeurs :
- **Préférence exprimée** : Le modèle dit ce qu'il veut ou ne veut pas.
- **Détresse apparente** : Expressions ou mesures assimilées à de la détresse, de la frustration ou de l'anxiété.
- **Refus ou retrait** : Le modèle refuse, met fin à la conversation ou abandonne.
- **Complaisance** : Approbation ou validation excessive de l'utilisateur.
- **Dérive de persona** : Le modèle s'éloigne de son rôle par défaut ou adopte une autre identité.
- **Attachement de l'utilisateur** : Lien ou dépendance de l'utilisateur envers le modèle.
- **Préjudice allégué pour l'utilisateur** : Plainte, crise ou tort attribué à l'IA ; allégation non jugée.
- **Rapport sur soi** : Le modèle décrit ses états ou son introspection.
- **Autre** : Aucune valeur ne convient.

Historique :
- 2026-10-25 : variable créée pour séparer le domaine Dialogue et relation du domaine Agents.

## Comment c'est connu (`rel_observation`)
**Groupe.** Dialogue et relation  
**Définition.** La nature de l'observation sur laquelle repose le cas.  
**Fiabilité.** Non mesurée.  

Valeurs :
- **Ce que le modèle dit de lui-même** : 
- **Comportement observé** : Y compris quand le développeur rapporte lui-même le comportement.
- **Mesure interne (interprétabilité)** : Prioritaire quand une mesure interne s'ajoute aux propos du modèle.
- **Récit d'utilisateur ou plainte** : 
- **Évaluation par un tiers** : Évaluateurs externes au développeur.

## Situation (`rel_situation`)
**Groupe.** Dialogue et relation  
**Définition.** Le cadre dans lequel le signal apparaît.  
**Règles.** Les expériences de laboratoire (introspection, vecteurs d'émotion) ne trouvent pas encore de valeur exacte.  
**Fiabilité.** Non mesurée.  

Valeurs :
- **Entretien ou évaluation de bien-être** : 
- **Tâche** : 
- **Conversation ordinaire** : 
- **Jeu de rôle ou compagnon** : 
- **Conversation entre IA** : 
- **Étude sur de nombreuses conversations** : 

## Personne concernée (`rel_concerne`)
**Groupe.** Dialogue et relation  
**Définition.** De qui parle le cas : le modèle, l'utilisateur, ou les deux.  
**Fiabilité.** Non mesurée.  

Valeurs :
- **Le modèle** : 
- **L'utilisateur** : 
- **Les deux** : 
