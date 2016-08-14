#!/usr/bin/env python
import json
import re
import sys

# Adds the ability to add inline tags to a task, from description text 

# concept and whining by djp
# working code by bqf

# Turns
#    $ task add I saw :bob: in the :tool:shed:
# Into the equivalent of
#    $ task add I saw :bob: in the :tool:shed: +bob +tool +shed
# This :tag:format: is used by vimwiki (taskwiki), orgmode and  *ledger

### SETUP
# Save (or symlink) this file as
#   ~/.task/hooks/on-add_wikitags.py
# change to that directory:
#   $ cd ~/.task/hooks
# make the script executable:
#   $ chmod +x on-add_wikitags.py
# then create a symlinks to that file, to make it an on-modify hook as well:
#   $ ln -s on-add_wikitags.py on-modify_wikitags.py
# so that tags are created whether you are adding OR modifying a task

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
