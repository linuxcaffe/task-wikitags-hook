#!/usr/bin/env python
import json
import re
import sys


def add_inline_tags(task):
    inline_tags = re.findall(r"(?:\A| ):([^ ]+):", task['description'])
    for tags in inline_tags:
       for tag in tags.split(":"):
           if 'tags' not in task:
              task['tags'] = [tag]
           elif tag not in task['tags']:
              task['tags'].append(tag)

    print(json.dumps(task))


old = sys.stdin.readline()
new = sys.stdin.readline()

if not new:
    add_inline_tags(json.loads(old))
else:
    add_inline_tags(json.loads(new))
