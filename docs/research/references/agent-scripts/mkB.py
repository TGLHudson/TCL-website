import json
R=[]
def a(note,authors,year,title,source,typ,doi=None,doi_basis=None,url=None,url_kind=None,evidence=None,comment=None):
    R.append(dict(note=note,authors=authors,year=year,title=title,source=source,type=typ,doi=doi,doi_basis=doi_basis,url=url,url_kind=url_kind,evidence=evidence,comment=comment))
# Appendix H
a(0,"National Commission on the BP Deepwater Horizon Oil Spill and Offshore Drilling (Chief Counsel)","2011","Macondo: The Gulf Oil Disaster","Chief Counsel's Report, February 2011","report",
  url="https://www.govinfo.gov/content/pkg/GOVPUB-PR-PURL-gpo4390/pdf/GOVPUB-PR-PURL-gpo4390.pdf",url_kind="official",
  evidence="govinfo.gov search result 'Chief Counsel's Report | 2011' (GPO PURL gpo4390)",comment="Full citation given in Appendix H; the numbered note with the full citation is note 149 (outside this range).")
a(0,"National Commission on the BP Deepwater Horizon Oil Spill and Offshore Drilling","2011","Deep Water: The Gulf Oil Disaster and the Future of Offshore Drilling","Final report to the President, January 2011","report",
  url="https://fdlp.gov/deep-water",url_kind="official",evidence="fdlp.gov 'Deep Water: The Gulf Oil Disaster and the Future of Offshore Drilling' (Federal Depository Library Program page)",
  comment="A govinfo.gov PDF (package GPO-OILCOMMISSION) also appeared but I could not confirm which file is the full report. Full numbered citation is note 150 (outside this range).")
a(0,"National Commission on the BP Deepwater Horizon Oil Spill and Offshore Drilling","2011","Press statement of 17 February 2011","Press statement accompanying the Chief Counsel's Report","web",
  comment="The Commission's own release was not found; only press coverage and the Bartlit Beck law firm's release. The book quotes 'entirely preventable' and 'poor decisions by management'; coverage attributes this to Chief Counsel Fred Bartlit's statement.")
a(0,"Joint Investigation Team (US Coast Guard and BOEMRE), Vol. I: US Coast Guard","2011","Report of Investigation into the Circumstances Surrounding the Explosion, Fire, Sinking and Loss of Eleven Crew Members Aboard the Mobile Offshore Drilling Unit Deepwater Horizon","Volume I, April 2011","report",
  url="https://www.bsee.gov/sites/bsee.gov/files/reports/safety/2-deepwaterhorizon-roi-uscg-volume-i-20110707-redacted-final.pdf",url_kind="official",
  evidence="bsee.gov PDF 'United States Coast Guard' Volume I redacted final; also dco.uscg.mil copy",
  comment="The book gives only 'the Coast Guard's Report of Investigation (April 2011)'; the long title is mine and should be checked against the cover. Hosted copy is the redacted version dated July 2011.")
a(74,"Bureau of Ocean Energy Management, Regulation and Enforcement (BOEMRE) (Joint Investigation Team, Vol. II)","2011","Report Regarding the Causes of the April 20, 2010 Macondo Well Blowout","Joint Investigation Team, Volume II, 14 September 2011","report",
  url="https://www.bsee.gov/sites/bsee.gov/files/reports/safety/dwhfinal.pdf",url_kind="official",
  evidence="bsee.gov search result dwhfinal.pdf, contents covering Macondo well design, temporary abandonment, kick detection",
  comment="Also cited in full in Appendix H (note 0). PDF contents not opened; matched on table of contents.")
a(0,"US District Court, Eastern District of Louisiana (Barbier, J.)","2014","Findings of Fact and Conclusions of Law, Phase One Trial","In re Oil Spill by the Oil Rig 'Deepwater Horizon', MDL 2179, Rec. Doc. 13381-1 (E.D. La., 4 September 2014, revised 9 September 2014)","other",
  comment="Court ruling (reported as 21 F. Supp. 3d 657). Court's MDL 2179 page is laed.uscourts.gov/OilSpill/OilSpill.htm but I did not confirm the document is posted there.")
a(0,"BP (Bly Report)","2010","Deepwater Horizon Accident Investigation Report","BP, 8 September 2010 (including Appendix A, Terms of Reference, 23 April 2010)","report",
  url="https://www.dco.uscg.mil/Portals/9/OCSNCOE/Casualty-Information/DWH-Macondo/BP/BP-DWH-Accident-Investigation-Report-2010.09.08.pdf",url_kind="official",
  evidence="dco.uscg.mil search result 'BP DWH Accident Investigation Report 2010.09.08'; also filed with the SEC as Exhibit 99.3 (sec.gov)",
  comment="Appendix H lists Appendix A (Terms of Reference) separately; merged here. Not confirmed whether the hosted copy includes the appendices. Company report hosted by US Coast Guard.")
a(73,"Baker, J.A. (Chair) (The Baker Panel)","2007","Report of the BP U.S. Refineries Independent Safety Review Panel","Washington, DC: The Baker Panel, January 2007","report",
  url="http://www.bp.com/bakerpanelreport",url_kind="given-in-book",evidence="URL given in note 73; a 2007 trade article confirms BP posted the report there",
  comment="Also in Appendix H. The bp.com link is probably dead; no official live copy found (only a third-party test-corpus mirror, not used).")
a(0,"US District Court, Eastern District of Louisiana (Barbier, J.)","2012","Order and Reasons","In re Oil Spill by the Oil Rig 'Deepwater Horizon', MDL 2179, Rec. Doc. 5634 (E.D. La., 9 February 2012)","other",
  comment="Court order; not found online in searches.")
a(0,"BP","","GDP 4.4-0002, Incident Investigation (BP Group Defined Practice, part of OMS)","BP internal standard","report",
  comment="Book gives a Scribd copy, which is not an acceptable source; no official copy found. No date given. Consider whether to list at all.")
a(0,"US District Court, Eastern District of Louisiana","2013","MDL 2179 trial transcripts, Phase One","Testimony of Dr Frederick E. Beck, Morten Emilsen, John Guide and Lamar McKay","other",comment="Trial record; not searched.")
a(0,"BP (trial exhibits, MDL 2179)","2009/2010","TREX-45036 (Macondo Project Risk Register, 20 June 2009) and TREX-04160 (BP Drilling and Completions entity Risk Register, 12 March 2010)","MDL 2179 trial exhibits","other",comment="Trial exhibits; not searched.")
a(72,"Hopkins, A.","2012","Disastrous Decisions: The Human and Organisational Causes of the Gulf of Mexico Blowout","Sydney: CCH Australia","book",comment="Also in Appendix H.")
a(72,"Hopkins, A.","2008","Failure to Learn: The BP Texas City Refinery Disaster","Sydney: CCH Australia","book",comment="Also in Appendix H.")
# notes
a(59,"Reichers, A.E., Wanous, J.P. & Austin, J.T.","1997","Understanding and Managing Cynicism about Organizational Change","Academy of Management Executive, 11(1), 48-59","journal",
  comment="A DOI 10.5465/AME.1997.9707100659 appeared only as a bare string in one reference list, not attached to this title, so not reported. Worth checking on Crossref.")
a(60,"Seligman, M.E.P.","1975","Helplessness: On Depression, Development, and Death","San Francisco: W.H. Freeman","book")
a(60,"Morrison, E.W. & Milliken, F.J.","2000","Organizational Silence: A Barrier to Change and Development in a Pluralistic World","Academy of Management Review, 25(4), 706-725","journal",
  doi="10.5465/amr.2000.3707697",doi_basis="search",evidence="scilit.com record for this title, AMR 25(4) 706-725, DOI 10.5465/amr.2000.3707697",
  comment="A JSTOR DOI 10.2307/259200 is also attached to it; the 10.5465 one is the publisher's.")
a(61,"Argyris, C.","1990","Overcoming Organizational Defenses: Facilitating Organizational Learning","Boston: Allyn & Bacon","book")
a(62,"Shook, J.","2010","How to Change a Culture: Lessons from NUMMI","MIT Sloan Management Review, 51(2), 63-68","journal",
  url="https://sloanreview.mit.edu/article/how-to-change-a-culture-lessons-from-nummi/",url_kind="official",evidence="sloanreview.mit.edu article page, Winter 2010, vol. 51 no. 2",
  comment="No DOI found (MIT SMR does not generally issue them). Publisher's page is paywalled; the URL is the article's home, not a free copy.")
a(63,"Adler, P.S.","1993","The 'Learning Bureaucracy': New United Motor Manufacturing, Inc.","In B.M. Staw & L.L. Cummings (Eds.), Research in Organizational Behavior, vol. 15, pp. 111-194. Greenwich, CT: JAI Press","chapter",comment="Not searched for a DOI (pre-digital JAI series; unlikely to have one).")
a(64,"Cullen, Lord W.D.","1990","The Public Inquiry into the Piper Alpha Disaster","2 vols. Cm 1310. London: HMSO","report",
  comment="HSE made both volumes free to download in 2018 (The Chemical Engineer, 'Landmark Piper Alpha Cullen report now free to download'), but the only link found was a bit.ly short link, so no direct HSE URL is reported. Worth finding on hse.gov.uk.")
a(65,"UK Government","1992","The Offshore Installations (Safety Case) Regulations 1992","SI 1992/2885","legislation",url="https://www.legislation.gov.uk/uksi/1992/2885",url_kind="given-in-book",evidence="URL given in note 65 (legislation.gov.uk)")
a(66,"US Chemical Safety and Hazard Investigation Board (CSB)","2007","Investigation Report: Refinery Explosion and Fire (15 Killed, 180 Injured), BP Texas City, Texas, March 23, 2005","Report No. 2005-04-I-TX. Washington, DC: CSB","report",
  url="https://purl.fdlp.gov/GPO/LPS100906",url_kind="official",evidence="Texas A&M library catalogue record for this report links the GPO Federal Depository copy purl.fdlp.gov/GPO/LPS100906",
  comment="csb.gov PDF itself did not appear in results (only the CSB news release). The PURL was taken from a catalogue record, not opened. Also cited in Appendix H.")
a(69,"Argyris, C. & Schön, D.A.","1978","Organizational Learning: A Theory of Action Perspective","Reading, MA: Addison-Wesley","book")
a(69,"Hudson, T.G.L., Hudson, P.A.R. & Hudson, P.T.W.","2024","Risk Space and Driving: Elementary Failures in Understanding","SPE-220251-MS. SPE International Health, Safety, Environment, and Sustainability Conference and Exhibition, Abu Dhabi, UAE, 10-12 September 2024","conference",
  doi="10.2118/220251-MS",doi_basis="SPE pattern")
a(69,"Maurino, D.E., Reason, J., Johnston, N. & Lee, R.B.","1998","Beyond Aviation Human Factors: Safety in High Technology Systems","Aldershot: Ashgate","book")
a(69,"Moshansky, V.P. (Commissioner)","1992","Commission of Inquiry into the Air Ontario Crash at Dryden, Ontario: Final Report","3 vols. Ottawa: Privy Council Office","report",
  url="https://epe.lac-bac.gc.ca:443/100/200/301/pco-bcp/commissions-ef/moshansky1992-eng/moshansky1992vol3-eng/moshansky1992vol3-part1-eng.pdf",url_kind="official",
  evidence="Library and Archives Canada PDF 'moshansky1992vol3 part1 eng'; Government of Canada Publications catalogue (publications.gc.ca, CP32-55/1-1992E-PDF etc.) lists all volumes",
  comment="This URL is Vol. 3 part 1 only; a landing page for the whole set on publications.gc.ca would be better, but I could not tell which catalogue record is the set.")
a(69,"International Association of Oil & Gas Producers (IOGP)","2018","Life-Saving Rules","Report 459. London: IOGP","report",
  url="https://www.iogp.org/bookstore/product/life-saving-rules/",url_kind="official",evidence="iogp.org bookstore 'Life-Saving Rules', IOGP Report 459, freely available",
  comment="Bookstore now serves a later revision (version 3.00, reviewed September 2023), not necessarily the 2018 text.")
a(70,"President's Commission on the Accident at Three Mile Island (the Kemeny Commission)","1979","Report of the President's Commission on the Accident at Three Mile Island: The Need for Change: The Legacy of TMI","Washington, DC: US Government Printing Office","report",
  url="https://archive.org/download/needforchangeleg00unitrich/needforchangeleg00unitrich.pdf",url_kind="official",evidence="archive.org scan 'needforchangeleg00unitrich' (university library scan); HathiTrust full view also listed",
  comment="Internet Archive scan of a library copy of a US government publication (public domain), not an official-site copy; url_kind 'official' is a stretch.")
a(70,"Rees, J.V.","1994","Hostages of Each Other: The Transformation of Nuclear Safety since Three Mile Island","Chicago: University of Chicago Press","book")
a(71,"Deming, W.E.","1986","Out of the Crisis","Cambridge, MA: MIT Center for Advanced Engineering Study","book")
a(72,"Hopkins, A.","2019","Organising for Safety: How Structure Creates Culture","Sydney: CCH Australia","book")
a(75,"Federal Aviation Administration (FAA)","","Safety Management System (SMS)","Web page","web",url="https://www.faa.gov/about/initiatives/sms",url_kind="given-in-book",evidence="URL given in note 75",comment="No date or access date in the book. Not checked.")
a(76,"Federal Aviation Administration (FAA)","2018","Out Front on Airline Safety: Two Decades of Continuous Evolution","Fact sheet, 2 August 2018","web",url="https://www.faa.gov/newsroom/out-front-airline-safety-two-decades-continuous-evolution",url_kind="given-in-book",
  evidence="URL given in note 76; FAA fact sheets index lists the title dated 2 August 2018",comment="Mentions the Commercial Aviation Safety Team (CAST).")
a(78,"Brady, S.","2019","Review of all fatal accidents in Queensland mines and quarries from 2000 to 2019","Brisbane: Department of Natural Resources, Mines and Energy, December 2019. Tabled in the Queensland Parliament","report",
  url="https://www.parliament.qld.gov.au/Work-of-the-Assembly/Tabled-Papers/docs/5620t197/5620t197.pdf",url_kind="given-in-book",evidence="Same URL returned by search (Queensland Parliament tabled papers)")
a(79,"Power, M.","1997","The Audit Society: Rituals of Verification","Oxford: Oxford University Press","book",comment="Book carries a flag on the edition year (1997 vs 1999 printing); not resolved here.")
a(80,"European Parliament and Council","2012","Directive 2012/18/EU of the European Parliament and of the Council of 4 July 2012 on the control of major-accident hazards involving dangerous substances (Seveso III)","Official Journal of the European Union","legislation",url="https://eur-lex.europa.eu/eli/dir/2012/18/oj",url_kind="given-in-book",evidence="URL given in note 80 (EUR-Lex)")
a(81,"Sendelbach, S. & Funk, M.","2013","Alarm Fatigue: A Patient Safety Concern","AACN Advanced Critical Care, 24(4), 378-386","journal",
  comment="A DOI '10.4037/NCI.0b013e3182a903f9' appeared only in another paper's reference list, with an odd prefix; not confirmed, so not reported. Worth a Crossref or PubMed check.")
a(81,"The Joint Commission","2013","Medical Device Alarm Safety in Hospitals","Sentinel Event Alert 50, 8 April 2013","report",url="https://jointcommission.org/sea_issue_50",url_kind="official",evidence="jointcommission.org 'Sentinel Event Alert 50: Medical device alarm safety in hospitals'")
a(84,"Meyer, J.W. & Rowan, B.","1977","Institutionalized Organizations: Formal Structure as Myth and Ceremony","American Journal of Sociology, 83(2), 340-363","journal",
  doi="10.1086/226550",doi_basis="search",evidence="journals.uchicago.edu/doi/10.1086/226550 (publisher page for this title)")
a(87,"Hudson, T.G.L. & Hudson, P.A.R.","2026","Transitions in Safety Culture: Practical Risk-Space Tools for Deciding When and How to Change","SPE-233663-MS. SPE International Health, Safety, Environment, and Sustainability Conference and Exhibition, Abu Dhabi, UAE, 7-9 September 2026. Society of Petroleum Engineers","conference",
  doi="10.2118/233663-MS",doi_basis="SPE pattern",comment="Book says 'in press'; the DOI may not resolve yet.")
a(88,"Center for Chemical Process Safety (CCPS) & Energy Institute","2018","Bow Ties in Risk Management: A Concept Book for Process Safety","CCPS of the American Institute of Chemical Engineers and the Energy Institute. ISBN 978-1-119-49039-5","book")
a(93,"Shell International Exploration and Production","2001","HSE: Understanding Your Culture","The Hague: Shell International Exploration and Production (EP 2001-5124)","report",
  comment="Hearts and Minds tool, now published by the Energy Institute (see note 214). Not searched; probably commercial or member-only.")
a(94,"Covey, S.R.","1989","The Seven Habits of Highly Effective People: Restoring the Character Ethic","New York: Simon and Schuster","book")
a(96,"Hudson, T.G.L. & Hudson, P.A.R.","2026","Transitions, Timing, and Tools: Choosing What Fits the Risk Space and Safety Culture","SPE-233645-MS. Special Session, SPE International Health, Safety, Environment, and Sustainability Conference and Exhibition, Abu Dhabi, UAE, 7-9 September 2026. Society of Petroleum Engineers","conference",
  doi="10.2118/233645-MS",doi_basis="SPE pattern",comment="Book says 'in press'; the DOI may not resolve yet.")
a(98,"High Court of England and Wales (Fraser J)","2019","Bates and Others v Post Office Ltd (No 6: Horizon Issues)","[2019] EWHC 3408 (QB)","legislation",
  url="https://caselaw.nationalarchives.gov.uk/ewhc/qb/2019/3408",url_kind="official",evidence="The National Archives Find Case Law: 'Bates & Ors v the Post Office Ltd (No 6: Horizon Issues) (Rev 1)'",
  comment="Case law: classed as legislation for want of a better type; could be 'other'. The '(No 6: Horizon Issues)' is the official title, the book gives the short name.")
a(98,"Court of Appeal (Criminal Division)","2021","Hamilton and Others v Post Office Ltd","[2021] EWCA Crim 577","legislation",
  url="https://caselaw.nationalarchives.gov.uk/ewca/crim/2021/577",url_kind="official",evidence="The National Archives Find Case Law: 'Hamilton & Ors v Post Office Ltd'; PDF also on judiciary.uk",
  comment="Case law; see comment on Bates.")
a(98,"Post Office Horizon IT Inquiry (Chair: Sir Wyn Williams)","2021","Post Office Horizon IT Inquiry","Statutory inquiry from 1 June 2021","web",
  url="https://www.postofficehorizoninquiry.org.uk/",url_kind="official",evidence="postofficehorizoninquiry.org.uk 'Welcome to the Post Office Horizon IT Inquiry website'",
  comment="Not a single document: the book cites the inquiry generally for conviction figures. Volume 1 of the Final Report is now published.")
a(100,"Crosby, P.B.","1979","Quality Is Free: The Art of Making Quality Certain","New York: McGraw-Hill","book")
a(101,"International Civil Aviation Organization (ICAO)","2002","Line Operations Safety Audit (LOSA)","Doc 9803","report",
  comment="Sold by ICAO (store.icao.int); not freely available from ICAO. A copy on ukfsc.co.uk was not used as its authorisation is unclear.")
a(102,"Merton, R.K.","1940","Bureaucratic Structure and Personality","Social Forces, 18(4), 560-568","journal",comment="No DOI found in search; JSTOR record confirms volume and pages.")
a(105,"Perrow, C.","1984","Normal Accidents: Living with High-Risk Technologies","New York: Basic Books","book")
a(105,"Hopkins, A.","1999","The limits of normal accident theory","Safety Science, 32, 93-102","journal",
  url="https://openresearch-repository.anu.edu.au/items/c9046717-d06d-4e99-8a77-d468c025df4f",url_kind="open-access",
  evidence="ANU Open Research repository record 'The limits of normal accident theory' (Safety Science 32(2-3) 93-102), listed open access",
  comment="Elsevier DOI exists under prefix 10.1016/S0925-7535 but the full string did not appear in results, so not reported. Check the ANU record.")
a(106,"Chapman, J.C.","1998","Collapse of the Ramsgate Walkway","The Structural Engineer, 76(1)","journal",
  url="https://www.istructe.org/journal/volumes/volume-76-(published-in-1998)/issue-1/collapse-of-the-ramsgate-walkway/",url_kind="official",
  evidence="istructe.org journal page 'Collapse of the Ramsgate Walkway', vol. 76 issue 1",comment="No DOI found. Publisher page is paywalled (members free); it is the article's home, not a free copy.")
a(107,"Onderzoeksraad voor Veiligheid (Dutch Safety Board)","2012","Instorten van het dak van de aanbouw van het stadion van FC Twente, te Enschede, 7 juli 2011","Den Haag: Onderzoeksraad voor Veiligheid, July 2012. Project number M2011BD0707-01","report",
  url="https://onderzoeksraad.nl/en/onderzoek/collapsed-roof-grolsch-veste-7-july-2011/",url_kind="official",
  evidence="onderzoeksraad.nl 'Collapsed roof Grolsch Veste, 7 July 2011' investigation page",
  comment="Book gives only https://www.onderzoeksraad.nl; this is the investigation page on that site. Did not confirm the report PDF is linked from it.")
a(108,"Hudson, P.A.R. & Hudson, T.G.L.","2026","Construction as a Moving Risk Ecology: How Trade Integration Raises Complexity and Changes the Culture Needed to Hold Barriers","SPE-233678-MS. SPE International Health, Safety, Environment, and Sustainability Conference and Exhibition, Abu Dhabi, UAE, 2026. Society of Petroleum Engineers","conference",
  doi="10.2118/233678-MS",doi_basis="SPE pattern",comment="Book says 'in press, accepted for presentation'; the DOI may not resolve yet.")
a(109,"Hudson, T.G.L., Hudson, P.A.R. & Hudson, P.T.W.","2024","Non-compliance in complex operations: A case study-led discussion","SPE-220344-MS. Abu Dhabi, UAE, 10-12 September 2024. Society of Petroleum Engineers","conference",
  doi="10.2118/220344-MS",doi_basis="SPE pattern",comment="Title in sentence case as the book gives it.")
a(111,"Snook, S.A.","2000","Friendly Fire: The Accidental Shootdown of U.S. Black Hawks over Northern Iraq","Princeton, NJ: Princeton University Press","book")
a(112,"Frontline Consultants","2012","London 2012: The Construction (Design and Management) Regulations 2007, Dutyholder roles and impact","HSE Research Report RR941. Commissioned by the Olympic Delivery Authority; funded by the Health and Safety Executive and the Institution of Civil Engineers","report",
  url="https://www.hse.gov.uk/research/rrpdf/rr941.pdf",url_kind="given-in-book",evidence="URL given in note 112; search confirms HSE page hse.gov.uk/research/rrhtm/rr941.htm")
a(112,"Healey, N. & Sugden, C.","2012","Safety culture on the Olympic Park","HSE Research Report RR942. Buxton: Health and Safety Laboratory","report",
  url="https://www.hse.gov.uk/research/rrpdf/rr942.pdf",url_kind="given-in-book",evidence="URL given in note 112; search confirms HSE page hse.gov.uk/Research/rrhtm/rr942.htm")
a(114,"Hudson, P.T.W., van der Graaf, G.C., Verschuur, W.L.G., Lawton, R., Parker, D. & Reason, J.T.","1998","Bending the Rules: Violation of Procedures","SPE International Conference on Health, Safety and Environment in Oil and Gas Exploration and Production, Caracas, Venezuela, 7-10 June 1998. Society of Petroleum Engineers","conference",
  comment="SPE paper number not given in the book and not found in search, so no DOI. Needs the number from OnePetro.")
a(114,"Verschuur, W.L.G., Hudson, P.T.W. & Parker, D.","1996","Violations of Rules and Procedures: Results of Item Analysis and Tests of the Behavioural Cause Model","Leiden University report for Shell International Exploration and Production (internal)","report",
  comment="Internal report, not public. Consider leaving it off the public page.")
a(116,"Reason, J.","1997","Managing the Risks of Organizational Accidents","Ashgate","book",comment="Book gives no place of publication (Aldershot).")
a(116,"Wagenaar, W.A., Hudson, P.T.W. & Reason, J.T.","1990","Cognitive failures and accidents","Applied Cognitive Psychology, 4(4), 273-294","journal",
  doi="10.1002/acp.2350040405",doi_basis="search",evidence="scilit.com record 'Cognitive failures and accidents', Applied Cognitive Psychology 4(4) 273-294, DOI 10.1002/acp.2350040405")
json.dump(R,open('/tmp/claude-0/-home-user/ebcd420f-94ce-55f8-a8c9-103d7b678fc3/scratchpad/refs_B.json','w'),indent=2,ensure_ascii=False)
print(len(R),sum(1 for r in R if r['doi']),sum(1 for r in R if r['url']),sum(1 for r in R if not r['doi'] and not r['url']))
