from libs import command
import re

class Command(command.DirectOnlyCommand, command.AdminCommand):
    '''Change my nickname
**Usage**
```@Idea change nickname to "<name>" ```
Where
**`<name>`** is the nickname you want me to have

**Example**
`@Idea change nickname to "NGnius is awesome!" ` '''
    def collect_args(self, message):
        return re.search(r'\b(?:change|set)\s*nick(?:name)?(?:\s*to)?\s+(.+)?', message.content, re.I)

    def matches(self, message):
        return self.collect_args(message) is not None and message.server is not None

    def action(self, message, bot):
        args = self.collect_args(message)
        new_nick = ''
        quoted_name1 = re.search(r'\"(.*)\"', args.group(1))
        if quoted_name1 is not None:
            new_nick = quoted_name1.group(1)
        else:
            new_nick = args.group(1)

        yield from bot.change_nickname(message.server.me, new_nick)
        yield from self.send_message(message.channel, 'Success! Changed nickname to `%s`' % new_nick)
