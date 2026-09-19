from guides_a import *

# ---------- numeric checks ----------
RB = 12*2/6; RA = 12-RB; assert (RB,RA)==(4,8)
assert 20000/100==200 and 200/200000==0.001
M = 6*2/4; assert M==3.0
I = 40*80**3/12; sig = 3e6*40/I
assert abs(I-1706666.67)<1 and abs(sig-70.3125)<1e-3
assert abs(60-5e6*50/(50*100**3/12))<1e-6
R1=0.10/(0.7*10); R2=0.05/(0.04*10); Q=20/(R1+R2); assert abs(Q-143.6)<0.1
R3=0.0125/(0.16*10); R4=0.09/(0.04*10); Rt=R3+R4; Q2=25/Rt
assert abs(R4-0.225)<1e-9 and abs(Rt-0.2328125)<1e-9 and abs(Q2-107.38)<0.01
assert 250/70.3125>3.55 and abs(250/70.3125-3.5556)<1e-3
assert abs(1.1**3-1-0.331)<1e-9

REF = dict(code='REF', title='Engineering Reference Cards, Interactive', minutes=35,
intro='Five reference cards, one per idea: static equilibrium, stress and strain, beam bending, thermal resistance, and factor of safety. In the lab you will be handed the formulas. What matters is knowing what each symbol means, keeping the units straight, and sanity-checking the answer. Each card gives the formulas, one worked example, then practice. These are simplified: if your lab card differs from this guide, the lab card wins.',
footer=FOOT+' Formulas and numbers were checked by script but not by an engineering instructor.',
steps=[
dict(title='Card 1: Static equilibrium', body=
 '<p>If nothing is accelerating, the forces and turning effects balance.</p>'
 + card('formula','Formula card','<p style="margin:0"><code>&Sigma;F = 0</code> (up = down, left = right)<br><code>&Sigma;M = 0</code> about any point you choose<br>Simply supported beam, span L, point load P at distance a from the left support A:<br><code>R_B = P &times; a / L</code> and <code>R_A = P &minus; R_B</code><br>Sanity check: <code>R_A + R_B = P</code></p>')
 + card('worked','Worked example','<p style="margin:0">L = 4 m, P = 10 kN, a = 1 m. Moments about A: R_B &times; 4 = 10 &times; 1, so R_B = <b>2.5 kN</b>. Then R_A = 10 &minus; 2.5 = <b>7.5 kN</b>. The load is close to A, so A carries most of it.</p>'),
 qs=[
  num('L = 6 m, P = 12 kN at a = 2 m from A. What is R_B (kN)?',4,0.01,'R_B = 12 &times; 2 / 6 = 4 kN.',unit='kN',hint='R_B = P &times; a / L.'),
  num('Same beam. What is R_A (kN)?',8,0.01,'R_A = 12 &minus; 4 = 8 kN.',unit='kN',hint='R_A = P &minus; R_B.'),
  mc('When the load sits closer to support A, which support carries more?',['A','B','They always carry the same'],0,'The nearer support takes the larger share.'),
 ]),
dict(title='Card 2: Stress and strain', body=
 '<p>Stress is force spread over area. Strain is stretch as a fraction of original length.</p>'
 + card('formula','Formula card','<p style="margin:0"><code>&sigma; = F / A</code> (N/mm&sup2; = MPa)<br><code>&epsilon; = &Delta;L / L</code> (no units)<br><code>&sigma; = E &times; &epsilon;</code> (elastic range)<br><code>&Delta;L = F &times; L / (A &times; E)</code><br>Steel: E &asymp; 200 GPa = 200,000 MPa</p>')
 + card('worked','Worked example','<p style="margin:0">F = 20 kN = 20,000 N, A = 100 mm&sup2;: &sigma; = 20,000 / 100 = <b>200 MPa</b>. &epsilon; = 200 / 200,000 = <b>0.001</b>. For L = 2,000 mm, &Delta;L = 0.001 &times; 2,000 = <b>2 mm</b>.</p>'),
 qs=[
  num('F = 15 kN on A = 50 mm&sup2;. Stress in MPa?',300,0.5,'15,000 N / 50 mm&sup2; = 300 MPa.',unit='MPa',hint='Convert kN to N first: 15 kN = 15,000 N.'),
  num('Strain is 0.0015 on a 1.5 m bar (1,500 mm). Elongation in mm?',2.25,0.01,'&Delta;L = 0.0015 &times; 1,500 = 2.25 mm.',unit='mm',hint='&Delta;L = &epsilon; &times; L. Use consistent length units.'),
  num('Steel stressed to 150 MPa. What is the strain (E = 200,000 MPa)?',0.00075,0.00001,'&epsilon; = 150 / 200,000 = 0.00075.',hint='&epsilon; = &sigma; / E, both in MPa.'),
  mc('Force is in kN and area in mm&sup2;. To get MPa you should:',['Divide directly; the answer is already MPa','Convert kN to N (&times;1000) first, then divide by mm&sup2;','Multiply by the area','Convert mm&sup2; to m&sup2; only'],1,'N/mm&sup2; is MPa. kN/mm&sup2; would be off by a factor of 1,000.'),
 ]),
dict(title='Card 3: Beam bending', body=
 '<p>Bending puts the top and bottom surfaces of a beam in tension and compression. The maximum stress is at the outer edge.</p>'
 + card('formula','Formula card','<p style="margin:0">Simply supported beam, point load P at midspan: <code>M = P &times; L / 4</code><br>Rectangular section, width b and depth h: <code>I = b &times; h&sup3; / 12</code> and <code>c = h / 2</code><br>Max bending stress: <code>&sigma; = M &times; c / I</code><br>Use N&middot;mm and mm&#8308; to get MPa. 1 kN&middot;m = 1,000,000 N&middot;mm.</p>')
 + card('worked','Worked example','<p style="margin:0">P = 10 kN, L = 2 m, b = 50 mm, h = 100 mm. M = 10 &times; 2 / 4 = 5 kN&middot;m = 5,000,000 N&middot;mm. I = 50 &times; 100&sup3; / 12 = 4,166,667 mm&#8308;. c = 50 mm. &sigma; = 5,000,000 &times; 50 / 4,166,667 = <b>60 MPa</b>.</p>'),
 qs=[
  num('P = 6 kN at midspan, L = 2 m. Maximum moment in kN&middot;m?',3,0.01,'M = 6 &times; 2 / 4 = 3 kN&middot;m.',unit='kN&middot;m',hint='M = P &times; L / 4 with P in kN and L in m.'),
  num('Section b = 40 mm, h = 80 mm. What is I in mm&#8308;?',1706667,100,'I = 40 &times; 80&sup3; / 12 = 40 &times; 512,000 / 12 = 1,706,667 mm&#8308;.',unit='mm&#8308;',hint='80&sup3; = 512,000.'),
  num('Now the bending stress: M = 3,000,000 N&middot;mm, c = 40 mm, I = 1,706,667 mm&#8308;. &sigma; in MPa?',70.3,0.5,'&sigma; = 3,000,000 &times; 40 / 1,706,667 = 70.3 MPa.',unit='MPa',hint='&sigma; = M &times; c / I.'),
  mc('You double the depth h of a rectangular beam and keep everything else the same. The maximum bending stress becomes:',['Half','One quarter','The same','Double'],1,'I grows by 2&sup3; = 8 and c grows by 2, so &sigma; = M c / I changes by 2 / 8 = 1/4.',{0:'Depth enters I as h&sup3; and c as h.'}),
 ]),
dict(title='Card 4: Thermal resistance', body=
 '<p>Heat flow through layers works like current through resistors in series: the resistances add, and the same heat flow passes through every layer.</p>'
 + card('formula','Formula card','<p style="margin:0">Conduction through one layer: <code>R = L / (k &times; A)</code> in K/W. L = thickness (m), k = conductivity (W/m&middot;K), A = area (m&sup2;)<br>Layers in series: <code>R_total = R1 + R2 + ...</code><br>Heat flow: <code>Q = &Delta;T / R_total</code> in W</p>')
 + card('worked','Worked example','<p style="margin:0">A 10 m&sup2; wall: brick 0.10 m, k = 0.7; insulation 0.05 m, k = 0.04. R1 = 0.10 / (0.7 &times; 10) = 0.0143 K/W. R2 = 0.05 / (0.04 &times; 10) = 0.125 K/W. R_total = 0.1393 K/W. With &Delta;T = 20 K, Q = 20 / 0.1393 = <b>143.6 W</b>. The insulation is 90% of the resistance.</p>'),
 qs=[
  num('Fiberglass: L = 0.09 m, k = 0.04, A = 10 m&sup2;. R in K/W?',0.225,0.001,'R = 0.09 / (0.04 &times; 10) = 0.225 K/W.',unit='K/W',hint='R = L / (k &times; A).'),
  num('Add a gypsum board (L = 0.0125 m, k = 0.16, A = 10 m&sup2;) in series with that fiberglass. R_total in K/W?',0.2328,0.001,'Gypsum R = 0.0125 / 1.6 = 0.0078. Total = 0.0078 + 0.225 = 0.2328 K/W.',unit='K/W',hint='Compute the gypsum R, then add the fiberglass R.'),
  num('With &Delta;T = 25 K across that wall, what is Q in W?',107.4,0.5,'Q = 25 / 0.2328 = 107.4 W.',unit='W',hint='Q = &Delta;T / R_total.'),
  mc('Which layer controls the heat flow through a wall?',['The thickest','The one with the largest resistance','The one added first','All layers equally'],1,'In series, the largest resistance dominates. Here the fiberglass is about 97% of the total.'),
 ]),
dict(title='Card 5: Factor of safety', body=
 '<p>The factor of safety is how many times stronger the part is than the stress it sees.</p>'
 + card('formula','Formula card','<p style="margin:0"><code>FS = strength / actual stress</code> (use yield strength for ductile metals)<br><code>allowable stress = strength / FS_required</code><br>FS = 1.0 means no margin at all.</p>')
 + card('worked','Worked example','<p style="margin:0">Yield strength 250 MPa, actual stress 100 MPa: FS = 250 / 100 = <b>2.5</b>.</p>')
 + card('warn','What FS does not cover','<p style="margin:0">FS is only as good as the stress number. If the load is wrong, the model is wrong, or a unit is off by 1,000, a comfortable FS is false comfort.</p>'),
 qs=[
  num('Yield strength 350 MPa, actual stress 200 MPa. FS?',1.75,0.01,'350 / 200 = 1.75.',hint='FS = strength / stress.'),
  num('Yield strength 240 MPa and a required FS of 3. What is the allowable stress (MPa)?',80,0.1,'240 / 3 = 80 MPa.',unit='MPa',hint='allowable = strength / FS_required.'),
  num('Use the beam from Card 3: actual stress 70.3 MPa, yield strength 250 MPa. FS?',3.56,0.02,'250 / 70.3 = 3.56.',hint='FS = 250 / 70.3.'),
  mc('What does FS = 1.0 mean?',['Perfectly safe','The part is expected to be right at its strength limit, with no margin','The part is twice as strong as needed','The stress is zero'],1,'No margin for error in load, material, or model.'),
 ]),
])

# ---------- OPTIONAL ----------
OPT = dict(code='OPT', title='Optional Concepts: ten short cards', minutes=30,
intro='Ten ideas that were cut from the required Spring 2027 sequence to make the calendar fit. Each is a short card and one or two checks. Ask your instructor whether any of them appear in an assessment or project; this guide does not assume they do.',
footer=FOOT,
steps=[
dict(title='Calibration', body=
 '<p>Two meanings show up in this course. <b>Instrument calibration</b>: comparing a device to a known reference and correcting the difference. <b>Confidence calibration</b>: whether stated confidence matches how often you are right. Someone who says &ldquo;90% sure&rdquo; should be right about 90 times out of 100. (Confirm with your instructor which meaning the course uses.)</p>',
 qs=[mc('A scale reads 0.3 kg with nothing on it. What is the problem and the fix?',['Random noise; take more readings','A constant offset (bias); re-zero it or subtract 0.3 kg from every reading','The scale is too heavy','No problem'],1,'A constant error is bias. Averaging more readings will not remove it.'),
      mc('An AI assistant says it is &ldquo;90% sure&rdquo; on 20 answers and gets 12 right (60%). It is:',['Well calibrated','Overconfident','Underconfident'],1,'Stated confidence (90%) was higher than the hit rate (60%).')]),
dict(title='Multiple regression', body=
 '<p>Regression that predicts one outcome from <b>several</b> inputs at once, e.g. <code>y = 5 + 2&middot;x1 &minus; 3&middot;x2</code>. Each coefficient is the effect of that input <i>holding the others fixed</i>. Caution: if the inputs move together (say, temperature and humidity), the individual coefficients become unreliable even when the overall prediction is fine.</p>',
 qs=[num('For <code>y = 5 + 2&middot;x1 &minus; 3&middot;x2</code>, what is the predicted y when x1 = 4 and x2 = 1?',10,0.01,'5 + 2&times;4 &minus; 3&times;1 = 5 + 8 &minus; 3 = 10.',hint='Substitute both values and compute.'),
      mc('The coefficient +2 on x1 means:',['y always equals 2','Each +1 in x1 raises predicted y by 2 while x2 is held fixed','x1 causes y'],1,'Regression describes association holding other inputs fixed; it does not by itself prove cause.')]),
dict(title='Log scale', body=
 '<p>On a log axis, each gridline is <b>multiplied</b> (1, 10, 100, 1000), not added to. Equal distances mean equal <b>ratios</b>. Use it when values span orders of magnitude or when percentage change is what matters.</p>',
 qs=[mc('On a log axis with gridlines at 10 and 1000, a point visually halfway between them is about:',['500','100','505','50'],1,'Halfway in ratio terms: 10 &times; 10 = 100, then &times; 10 = 1000.'),
      mc('On a log axis, equal distances mean equal:',['Differences','Ratios (multiples)','Averages'],1,'Going from 1 to 10 is the same distance as 10 to 100.')]),
dict(title='Sensitivity analysis', body=
 '<p>Change one input at a time by a fixed percent and see how much the output moves. The inputs that move the output most are the ones to measure carefully and double-check. Example: beam deflection is proportional to L&sup3;, so a 10% change in length has an outsized effect.</p>',
 qs=[num('Deflection is proportional to L&sup3;. If L increases by 10%, by what percent does deflection increase?',33.1,0.5,'1.1&sup3; = 1.331, an increase of 33.1%.',unit='%',hint='Compute 1.1 &times; 1.1 &times; 1.1, then subtract 1.'),
      mc('The purpose of a sensitivity analysis is to:',['Prove the model is right','Find which inputs matter most so you check those first','Remove outliers'],1,'It ranks inputs by how much their uncertainty affects the result.')]),
dict(title='Standard of care', body=
 '<p>A professional standard, not a perfection standard: what a reasonably careful, competent engineer in the same field would do under similar circumstances. Using a tool, including AI, does not move responsibility off the engineer. (General information, not legal advice.)</p>',
 qs=[mc('The standard of care is best described as:',['Never making an error','What a reasonably careful engineer in that field would do in similar circumstances','Whatever the client accepts','Whatever the software vendor recommends'],1,'It is measured against peers, not against perfection.'),
      mc('You paste an AI-generated load calculation into a design without checking it, and it is wrong. Who is responsible?',['The AI vendor','The engineer who used it','No one'],1,'The engineer who signs or relies on the work owns the check.')]),
dict(title='Code of ethics', body=
 '<p>Professional societies publish codes; NSPE&rsquo;s is one example (ASCE and ASME are similar). Its fundamental canons include: hold paramount the safety, health, and welfare of the public; perform services only in areas of competence; issue public statements only in an objective and truthful manner; act as faithful agents for employers and clients; avoid deceptive acts; conduct yourself honorably and lawfully.</p>',
 qs=[mc('Which comes first in the NSPE canons?',['Maximize client profit','Hold paramount the safety, health, and welfare of the public','Meet the deadline','Use the latest software'],1,'Public safety comes first.'),
      mc('An AI tool gives you a result on a topic outside your competence. The best next step?',['Use it; the tool knows more','Get it reviewed by a qualified engineer, or decline that part of the work','Hide that AI was used'],1,'&ldquo;Only in areas of competence&rdquo; means getting qualified review when you are outside yours.')]),
dict(title='Corroborating sources', body=
 '<p>Check an important claim against two or more <b>independent</b> sources. Independent means they did not just copy each other. AI tools can also produce citations that look real but are not, so confirm that a cited source exists and says what is claimed.</p>',
 qs=[mc('Three websites give the same figure, and all quote the same press release. How many independent sources do you have?',['Three','One','Zero'],1,'They all trace to the same origin.'),
      mc('An AI gives a citation for a paper. What do you check first?',['Nothing; citations are reliable','That the paper exists and actually says what was claimed','How long the title is'],1,'Fabricated citations are a known failure mode.')]),
dict(title='Context window', body=
 '<p>An AI model can only &ldquo;see&rdquo; a limited amount of text at once, measured in <b>tokens</b> (roughly 3/4 of an English word each). In a very long chat, early details can fade or drop out. Put key constraints in the message, and restate them or start a fresh chat with a summary when things get long.</p>',
 qs=[num('About how many tokens is a 3,000-word document (1 token &asymp; 0.75 words)?',4000,300,'3,000 / 0.75 = 4,000 tokens.',unit='tokens',hint='Divide words by 0.75.'),
      mc('Your specs were in message 1 of a very long chat and the assistant now ignores them. Best fix?',['Nothing; it will remember','Restate the key constraints, or start a new chat with a short summary','Type in capitals'],1,'The early text may have fallen out of what the model can use.')]),
dict(title='Stale data', body=
 '<p>Stale data was correct once and is out of date now: a price, a code edition, a supplier spec. AI models are trained on text up to a cutoff date and can quote old numbers confidently. Always check the date on anything that changes over time.</p>',
 qs=[mc('An AI quotes a steel price from its training data. The risk is:',['The price may be stale','Steel has no price','Prices never change'],0,'Prices change; check a current source.'),
      mc('Which item is the most likely to have gone stale?',['The value of pi','A building-code edition number','The definition of a newton'],1,'Codes are revised on a cycle; check the edition your project is under.')]),
dict(title='Tradeoff uncertainty', body=
 '<p>When comparing options you usually trade one goal against another and the numbers carry uncertainty. Compare <b>ranges</b>, not single values. If the ranges overlap, you cannot yet say one is better.</p>',
 qs=[mc('Option A costs 100 &plusmn; 5. Option B costs 90 &plusmn; 20. Is B clearly cheaper?',['Yes, 90 is less than 100','No. A spans 95 to 105 and B spans 70 to 110, so the ranges overlap','Yes, because B has more uncertainty'],1,'Overlapping ranges mean the data cannot separate them yet.'),
      mc('Best next step in that comparison?',['Pick B','Reduce B&rsquo;s uncertainty (better data), or decide on other criteria','Pick A because 100 is rounder'],1,'B&rsquo;s wide range is what blocks the decision, so that is where to spend effort.')]),
])
