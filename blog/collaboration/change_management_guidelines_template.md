# Change Management Guidelines - Template

# Instructions

Use this doc as a starting point for a discussion within a team so everyone can understand and align on each other's expectations.

This doc is based on experience with multiple teams over the years in [various stages of development](https://en.wikipedia.org/wiki/Tuckman%27s_stages_of_group_development) and understanding of CI tools (e.g. new to git, new to code review tools in GitHub/Gitlab/Bitbucket/gerrit/etc); as such, it might include some very detailed instructions which may seem out of place.

Terminology:
* `CR`,`PR`,`MR`: Change Request. This concept has various names depending on the git hosting provider. GitHub: "Pull Request" or `PR`. GitLab: "Merge Request" or `MR`.

# 5 Minute Summary

Minimum Requirements for Effective Communication:

* Ask questions, instead of assuming. Think [`TCP` instead of `UDP`](https://www.old.reddit.com/r/ProgrammerHumor/comments/14wv9p/i_was_gonna_tell_you_guys_a_joke_about_udp/)! Err on the side of caution. Remember that all language is a [lossy](https://en.wikipedia.org/wiki/Lossy_compression#Information_loss) transformation of thoughts, so it makes sense to keep error correction turned on and look for an `ack` from other people :-)
  * Instead of _assuming_ "well where you're wrong is..", _ask_ "hey, are you saying..!
* opinion or fact? try to base opinions on industry standards, even when deviating from them.
  * default: stick to industry standard, and avoid the overhead of having to discuss individual opinions on how to interpret them
  * deviate: justify the deviation while citing the standard, so that the rationale is clear
* [CRs should be atomic](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/helping-others-review-your-changes), in the same sense that [git commits should be atomic](https://about.gitlab.com/topics/version-control/version-control-best-practices). Essentially, follow the Single Responsiblity Principle](https://en.wikipedia.org/wiki/Single-responsibility_principle).
  * reviewers: feel free to ask the submitter whether the Change Request (CR) is "too large", i.e. if it seems like a CR contains multiple features, disucss [splitting it up per-feature](https://en.wikipedia.org/wiki/Separation_of_concerns).
  * there can be multiple CRs per ticket ;-) and git branches are cheap ;-)

# 25 Minute Background

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

# Miscellaneous

## When to rewrite _personal_ history - Specific to GitHub

Caveat: Prerequisite: Understand the [consequences of rewriting git history](https://git-scm.com/book/ms/v2/Git-Tools-Rewriting-History#_rewriting_history)

While continuing to contribute to a CR actively under review, keep in mind that people are reviewing it

DO NOT re-arrange history and then force push to your branch; it resets the CR history and reviewers have to figure out which commits are new and which aren't.

I.e. with normal pushes, GitHub will show reviewers `New changes since you Last viewed` (see below)i; with a force push, the commit history gets reset and there's no simple way to track which commits are new and which aren't.

Text Example of Github's Message
```image
New changes since you last viewed [View changes]
```
