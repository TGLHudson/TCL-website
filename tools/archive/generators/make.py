"""Build research.html for the TCL website from a bibliography list.
Header and footer are copied from book.html so the page matches the rest of the site."""
import html, pathlib, re

SITE = pathlib.Path("/home/user/tcl-website")
HSE = "SPE International Health, Safety, Environment, and Sustainability Conference and Exhibition"
HSE20 = "SPE International Conference and Exhibition on Health, Safety, Environment, and Sustainability"
HSSE = "SPE International Conference on Health, Safety, Security, Environment, and Social Responsibility"
HSSE16 = "SPE International Conference and Exhibition on Health, Safety, Security, Environment and Social Responsibility"
OG = "SPE International Conference on Health, Safety and Environment in Oil and Gas Exploration and Production"

def spe(n):
    return f"10.2118/{n}-MS"

# (authors, year, title, venue, identifier, doi, in_press)
GROUPS = [
 ("origins", "Where the ladder comes from",
  "The five-level ladder grew out of Ron Westrum's three cultures and the Hearts and Minds research programme. These are the papers that set it out and first tested it.",
  [
   ("Westrum, R.", "2004", "A typology of organisational cultures", "<i>Quality and Safety in Health Care</i>, 13 (Suppl 2), ii22–ii27", "", "10.1136/qshc.2003.009522", False),
   ("Hudson, P. T. W., Reason, J. T., Wagenaar, W. A., Bentley, P. D., Primrose, M. & Visser, J. P.", "1994", "Tripod Delta: Proactive approach to enhanced safety", "<i>Journal of Petroleum Technology</i>, 46 (1), 58–62", "", "10.2118/27846-PA", False),
   ("Parker, D., Lawrie, M. & Hudson, P. T. W.", "2006", "A framework for understanding the development of organisational safety culture", "<i>Safety Science</i>, 44 (6), 551–562", "", "10.1016/j.ssci.2005.10.004", False),
   ("Lawrie, M., Parker, D. & Hudson, P. T. W.", "2006", "Investigating employee perceptions of a framework of safety culture maturity", "<i>Safety Science</i>, 44 (3), 259–276", "", "10.1016/j.ssci.2005.10.003", False),
   ("Hudson, P. T. W.", "2007", "Implementing a safety culture in a major multi-national", "<i>Safety Science</i>, 45 (6), 697–722", "", "10.1016/j.ssci.2007.04.005", False),
  ]),
 ("structure", "Structure: why the rungs sit where they do",
  "Each rung is a different arrangement for deciding who acts on risk. These papers give the structural account of the ladder and of the transitions between rungs.",
  [
   ("Hudson, T. G. L., Hudson, P. A. R. & Hudson, P. T. W.", "2024", "Structural understanding underlying the safety culture ladder", HSE + ", Abu Dhabi", "SPE-220464-MS", spe(220464), False),
   ("Hudson, T. G. L. & Hudson, P. T. W.", "2018", "Moving up the culture ladder: Creation and application of management methods to guide organisations towards Generative, a case study", HSSE + ", Abu Dhabi", "SPE-190676-MS", spe(190676), False),
   ("Hudson, T. G. L. & Hudson, P. A. R.", "2026", "Transitions in safety culture: Practical risk-space tools for deciding when and how to change", HSE + ", Abu Dhabi", "SPE-233663-MS", spe(233663), True),
   ("Hudson, T. G. L. & Hudson, P. A. R.", "2026", "Transitions, timing, and tools: Choosing what fits the risk space and safety culture", "Special Session, " + HSE + ", Abu Dhabi", "SPE-233645-MS", spe(233645), True),
  ]),
 ("risk-space", "Risk space: what the work demands",
  "The risk space describes every condition an operation's safety turns on, and sets the floor a culture has to hold. These papers define it and apply it to driving and to construction.",
  [
   ("Hudson, T. G. L. & Hudson, P. T. W.", "2020", "Risk space: Understanding the complexity of operational risk", HSE20 + ", virtual", "SPE-199401-MS", spe(199401), False),
   ("Hudson, T. G. L., Hudson, P. A. R. & Hudson, P. T. W.", "2024", "Risk space and driving: Elementary failures in understanding", HSE + ", Abu Dhabi", "SPE-220251-MS", spe(220251), False),
   ("Hudson, P. A. R.", "2016", "Successfully managing a large high-hazard road transport operation using the 'Hearts and Minds' tool 'Driving for Excellence'", HSSE16 + ", Stavanger", "SPE-179472-MS", spe(179472), False),
   ("Hudson, P. A. R. & Hudson, T. G. L.", "2026", "Construction as a moving risk ecology: How trade integration raises complexity and changes the culture needed to hold barriers", HSE + ", Abu Dhabi", "SPE-233678-MS", spe(233678), True),
  ]),
 ("skill", "Skill: competence plus experience",
  "Structure decides who holds authority; skill decides whether they can carry it. These papers set out the skill framework, its interaction with the risk space, and two case studies from aviation maintenance, repair and overhaul (MRO).",
  [
   ("Hudson, T. G. L. & Hudson, P. T. W.", "2020", "Skill equals competence plus experience", HSE20 + ", virtual", "SPE-199446-MS", spe(199446), False),
   ("Hudson, T. G. L., Hudson, P. A. R. & Hudson, P. T. W.", "2024", "Interaction between skill and risk spaces in operational risk", HSE + ", Abu Dhabi", "SPE-220498-MS", spe(220498), False),
   ("Hudson, T. G. L., Hudson, P. A. R., Hudson, P. T. W. & Phee, P.", "2026", "Building trust and accountability through structure and competence: Two aviation MRO case studies", HSE + ", Abu Dhabi", "SPE-233662-MS", spe(233662), True),
  ]),
 ("barriers", "Barriers and the bowtie",
  "The barrier model, and the levels of governance that keep frontline barriers working.",
  [
   ("Hudson, P. T. W. & Hudson, T. G. L.", "2015", "Integrating cultural and regulatory factors in the bowtie: Moving from hand-waving to rigor", "In V. Ebrahimipour &amp; S. Yacout (Eds.), <i>Ontology Modeling in Physical Asset Integrity Management</i>, 171–198. Cham: Springer", "", "10.1007/978-3-319-15326-1_6", False),
   ("Hudson, T. G. L.", "2018", "'Famous' barriers: A novel approach to improving management understanding of critical functions", HSSE + ", Abu Dhabi", "SPE-190633-MS", spe(190633), False),
   ("Hudson, P. A. R. & Hudson, T. G. L.", "2020", "That is not a barrier! Investigating improper barrier placement in bowties using road traffic bowties as a case study", HSE20 + ", virtual", "SPE-199380-MS", spe(199380), False),
   ("Hudson, T. G. L.", "2020", "Famous barriers within the bowtie levels analysis: Creating middle and senior management understanding about the relative importance of management activities", HSE20 + ", virtual", "SPE-199424-MS", spe(199424), False),
   ("Hudson, T. G. L. & Hudson, P. T. W.", "2020", "Sparseness and completeness: Simplifying bowties to improve understanding and predictive power", HSE20 + ", virtual", "SPE-199496-MS", spe(199496), False),
  ]),
 ("learning", "Incidents, non-compliance and a fair culture",
  "What incident records can show when they are analysed together rather than one at a time, and how to respond fairly when rules are broken.",
  [
   ("Hudson, P. T. W., Vuijk, M., Bryden, R., Biela, D. & Cowley, C.", "2008", "Meeting expectations: A new model for a just and fair culture", OG + ", Nice", "SPE-111977-MS", spe(111977), False),
   ("Hudson, P. T. W. & Hudson, T. G. L.", "2010", "Moving from investigating to analysing incidents: Supporting organisational learning", OG + ", Rio de Janeiro", "SPE-127182-MS", spe(127182), False),
   ("Hudson, T. G. L.", "2018", "Refining Heinrich: Power laws in incident severity distributions", HSSE + ", Abu Dhabi", "SPE-190669-MS", spe(190669), False),
   ("Hudson, T. G. L., Hudson, P. A. R. & Hudson, P. T. W.", "2024", "Non-compliance in complex operations: A case study-led discussion", HSE + ", Abu Dhabi", "SPE-220344-MS", spe(220344), False),
  ]),
 ("decisions", "Decisions under pressure and emergency response",
  "Who decides when conditions change fast, and how emergency arrangements fit the culture that has to run them.",
  [
   ("Hudson, P. T. W. & van der Graaf, G. C.", "1998", "The Rule of Three: Situation awareness in hazardous situations", OG + ", Caracas", "SPE-46765-MS", spe(46765), False),
   ("Hudson, P. A. R. & Hudson, T. G. L.", "2016", "Making safety critical decisions in a high-hazard high-consequence environment: A case study", HSSE16 + ", Stavanger", "SPE-179436-MS", spe(179436), False),
   ("Hudson, P. A. R.", "2018", "That wasn't supposed to happen! Emergency response planning with unforeseen high consequence low probability events", HSSE + ", Abu Dhabi", "SPE-190662-MS", spe(190662), False),
   ("Hudson, P. A. R. & Hudson, T. G. L.", "2026", "Emergency response planning as a function of organisational culture: Delegated authority, information flow, and the management of complexity", HSE + ", Abu Dhabi", "SPE-233694-MS", spe(233694), True),
  ]),
 ("tools", "Choosing tools that fit",
  "Which health, safety and environment (HSE) tools work at which rung, and why a tool used before its rung tends to change into something else.",
  [
   ("Hudson, P. T. W., van der Graaf, G. C., Parker, D., Lawton, R. & Verschuur, W. L. G.", "2000", "HSE tools: Which tools are appropriate?", "SPE International Conference on Health, Safety, and the Environment in Oil and Gas Exploration and Production, Stavanger", "SPE-61229-MS", spe(61229), False),
  ]),
]

def entry(a, y, t, v, ident, doi, press):
    t = html.escape(t, quote=False); t = re.sub(r"(^|[\s(])'", "\\1&#8216;", t).replace("'", "&#8217;")
    year = f"{y}, in press" if press else y
    idpart = f" {ident}." if ident else ""
    badge = ' <span class="badge">In press</span>' if press else ""
    return (f'            <li>\n'
            f'              <span class="cite-title">{t}</span>{badge}\n'
            f'              <span class="cite-meta">{html.escape(a, quote=False)} ({year}). {v}.{idpart}</span>\n'
            f'              <span class="links"><a class="doi" href="https://doi.org/{doi}">doi.org/{doi}</a>{copy_link(a, ident)}</span>\n'
            f'            </li>')

def copy_link(authors, ident):
    # Offer a copy only for the Hudsons' own papers
    if "Hudson" not in authors:
        return ""
    label = ident or "this paper"
    return f' <a class="copy" href="contact.html#copies" aria-label="Request a copy of {label}">Request a copy</a>'

sections = []
for i, (anchor, head, intro, items) in enumerate(GROUPS):
    cls = ' class="tint"' if i % 2 else ""
    lis = "\n".join(entry(*it) for it in items)
    sections.append(f'''    <section{cls} id="{anchor}">
      <div class="wrap split">
        <div>
          <h2>{head}</h2>
          <p class="group-intro">{intro}</p>
        </div>
        <ol class="papers">
{lis}
        </ol>
      </div>
    </section>''')

count = sum(len(g[3]) for g in GROUPS)
toc = "\n".join(f'            <li><a href="#{a}">{h}</a></li>' for a, h, _, _ in GROUPS)
body = f'''    <section class="hero deep">
      <div class="wrap">
        <div class="prose">
          <p class="eyebrow">Papers</p>
          <h1>The research behind the book</h1>
          <p class="lede">The book draws together work presented over more than a decade, most of it at the Society of Petroleum Engineers (SPE) conferences on health, safety, environment and sustainability. Each paper sets out one part of the argument in fuller technical form.</p>
          <p>Co-authors include Professor P. T. W. Hudson, who originated the safety culture ladder with Professor James Reason, and P. A. R. Hudson, a director at Hudson Global Consulting. SPE papers are held in OnePetro, the SPE's online library; every entry below links to its Digital Object Identifier (DOI).</p>
          <p>Every other source the book cites with a DOI is on the <a href="references.html">References</a> page.</p>
          <p><strong>Request a copy.</strong> SPE papers sit behind OnePetro's paywall. If you cannot reach one of our papers through a library or employer, ask and we will send you a copy for your own study. Use the <em>Request a copy</em> link beside the paper, or the <a href="contact.html#copies">contact page</a>.</p>
          <p class="todo">Tim to confirm that the SPE copyright agreement allows authors to share copies on request, and on what terms.</p>
          <p class="todo">The SPE DOIs are formed from each paper's number. Check that each link resolves before launch, especially the four papers marked In press.</p>
        </div>
        <nav aria-label="Themes">
          <p class="eyebrow">{count} papers in eight themes</p>
          <ul class="theme-list">
{toc}
          </ul>
        </nav>
      </div>
    </section>

{chr(10).join(sections)}
'''

tmpl = (SITE / "book.html").read_text()
head, rest = tmpl.split('  <main id="main">', 1)
foot = rest.split("  </main>", 1)[1]
title = "Papers | The Culture Ladder"
desc = "The peer-reviewed papers behind The Culture Ladder by Tim Hudson, grouped by theme, each with its Digital Object Identifier (DOI)."
head = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", head)
head = re.sub(r'(name="description" content=")[^"]*', r"\g<1>" + desc, head)
head = re.sub(r'(property="og:description" content=")[^"]*', r"\g<1>" + desc, head)
head = re.sub(r'(property="og:title" content=")[^"]*', r"\g<1>" + title, head)
head = head.replace("https://thecultureladder.com/book.html", "https://thecultureladder.com/research.html")
head = head.replace(' aria-current="page"', "")
head = head.replace('<a href="research.html">', '<a href="research.html" aria-current="page">')
out = head + '  <main id="main">\n' + body + "  </main>" + foot
(SITE / "research.html").write_text(out)
print("wrote research.html with", count, "papers")
