# Change Management Guidelines - Template

# Instructions

Use this doc as a starting point for a discussion within a team so everyone can understand and align on each other's expectations.

Terminology:
* `CR`,`PR`,`MR`: Change Request. This concept has various names depending on the git hosting provider. GitHub: "Pull Request" or `PR`. GitLab: "Merge Request" or `MR`.

# Miscellaneous

Code Review Conduct
Purpose: These guidelines are meant to be like a [bumper rail in a bowling alley](https://duckduckgo.com/?q=wikipedia+bowling+alley+bumper+rail&t=ffab&ia=images&iax=images); keep the conversations out of the gutter without defining a rigid track to follow.

When opening a CR, keep in mind that this is a communication:
* The related ticket provides context for the changeset; a reviewer will use the ticket's completion criteria to evaluate the changeset.
  * if the CR content is not reflected in the ticket's completion criteria, it is confusing for reviewers. Even if the CR clearly explains a deviation from the ticket's purpose, this is a lot of 
overhead.
    * for a changeset which ls related to a ticket, but does not implement it, just create a new ticket for the purpose being explored.

When reviewing a CR, keep in mind that this continues a communication:
* Language used: Keep in mind that written messages tend to be perceived as impersonal.
  * Consider using [Conventional Comments](https://conventionalcomments.org/); these guidelines make the code review comments more clear and targeted, as well as providing a standard language for expressing intent (in particular, the article even mentions how to be perceived more positively and how to avoid negatively charged language).
* Try to ensure that all comments have been addressed => Drive to Conclusion!
  * Reviewer: Try to comment on the relevant line, and if there are several points, definitely number them!
  * Contributor: Get a general idea of the reply before typing! Try to address each point; treat the numbers as a checklist. If this is tedious, it might be time for a synchronous discussion (i.e. a meeting).
  * Everyone: Drive to conclusion. If a reply doesn't address the original concern, just point it out and wait for the updated response
    * Wait before addressing the other replies; otherwise the other person now has to reply to _two_ of your comments. This can be overwhelming, and makes it even more unlikely to get all of the points addressed.

While continuing to contribute to a CR actively under review, keep in mind that people are reviewing it

DO NOT force push; it resets the history and reviewers have to figure out which commits are new and which aren't.

I.e. with normal pushes, GitHub will show reviewers `New changes since you Last viewed` (see below)i; with a force push, the commit history gets reset and there's no simple way to track which commits are new and which aren't.

Text Example of Github's Message <!-- Note: author lost the screenshot -->
```image
New changes since you last viewed [View changes]
```

Suggestions
* [CRs should be atomic](), in the same sense that [git commits should be atomic]().
  * reviewers: feel free to ask the submitter about the [atomicity](https://en.wikipedia.org/wiki/Atomicity_(database_systems)) of the CR, i.e. if it seems like a CR contains multiple features, ask to have it split up per-feature.
  * there can be multiple CRs per ticket ;-) and git branches are cheap ;-)
* Ask questions, instead of assuming. Think `TCP` instead of `UDP`! Err on the side of caution. Remember that all language is a [lossy](https://en.wikipedia.org/wiki/Lossy_compression#Information_loss) transformation of thoughts, so it makes sense to keep error correction turned on and look for an `ack` from other people :-)
  * Instead of _assuming_ "well where you're wrong is..", _ask_ "hey, are you saying..!
* opinion or fact? try to base opinions on industry standards, even when deviating from them.
  * default: stick to industry standard, and avoid the overhead of having to discuss individual opinions on how to interpret them
  * deviate: justify the deviation while citing the standard, so that the rationale is clear
