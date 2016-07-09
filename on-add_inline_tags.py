#!/usr/bin/env python
#
# PoC for "inline tags", by bqf, as described in TW-1357
# https://bug.tasktools.org/browse/TW-1357
#
# 
# proposed functionality;
# Turns
#    $ task add I saw :bob: in the :garden:
# Into the equivalent of
#    $ task add I saw :bob: in the :garden: +bob +garden
# And on modify, 
#   a) looks to see if modified task has
#       :tag1: or :tag2:tag3: in description, and if it does, 
#   b) looks to see if +tag1 or +tag2 or tag3 exists, if not
#   c) creates missing tag(s)
# The script creates tags as needed, but never removes them.
# Unlike the original script, this version doesn't remove the 
#    inline :tag1: markiing colons.

import json
import re
import sys

t = json.loads(sys.stdin.readline())

inline_tags = re.findall(r"(?:\A| )@([^ ]+)", t['description'])
for newtag in inline_tags:
 if 'tags' not in t:
  t['tags'] = [newtag]
 elif newtag not in t['tags']:
  t['tags'].append(newtag)
t['description'] = re.sub(r"(\A| )@([^ ]+)", r"\1\2", t['description'])

print(json.dumps(t))
