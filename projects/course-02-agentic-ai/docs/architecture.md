# Information ownership

Draft for [issue 3](https://github.com/jpboliv/meridian-agents/issues/3).

Alert → select context → investigate → authorize an action → observe its effect → report to the operator.

Context is the information in one model call. Working state tracks the open incident. Memory carries lessons across incidents. A cache reuses a result under specified conditions. A checkpoint records where interrupted work can resume.

Design question: if a checkpoint says an action is pending but the executor recorded its effect, which source answers each question? Specify who can read, write, and correct each record.
