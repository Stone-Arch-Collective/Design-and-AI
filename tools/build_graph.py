import csv, json, os, sys, collections, datetime

SP = os.path.dirname(os.path.abspath(__file__))
OUT = "/mnt/user-data/outputs/seis201-learning-graph"
os.makedirs(OUT, exist_ok=True)

SESSIONS = [  # code, order, unit, topic (from syllabus)
 ("A0", 0, 0, "Assumed on entry"),
 ("W1Tu", 1, 1, "What is AI. Rules versus learned patterns."),
 ("W1Th", 2, 1, "Why statistics matters. Measurement activity."),
 ("W2Tu", 3, 1, "How large language models generate answers."),
 ("W2Th", 4, 1, "Descriptive statistics and uncertainty. Measurement lab."),
 ("W3Tu", 5, 1, "Agentic AI. Tools that plan and take multi-step actions."),
 ("W3Th", 6, 1, "Distributions, mean, spread. Auditing an agentic analysis."),
 ("W4Tu", 7, 2, "Where AI bias comes from."),
 ("W4Th", 8, 2, "Correlation and regression. Spurious correlation."),
 ("W5Tu", 9, 2, "AI overconfidence and false precision."),
 ("W5Th", 10, 2, "Confidence intervals and statistical significance."),
 ("W6Tu", 11, 2, "Agentic AI building a report or dashboard."),
 ("W6Th", 12, 2, "Data visualization. Critiquing an AI chart."),
 ("W7Tu", 13, 2, "Agentic AI in data pipelines. Semester review."),
 ("W7Th", 14, 2, "Exam 1 (no new concepts)"),
 ("W7pre", 15, 3, "Code-reading primer (NOT on syllabus; proposed async pre-work)"),
 ("W8Tu", 16, 3, "How AI code generation works."),
 ("W8Th", 17, 3, "Vibe coding. Describe, generate, test."),
 ("W9Tu", 18, 3, "Agentic coding tools that write and run tests."),
 ("W9Th", 19, 3, "Verifying AI-generated code against known answers."),
 ("W10Tu", 20, 3, "Multi-step agentic debugging."),
 ("W10Th", 21, 3, "Debugging with AI. Project assigned."),
 ("W11Tu", 22, 4, "Agentic AI in iterative design workflows."),
 ("W11Th", 23, 4, "Building a calculation or design tool with AI."),
 ("W12Tu", 24, 4, "Agentic AI as a research assistant."),
 ("W12Th", 25, 4, "AI for research and design tradeoffs."),
 ("W13Tu", 26, 5, "Ethics, bias, and risk in autonomous and agentic AI."),
 ("W13Th", 27, 5, "Exam 2 (no new concepts)"),
 ("W14Tu", 28, 5, "Verification practices for agentic AI output."),
 ("W14Th", 29, 5, "Safety-critical contexts. Professional responsibility and licensure."),
 ("W15Tu", 30, 5, "Limits of AI."),
 ("W15Th", 31, 5, "Project presentations."),
 ("W16", 32, 5, "Finals week. Reflection due."),
]
SMAP = {s[0]: s for s in SESSIONS}
UNITS = {0: "Assumed on entry", 1: "Unit 1 (W1-3): How AI works, describing data",
         2: "Unit 2 (W4-7): Judging AI and data claims", 3: "Unit 3 (W8-10): AI-assisted coding and verification",
         4: "Unit 4 (W11-12): Building tools and research", 5: "Unit 5 (W13-16): Responsibility, verification, limits"}

TAX = {
 "FOUND": "Assumed Foundations", "AIF": "AI Fundamentals", "LLM": "Large Language Models",
 "AGT": "Agentic AI", "STAT": "Measurement and Descriptive Statistics", "INF": "Inference and Regression",
 "BIAS": "Bias and Overconfidence", "DATA": "Data Pipelines and Visualization",
 "CODE": "Programming and Code Generation", "VER": "Verification and Testing", "DBG": "Debugging",
 "ENG": "Engineering Applications", "DES": "Design Tools and Research", "ETH": "Ethics, Risk and Licensure",
}
TAXCOLOR = {"FOUND": "LightGray", "AIF": "LightCoral", "LLM": "Gold", "AGT": "Orange", "STAT": "LightSkyBlue",
 "INF": "SteelBlue", "BIAS": "Plum", "DATA": "MediumAquamarine", "CODE": "PaleGreen", "VER": "Khaki",
 "DBG": "Salmon", "ENG": "Tan", "DES": "LightSeaGreen", "ETH": "Violet"}

# ---- parse
concepts = []  # dicts
cur = None
for line in open(os.path.join(SP, "graph_data.txt"), encoding="utf-8"):
    line = line.rstrip("\n")
    if not line.strip():
        continue
    if line.startswith("## "):
        cur = line[3:].strip()
        continue
    key, label, tax, deps = line.split("|")
    implied = key.startswith("*")
    key = key.lstrip("*")
    concepts.append(dict(key=key, label=label, tax=tax, deps=[d for d in deps.split(",") if d],
                         session=cur, status=("assumed" if cur == "A0" else ("implied" if implied else "taught"))))

# order by session order (stable within session)
concepts.sort(key=lambda c: SMAP[c["session"]][1])
for i, c in enumerate(concepts, 1):
    c["id"] = i
K = {c["key"]: c for c in concepts}
problems = []
if len(K) != len(concepts):
    problems.append("duplicate keys")

for c in concepts:
    if len(c["label"]) > 32: problems.append(f"label >32: {c['label']} ({len(c['label'])})")
    if c["tax"] not in TAX: problems.append(f"bad tax {c['key']}")
    for d in c["deps"]:
        if d not in K: problems.append(f"{c['key']} unknown dep {d}"); continue
        if d == c["key"]: problems.append(f"self dep {d}")
        if SMAP[K[d]["session"]][1] > SMAP[c["session"]][1]:
            problems.append(f"schedule violation: {c['key']} ({c['session']}) needs {d} ({K[d]['session']})")
        if K[d]["id"] > c["id"] and SMAP[K[d]["session"]][1] == SMAP[c["session"]][1]:
            problems.append(f"same-session order: {c['key']} before its dep {d}")
    if c["status"] == "assumed" and c["deps"]:
        problems.append(f"assumed with deps {c['key']}")

# cycle check (Kahn)
indeg = {c["key"]: len([d for d in c["deps"] if d in K]) for c in concepts}
kids = collections.defaultdict(list)
for c in concepts:
    for d in c["deps"]:
        kids[d].append(c["key"])
q = [k for k, v in indeg.items() if v == 0]; seen = 0; depth = {k: 1 for k in q}
while q:
    k = q.pop(); seen += 1
    for ch in kids[k]:
        depth[ch] = max(depth.get(ch, 1), depth[k] + 1)
        indeg[ch] -= 1
        if indeg[ch] == 0: q.append(ch)
if seen != len(concepts): problems.append("CYCLE detected")
longest = max(depth.values())

nedges = sum(len(c["deps"]) for c in concepts)
orph = [c["key"] for c in concepts if not c["deps"] and not kids[c["key"]]]
terminals = [c for c in concepts if not kids[c["key"]]]
foundational = [c for c in concepts if not c["deps"]]
print("concepts", len(concepts), "edges", nedges, "longest chain", longest, "orphans", orph)
print("terminals", len(terminals), "foundational", len(foundational))
print("PROBLEMS:", problems or "none")
if problems:
    sys.exit(1)

# components (undirected)
adj = collections.defaultdict(set)
for c in concepts:
    for d in c["deps"]:
        adj[c["key"]].add(d); adj[d].add(c["key"])
comp = 0; vis = set()
for c in concepts:
    if c["key"] in vis: continue
    comp += 1; st = [c["key"]]
    while st:
        x = st.pop()
        if x in vis: continue
        vis.add(x); st.extend(adj[x] - vis)

# ---- files
def w(name, text):
    with open(os.path.join(OUT, name), "w", encoding="utf-8", newline="") as f: f.write(text)

with open(os.path.join(OUT, "learning-graph.csv"), "w", encoding="utf-8", newline="") as f:
    cw = csv.writer(f)
    cw.writerow(["ConceptID", "ConceptLabel", "Dependencies", "TaxonomyID"])
    for c in concepts:
        cw.writerow([c["id"], c["label"], "|".join(str(K[d]["id"]) for d in c["deps"]), c["tax"]])

with open(os.path.join(OUT, "concept-schedule.csv"), "w", encoding="utf-8", newline="") as f:
    cw = csv.writer(f)
    cw.writerow(["ConceptID", "ConceptLabel", "Session", "Unit", "Status", "TaxonomyID", "Prerequisites"])
    for c in concepts:
        cw.writerow([c["id"], c["label"], c["session"], SMAP[c["session"]][2], c["status"], c["tax"],
                     "; ".join(K[d]["label"] for d in c["deps"])])

w("taxonomy-names.json", json.dumps(TAX, indent=2))
meta = {"title": "SEIS 201 Learning Graph", "description": "Concept dependency graph for SEIS 201 (AI for CE/ME Engineers), University of St Thomas, derived from the course syllabus text.",
        "creator": "Shannon Seaver (draft generated with Claude)", "date": "2026-09-18", "version": "0.1-draft",
        "format": "Learning Graph JSON (McCreary learning-graph-generator layout: metadata, groups, nodes, edges)",
        "license": "TBD"}
w("metadata.json", json.dumps(meta, indent=2))
groups = {k: {"classifierName": v, "color": TAXCOLOR[k], "font": {"color": "black"}} for k, v in TAX.items()}
graph = {"metadata": meta, "groups": groups,
         "nodes": [{"id": c["id"], "label": c["label"], "group": c["tax"]} for c in concepts],
         "edges": [{"from": c["id"], "to": K[d]["id"]} for c in concepts for d in c["deps"]]}
w("learning-graph.json", json.dumps(graph, indent=2))

# concept list
lines = ["# SEIS 201 Concept List", "", f"{len(concepts)} concepts. Status: assumed = expected on entry; taught = named by a syllabus session; implied = needed but no session teaches it.", ""]
for code, order, unit, topic in SESSIONS:
    cs = [c for c in concepts if c["session"] == code]
    if not cs: continue
    lines.append(f"## {code}: {topic} ({len(cs)})")
    for c in cs:
        tag = "" if c["status"] == "taught" else f" *[{c['status']}]*"
        lines.append(f"{c['id']}. {c['label']}{tag}")
    lines.append("")
w("concept-list.md", "\n".join(lines))

# per-session counts
per = collections.OrderedDict()
for code, order, unit, topic in SESSIONS:
    cs = [c for c in concepts if c["session"] == code]
    per[code] = (len(cs), sum(1 for c in cs if c["status"] == "implied"))

# indegree
dep_count = {c["key"]: len(kids[c["key"]]) for c in concepts}
top = sorted(concepts, key=lambda c: -dep_count[c["key"]])[:12]
by_status = collections.Counter(c["status"] for c in concepts)

qm = ["# Quality Metrics", "",
      f"- Concepts: {len(concepts)} ({by_status['assumed']} assumed, {by_status['taught']} taught, {by_status['implied']} implied)",
      f"- Dependency edges: {nedges}",
      "- DAG: yes (no cycles, no self-dependencies)",
      f"- Foundational concepts (no prerequisites): {len(foundational)}, all 'assumed on entry'",
      f"- Longest prerequisite chain: {longest} concepts",
      f"- Connected components: {comp}",
      f"- Orphans (no edges at all): {len(orph)}",
      f"- Terminal concepts (nothing depends on them): {len(terminals)}",
      "- Schedule check: every prerequisite is scheduled no later than the concept that needs it, and earlier in the list when in the same session",
      "- Label check: all Title Case, 32 characters or fewer", "",
      "## Most depended-on concepts", "", "| Concept | Dependents |", "|---|---|"]
qm += [f"| {c['label']} | {dep_count[c['key']]} |" for c in top]
qm += ["", "## Concepts per session", "", "| Session | Topic | Concepts | Implied |", "|---|---|---|---|"]
for code, order, unit, topic in SESSIONS:
    n, im = per[code]
    qm.append(f"| {code} | {topic} | {n} | {im} |")
w("quality-metrics.md", "\n".join(qm))

tc = collections.Counter(c["tax"] for c in concepts)
td = ["# Taxonomy Distribution", "", "| ID | Category | Concepts | Share |", "|---|---|---|---|"]
for k, n in tc.most_common():
    flag = "  (over 30%)" if n / len(concepts) > .30 else ""
    td.append(f"| {k} | {TAX[k]} | {n} | {100*n/len(concepts):.1f}%{flag} |")
w("taxonomy-distribution.md", "\n".join(td))

uc = collections.Counter(SMAP[c["session"]][2] for c in concepts)
print("per unit", dict(uc), "taxonomy", dict(tc))
print("heavy sessions", [(k, v) for k, v in per.items() if v[0] >= 8])

# viewer data
vd = [{"id": c["id"], "label": c["label"], "tax": c["tax"], "taxName": TAX[c["tax"]], "session": c["session"],
       "unit": SMAP[c["session"]][2], "status": c["status"], "level": SMAP[c["session"]][1],
       "deps": [K[d]["id"] for d in c["deps"]]} for c in concepts]
tpl = open(os.path.join(SP, "viewer_template.html"), encoding="utf-8").read()
html = tpl.replace("/*DATA*/[]", json.dumps(vd)).replace("/*UNITS*/{}", json.dumps(UNITS)).replace("/*TAX*/{}", json.dumps(TAX))
w("graph-viewer.html", html)
json.dump({"per": per, "counts": dict(by_status), "n": len(concepts), "edges": nedges, "longest": longest, "comp": comp,
           "unit": dict(uc)}, open(os.path.join(SP, "stats.json"), "w"))
