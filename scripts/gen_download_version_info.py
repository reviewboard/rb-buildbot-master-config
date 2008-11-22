#!/usr/bin/env python

import os
from pkg_resources import parse_version


downloads_dir = "/var/www/review-board.org/htdocs/downloads"
version_map = {
    "nightlies": {},
    "bleeding": {},
}

for root, dirs, files in os.walk(downloads_dir):
    if os.path.basename(root) not in version_map:
        continue

    for filename in files:
        for ext in [".egg", ".tar.gz", ".zip", ".exe"]:
            if filename.endswith(ext):
                dirname = os.path.basename(root)

                project, rest = filename.split("-", 1)

                version = filename[len(project) + 1:-len(ext)]
                if (version.endswith("-py2.4") or
                    version.endswith("-py2.5") or
                    version.endswith("-py2.6")):
                    version = version[:-6]

                if project in version_map[dirname]:
                    cur_version = version_map[dirname][project]['version']

                    if (parse_version(cur_version) >= version):
                        break

                version_map[dirname][project] = {
                    'filename': filename,
                    'version': version,
                }
                break

print version_map
