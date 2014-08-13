# -*- coding: utf-8  -*-
import pywikibot
import pywikibot.data.wikidataquery as pwq
import json

site = pywikibot.Site("wikidata", "wikidata")
repo = site.data_repository()
#page = pywikibot.Page(site, u"Raimond de Prinhac")
#item = pywikibot.ItemPage.fromPage(page)
#dictionary = item.get()
#print dictionary

# define repo
site = pywikibot.Site("fr", "wikipedia")
repo = site.data_repository()

# retrieve airport list 106:2937507
q= pwq.HasClaim(106, items=[2937507])
dat = pwq.WikidataQuery(cacheMaxAge=600).query(q)
items = dat['items']
for i in items:
    item = pywikibot.ItemPage(repo, "Q%s" % i)
    item.get()
    print item.labels
