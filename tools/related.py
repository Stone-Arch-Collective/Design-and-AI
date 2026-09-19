import csv, re, json, collections
P='/mnt/user-data/outputs/seis201-learning-graph-v2/'
defs={int(r['ConceptID']):r for r in csv.DictReader(open(P+'definitions.csv'))}
sched={int(r['ConceptID']):r for r in csv.DictReader(open(P+'concept-schedule.csv'))}
graph={int(r['ConceptID']):r for r in csv.DictReader(open(P+'learning-graph.csv'))}
deps={i:set(int(x) for x in graph[i]['Dependencies'].split('|') if x) for i in graph}
kids=collections.defaultdict(set)
for i,d in deps.items():
    for p in d: kids[p].add(i)
STOP=set('a an the of to in on for and or is are be by with that this it its as at from so such than when where which who how into not no can will may their they them there has have been being was were ai data basics basic using use versus'.split())
def toks(s): return {w.rstrip('s') for w in re.sub('[^a-z ]',' ',s.lower()).split() if len(w)>2 and w not in STOP}
LT={i:toks(defs[i]['ConceptLabel']) for i in defs}; DT={i:toks(defs[i]['Definition']) for i in defs}
# truly-overlapping pairs (either could be defended as the answer): never shown together
CONF=[(107,133),(86,118),(31,136),(31,147),(49,147),(50,51),(55,159),(76,143),(144,155),(60,61),(38,101),(75,142),(37,67),(103,106),(119,120),(54,159),(53,159)]
CS={tuple(sorted(p)) for p in CONF}
# hand clusters: concepts a student would genuinely mix up
CL=[[33,34,35,37,67,21],[36,52,65,66],[67,68,69,70,71],[44,45,46,47,48],[56,57,58,59,60,61],[50,51,53,54,55,62],[19,20,22,23,24,63],[14,15,17,18,16],[13,14,15,25,38],[27,28,29,30,62],[38,39,40,41,75,76],[93,95,96,94,97,98],[99,102,103,104,105,106],[107,108,109,110,111,112],[113,114,115,121,122],[81,82,83,84,85,86],[42,43,72,73],[77,78,79,80],[123,124,125,126,127,128],[137,138,139,140,141],[142,143,144,145,146],[148,149,150,151,133],[152,153,154,155,156],[157,158,159,160,161,162,163],[116,117,118,119,120],[87,88,89,90],[129,130,131,132,134,135,136],[1,2,3,4,5],[6,7,8],[9,10],[11,29]]
cl=collections.defaultdict(set)
for c in CL:
    for a in c:
        for b in c:
            if a!=b: cl[a].add(b)
def score(t,c):
    s=0
    if c in deps[t] or c in kids[t]: s+=4
    sib=len(deps[t]&deps[c]); 
    if sib: s+=1.5+0.5*min(sib,3)
    two=set().union(*[deps[x] for x in deps[t]]) if deps[t] else set()
    if c in two or t in set().union(*[deps[x] for x in deps[c]]) if deps[c] else False: s+=1.5
    if sched[t]['Meeting']==sched[c]['Meeting']: s+=2
    if graph[t]['TaxonomyID']==graph[c]['TaxonomyID']: s+=1.5
    s+=2*len(LT[t]&LT[c])
    s+=min(2,0.5*len(DT[t]&DT[c]))
    if c in cl[t]: s+=6
    return s
rel={}
for t in defs:
    cs=[(score(t,c),c) for c in defs if c!=t and tuple(sorted((t,c))) not in CS]
    cs.sort(key=lambda x:(-x[0],x[1]))
    rel[t]=[c for s,c in cs[:14]]
if __name__=='__main__':
    L={i:defs[i]['ConceptLabel'] for i in defs}
    for t in [33,36,43,46,57,68,71,80,88,96,104,110,123,131,140,153,161,25,29,42,9,2]:
        print(f'{t} {L[t]}  ->  '+' | '.join(L[c] for c in rel[t][:8]))
    json.dump(rel,open('rel.json','w'))
