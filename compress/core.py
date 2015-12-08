import gzip
from StringIO import StringIO

def ungzip(data):
    buf = StringIO(data)
    f = gzip.GzipFile(fileobj=buf)
    result = f.read()

    return result


def ungzip_html(resp):
    if resp.info().get('Content-Encoding') == 'gzip':
        return ungzip(resp.read())

    else:
        return resp.read()


