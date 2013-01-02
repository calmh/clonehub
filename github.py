import re
import json
import urllib2


def _repos(url):
    try:
        apidata = urllib2.urlopen(url)
    except urllib2.HTTPError, e:
        print ' * GitHub API error: %d %s' % (e.code, e.msg)
        return []
    repos = json.loads(apidata.read())

    if 'Link' in apidata.info():
        links = apidata.info()['Link']
        pm = re.search('<(http[^>]+)>;\s*rel="next"', links)
        if pm:
            next = pm.group(1)
            repos.extend(_repos(next))

    return repos


def repos(user):
    return _repos('https://api.github.com/users/%s/repos' % user)

