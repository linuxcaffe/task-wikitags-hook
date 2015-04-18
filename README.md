# task-wikitags-hook
_inline :tags: treated like +tags_

    CAVEAT: all concept, no code, so far
    
This feature-request-posing-as-a-repository is for a hook that extends taskwarriors +tag behavior.

Vimwiki, *ledger and several other projects, use a tag format that looks like :tag1:tag2:tag3:. There have been discussions among taskwarrior users and developers about "in-line" tags, that is, tags that can exist as part of the task description, but are still treated like (non-in-line) tags.

So I would like to propose this task-wikitags-hook, that extends task filterring so that a :tag: is treated just like a +tag or -tag. Unlike the suggestions in https://bug.tasktools.org/browse/TW-1357, which suggests using a token in the description, to cause a matching +tag to be created, this tag would not create an "actual" tag, but extends task's searching to find a :tag: when asked for a +tag. 

In other words, with these two imaginary tasks;
<pre> 
Id Project Tags Description
------------------------------------
14 foo     +bar do this example task
21 buz          do this other thing at the :bar:
</pre>
with the task query
<pre>
task +bar list
</pre>
would find both 14 and 21
<pre>
task -bar list
</pre>
would exclude both tasks
<pre>
task tag:bar list
</pre>
would only find task 14, and 
<pre>
task desc.has:':bar:' list
</pre>
would find only task 21

That's it!
