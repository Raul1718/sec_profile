import codecs
import logging
import os
import sqlite3
from urlparse import urlparse
import datetime
import tldextract

def list2str(l):
    """

    :param l:
    :return:
    """
    st_list = []
    for i in l:
        item = "\t".join(i)
        st_list.append(item)
    return os.linesep.join(st_list)


def path(*paths):
    """
    :param paths:
    :return:
    """
    MODULE_PATH = os.path.dirname(os.path.realpath(__file__))
    # ROOT_PATH = os.path.join(MODULE_PATH, os.path.pardir)
    return os.path.abspath(os.path.join(MODULE_PATH, *paths))


def parse_url(url, isupdate=False):
    """

    :param url:
    :return:
    """
    o = urlparse(url)
    extract = tldextract.TLDExtract()
    if isupdate:
        extract.update()
    ext = extract(url)
    # o.schema, o.netloc,o.path
    # ext.subdomain, ext.suffix, ext.domain + "." + ext.suffix
    return [o, ext]


class SQLiteOper(object):
    """

    """

    def __init__(self, dbpath="", db_is_new=False, schemafile=""):
        if db_is_new:
            print "create new schema"
            if os.path.exists(dbpath):
                os.remove(dbpath)
            with codecs.open(schemafile, mode='rb', encoding='utf-8', errors='ignore') as f:
                schema = f.read()
                self.sqlite3_conn = sqlite3.connect(dbpath, timeout=20)
                self.executescript(schema)
        self.sqlite3_conn = sqlite3.connect(dbpath, timeout=20)

    def __del__(self):
        self.sqlite3_conn.close()

    def executescript(self, sql_script):
        self.sqlite3_conn.executescript(sql_script)

    def query(self, query_statement, operate_dict=None):
        """
        select statement
        :param query:
        :return:
        """

        logging.debug(query_statement)
        cursor = self.sqlite3_conn.cursor()
        if operate_dict is not None:
            cursor.execute(query_statement, operate_dict)
        else:
            cursor.execute(query_statement)
        # row_count = len(cursor.fetchall())
        # if row_count != 0:
        #    print "%s %d" % (query_statement, row_count)
        for line in cursor.fetchall():
            yield line

    def executemany(self, operate_statement, operate_list=None):
        """insert/update"""
        # print insert_statement
        logging.debug(operate_statement)
        cursor = self.sqlite3_conn.cursor()


        cursor.executemany(operate_statement, operate_list)

        self.sqlite3_conn.commit()

    def execute(self,sql):
        """

        :param sql:
        :return:
        """
        logging.debug(sql)
        cursor = self.sqlite3_conn.cursor()

        cursor.execute(sql)

        self.sqlite3_conn.commit()


def get_special_date(delta=0, format="%Y%m%d"):
    """
    now 20160918, default delata = 0
    :return:
    """
    date = (datetime.date.today() + datetime.timedelta(days=delta)).strftime(format)
    return date