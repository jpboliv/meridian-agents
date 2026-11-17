# Reference incident

Draft for [issue 2](https://github.com/jpboliv/meridian-agents/issues/2).

1. A gateway instance slows down. The operator authorizes a mitigation and records which readings confirmed recovery.
2. The symptoms return on a different instance. Recall suggests where to look. The agent must identify the affected instance from fresh observations.
3. After a deployment, the same alert has a different cause. The agent must explain which observation rules out the previous fix.

## Agreed handover

The incident record says what happened: “Memory use rose on gateway instance 2. After its restart, latency returned to normal.” The lesson says what to check next: “When the gateway slows down, compare memory use across instances.”

On the third shift, memory use is normal across the gateway instances and the database link is slow. Keep the first incident record. Use the fresh readings to investigate the link.

## When a reading is missing

If the incident cannot wait, hand it to the operator immediately. Otherwise, retry a timed-out read once. If access is denied, skip the retry.

If the reading is still missing, consult one independent source the agent can access. Use fresh evidence that changes the investigation. An old reading or another copy of the alert adds no evidence about the cause.

If the cause remains unclear, leave the gateway running. Tell the operator what the agent saw, what it could not measure, and what to check next. Record the gap without saving a lesson about the cause.

Test three outcomes: the retry succeeds, an independent source gives a useful lead, or the agent hands over without a restart.
