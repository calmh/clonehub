import re
import json
import urllib2
import base64
import os


def _repos(url):
    try:
        req = urllib2.Request(url)
        try:
            username = os.environ['GITHUB_USERNAME']
            token = os.environ['GITHUB_TOKEN']
            base64string = base64.encodestring('%s:%s' % (username, token)).replace('\n', '')
            req.add_header('Authorization', 'Basic ' + base64string)
        except NameError:
            pass
        apidata = urllib2.urlopen(req)
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

def my_repos():
    return _repos('https://api.github.com/user/repos')
