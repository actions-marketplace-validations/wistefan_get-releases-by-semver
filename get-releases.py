from github import Github

import os
import re

repo = os.environ['REPOSITORY']
pattern = os.environ['VERSION_PATTERN']

regex = re.compile(pattern)
github = Github()
repository = github.get_repo(repo)
matching_releases = []
for release in repository.get_releases():
    print(release.title)
    if regex.match(release.title):
        matching_releases.append(release)

for v in matching_releases:
    print(v)