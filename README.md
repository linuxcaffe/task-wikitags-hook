# tw-wikitags-hook

Adding or modifying a task, with this hook installed, turns

`$ task add help :bob: build the :tool:shed:`

into the equivalent of

`$ task add help :bob: build the :tool:shed: +bob +tool +shed`

(this :tag: format is used by vimwiki (taskwiki), orgmode and  *ledger)

The advantages are;

- Multiple tags can be created while writing the description. Often, words from the description are also good candidates for tags, but who wants to write them all twice?

 `task add take the :car: to the :dump: and :sell: it for scrap`

- This type of tag, as part of the description, can be used for several different things by several other applications (see: above); Vimwiki (and therefore taskwiki) highlight these as :tags:, tagbar can use them as anchors, ledger and hledger can use this sort of embedded tag in queries (as well as maintaining "actual" tag metadata) and who /knows/ how they work in orgmode!?

- There's also valuable information seeing :tags:like: :this: in description text and knowing that means taskwarrior +tags +like +this exist as metadata in the actual task info, even if they're not always displayed in various reports, or taskwikis. 


(install notes can be found in the script comments.)

