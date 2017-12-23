# check_mk-misc

Miscellaneous Check_MK checks.

## agent_grandstream

Agent to check Grandstream IP phones. As of now, this is only tested with a Grandstream GXP1620.
To use it,
* copy the check to `~/local/share/check_mk/agents/special/agent_grandstream`
* add a rule "Individual program call instead of agent access" with the command `~/local/share/check_mk/agents/special/agent_grandstream $HOSTADDRESS$ --user user --password $your-user-password`
