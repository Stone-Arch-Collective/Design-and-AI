import html, math
def code(s): return '<pre><code>'+html.escape(s.strip('\n'))+'</code></pre>'
def mc(q, options, answer, why, hints=None):
    return dict(type='mc', q=q, options=options, answer=answer, why=why, hints=hints or {})
def num(q, answer, tol, why, unit='', hint=None):
    return dict(type='num', q=q, answer=answer, tol=tol, why=why, unit=unit, hint=hint)
def card(kind, label, body): return f'<div class="card {kind}"><div class="lab">{label}</div>{body}</div>'

FOOT = ('Draft for SEIS 201 (Spring 2027), written with Claude for Shannon Seaver. Not yet reviewed by a subject-matter expert. '
        'This is a self-check: it teaches and gives instant feedback, but the completion code is honor-system and can be shared.')

# ---------- t table check ----------
T = {4:2.776, 9:2.262, 14:2.145, 29:2.045}
se5 = 10/math.sqrt(5); m5 = T[4]*se5
se10 = 20/math.sqrt(10); m10 = T[9]*se10
assert abs(m5-12.415)<0.01 and abs(m10-14.30)<0.01

PROB = dict(code='PROB', title='Probability and Sampling: a 35-minute primer', minutes=35,
intro='Six ideas you need before the statistics sessions: probability, sample vs. population, random sampling, sampling variability, standard error, and the t multiplier. No prior statistics assumed. Use a calculator; every answer can be checked with one.',
footer=FOOT,
steps=[
dict(title='Probability basics', body=
 '<p>Probability is the long-run fraction of times something happens. It runs from <b>0</b> (never) to <b>1</b> (always).</p>'
 + card('formula','Rules you need',
   '<p style="margin:0">Not A: <code>P(not A) = 1 &minus; P(A)</code><br>Both A and B, when they do not affect each other (independent): <code>P(A and B) = P(A) &times; P(B)</code><br>At least one: <code>1 &minus; P(none)</code></p>')
 + card('worked','Worked example',
   '<p style="margin:0">A sensor fails with probability 0.02 on a test. It works with probability 1 &minus; 0.02 = 0.98. Three independent sensors all work: 0.98 &times; 0.98 &times; 0.98 = <b>0.941</b>.</p>'),
 qs=[
  num('4% of bolts in a lot are defective. If you pick one bolt at random, what is the probability it is good?',0.96,0.001,'1 &minus; 0.04 = 0.96.',hint='Use P(not A) = 1 &minus; P(A). Write 4% as 0.04.'),
  num('Two independent sensors each fail with probability 0.1. What is the probability that both fail?',0.01,0.0005,'0.1 &times; 0.1 = 0.01.',hint='Independent events multiply.'),
  num('Same two sensors: what is the probability that at least one works?',0.99,0.0005,'&ldquo;At least one works&rdquo; is the opposite of &ldquo;both fail&rdquo;: 1 &minus; 0.01 = 0.99.',hint='Find the probability of the opposite event (both fail) and subtract from 1.'),
  mc('Which of these cannot be a probability?',['0.35','1.2','0','1'],1,'A probability can never exceed 1.'),
 ]),
dict(title='Sample vs. population', body=
 '<p>The <b>population</b> is everything you want to know about. The <b>sample</b> is the part you actually measured. A number describing the population is a <b>parameter</b> (usually unknown). A number computed from the sample is a <b>statistic</b> (what you actually have).</p>'
 + card('formula','Notation',
   '<p style="margin:0">Population mean: <code>&mu;</code> (unknown). Sample mean: <code>x&#772;</code> (computed). Sample standard deviation: <code>s</code>. Sample size: <code>n</code>.</p>'),
 qs=[
  mc('A lab tests 25 cylinders from a 2,000-cylinder concrete pour and reports a mean compressive strength of 32.1 MPa. What is the population?',['The 25 cylinders tested','All 2,000 cylinders in the pour','The number 32.1 MPa','The lab'],1,'The population is everything you want to know about: the whole pour.'),
  mc('In that example, 32.1 MPa is a:',['Parameter','Statistic','Population','Probability'],1,'It is computed from the sample, so it is a statistic. It estimates the parameter (the true mean of the pour).'),
  mc('True or false: the mean of 25 specimens equals the true mean of the whole pour.',['True, 25 is enough','False. It is an estimate that will usually be off by some amount','True if the specimens were tested carefully'],1,'Careful testing removes measurement error, not the sample-to-sample difference. That difference is the subject of the next two steps.'),
 ]),
dict(title='Random sampling', body=
 '<p>A <b>random sample</b> gives every unit in the population an equal chance of being picked, with no human preference in the choice. Picking what is easy to reach (top of the pallet, first parts off the line, the ones that look suspicious) is <b>convenience sampling</b>. It can be biased in a direction you cannot see.</p>'
 + card('warn','The trap','<p style="margin:0">A bigger sample reduces random noise. It does <b>not</b> fix bias from how you picked. A thousand top-of-pallet parts are still top-of-pallet parts.</p>'),
 qs=[
  mc('You must estimate the defect rate among 10,000 parts. Which method gives a random sample of 50?',['The first 50 off the line at the start of the shift','The 50 that the operator thinks look suspicious','50 serial numbers chosen by a random-number generator','50 parts from the bin nearest the door'],2,'A random-number generator on the full list of serial numbers gives every part the same chance.'),
  mc('You sampled 50 parts from the top of the pallet and worry about bias. You sample 1,000 from the top instead. Is the bias fixed?',['Yes, bigger samples cancel bias','No. A larger sample reduces random noise, not bias from how the parts were chosen'],1,'Bias comes from the selection method. Change the method, not just the size.'),
 ]),
dict(title='Sampling variability', widget='sim', body=
 '<p>Take two different random samples from the same population and you get two different sample means. Nothing is wrong with your measuring; that is what sampling does. How much the means wobble depends on the sample size <b>n</b> and on how spread out the population is.</p>',
 qs=[
  mc('Use the simulator. When you go from n = 5 to n = 20 (four times as many specimens), the spread of the sample means roughly:',['Stays the same','Halves','Drops to a quarter','Doubles'],1,'It halves. Four times the data cuts the wobble by the square root of 4, which is 2. You will see that written as a formula next.',{0:'Try it: set n = 5, draw, then n = 20, draw, and compare the reported spreads.',2:'Compare the two spreads the simulator reports. Is the second a quarter of the first?',3:'More data does not make the means wobble more.'}),
  mc('Which statement is true?',['Two samples of the same size from the same population always give the same mean','Sample means differ from sample to sample even when the measuring is perfect','A sample mean is always exactly the population mean if n is at least 30'],1,'Sample-to-sample difference is built into sampling.'),
 ]),
dict(title='Standard error', body=
 '<p>The <b>standard deviation (SD)</b> describes how spread out individual specimens are. The <b>standard error (SE)</b> describes how uncertain your <i>sample mean</i> is. Same units, different question.</p>'
 + card('formula','Formula card','<p style="margin:0"><code>SE = s / &radic;n</code><br>s = sample standard deviation, n = number of specimens. SE has the same units as s.</p>')
 + card('worked','Worked example','<p style="margin:0">s = 20 MPa, n = 25. &radic;25 = 5. SE = 20 / 5 = <b>4 MPa</b>.</p>'),
 qs=[
  num('s = 8 MPa, n = 16. What is the SE (MPa)?',2,0.01,'&radic;16 = 4, so 8 / 4 = 2.',unit='MPa',hint='Divide s by the square root of n, not by n.'),
  num('s = 30 MPa, n = 36. What is the SE (MPa)?',5,0.01,'&radic;36 = 6, so 30 / 6 = 5.',unit='MPa',hint='&radic;36 = 6.'),
  mc('To cut the SE in half, you need:',['Twice as many specimens','Four times as many specimens','Half as many specimens','Ten times as many specimens'],1,'SE depends on &radic;n. To halve it, &radic;n must double, so n must quadruple.'),
  mc('A batch has SD = 20 MPa and SE = 4 MPa. Which number describes how far a single specimen is likely to be from the batch mean?',['SD, 20 MPa','SE, 4 MPa'],0,'SD is about individuals. SE is about the uncertainty of the mean.'),
 ]),
dict(title='The t multiplier and a 95% interval', body=
 '<p>A 95% confidence interval for the true mean is <b>x&#772; &plusmn; t* &times; SE</b>. The multiplier <b>t*</b> is close to 2 for large samples and bigger for small samples, because with few specimens even your estimate of the SD is shaky.</p>'
 + card('formula','t* for a 95% interval (degrees of freedom = n &minus; 1)',
   '<table><tr><th>n</th><th>df</th><th>t*</th></tr><tr><td>5</td><td>4</td><td>2.776</td></tr><tr><td>10</td><td>9</td><td>2.262</td></tr><tr><td>15</td><td>14</td><td>2.145</td></tr><tr><td>30</td><td>29</td><td>2.045</td></tr><tr><td>very large</td><td>&infin;</td><td>1.960</td></tr></table>')
 + card('worked','Worked example','<p style="margin:0">n = 10, x&#772; = 400 MPa, s = 20. SE = 20/&radic;10 = 6.32. t* = 2.262. Margin = 2.262 &times; 6.32 = 14.3. Interval: <b>385.7 to 414.3 MPa</b>.</p>'),
 qs=[
  num('n = 5 specimens, s = 10 MPa. Using the table, what is the margin of error, t* &times; SE (MPa)?',round(m5,3),0.1,'SE = 10/&radic;5 = 4.47. Margin = 2.776 &times; 4.47 = 12.4.',unit='MPa',hint='SE first (s divided by &radic;5), then multiply by t* for n = 5, which is 2.776.'),
  mc('Why is t* larger when n is small?',['Small samples are always biased','With few specimens the SD estimate is itself unreliable, so the interval has to be wider to stay honest','Because the units change','It is not larger; it is always 1.96'],1,'Less data means less certainty about the spread, so the interval widens.'),
  mc('A 95% interval for mean strength is 385.7 to 414.3 MPa. Which reading is correct?',['95% of individual specimens fall in this range','If we repeated the whole sampling process many times, about 95% of intervals built this way would contain the true mean','There is a 95% chance the next specimen falls in this range','The true mean is definitely in this range'],1,'The 95% describes the method, not the individual specimens. It is about the mean, not about single parts.',{0:'That would be a statement about individuals. The interval is about the mean.',3:'Nothing is definite; 95% describes how often the method works.'}),
 ]),
])

# ---------- CODE ----------
CODE = dict(code='CODE', title='Reading Code: a Python primer for engineers', minutes=40,
intro='You will not be asked to write programs from scratch. You will be asked to read code an AI assistant wrote, decide whether to trust it, and fix small problems. This guide covers the four things you need: variables and types, functions and imports, conditionals and loops, and error messages. It assumes Python (confirm with your instructor that this is the course language). Code here is for reading; nothing runs on this page.',
footer=FOOT,
steps=[
dict(title='Variables and data types', body=
 '<p>A <b>variable</b> is a name attached to a value. <code>=</code> means &ldquo;store this value under that name.&rdquo; Every value has a <b>type</b>, and the type controls what you can do with it.</p>'
 + code('''
load_kn = 12.5            # float: number with a decimal
span_m = 4                # int: whole number
material = "steel"        # str: text (quotes make it text)
loads = [10, 12.5, 8]     # list: ordered collection, counts from 0
beam = {"L": 4, "E": 200} # dict: look things up by name
''')
 + '<p>Watch for: <code>loads[0]</code> is the <i>first</i> item (counting starts at 0). <code>beam["E"]</code> looks up the value stored under &ldquo;E&rdquo;. Putting a number in quotes turns it into text, and text does not do math. Put units in variable names (<code>load_kn</code>): Python does not track units for you.</p>',
 qs=[
  mc('What does this print?'+code('span_m = 4\nload_kn = 12.5\nprint(span_m * load_kn)'),['50','50.0','16.5','Error'],1,'int &times; float gives a float, so Python prints 50.0.'),
  mc('What does this print?'+code('loads = [10, 12.5, 8]\nprint(loads[0])'),['10','12.5','8','Error'],0,'Counting starts at 0, so loads[0] is the first item.'),
  mc('Which describes <code>reading = "5.2"</code>?',['A float','A string (text). The quotes make it text','A list','An int'],1,'It looks like a number but the quotes make it text. You cannot do math on it until it is converted with float().'),
  mc('What does this print?'+code('beam = {"L": 4, "E": 200}\nprint(beam["E"])'),['4','200','E','Error'],1,'A dict looks up by name; &ldquo;E&rdquo; maps to 200.'),
 ]),
dict(title='Functions and imports', body=
 '<p>A <b>function</b> is a named recipe: values go in (arguments), a value comes out (<code>return</code>). An <b>import</b> brings in a library of ready-made functions. To read a function, find the <code>def</code> line, what goes in, and what comes out.</p>'
 + code('''
import math
import pandas as pd

def stress_mpa(force_n, area_mm2):
    return force_n / area_mm2

s = stress_mpa(20000, 100)
print(s)                          # 200.0
print(math.sqrt(16))              # 4.0
df = pd.read_csv("tests.csv")     # loads a table from a file
print(df["strength"].mean())      # average of one column
''')
 + '<p><code>module.function()</code> and <code>object.method()</code> use a dot. <code>as pd</code> is just a nickname. Defining a function does not run it; only calling it does.</p>',
 qs=[
  mc('What does this print?'+code('def area(w, h):\n    return w * h\n\nprint(area(3, 5))'),['8','15','area','Error'],1,'w = 3, h = 5, returns 15.'),
  mc('What does <code>import pandas as pd</code> do?',['Makes the pandas library available under the nickname pd','Creates a file named pd','Downloads a data set','Runs the pandas tests'],0,'It loads the library and gives it a short name.'),
  mc('Most likely meaning of <code>df["strength"].mean()</code>?',['The average of the strength column','The largest strength','Deletes the strength column','The number of rows'],0,'.mean() is the average; df["strength"] picks one column of the table.'),
  mc('What does this print?'+code('def double(x):\n    return 2 * x\n\nprint("done")'),['8','done','Nothing','Error'],1,'The function is defined but never called. Only the print line runs.'),
 ]),
dict(title='Conditionals and loops', body=
 '<p><b>Indentation is structure.</b> Lines indented under <code>if</code> or <code>for</code> belong to it. <code>if / elif / else</code> picks one branch. <code>for</code> repeats once per item. <code>==</code> asks &ldquo;are these equal?&rdquo;; <code>=</code> stores a value.</p>'
 + code('''
loads = [4.0, 9.5, 12.0]
limit = 10
for load in loads:
    if load > limit:
        print("over", load)
    else:
        print("ok", load)
''')
 + '<p>Common pattern, a running total: <code>total = 0</code>, then inside a loop <code>total = total + x</code>. <code>range(4)</code> gives 0, 1, 2, 3.</p>',
 qs=[
  mc('What does the loop above print, line by line?',['ok 4.0 / ok 9.5 / over 12.0','over 4.0 / over 9.5 / over 12.0','ok 4.0 / over 9.5 / over 12.0','over 12.0'],0,'Only 12.0 exceeds the limit of 10.'),
  num('What does this print?'+code('total = 0\nfor x in [3, 5, 7]:\n    total = total + x\nprint(total)'),15,0,'0 + 3 + 5 + 7 = 15.',hint='Add the items one at a time.'),
  num('<code>for i in range(4): print(i)</code> &mdash; what is the last number printed?',3,0,'range(4) gives 0, 1, 2, 3.',hint='range(4) starts at 0.'),
  mc('What is the difference between <code>=</code> and <code>==</code>?',['They are the same','= stores a value; == asks whether two values are equal','== stores a value; = asks whether two values are equal'],1,'One assigns, one compares. Mixing them up is a classic bug.'),
  mc('What does this print?'+code('n = 7\nif n > 10:\n    print("big")\nelif n > 5:\n    print("medium")\nelse:\n    print("small")'),['big','medium','small','Nothing'],1,'7 is not above 10, but it is above 5.'),
 ]),
dict(title='Reading error messages', body=
 '<p>Errors are information. <b>Read the last line first</b>: it names the error type and says what went wrong. The lines above it say where.</p>'
 + code('''
Traceback (most recent call last):
  File "beam.py", line 6, in <module>
    print(stress)
NameError: name 'stress' is not defined
''')
 + '<table><tr><th>Error</th><th>Usually means</th></tr>'
   '<tr><td>NameError</td><td>Typo, or you used a name before creating it</td></tr>'
   '<tr><td>TypeError</td><td>Wrong kind of value, e.g. adding a number to text</td></tr>'
   '<tr><td>KeyError</td><td>A dict key or table column name is not there. Check spelling and capitals</td></tr>'
   '<tr><td>IndexError</td><td>List position past the end</td></tr>'
   '<tr><td>ZeroDivisionError</td><td>Divided by 0, often from missing data</td></tr>'
   '<tr><td>SyntaxError / IndentationError</td><td>Structure typo; check the line above the one reported</td></tr>'
   '<tr><td>ModuleNotFoundError</td><td>Library not installed</td></tr>'
   '<tr><td>FileNotFoundError</td><td>Wrong file name or folder</td></tr></table>'
 + card('warn','No error does not mean right','<p style="margin:0">AI-written code can run cleanly and still be wrong. Before you trust it: run it on an input where you know the answer, and check the units.</p>'),
 qs=[
  mc('Your code has <code>df["Strength"]</code> and fails with <code>KeyError: \'Strength\'</code>. The CSV header is <code>strength</code>. What is the fix?',['Install pandas again','Change it to df["strength"] to match the header exactly','Restart the computer','Add more data'],1,'Column names must match exactly, including capitals.'),
  mc('<code>TypeError: unsupported operand type(s) for +: \'int\' and \'str\'</code> most likely means:',['A file is missing','You tried to add a number and text; one value is a string and needs converting','A library is not installed','The loop is too long'],1,'One value is text. Convert it with float() or fix where it was read in.'),
  mc('In a long error message, where do you look first?',['The first line','The last line','The middle','It does not matter'],1,'The last line names the error and the reason.'),
  mc('<code>ZeroDivisionError</code> on <code>stress = force / area</code>. Most likely cause?',['force is too large','area is 0, for example from missing data or the wrong column','Python is out of date','The variable name is too long'],1,'You divided by zero. Look at where area came from.'),
  mc('An AI assistant writes code to find stress for a 20 kN load on 100 mm&sup2;. It runs with no errors and prints 0.0002. Is it right?',['Yes, no errors means correct','No. Expected about 200 MPa; clean code can still have a units mistake','Yes, small numbers are normal','Cannot tell'],1,'20,000 N / 100 mm&sup2; = 200 MPa. Running without errors says nothing about whether the answer is right; the units were probably mishandled.',{0:'Errors only catch crashes, not wrong answers. Do the hand calculation.'}),
 ]),
])
