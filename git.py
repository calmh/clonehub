import commands


def _command(cmd):
    s, o = commands.getstatusoutput(cmd)
    if s != 0:
        for line in o.split('\n'):
            print '   * ' + line
        return
    lines = o.split('\n')
    for line in lines:
        if line.find('FETCH_HEAD') >= 0:
            continue
        if line.find('->') >= 0:
            print line


def fetch(repo):
    print ' . Fetching %s' % repo
    _command('cd %s ; git remote update -p' % repo)


def clone(repo, dst, checkout=False):
    print ' + Cloning %s' % repo
    if checkout:
        mirror = ''
    else:
        mirror = '--mirror'
    _command('git clone %s %s %s' % (mirror, repo, dst))


def gc(repo):
    print ' . Garbage collecting %s' % repo
    _command('cd %s ; git gc' % repo)
