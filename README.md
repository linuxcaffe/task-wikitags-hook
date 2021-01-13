# tw-wikitags-hook

Adding or modifying a task, with this hook installed, turns

`$ task add I saw :bob: in the :tool:shed:`

into the equivalent of

`$ task add I saw :bob: in the :tool:shed: +bob +tool +shed`

(this :tag: format is used by vimwiki (taskwiki), orgmode and  *ledger)

The advantages are that tags can be created while writing the description and that this type of tag can be used for several different things by several applications. There's also valuable information seeing :tags:like: :this: in description text and knowing that taskwarrior +tags +like +this exist, even if they're not displayed in the current report, or wiki. 

(install notes can be found in the script comments.)

