#! /bin/bash
#
# check_wikitags.sh
# Copyright (C) 2016 djp <djp@cutter>
#
# Distributed under terms of the MIT license.
#
# this script designed to check for wikitags, in any task description, that 
# do not have corresponding taskwarrior tags.

# task executable
# taskrc
# taskdata

echo -e "You have `task +PENDING '/(^| ):([^:]+:)+( |$)/' count` pending tasks with wikitags"
exit
