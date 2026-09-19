import json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from guides_b import PROB, CODE, REF, OPT
OUT = '/mnt/user-data/outputs/seis201-guides'
os.makedirs(OUT, exist_ok=True)
tpl = open(os.path.join(os.path.dirname(__file__), 'guide_template.html')).read()
files = {'probability-and-sampling': PROB, 'code-reading-primer': CODE, 'engineering-reference-cards': REF, 'optional-concepts': OPT}
def h(s):
    x = 7
    for c in s: x = (x*31 + ord(c)) % 65521
    return format(x, '04X')
for name, g in files.items():
    n = sum(len(s.get('qs', [])) for s in g['steps'])
    js = json.dumps(g, ensure_ascii=False).replace('</', '<\\/')
    out = tpl.replace('/*TITLE*/', g['title']).replace('/*GUIDE*/{}', js)
    open(f'{OUT}/{name}.html', 'w').write(out)
    print(name, n, 'questions', round(len(out)/1024), 'KB')
