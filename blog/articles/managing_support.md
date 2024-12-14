# [WIP][DRAFT] Zen and the Art of Helpdesk Maintenance

# aka Managing Support


e.g. helpdesk, on-call, product support

Terminology:
* `entity`: Usually a person, but let's imagine a nifty world in which cats can report their empty food bowls and dogs can get tier1 support going for a walk.
* `SME` (`subject matter expert`) : The entity providing 
* `customer`,`end-user` : The entity requesting support, e.g. troubleshooting something which isn't working, or enabling a service, etc. Note: This article makes no distinction between `internal` and `external` customers.
* `triage` : The process of evaluating incoming requests by various criteria. At a minimum, these criteria include [urgency and importance](https://en.wikipedia.org/wiki/Time_management#Eisenhower_method). See also [Requirement Prioritisation](https://en.wikipedia.org/wiki/Requirement_prioritization).
* `Eisenhower Matrix`, `Eisenhower Method` : The [Eisenhower Matrix](https://en.wikipedia.org/wiki/Time_management#Eisenhower_method) is a simple time management technique for prioritising tasks. It is a very useful way to start a `triage` process.
* `tier 0` : self-service support, i.e. steps customers can take independently.
* `tier 1` : first contact between customer and SME, initial triage
* `tier 2` : minor escalation from SME to a colleague, e.g. asking questions to resolve the issue, or for help applying a known solution.
* `tier 3` : further escalation to other colleauges, e.g. realising that an issue requires deep analysis or more effort or expertise to t


Why this article makes no distinction between Internal and External Customers:

Customers can be `internal` to the company as a colleague, or `external` as someone using the services provided by the company.

Generally, the approach to managing internal and external customers is the same:
Manage the incoming requests in a way that preserves the sanity of the support team while providing a positive experience for the customer.

Of course there are differences between supporting a colleauge with whom one can interact on a general basis,
and supporting a relatively anonymous person who needs help with "the thing", but this article ignores those differences.

# Triaging Requests

It's important to triage every incoming request.

Ask a few key questions:

* urgency - what is this blocking?
* impact - how many people are blocked?
* ???


It's important to establish guidelines for interacting with requestors:

* a "first response time" guideline, e.g. "someone will reply within 4 hours".
    * this buys you time to breathe instead of doom-scrolling the support backlog, trying to manage it all and somehow never making it.
    * aka "how to drink from the firehose"
* a "volume" metric, e.g. "I can't hold all of these limes, can the rest of the team help?
    * this provides a guideline for when to activate the shadow support. (definition: "shadow" support refers to the next person on the support rotation. This clear definition helps avoid having to "round robin" within the team to find someone to help out).

With this kind of triage, and support agreements, everyone working on support can have more time to breathe and have an easy-breasy time drinking from the firehose!


# How to Sip from the Firehose without Getting Soaking Wet

Caveat: For the following section, assume that everyone has positive intent - everyone is sympathetic to each other's needs.

Caveat: 🥘 At some point, metaphors for cooking and food will be used 🥘.

When working in a support-oriented role, it is common to feel overhelmed by the volume of incoming requests, which each have different priorities and clarity (sometimes... things just don't make sense).

This flood of work is commonly referred to as [drinking from a firehose](https://en.wiktionary.org/wiki/drink_from_a_firehose).

The key is to have healthy [personal boundaries](https://en.wikipedia.org/wiki/Personal_boundaries), and to not view incoming requests as demands, no matter how they are phrased.

If you're used to agile methodologies, think of support requests as the backlog on a [kanban board](https://en.wikipedia.org/wiki/Kanban_board) :-) .

# Why Triaging is better for Everyone

## Scenario: Fulfil each request as it arrives

This approach has a quick `time-to-first-response`, which will make customers will feel like their request is important.

However, immediately fulfilling each request 
 increases the `time-to-resolution` - the constant context switching and struggling to [hold all these limes](https://i.kym-cdn.com/entries/icons/original/000/003/980/limesguy.jpg) makes each task take longer, and customers start noticing delays.

🥘 So in the end, this approach is like "[empty calories](https://en.wiktionary.org/wiki/empty_calorie#English)" - the customer is happy because they got to eat a full bag of crisps, but winds up hungry again in half an hour. (food metaphor)


## Introducing a Triage Process

Introducing a triage process it may initially cause discontent,
but very quickly, people will start seeing the increased reliability and predictability of their requests.

🥘 Soon, they will appreciate the value of waiting a bit longer for the chef to prepare a proper meal. (food metaphor)

Managing that transition is the key - you are not letting them down, even if that's the overall perception - you are taking steps to ensure that everyone gets better service.

One way to do this would be:
* quick `time-to-first-response`
    * triage the urgency,importance (e.g. using [Eisenhower Matrix](https://en.wikipedia.org/wiki/Time_management#Eisenhower_method))
    * => manages expectations: customer feels acknowledged, understands the timeline
* longer `time-in-backlog`
    * i.e. you won't "start working" on each request as it comes in, so technically they are in the backlog for a longer time. But this has been communicated to the customer, so as long as the expectations are managed, this is good!
* shorter `time-to-resolution-once-in-progress`
    * less context-switching means each issue gets resolved faster
    * triaging means issues get assigned to best available resource
* shorter `time-spent-in-backlog`
    * overall everyone's issues will get processed faster

Caveat: The name for most of these metrics are novel to avoid re-using terminology from toxic call centers. Please suggest better alternatives if desired!


<!-- backlog: useful resources, not yet referenced and therefore not in the main text:
https://www.proprofsdesk.com/blog/help-desk-glossary/
https://knowyourmeme.com/memes/limes-guy-why-cant-i-hold-all-these-limes
-->
