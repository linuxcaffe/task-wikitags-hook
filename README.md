# tw-wikitags-hook
_in task description :tag-one:tag-two: creates like +tag-one +tag-two_

This feature-request-posing-as-a-repository is for a hook that extends taskwarriors +tag behavior.

Vimwiki, *ledger and several other projects, use a tag format that looks like :tag1: and/or :tag2:tag3:. There have been discussions among taskwarrior users and developers about "in-line" tags, that is, tags that can exist as part of the task description, but are still treated like (non-in-line) tags.

So I would like to propose an adaptation of bqf's P.O.C. hook script; on-add_inline_tags.py (https://gist.github.com/wbsch/164757889ba4554df359) which allows for "inline tags" when adding tasks. The adaptation(s) are to a) match based on the :something:something-else: format, and b) creates matching +something +something-else tags on-modify or on-add. 

more description of intent can be found in the script comments.

