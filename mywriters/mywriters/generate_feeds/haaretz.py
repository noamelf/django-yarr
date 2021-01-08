import csv
import logging
from mywriters import generate_feeds
import os
from datetime import datetime

import requests as req
from bs4 import BeautifulSoup
from feedgen.feed import FeedGenerator

logger = logging.getLogger(__name__)


def generate_feed(author, url, entries):
    fg = FeedGenerator()
    fg.link(href=url)
    fg.author({"name": author})
    fg.title(author)
    fg.description(author)
    fg.language("he")
    fg.image()

    for entry in entries:
        fe = fg.add_entry()
        fe.id(entry["url"])
        fe.title(entry["title"])
        fe.link(href=entry["url"])
        fe.pubDate(entry["date"])

    return fg.rss_str().decode()


def get_writer_page(writer_url):
    logger.info(f"Fetching writer: {writer_url}")
    resp = req.get(writer_url)
    soup = BeautifulSoup(resp.text, "lxml")
    author = soup.find_all("section")[0].find_all("div")[2].text
    entries = []
    for elem in soup.find_all("article"):
        url = elem.find_all("a")[0].attrs["href"]
        title = elem.find_all("a")[0].text
        if not title:
            title = elem.find_all("a")[1].text
        if elem.find("time"):
            date = elem.find("time").attrs["datetime"]
        else:
            date = str(datetime.now().astimezone())

        entries.append({"title": title, "url": "http:" + url, "date": date})

    return author, entries


def get_writers():
    resp = req.get("https://www.haaretz.co.il/misc/editors")
    soup = BeautifulSoup(resp.text, "lxml")

    authors = soup.find_all("div")[3].find_all("ul")[4:9]
    # notice: if the page will be changed, this code might not work

    writers = (
        authors[0].find_all("a")
        + authors[1].find_all("a")
        + authors[2].find_all("a")
        + authors[3].find_all("a")
        + authors[4].find_all("a")
    )

    logger.info(f"Found {len(writers)} writers")

    for writer in writers:
        yield writer.text, f'https:{writer.attrs["href"]}'


def create_haaretz_feeds():
    for name, url in get_writers():
        author, entries = get_writer_page(url)
        rss = generate_feed(author, url, entries)
        yield (author, url, rss)
