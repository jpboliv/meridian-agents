# Permissions and approvals

![Proposed flow](../flows/permissions.svg)

First ask whether this person can perform the action. Then ask whether this particular change has the approval it needs.

Draft for [issue 9](https://github.com/jpboliv/meridian-agents/issues/9). A support user requests a cached summary that an on-call engineer produced. Does the summary reveal information outside the user's scope?

Specify the effective identity, approval scope, data masking, and denial response. Test both an allowed action and a denied action against actual effects.
