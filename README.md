clonehub
========

Keep a local mirror of all your (or someone elses) public GitHub repositories.

Usage
-----

Hop into the destination directory, run `clonehub` while passing it one or more
user names as parameters. All public repositories belonging to those users will
be cloned, or fetched if they already exit.

```
jb@zlogin:~ % cd /srv/bk/GitHub 
jb@zlogin:/srv/bk/GitHub % clonehub calmh nymnetworks
Backing up calmh
 . Fetching Aggregator.git
 . Fetching beets.git
 + Cloning https://github.com/calmh/clonehub.git
 . Fetching ClusteredPoller.git
 . Fetching facter.git
...
```

Cron it, and live happily everafter.

License
-------

MIT
