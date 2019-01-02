import codecs
import logging
import re
from urlparse import urlparse

import tldextract


def parse_url(url, isupdate=False):
    """

    :param url:
    :return:
    """
    o = urlparse(url)
    scheme = o.scheme
    netloc = o.netloc
    path = o.path
    extract = tldextract.TLDExtract()
    if isupdate:
        extract.update()
    ext = extract(url)
    return [scheme, ext.subdomain, ext.suffix, ext.domain + "." + ext.suffix, netloc, path,url]


def parse_sec_item(fname):
    """

    :param fname:
    :return:
    """
    with codecs.open(fname, mode='rb') as fr:
        for line in fr:
            line = line.strip()
            if fname.find("xuanwu") != -1:
                source = "xuanwu"
                parts = re.split(r'\t', line, maxsplit=5)
                day = parts[0]
                twitter_id = parts[1]
                tag = parts[2]
                urls = parts[3]
                title = parts[4]
            elif fname.find('secwiki') != -1:
                source = "secwiki"
                parts = re.split(r'\t', line, maxsplit=4)
                day = parts[0]
                tag = parts[1]
                urls = parts[2]
                title = parts[3]
                twitter_id = ""
            try:
                urls_list = eval(urls)
                for url in urls_list:
                    url_details = parse_url(url)

                print source, day, tag, "\t".join(url_details), twitter_id, title
            except Exception as e:
                logging.error("[URLS_EVAL_ERROR]: %s %s" % (str(e), line))


if __name__ == "__main__":
    """
    """

    fname_secwiki = "data/secwiki/secwiki.txt"
    fname_xuanwu = "data/xuanwu/xuanwu.txt"
    for fname in [fname_secwiki, fname_xuanwu]:
        parse_sec_item(fname)
