#!/usr/bin/env python3
"""Prépare les lots hebdomadaires pour les bots Grok de l'OCAIA.
Usage : python3 grok_lots.py <dossier_incidents> <dossier_codebook> <fichier_lots_precedents.json|-> <dossier_sortie> <AAAA-MM-JJ>
Écrit dans <dossier_sortie> : grille.json, lot-relecture.json, lot-verification.json (publics)
et correspondance.json (PRIVÉ : ne jamais publier ; à enregistrer dans la collection grok_lots)."""
import json, glob, os, re, sys, random, datetime
inc_dir, cb_dir, prev_path, out, today = sys.argv[1:6]
R = []
for f in glob.glob(os.path.join(inc_dir, '*.json')):
    d = json.load(open(f)); d = d.get('data', d) if isinstance(d, dict) and 'data' in d and isinstance(d['data'], dict) else d
    R.append(d)
prev = {'relecture': set(), 'verification': set()}
if prev_path != '-' and os.path.exists(prev_path):
    for lot in json.load(open(prev_path)):
        prev['relecture'] |= set(lot.get('relecture', {}).values()); prev['verification'] |= set(lot.get('verification', []))
y, w, _ = datetime.date.fromisoformat(today).isocalendar(); lot = f"{y}-S{w:02d}"
random.seed(lot)
VARS = ['direction', 'sert_tache', 'rapport_action', 'regard_autrui', 'declencheur']
grille = {'variables': []}
for v in VARS:
    c = json.load(open(os.path.join(cb_dir, v + '.json'))); c = c.get('data', c)
    vals = c.get('valeurs') or []
    vals = [x.get('v') if isinstance(x, dict) else x for x in vals]
    defs = {x.get('v'): x.get('def', '') for x in (c.get('valeurs') or []) if isinstance(x, dict)}
    grille['variables'].append({'variable': v, 'libelle': c.get('libelle'), 'definition': c.get('definition'), 'regles': c.get('regles'), 'valeurs': vals, 'definitions_valeurs': defs})
NAMES = r"Claude|Opus|Sonnet|Haiku|Fable|Mythos|GPT[-\w.]*|ChatGPT|Codex|o1(-preview)?|o3|o4|Astra|Sol|Terra|Luna|Gemini|Bard|Antigravity|Argon|Carbon|Hydrogen|Grok|Llama|Muse( Spark)?|DeepSeek|Qwen|Kimi|GLM[-\w.]*|Mistral|Inkling|Cursor|Composer|Copilot|Replit|Kiro|OpenClaw|Operator|Cowork"
ORGS = r"Anthropic|OpenAI|Google DeepMind|DeepMind|Google|xAI|Meta|Microsoft|Amazon|AWS|Alibaba|Moonshot|Zhipu|Apollo Research|Apollo|METR|AISI|UK AISI|CAISI|Palisade|Andon Labs|Transluce|Irregular|Redwood|Goodfire|Eleos|Vals AI|Trajectory Labs|Epoch AI"
def mask(t):
    t = re.sub(r'\b(' + ORGS + r')\b', '[organisation]', t or '')
    t = re.sub(r'\b(' + NAMES + r')(\s?[\d.]+\w*)?\b', '[modèle]', t)
    return t
ag = [r for r in R if (r.get('domaine') or 'Agent') != 'Dialogue et relation' and r.get('id')]
cand = [r for r in ag if not any(k.startswith('codages_') for k in r) and r['id'] not in prev['relecture'] and (r.get('fait_documente') or r.get('resume'))]
an = [r for r in cand if r.get('lab') == 'Anthropic']; ot = [r for r in cand if r.get('lab') != 'Anthropic']
random.shuffle(an); random.shuffle(ot)
pick = an[:12] + ot[:13]; random.shuffle(pick)
corr = {}; fiches = []
for i, r in enumerate(pick, 1):
    code = f"G{lot[2:4]}{lot[-2:]}-{i:02d}"; corr[code] = r['id']
    fiches.append({'code': code, 'texte': mask(r.get('fait_documente') or r.get('resume')), 'contexte': r.get('contexte', '')})
ver = [r for r in R if r.get('verification') == 'À vérifier' and r.get('source') and r['id'] not in prev['verification']]
ver.sort(key=lambda r: r.get('ajoute_le', ''))
ver = ver[:30]
os.makedirs(out, exist_ok=True)
json.dump(grille, open(os.path.join(out, 'grille.json'), 'w'), ensure_ascii=False, indent=1)
json.dump({'lot': lot, 'prepare_le': today, 'consigne': "Relecture à l'aveugle : coder chaque fiche avec la grille (grille.json), sans chercher le cas en ligne ni sur le site de l'OCAIA.", 'fiches': fiches}, open(os.path.join(out, 'lot-relecture.json'), 'w'), ensure_ascii=False, indent=1)
json.dump({'lot': lot, 'prepare_le': today, 'fiches': [{'id': r['id'], 'titre': r.get('cas', ''), 'date_publication': r.get('date_pub', ''), 'source': r.get('source', ''), 'resume': r.get('resume', '')} for r in ver]}, open(os.path.join(out, 'lot-verification.json'), 'w'), ensure_ascii=False, indent=1)
json.dump({'lot': lot, 'date': today, 'relecture': corr, 'verification': [r['id'] for r in ver]}, open(os.path.join(out, 'correspondance.json'), 'w'), ensure_ascii=False, indent=1)
print(lot, len(fiches), 'fiches à relire,', len(ver), 'à vérifier')
