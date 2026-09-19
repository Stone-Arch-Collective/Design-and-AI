import csv, json, os
P='/mnt/user-data/outputs/seis201-learning-graph-v2/'
defs={int(r['ConceptID']):r for r in csv.DictReader(open(P+'definitions.csv'))}
sched={int(r['ConceptID']):r for r in csv.DictReader(open(P+'concept-schedule.csv'))}
tax=json.load(open(P+'taxonomy-names.json'))
assert set(defs)==set(sched)==set(range(1,164))
concepts=[dict(id=i,label=defs[i]['ConceptLabel'],**{'def':defs[i]['Definition']},tax=sched[i]['TaxonomyID'],unit=int(sched[i]['Unit'])) for i in range(1,164)]
units={0:dict(short='Before class',name='Expected on entry or lab-supplied'),
1:dict(short='Unit 1: How AI works',name='Unit 1 (Feb 2-18): How AI works, describing data'),
2:dict(short='Unit 2: Judging claims',name='Unit 2 (Feb 23-Mar 18): Judging AI and data claims'),
3:dict(short='Unit 3: AI coding',name='Unit 3 (Mar 30-Apr 15): AI-assisted coding and verification'),
4:dict(short='Unit 4: Building tools',name='Unit 4 (Apr 20-27): Building tools and research'),
5:dict(short='Unit 5: Responsibility',name='Unit 5 (Apr 29-finals): Responsibility, verification, limits')}
from related import rel, CONF
conf=CONF
data=dict(concepts=concepts,tax=tax,units=units,confusable=[list(c) for c in conf],rel={str(k):v[:12] for k,v in rel.items()})
out=open('game_template.html').read().replace('const DATA=/*DATA*/{};','const DATA='+json.dumps(data,ensure_ascii=False).replace('</','<\\/')+';')
os.makedirs('/mnt/user-data/outputs/seis201-games',exist_ok=True)
open('/mnt/user-data/outputs/seis201-games/vocab-lab.html','w').write(out)
print(len(out)//1024,'KB')
