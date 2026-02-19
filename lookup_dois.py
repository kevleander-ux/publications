import requests
import time
import urllib.parse

YOUR_EMAIL = "kevin.leander@vanderbilt.edu"

publications = [
    # Journal Articles
    {"title": "Critical posthumanist literacy: Building theory for reading, writing, and living ethically with everyday artificial intelligence", "author": "Burriss Leander"},
    {"title": "Generative AI and composing: An intergenerational conversation among literacy scholars", "author": "Enriquez Leander"},
    {"title": "We got so much better at reading each other's energy: Knowing, acting, and attuning as an improv ensemble", "author": "Leander Carter-Stone Supica"},
    {"title": "Rethinking sociocultural notions of learning in the digital era", "author": "Unlusoy Leander de Haan"},
    {"title": "Affect theory in reading research: Imagining the radical difference", "author": "Boldt Leander"},
    {"title": "Critical literacy for a posthuman world: When people read, and become, with machines", "author": "Leander Burriss"},
    {"title": "Ways with worlds: Bringing improvisational theater into play with reading", "author": "Tanner Leander Carter-Stone"},
    {"title": "Design, desire, and difference", "author": "Leander Boldt"},
    {"title": "Readings and experiences of multimodality", "author": "Leander Aziz Botzakis"},
    {"title": "Becoming through the break: A post-human account of a child's play", "author": "Boldt Leander"},
    {"title": "The embodied rhythms of learning: From learning across settings to learners crossing settings", "author": "Leander Hollett"},
    {"title": "Networked identity: How immigrant youth employ online identity resources", "author": "Prinsen de Haan Leander"},
    {"title": "Moving, feeling, desiring, teaching", "author": "Boldt Lewis Leander"},
    {"title": "Challenging ideals of connected learning: the networked configurations for learning of migrant youth in the Netherlands", "author": "de Haan Leander Unlusoy Prinsen"},
    {"title": "Editorial on Media and Migration: Learning in a Globalized World", "author": "Leander de Haan"},
    {"title": "ChipScope: Actually, that funny way of looking at it works pretty well", "author": "Leander"},
    {"title": "Learning potential in youth's online networks: A multilevel approach", "author": "Unlusoy de Haan Leander Volker"},
    {"title": "Rereading A Pedagogy of Multiliteracies: Texts, identities, and futures", "author": "Leander Boldt"},
    {"title": "The construction of ethnic boundaries in classroom interaction through social space", "author": "de Haan Leander"},
    {"title": "From I-Search to iSearch 2.0", "author": "Alvey Phillips Smith Leander"},
    {"title": "The changing social spaces of learning: Mapping new mobilities", "author": "Leander Phillips Taylor"},
    {"title": "Editorial: English afloat on a digital sea", "author": "Beavis Davies Leander"},
    {"title": "Complex positioning: Teachers as agents of curricular and pedagogical reform", "author": "Leander Osborne"},
    {"title": "The aesthetic production and distribution of image/subjects among online youth", "author": "Leander Frank"},
    {"title": "Mapping literacy spaces in motion: A rhizomatic analysis of a classroom literacy performance", "author": "Leander Rowe"},
    {"title": "Literacy networks: Following the circulation of texts, bodies, and objects in the schooling and online gaming of one youth", "author": "Leander Lovvorn"},
    {"title": "They took out the wrong context: Uses of time-space in the practice of positioning", "author": "Leander"},
    {"title": "Ethnographic studies of positioning and subjectivity: An introduction", "author": "Holland Leander"},
    {"title": "Writing travelers' tales on New Literacyscapes", "author": "Leander"},
    {"title": "Tracing the everyday sitings of adolescents on the Internet: A strategic adaptation of ethnography across online and offline spaces", "author": "Leander McKim"},
    {"title": "Locating Latanya: The situated production of identity artifacts in classroom interaction", "author": "Leander"},
    {"title": "Polycontextual construction zones: Mapping the expansion of schooled space and identity", "author": "Leander"},
    {"title": "Silencing in classroom interaction: Producing and relating social spaces", "author": "Leander"},
    {"title": "This is our freedom bus going home right now: Producing and hybridizing space-time contexts in pedagogical discourse", "author": "Leander"},
    {"title": "Case studies of a virtual school", "author": "Hinn Leander Bruce"},
    {"title": "Laboratories for writing", "author": "Leander"},
    {"title": "You understand but you don't believe it: Tracing the stabilities and instabilities of interaction in a physics classroom", "author": "Leander Brown"},
    {"title": "Searching for digital libraries in education: Why computers cannot tell the story", "author": "Bruce Leander"},
]


def make_crossref_url(title, author):
    params = {
        "query.title": title,
        "query.author": author,
        "rows": "1",
        "select": "DOI,title,author",
        "mailto": YOUR_EMAIL,
    }
    return "https://api.crossref.org/works?" + urllib.parse.urlencode(params)


def lookup_doi(title, author):
    url = make_crossref_url(title, author)
    try:
        r = requests.get(url, timeout=10)
        items = r.json()["message"]["items"]
        if items:
            return items[0].get("DOI"), items[0].get("title", [""])[0]
    except Exception as e:
        print(f"  Error: {e}")
    return None, None


print(f"{'#':<4} {'DOI':<45} {'Matched Title'}")
print("-" * 120)

results = []
for i, pub in enumerate(publications, 1):
    doi, matched_title = lookup_doi(pub["title"], pub["author"])
    results.append({"input_title": pub["title"], "author": pub["author"], "doi": doi, "matched_title": matched_title})
    status = doi if doi else "NOT FOUND"
    print(f"{i:<4} {status:<45} {(matched_title or '')[:70]}")
    time.sleep(0.2)  # Be polite to Crossref

# Write results to TSV
with open("leander_dois.tsv", "w") as f:
    f.write("Input Title\tAuthor Query\tDOI\tMatched Title\n")
    for r in results:
        f.write(f"{r['input_title']}\t{r['author']}\t{r['doi'] or ''}\t{r['matched_title'] or ''}\n")

print("\nResults saved to leander_dois.tsv")
