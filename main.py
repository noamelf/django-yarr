
from bs4 import BeautifulSoup
import requests as req
from feedgen.feed import FeedGenerator

resp = req.get('https://www.haaretz.co.il/misc/writers/WRITER-1.681400')

soup = BeautifulSoup(resp.text, 'lxml')

#print(soup.title)
#subtitle
print(soup.select_one('#pageRoot > section.n.o.nd > div > article.gp.ns.as.n.ac.nt.nu.nv.nw.nx.ny.nz.oa.ob.oc.od > div.oi.oj.ok.ol.om.on.oo.op.oq').text)
#time
print(soup.select_one('#pageRoot > section.n.o.nd > div > article.gp.ns.as.n.ac.nt.nu.nv.nw.nx.ny.nz.oa.ob.oc.od > footer > time').text)
#author
print(soup.select_one('#pageRoot > section.n.o.nd > div > article.gp.ns.as.n.ac.nt.nu.nv.nw.nx.ny.nz.oa.ob.oc.od > footer > span.oz').text)
#image
print(soup.select_one('#pageRoot > section.n.o.nd > div > article.gp.ns.as.n.ac.nt.nu.nv.nw.nx.ny.nz.oa.ob.oc.od > div.oe.as.of').getText)
author =soup.select_one('#pageRoot > section.n.o.nd > div > article.gp.ns.as.n.ac.nt.nu.nv.nw.nx.ny.nz.oa.ob.oc.od > footer > span.oz').text





fg = FeedGenerator()
fg.id('https://www.haaretz.co.il/misc/writers/WRITER-1.681400')
fg.title(soup.select_one('#pageRoot > section.n.o.nd > div > article.gp.ns.as.n.ac.nt.nu.nv.nw.nx.ny.nz.oa.ob.oc.od > div.oi.oj.ok.ol.om.on.oo.op.oq').text)
fg.author({'name': author})
#fg.link(href='http://example.com', rel='alternate')
fg.logo(soup.select_one('#pageRoot > section.n.o.nd > div > article.gp.ns.as.n.ac.nt.nu.nv.nw.nx.ny.nz.oa.ob.oc.od > div.oe.as.of').getText)
fg.subtitle(soup.select_one('#pageRoot > section.n.o.nd > div > article.gp.ns.as.n.ac.nt.nu.nv.nw.nx.ny.nz.oa.ob.oc.od > footer > time').text)
#fg.link(href='http://larskiesow.de/test.atom', rel='self')
#fg.language('en')

rssfeed= fg.rss_str(pretty=True)# Get the RSS feed as string
fg.rss_file("rss.xml")# Write the RSS feed to a file