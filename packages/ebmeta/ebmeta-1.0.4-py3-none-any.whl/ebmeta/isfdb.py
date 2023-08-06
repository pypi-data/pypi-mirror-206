import sys
import urllib
import logging

import click
import requests

logger = logging.getLogger(__name__)


class ISFDBConnection:

    def __init__(self, host="www.isfdb.org"):
        self.base_url = f'https://{host}'
        self.session = requests.Session()

    def _get(self, url, *a, **kw):
        url = f'{self.base_url}{url}'
        response = self.session.get(url, *a, **kw)
        logging.debug("URL %s got %s", url, response.text)
        return response

    def _post(self, url, *a, **kw):
        url = f'{self.base_url}{url}'
        return self.session.post(url, *a, **kw)

    @property
    def connection(self):
        if self._connection is None:
            self.connection = httplib.HTTPConnection(self.host)

    def _firstQueryArgTo(self, line, pretext):
        if pretext not in line:
            return None
        return line.split(pretext, 1)[1].split('"', 1)[0]

        i = line.find(pretext)
        if i > -1:
            iquote = line.find('"', i)
            return line[i + len(pretext):iquote]
        return None

    def getPubListIDFromISBN(self, isbn):
        if isbn is None:
            return None
        headers = {
                "Content-type": "application/x-www-form-urlencoded",
                "Accept": "text/plain"
                }
        params ={'type': 'ISBN', 'arg': isbn }
        response = self._post("/cgi-bin/se.cgi", headers=headers, data=params)

        # <td><a href="http://www.isfdb.org/cgi-bin/pl.cgi?84332">84332</a></td>
        return self._firstQueryArgTo(response.text, "pl.cgi?")

    def getTitleIDFromPubListID(self, publistid):
        if publistid is None:
            return None
        response = self._get(f"/cgi-bin/pl.cgi?{publistid}")
        return self._firstQueryArgTo(response.text, "title.cgi?")

    def _findTextFieldAfter(self, line, pretext):
        i = line.find(pretext)
        if i < 0: return None
        pre = line.find(">", i) + 1
        post = line.find("<", pre)
        if pre > post: return None
        return line[pre:post]

    def getSeriesInfoFromTitleID(self, titleid):
        if titleid is None:
           return None, None
        response = self._get(f"/cgi-bin/title.cgi?{titleid}")
        text = response.text
        '''    
        <br>
        <b>Series:</b> <a href="http://www.isfdb.org/cgi-bin/pe.cgi?11694">Paladin of Shadows</a>
        <br>
        <b>Series Number:</b> 3
        <br>
        '''
    
        series = self._findTextFieldAfter(text, "pe.cgi")
        seriesNum = self._findTextFieldAfter(text, "Series Number:")
    
        #print "debug: text is %s" % repr(text)
        #print "debug: series is %s number %s" % repr(series), repr(seriesNum)

        return series, seriesNum

    def getSeriesInfoFromISBN(self, isbn):
        plid = self.getPubListIDFromISBN(isbn)
        tid = self.getTitleIDFromPubListID(plid)
        return self.getSeriesInfoFromTitleID(tid)





@click.group()
@click.option('--debug', is_flag=True, default=False, help='enable debug output for ebmeta')
@click.option('--debugall', is_flag=True, default=False, help='enable debug output for everything')
def cli(debug, debugall):
    if debug:
        logger.setLevel(logging.DEBUG)
    if debugall:
        logging.getLogger('').setLevel(logging.DEBUG)


@cli.command()
@click.argument('isbn', nargs=1, required=True)
def by_isbn(isbn):

    
   print(f"Looking up {isbn}...")

   isfdb = ISFDBConnection()

   plid = isfdb.getPubListIDFromISBN(isbn)
   print(f"Publication Listing ID: {plid}")
   tid = isfdb.getTitleIDFromPubListID(plid)
   print(f"Title ID: {tid}")
   series, bookno = isfdb.getSeriesInfoFromISBN(isbn)
   print(f"Series: {series} (book {bookno})")


if __name__ == '__main__':
    cli()
