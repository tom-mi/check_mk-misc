# check_mk-misc

Miscellaneous Check_MK checks.

## agent_grandstream

Agent to check Grandstream IP phones.

![Check_mk services for grandstream agent](screenshots/agent_grandstream.png)

### Notes
* As of now, this is only tested with a Grandstream GXP1620.
* Considering that some "magic" parameter names like `P402` are used to query the required information, this might not work out of the box for other phones.
* Running the agent logs out any user currently using the web interface of the phone.

### Usage
* copy the check to `~/local/share/check_mk/agents/special/agent_grandstream`
* add a rule "Individual program call instead of agent access" with the command `~/local/share/check_mk/agents/special/agent_grandstream $HOSTADDRESS$ --user user --password $your-user-password`

## agent_levelone_wap0006

Agent to check the uptime of LevelOne Wireless Access Point WAP 0006
(this is the only relevant information exposed by the web interface).

### Usage
* copy the check to `~/local/share/check_mk/agents/special/agent_levelone_wap0006`
* add a rule "Individual program call instead of agent access" with the command `~/local/share/check_mk/agents/special/agent_levelone_wap0006 $HOSTADDRESS$ --user admin --password $your-admin-password`
