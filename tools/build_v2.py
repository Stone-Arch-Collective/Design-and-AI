import csv, json, os, sys, collections, datetime as dt

SP = os.path.dirname(os.path.abspath(__file__))
OUT = "/mnt/user-data/outputs/seis201-learning-graph-v2"
os.makedirs(OUT, exist_ok=True)

# ---------- calendar: Spring 2027, Tue/Thu, classes Feb 1 - May 14, no class Mar 22-29
days = []
x = dt.date(2027, 2, 1)
while x <= dt.date(2027, 5, 14):
    if x.weekday() in (1, 3) and not (dt.date(2027, 3, 22) <= x <= dt.date(2027, 3, 29)):
        days.append(x)
    x += dt.timedelta(1)
assert len(days) == 28
TOPIC = {1: "What is AI. Rules versus learned patterns", 2: "Why statistics matters. Measurement activity",
 3: "How LLMs generate answers (+ probability basics)", 4: "Descriptive statistics. Measurement lab",
 5: "Agentic AI", 6: "Distributions. Auditing an agent's analysis", 7: "Where AI bias comes from",
 8: "Correlation and regression. Spurious correlation", 9: "Overconfidence and false precision (+ sampling)",
 10: "Confidence intervals and significance", 11: "Agentic dashboards", 12: "Data visualization. Critiquing AI charts (+ Exam 1 review)",
 13: "Agentic data pipelines", 14: "EXAM 1 (75-minute applied practical)", 15: "How AI code generation works",
 16: "Vibe coding (announce project options)", 17: "Agentic coding. AI-written tests", 18: "Verifying AI code against known answers",
 19: "Multi-step agentic debugging", 20: "Debugging with AI. Project assigned", 21: "Iterative design workflows",
 22: "Building a calculation or design tool", 23: "AI as research assistant and design partner (old W12 merged)",
 24: "Ethics, bias and risk in autonomous AI", 25: "Verification practices for agentic output",
 26: "Safety-critical work. Licensure and responsibility", 27: "Limits of AI (project due)", 28: "Project presentations"}
SESS = {"A0": (0, 0, "Expected on entry or lab-supplied")}
for n in range(1, 29):
    unit = 1 if n <= 6 else 2 if n <= 14 else 3 if n <= 20 else 4 if n <= 23 else 5
    SESS[f"M{n:02d}"] = (2 * n, unit, f"{days[n-1].strftime('%a %b %-d')}: {TOPIC[n]}")
SESS["ASYNC"] = (27, 3, "Async code-reading module (assigned M12, due before M15)")
SESS["FINALS"] = (58, 5, "Finals week May 17-21: Exam 2 + reflection")
UNITS = {0: "Expected on entry / lab-supplied", 1: "Unit 1 (Feb 2-18): How AI works, describing data",
         2: "Unit 2 (Feb 23-Mar 18): Judging AI and data claims", 3: "Unit 3 (Mar 30-Apr 15): AI-assisted coding and verification",
         4: "Unit 4 (Apr 20-27): Building tools and research", 5: "Unit 5 (Apr 29-finals): Responsibility, verification, limits"}
OLD2NEW = {"W1Tu": "M01", "W1Th": "M02", "W2Tu": "M03", "W2Th": "M04", "W3Tu": "M05", "W3Th": "M06", "W4Tu": "M07", "W4Th": "M08",
 "W5Tu": "M09", "W5Th": "M10", "W6Tu": "M11", "W6Th": "M12", "W7Tu": "M13", "W7pre": "ASYNC", "W8Tu": "M15", "W8Th": "M16",
 "W9Tu": "M17", "W9Th": "M18", "W10Tu": "M19", "W10Th": "M20", "W11Tu": "M21", "W11Th": "M22", "W12Tu": "M23", "W12Th": "M23",
 "W13Tu": "M24", "W14Tu": "M25", "W14Th": "M26", "W15Tu": "M27", "W15Th": "M28", "W16": "FINALS", "A0": "A0"}
MOVE = {"randsample": "M09", "sampvar": "M09"}   # sampling moves ahead of the CI session, into space freed in M09

TAX = {"FOUND": "Assumed Foundations", "AIF": "AI Fundamentals", "LLM": "Large Language Models", "AGT": "Agentic AI",
 "STAT": "Measurement and Descriptive Statistics", "INF": "Inference and Regression", "BIAS": "Bias and Overconfidence",
 "DATA": "Data Pipelines and Visualization", "CODE": "Programming and Code Generation", "VER": "Verification and Testing",
 "DBG": "Debugging", "ENG": "Engineering Applications", "DES": "Design Tools and Research", "ETH": "Ethics, Risk and Licensure"}
TAXCOLOR = {"FOUND": "LightGray", "AIF": "LightCoral", "LLM": "Gold", "AGT": "Orange", "STAT": "LightSkyBlue", "INF": "SteelBlue",
 "BIAS": "Plum", "DATA": "MediumAquamarine", "CODE": "PaleGreen", "VER": "Khaki", "DBG": "Salmon", "ENG": "Tan", "DES": "LightSeaGreen", "ETH": "Violet"}

# ---------- decisions
MERGE = {"modelio": "ml", "whystat": "meas", "precvsacc": "syserr", "token": "llm", "variance": "sd", "dashmetrics": "dashboard",
 "confounder": "spurious", "pvalue": "sigtest", "iterate": "dgtloop", "testrun": "unittest", "loadcase": "multiload",
 "sourcequality": "citation", "fabref": "citation", "objfunc": "tradeoff", "pestamp": "pe", "traceability": "docverif",
 "physgap": "tacit", "codemiss": "missedfailure", "codepred": "codegen", "codetrain": "codegen", "datatype": "variable",
 "importlib": "function", "loop": "conditional"}
EXAMPLE = ["damagemodel", "cylstrength", "fatiguedata", "yieldcoupon", "mixdesign", "fatiguelife", "flagdraft", "beamdefl", "deflcalc",
 "cantilever", "calccode", "truss", "gearratio", "wallmodel", "simplemodel", "bracket", "footing", "hx", "materialsel", "wtstrength",
 "costenergy", "selfmonitor", "designchange", "beamsize", "hvacload", "geardesign", "spectrum", "freq", "thermalres", "fos"]
OPTIONAL = ["calib", "multireg", "ctxwin", "logaxis", "staledata", "sensitivity", "tradeoffunc", "stdcare", "corroborate", "ethicscode"]
CUT = ["techcomm", "presentverif", "statelimits", "defend"]
RELABEL = {"syserr": "Systematic Error and Accuracy", "variable": "Variables and Data Types", "function": "Functions and Imports",
 "conditional": "Conditionals and Loops", "sd": "Variance and Standard Deviation", "llm": "Large Language Models and Tokens",
 "citation": "Citation and Source Verification", "tradeoff": "Design Tradeoff and Objectives", "pe": "Licensure and the PE Stamp",
 "tacit": "Tacit Knowledge and Physics Gaps", "missedfailure": "Missed Failure Modes and Codes", "docverif": "Documenting and Tracing Checks",
 "unittest": "Unit Tests and Test Runner", "dashboard": "Dashboard and Metrics", "sigtest": "Significance and P-Values",
 "codegen": "AI Code Generation Internals", "spurious": "Spurious Correlation", "meas": "Measurement and Why It Matters",
 "ml": "Machine Learning", "dgtloop": "Describe-Generate-Test Loop"}
SUPPLIED = ["eqbal", "stressstrain", "beambend"]
FILLED = {"prob": "hole: probability", "sampvspop": "hole: sampling", "randsample": "hole: sampling", "sampvar": "hole: sampling",
 "se": "hole: sampling", "tmult": "hole: sampling"}
PRIMER = ["variable", "function", "conditional", "traceback"]   # after merges

# ---------- parse v0.1
old = []
cur = None
for line in open(os.path.join(SP, "graph_data.txt"), encoding="utf-8"):
    line = line.rstrip("\n")
    if not line.strip(): continue
    if line.startswith("## "): cur = line[3:].strip(); continue
    key, label, tax, deps = line.split("|")
    imp = key.startswith("*"); key = key.lstrip("*")
    old.append(dict(key=key, label=label, tax=tax, deps=[d for d in deps.split(",") if d], session=cur, implied=imp))
OK = {c["key"]: c for c in old}
assert len(OK) == 230

disp = {}   # key -> (disposition, target/reason)
def resolve(k):
    while k in MERGE: k = MERGE[k]
    return k
dropped = set(EXAMPLE) | set(OPTIONAL) | set(CUT)
for k in OK:
    if k in MERGE: disp[k] = ("merged", OK[MERGE[k]]["label"] if MERGE[k] in OK else MERGE[k])
    elif k in EXAMPLE: disp[k] = ("lab example (not a graded concept)", "")
    elif k in OPTIONAL: disp[k] = ("optional / cut", "")
    elif k in CUT: disp[k] = ("cut (assessment skill, not a concept)", "")
    elif k in SUPPLIED: disp[k] = ("lab-supplied reference card", "")
    elif k in FILLED: disp[k] = ("kept: hole filled and taught", FILLED[k])
    elif OK[k]["session"] == "W7pre": disp[k] = ("kept: async module", "")
    elif OK[k]["session"] == "A0": disp[k] = ("kept: expected on entry", "")
    else: disp[k] = ("kept: taught", "")

# expand deps of a node through drops (inherit) and merges
memo = {}
def eff_deps(k):
    """effective deps of kept node k, after merging and dropping"""
    out = []
    def visit(d):
        d = resolve(d)
        if d in dropped:
            for dd in OK[d]["deps"]: visit(dd)
        else:
            out.append(d)
    srcs = [k] + [m for m, t in MERGE.items() if resolve(m) == k]   # merged nodes contribute their deps
    for s in srcs:
        for d in OK[s]["deps"]: visit(d)
    res = []
    for d in out:
        if d != k and d not in res: res.append(d)
    return res

kept = [c for c in old if c["key"] not in MERGE and c["key"] not in dropped]
newc = []
for c in kept:
    k = c["key"]
    if k in SUPPLIED or c["session"] == "A0": sess = "A0"
    elif k in MOVE: sess = MOVE[k]
    else:
        sess = OLD2NEW[c["session"]]
    # merged nodes may live in a different session: take earliest
    for m, t in MERGE.items():
        if resolve(m) == k:
            ms = OLD2NEW[OK[m]["session"]]
            if SESS[ms][0] < SESS[sess][0]: sess = ms
    status = ("supplied" if k in SUPPLIED else "assumed" if c["session"] == "A0" else "filled" if k in FILLED
              else "async" if sess == "ASYNC" else "taught")
    newc.append(dict(key=k, label=RELABEL.get(k, c["label"]), tax=c["tax"], deps=eff_deps(k), session=sess, status=status,
                     oldsession=c["session"]))
newc.sort(key=lambda c: SESS[c["session"]][0])
for i, c in enumerate(newc, 1): c["id"] = i
K = {c["key"]: c for c in newc}

# ---------- validate
problems = []
for c in newc:
    if len(c["label"]) > 32: problems.append(f"label>32 {c['label']} {len(c['label'])}")
    for d in c["deps"]:
        if d not in K: problems.append(f"{c['key']} dep missing {d}"); continue
        if SESS[K[d]["session"]][0] > SESS[c["session"]][0]:
            problems.append(f"schedule: {c['key']}@{c['session']} needs {d}@{K[d]['session']}")
        elif K[d]["id"] > c["id"]: problems.append(f"order {c['key']} before {d}")
kids = collections.defaultdict(list)
for c in newc:
    for d in c["deps"]: kids[d].append(c["key"])
indeg = {c["key"]: len(c["deps"]) for c in newc}
q = [k for k, v in indeg.items() if v == 0]; seen = 0; depth = {k: 1 for k in q}
while q:
    k = q.pop(); seen += 1
    for ch in kids[k]:
        depth[ch] = max(depth.get(ch, 1), depth[k] + 1); indeg[ch] -= 1
        if indeg[ch] == 0: q.append(ch)
if seen != len(newc): problems.append("CYCLE")
orph = [c["key"] for c in newc if not c["deps"] and not kids[c["key"]]]
print("concepts", len(newc), "edges", sum(len(c["deps"]) for c in newc), "longest", max(depth.values()), "orphans", orph)
print("PROBLEMS", problems or "none")
per = collections.OrderedDict((s, [c for c in newc if c["session"] == s]) for s in SESS)
print({s: len(v) for s, v in per.items() if v})
if problems: sys.exit(1)

# ---------- write
def wr(n, t): open(os.path.join(OUT, n), "w", encoding="utf-8", newline="").write(t)
with open(os.path.join(OUT, "learning-graph.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f); w.writerow(["ConceptID", "ConceptLabel", "Dependencies", "TaxonomyID"])
    for c in newc: w.writerow([c["id"], c["label"], "|".join(str(K[d]["id"]) for d in c["deps"]), c["tax"]])
with open(os.path.join(OUT, "concept-schedule.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f); w.writerow(["ConceptID", "ConceptLabel", "Meeting", "Unit", "Status", "TaxonomyID", "OldSession", "Prerequisites"])
    for c in newc:
        w.writerow([c["id"], c["label"], c["session"], SESS[c["session"]][1], c["status"], c["tax"], c["oldsession"],
                    "; ".join(K[d]["label"] for d in c["deps"])])
with open(os.path.join(OUT, "disposition-of-v01-concepts.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f); w.writerow(["V01Label", "V01Session", "Disposition", "Detail"])
    for c in old: w.writerow([c["label"], c["session"], disp[c["key"]][0], disp[c["key"]][1]])
meta = {"title": "SEIS 201 Learning Graph (Spring 2027 fit)", "description": "Concept dependency graph for SEIS 201 trimmed to the 28 Tue/Thu meetings of Spring 2027.",
        "creator": "Shannon Seaver (draft generated with Claude)", "date": "2026-09-18", "version": "0.2-draft",
        "format": "Learning Graph JSON (metadata, groups, nodes, edges; edges run dependent -> prerequisite)", "license": "TBD"}
wr("metadata.json", json.dumps(meta, indent=2)); wr("taxonomy-names.json", json.dumps(TAX, indent=2))
groups = {k: {"classifierName": v, "color": TAXCOLOR[k], "font": {"color": "black"}} for k, v in TAX.items()}
wr("learning-graph.json", json.dumps({"metadata": meta, "groups": groups,
   "nodes": [{"id": c["id"], "label": c["label"], "group": c["tax"]} for c in newc],
   "edges": [{"from": c["id"], "to": K[d]["id"]} for c in newc for d in c["deps"]]}, indent=2))

vd = [{"id": c["id"], "label": c["label"], "tax": c["tax"], "taxName": TAX[c["tax"]], "session": c["session"], "unit": SESS[c["session"]][1],
       "status": c["status"], "level": SESS[c["session"]][0], "deps": [K[d]["id"] for d in c["deps"]]} for c in newc]
tpl = open(os.path.join(SP, "viewer_template.html"), encoding="utf-8").read()
tpl = tpl.replace("d.status==='implied'", "(d.status==='filled'||d.status==='async')").replace("Implied (not taught)", "Added to fill a gap")
tpl = tpl.replace("Dashed outline = needed by the syllabus but not taught in any session.", "Dashed outline = added to fill a gap in the original syllabus.")
tpl = tpl.replace("Concept dependency graph built from the syllabus.", "Concept dependency graph trimmed to Spring 2027 (28 Tue/Thu meetings).")
tpl = tpl.replace("levelSeparation:260", "levelSeparation:240").replace("SEIS 201 learning graph<", "SEIS 201 learning graph, Spring 2027 fit<")
wr("graph-viewer.html", tpl.replace("/*DATA*/[]", json.dumps(vd)).replace("/*UNITS*/{}", json.dumps(UNITS)).replace("/*TAX*/{}", json.dumps(TAX)))

# concept list by meeting + calendar table
lines = ["# SEIS 201 concepts by meeting (Spring 2027 fit)", ""]
for s, cs in per.items():
    if not cs: continue
    lines.append(f"## {s}: {SESS[s][2]} ({len(cs)})")
    for c in cs:
        tag = "" if c["status"] == "taught" else f" *[{c['status']}]*"
        lines.append(f"- {c['label']}{tag}")
    lines.append("")
wr("concept-list.md", "\n".join(lines))
cal = ["| Meeting | Date | Topic | Concepts | Unit |", "|---|---|---|---|---|"]
for n in range(1, 29):
    s = f"M{n:02d}"; cal.append(f"| {n} | {days[n-1].strftime('%a %b %-d')} | {TOPIC[n]} | {len(per[s])} | {SESS[s][1]} |")
wr("calendar-table.md", "\n".join(cal))
by = collections.Counter(c["status"] for c in newc)
tc = collections.Counter(c["tax"] for c in newc)
print(dict(by), {k: round(100 * v / len(newc), 1) for k, v in tc.items()})
dc = collections.Counter(d[0] for d in disp.values()); print(dict(dc))
json.dump({"n": len(newc), "by": dict(by), "disp": dict(dc)}, open(os.path.join(SP, "stats2.json"), "w"))
