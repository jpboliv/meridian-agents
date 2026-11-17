# Cache policy

![Proposed flow](../flows/caching.svg)

A saved runbook can still be accurate after a deployment but describe the wrong version. Reuse depends on what changed and who is asking.

Draft for [issue 7](https://github.com/jpboliv/meridian-agents/issues/7). A runbook stays the same while the deployed component changes. Its content can still be correct even when its selection is wrong.

Specify the key, reader scope, source version, expiry, and invalidation event for each reusable result. Distinguish reused answers from provider prompt caching. Describe how a cache hit affects simulated time.
