"""Build references.html: every source cited in The Culture Ladder that carries a DOI.
Citations as given in the book's notes (v87); the last five DOIs were found by search for
sources the book cites without one. Header and footer copied from book.html."""
import html, pathlib, re, unicodedata

SITE = pathlib.Path("/home/user/tcl-website")
SPE_HSE20 = "SPE International Conference and Exhibition on Health, Safety, Environment, and Sustainability"
OG = "SPE International Conference on Health, Safety and Environment in Oil and Gas Exploration and Production"

# (authors, year, title, source, doi)
REFS = [
 ("Almklov, P.", "2024", "Work, organisational fragmentation and safety", "In J.-C. Le Coze &amp; B. Journé (Eds.), <i>Safe Performance in a World of Global Networks</i>. Cham: Springer", "10.1007/978-3-031-35163-1_2"),
 ("Almklov, P. G. & Antonsen, S.", "2014", "Making work invisible: New public management and operational work in critical infrastructure sectors", "<i>Public Administration</i>, 92 (2), 477–492", "10.1111/padm.12069"),
 ("Antonsen, S.", "2009", "Safety culture and the issue of power", "<i>Safety Science</i>, 47, 183–191", "10.1016/j.ssci.2008.02.004"),
 ("Antonsen, S.", "2009", "Safety culture assessment: A mission impossible?", "<i>Journal of Contingencies and Crisis Management</i>, 17 (4), 242–254", "10.1111/j.1468-5973.2009.00585.x"),
 ("Aven, T.", "2022", "A risk science perspective on the discussion concerning Safety I, Safety II and Safety III", "<i>Reliability Engineering &amp; System Safety</i>, 217, 108077", "10.1016/j.ress.2021.108077"),
 ("Aven, T. & Krohn, B. S.", "2014", "A new perspective on how to understand, assess and manage risk and the unforeseen", "<i>Reliability Engineering &amp; System Safety</i>, 121, 1–10", "10.1016/j.ress.2013.07.005"),
 ("Ayres, I. & Braithwaite, J.", "1991", "Tripartism: Regulatory capture and empowerment", "<i>Law &amp; Social Inquiry</i>, 16 (3), 435–496", "10.1111/j.1747-4469.1991.tb00291.x"),
 ("Baron, J. & Hershey, J. C.", "1988", "Outcome bias in decision evaluation", "<i>Journal of Personality and Social Psychology</i>, 54 (4), 569–579", "10.1037/0022-3514.54.4.569"),
 ("Bolton, R., Logan, C. & Gittell, J. H.", "2021", "Revisiting relational coordination: A systematic review", "<i>Journal of Applied Behavioral Science</i>, 57 (3), 290–322", "10.1177/0021886321991597"),
 ("Boskeljon-Horst, L., Sillem, S. & Dekker, S. W. A.", "2023", "'Ladder'-based safety culture assessments inversely predict safety outcomes", "<i>Journal of Contingencies and Crisis Management</i>, 31 (3), 372–391", "10.1111/1468-5973.12445"),
 ("Bromley, P. & Powell, W. W.", "2012", "From smoke and mirrors to walking the talk: Decoupling in the contemporary world", "<i>Academy of Management Annals</i>, 6 (1), 483–530", "10.5465/19416520.2012.684462"),
 ("Coglianese, C. & Lazer, D.", "2003", "Management-based regulation: Prescribing private management to achieve public goals", "<i>Law &amp; Society Review</i>, 37 (4), 691–730", "10.1111/j.0023-9216.2003.03703001.x"),
 ("de Ruijter, A. & Guldenmund, F.", "2016", "The bowtie method: A review", "<i>Safety Science</i>, 88, 211–218", "10.1016/j.ssci.2016.03.001"),
 ("Dekker, S. W. A.", "2009", "Just culture: Who gets to draw the line?", "<i>Cognition, Technology &amp; Work</i>, 11, 177–185", "10.1007/s10111-008-0110-7"),
 ("Dekker, S. W. A.", "2014", "The bureaucratization of safety", "<i>Safety Science</i>, 70, 348–357", "10.1016/j.ssci.2014.07.015"),
 ("Dekker, S. W. A. & Breakey, H.", "2016", "'Just culture:' Improving safety by achieving substantive, procedural and restorative justice", "<i>Safety Science</i>, 85, 187–193", "10.1016/j.ssci.2016.01.018"),
 ("Dickerson, S. S. & Kemeny, M. E.", "2004", "Acute stressors and cortisol responses: A theoretical integration and synthesis of laboratory research", "<i>Psychological Bulletin</i>, 130 (3), 355–391", "10.1037/0033-2909.130.3.355"),
 ("Drew, B. J., Harris, P., Zègre-Hemsey, J. K., et al.", "2014", "Insights into the problem of alarm fatigue with physiologic monitor devices: A comprehensive observational study of consecutive intensive care unit patients", "<i>PLOS ONE</i>, 9 (10), e110274", "10.1371/journal.pone.0110274"),
 ("Edmondson, A. C.", "1996", "Learning from mistakes is easier said than done: Group and organizational influences on the detection and correction of human error", "<i>Journal of Applied Behavioral Science</i>, 32 (1), 5–28", "10.1177/0021886396321001"),
 ("Fischhoff, B.", "1975", "Hindsight ≠ foresight: The effect of outcome knowledge on judgment under uncertainty", "<i>Journal of Experimental Psychology: Human Perception and Performance</i>, 1 (3), 288–299", "10.1037/0096-1523.1.3.288"),
 ("Fruhen, L. S., Flin, R. H. & McLeod, R.", "2014", "Chronic unease for safety in managers: A conceptualisation", "<i>Journal of Risk Research</i>, 17 (8), 969–979", "10.1080/13669877.2013.822924"),
 ("Gittell, J. H.", "2001", "Supervisory span, relational coordination and flight departure performance: A reassessment of postbureaucracy theory", "<i>Organization Science</i>, 12 (4), 468–483", "10.1287/orsc.12.4.468.10636"),
 ("Gonçalves Filho, A. P. & Waterson, P.", "2018", "Maturity models and safety culture: A critical review", "<i>Safety Science</i>, 105, 192–211", "10.1016/j.ssci.2018.02.017"),
 ("Grote, G.", "2012", "Safety management in different high-risk domains: All the same?", "<i>Safety Science</i>, 50 (10), 1983–1992", "10.1016/j.ssci.2011.07.017"),
 ("Grote, G.", "2018", "On the importance of culture for safety: Bridging modes of operation in adaptive safety management", "In C. Gilbert, B. Journé, H. Laroche &amp; C. Bieder (Eds.), <i>Safety Cultures, Safety Models: Taking Stock and Moving Forward</i>. Cham: Springer", "10.1007/978-3-319-95129-4"),
 ("Gunningham, N. & Sinclair, D.", "2009", "Organizational trust and the limits of management-based regulation", "<i>Law &amp; Society Review</i>, 43 (4), 865–900", "10.1111/j.1540-5893.2009.00391.x"),
 ("Hale, A. R.", "2000", "Culture's confusions", "<i>Safety Science</i>, 34 (1–3), 1–14", "10.1016/S0925-7535(00)00003-5"),
 ("Hale, A. & Borys, D.", "2013", "Working to rule, or working safely? Part 1: A state of the art review", "<i>Safety Science</i>, 55, 207–221", "10.1016/j.ssci.2012.05.011"),
 ("Hayes, J. & Tillement, S.", "2022", "Outsourcing and safety: An introduction", "In J. Hayes &amp; S. Tillement (Eds.), <i>Contracting and Safety</i>, 1–8. Cham: Springer", "10.1007/978-3-030-89792-5_1"),
 ("Haynes, A. B., Weiser, T. G., Berry, W. R., et al.", "2009", "A surgical safety checklist to reduce morbidity and mortality in a global population", "<i>New England Journal of Medicine</i>, 360 (5), 491–499", "10.1056/NEJMsa0810119"),
 ("Henriqson, É., Schuler, B., van Winsen, R. & Dekker, S. W. A.", "2014", "The constitution and effects of safety culture as an object in the discourse of accident prevention: A Foucauldian approach", "<i>Safety Science</i>, 70, 465–476", "10.1016/j.ssci.2014.07.004"),
 ("Hopkins, A.", "2006", "Studying organisational cultures and their effects on safety", "<i>Safety Science</i>, 44 (10), 875–889", "10.1016/j.ssci.2006.05.005"),
 ("Hopkins, A.", "2006", "What are we to make of safe behaviour programs?", "<i>Safety Science</i>, 44 (7), 583–597", "10.1016/j.ssci.2006.01.001"),
 ("Hopkins, A.", "2009", "Thinking about process safety indicators", "<i>Safety Science</i>, 47, 460–465", "10.1016/j.ssci.2007.12.006"),
 ("Hopkins, A.", "2011", "Risk-management and rule-compliance: Decision-making in hazardous industries", "<i>Safety Science</i>, 49, 110–120", "10.1016/j.ssci.2010.07.014"),
 ("Hudson, P. A. R.", "2016", "Successfully managing a large high-hazard road transport operation using the 'Hearts and Minds' tool 'Driving for Excellence'", "SPE International Conference and Exhibition on Health, Safety, Security, Environment and Social Responsibility, Stavanger. SPE-179472-MS", "10.2118/179472-MS"),
 ("Hudson, P. T. W.", "2007", "Implementing a safety culture in a major multi-national", "<i>Safety Science</i>, 45 (6), 697–722", "10.1016/j.ssci.2007.04.005"),
 ("Hudson, P. T. W. & Hudson, T. G. L.", "2010", "Moving from investigating to analysing incidents: Supporting organisational learning", OG + ", Rio de Janeiro. SPE-127182-MS", "10.2118/127182-MS"),
 ("Hudson, P. T. W. & Hudson, T. G. L.", "2015", "Integrating cultural and regulatory factors in the bowtie: Moving from hand-waving to rigor", "In V. Ebrahimipour &amp; S. Yacout (Eds.), <i>Ontology Modeling in Physical Asset Integrity Management</i>, 171–198. Cham: Springer", "10.1007/978-3-319-15326-1_6"),
 ("Hudson, P. T. W., Parker, D. & van der Graaf, G. C.", "2002", "The Hearts and Minds program: Understanding HSE culture", "SPE International Conference on Health, Safety and Environment in Oil and Gas Exploration and Production, Kuala Lumpur. SPE-73938-MS", "10.2118/73938-MS"),
 ("Hudson, P. T. W., Reason, J. T., Wagenaar, W. A., Bentley, P. D., Primrose, M. & Visser, J. P.", "1994", "Tripod Delta: Proactive approach to enhanced safety", "<i>Journal of Petroleum Technology</i>, 46 (1), 58–62", "10.2118/27846-PA"),
 ("Hudson, P. T. W., van der Graaf, G. C., Parker, D., Lawton, R. & Verschuur, W. L. G.", "2000", "HSE tools: Which tools are appropriate?", "SPE International Conference on Health, Safety, and the Environment in Oil and Gas Exploration and Production, Stavanger. SPE-61229-MS", "10.2118/61229-MS"),
 ("Hudson, P. T. W., Vuijk, M., Bryden, R., Biela, D. & Cowley, C.", "2008", "Meeting expectations: A new model for a just and fair culture", OG + ", Nice. SPE-111977-MS", "10.2118/111977-MS"),
 ("Hudson, T. G. L. & Hudson, P. T. W.", "2020", "Risk space: Understanding the complexity of operational risk", SPE_HSE20 + ", virtual. SPE-199401-MS", "10.2118/199401-MS"),
 ("Hudson, T. G. L. & Hudson, P. T. W.", "2020", "Skill equals competence plus experience", SPE_HSE20 + ", virtual. SPE-199446-MS", "10.2118/199446-MS"),
 ("Kahneman, D. & Lovallo, D.", "1993", "Timid choices and bold forecasts: A cognitive perspective on risk taking", "<i>Management Science</i>, 39 (1), 17–31", "10.1287/mnsc.39.1.17"),
 ("Lawrie, M., Parker, D. & Hudson, P. T. W.", "2006", "Investigating employee perceptions of a framework of safety culture maturity", "<i>Safety Science</i>, 44 (3), 259–276", "10.1016/j.ssci.2005.10.003"),
 ("Le Coze, J.-C.", "2019", "How safety culture can make us think", "<i>Safety Science</i>, 118, 221–229", "10.1016/j.ssci.2019.05.026"),
 ("Le Coze, J.-C.", "2020", "Hopkins' view of structure and culture (one step closer to strategy)", "<i>Safety Science</i>, 122, 104541", "10.1016/j.ssci.2019.104541"),
 ("Leveson, N., Dulac, N., Marais, K. & Carroll, J.", "2009", "Moving beyond normal accidents and high reliability organizations: A systems approach to safety in complex systems", "<i>Organization Studies</i>, 30 (2–3), 227–249", "10.1177/0170840608101478"),
 ("Liu, Y. & Yang, F.", "2026", "Moved by the lightest touch of meaning: Even minimal significance matters for motivation from childhood", "<i>Psychological Science</i>", "10.1177/09567976261462874"),
 ("Love, P. E. D.", "2026", "Rework as a systemic risk amplifier: Exposure-normalized modeling of safety frequency and severity", "<i>Production Planning &amp; Control</i>", "10.1080/09537287.2026.2708092"),
 ("McCulloch, W. S.", "1945", "A heterarchy of values determined by the topology of nervous nets", "<i>Bulletin of Mathematical Biophysics</i>, 7 (2), 89–93", "10.1007/BF02478457"),
 ("Mitchell, D. J., Russo, J. E. & Pennington, N.", "1989", "Back to the future: Temporal perspective in the explanation of events", "<i>Journal of Behavioral Decision Making</i>, 2 (1), 25–38", "10.1002/bdm.3960020103"),
 ("Nenonen, S.", "2011", "Fatal workplace accidents in outsourced operations in the manufacturing industry", "<i>Safety Science</i>, 49 (10), 1394–1403", "10.1016/j.ssci.2011.06.004"),
 ("Nichols, T., Walters, D. & Tasiran, A. C.", "2007", "Trade unions, institutional mediation and industrial safety: Evidence from the UK", "<i>Journal of Industrial Relations</i>, 49 (2), 211–226", "10.1177/0022185607074919"),
 ("Parker, D., Lawrie, M. & Hudson, P. T. W.", "2006", "A framework for understanding the development of organisational safety culture", "<i>Safety Science</i>, 44 (6), 551–562", "10.1016/j.ssci.2005.10.004"),
 ("Power, M.", "2000", "The audit society: Second thoughts", "<i>International Journal of Auditing</i>, 4, 111–119", "10.1111/1099-1123.00306"),
 ("Provan, D. J., Weber, D. E. & Dekker, S. W. A.", "2018", "Safety clutter: The accumulation and persistence of 'safety' work that does not contribute to operational safety", "<i>Policy and Practice in Health and Safety</i>, 16 (2), 194–211", "10.1080/14773996.2018.1491147"),
 ("Rae, A. & Provan, D.", "2019", "Safety work versus the safety of work", "<i>Safety Science</i>, 111, 119–127", "10.1016/j.ssci.2018.07.001"),
 ("Raheemy, Y., Hallowell, M. R., Lingard, H. & Sherratt, F.", "2026", "Safety clutter: An attribute-based conceptualization and taxonomy for diagnosis", "<i>Journal of Safety Research</i>, 98, 55–68", "10.1016/j.jsr.2026.06.005"),
 ("Reilly, B., Paci, P. & Holl, P.", "1995", "Unions, safety committees and workplace injuries", "<i>British Journal of Industrial Relations</i>, 33 (2), 275–288", "10.1111/j.1467-8543.1995.tb00435.x"),
 ("Richter, A. & Koch, C.", "2004", "Integration, differentiation and ambiguity in safety cultures", "<i>Safety Science</i>, 42 (8), 703–722", "10.1016/j.ssci.2003.12.003"),
 ("Roberts, K. H., Stout, S. K. & Halpern, J. J.", "1994", "Decision dynamics in two high reliability military organizations", "<i>Management Science</i>, 40 (5), 614–624", "10.1287/mnsc.40.5.614"),
 ("Rotter, J. B.", "1966", "Generalized expectancies for internal versus external control of reinforcement", "<i>Psychological Monographs: General and Applied</i>, 80 (1), 1–28", "10.1037/h0092976"),
 ("Silbey, S. S.", "2009", "Taming Prometheus: Talk about safety and culture", "<i>Annual Review of Sociology</i>, 35, 341–369", "10.1146/annurev.soc.34.040507.134707"),
 ("Tversky, A. & Kahneman, D.", "1974", "Judgment under uncertainty: Heuristics and biases", "<i>Science</i>, 185 (4157), 1124–1131", "10.1126/science.185.4157.1124"),
 ("Urbach, D. R., Govindarajan, A., Saskin, R., et al.", "2014", "Introduction of surgical safety checklists in Ontario, Canada", "<i>New England Journal of Medicine</i>, 370 (11), 1029–1038", "10.1056/NEJMsa1308261"),
 ("Vaughan, D.", "1999", "The dark side of organizations: Mistake, misconduct, and disaster", "<i>Annual Review of Sociology</i>, 25, 271–305", "10.1146/annurev.soc.25.1.271"),
 ("Walters, D. & Nichols, T.", "2007", "Worker Representation and Workplace Health and Safety", "Basingstoke: Palgrave Macmillan", "10.1057/9780230210714"),
 ("Weick, K. E.", "1993", "The collapse of sensemaking in organizations: The Mann Gulch disaster", "<i>Administrative Science Quarterly</i>, 38 (4), 628–652", "10.2307/2393339"),
 ("Westrum, R.", "2004", "A typology of organisational cultures", "<i>Quality and Safety in Health Care</i>, 13 (Suppl 2), ii22–ii27", "10.1136/qshc.2003.009522"),
 ("Westrum, R.", "2014", "The study of information flow: A personal journey", "<i>Safety Science</i>, 67, 58–63", "10.1016/j.ssci.2014.01.009"),
 ("Zohar, D.", "2000", "A group-level model of safety climate: Testing the effect of group climate on microaccidents in manufacturing jobs", "<i>Journal of Applied Psychology</i>, 85 (4), 587–596", "10.1037/0021-9010.85.4.587"),
 ("Zohar, D. & Luria, G.", "2005", "A multilevel model of safety climate: Cross-level relationships between organization and group-level climates", "<i>Journal of Applied Psychology</i>, 90 (4), 616–628", "10.1037/0021-9010.90.4.616"),
]

def key(r):
    s = unicodedata.normalize("NFKD", r[0]).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"^de ", "", s)  # file "de Ruijter" under R
    return (s, r[1], r[2].lower())

REFS.sort(key=key)
assert len({r[4] for r in REFS}) == len(REFS), "duplicate DOI"

def letter(r):
    s = unicodedata.normalize("NFKD", r[0]).encode("ascii", "ignore").decode()
    s = re.sub(r"^de ", "", s)
    return s[0].upper()

def entry(a, y, t, src, doi):
    t = html.escape(t, quote=False).replace("'", "&#8217;")
    return (f'            <li>\n'
            f'              <span class="cite-title">{t}</span>\n'
            f'              <span class="cite-meta">{html.escape(a, quote=False)} ({y}). {src}.</span>\n'
            f'              <a class="doi" href="https://doi.org/{doi}">doi.org/{html.escape(doi)}</a>\n'
            f'            </li>')

groups = {}
for r in REFS:
    groups.setdefault(letter(r), []).append(r)
letters = sorted(groups)

blocks = []
for L in letters:
    lis = "\n".join(entry(*r) for r in groups[L])
    blocks.append(f'''        <h2 class="ref-letter" id="ref-{L.lower()}">{L}</h2>
        <ol class="papers">
{lis}
        </ol>''')

jump = " ".join(f'<a href="#ref-{L.lower()}">{L}</a>' for L in letters)
body = f'''    <section class="hero deep">
      <div class="wrap">
        <div class="prose">
          <p class="eyebrow">References</p>
          <h1>Reference material</h1>
          <p class="lede">Every source cited in the book that carries a Digital Object Identifier (DOI), in alphabetical order by first author. Each link opens the source at its publisher.</p>
          <p>Papers from the Society of Petroleum Engineers (SPE) are held in OnePetro, the SPE's online library. Books, inquiry reports and other sources without a DOI are listed in the book's notes. The research programme behind the book is set out by theme on the <a href="research.html">Papers</a> page.</p>
          <p class="todo">Check that every DOI resolves before launch.</p>
        </div>
      </div>
    </section>

    <section>
      <div class="wrap">
        <nav class="az" aria-label="Jump to letter">{jump}</nav>
        <div class="refs">
{chr(10).join(blocks)}
        </div>
      </div>
    </section>
'''

tmpl = (SITE / "book.html").read_text()
head, rest = tmpl.split('  <main id="main">', 1)
foot = rest.split("  </main>", 1)[1]
title = "References | The Culture Ladder"
desc = "Every source cited in The Culture Ladder by Tim Hudson that carries a Digital Object Identifier (DOI), with a link to each."
head = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", head)
head = re.sub(r'(name="description" content=")[^"]*', r"\g<1>" + desc, head)
head = re.sub(r'(property="og:description" content=")[^"]*', r"\g<1>" + desc, head)
head = re.sub(r'(property="og:title" content=")[^"]*', r"\g<1>" + title, head)
head = head.replace("https://thecultureladder.com/book.html", "https://thecultureladder.com/references.html")
head = head.replace(' aria-current="page"', "")
(SITE / "references.html").write_text(head + '  <main id="main">\n' + body + "  </main>" + foot)
print("wrote references.html:", len(REFS), "references,", len(letters), "letters")
