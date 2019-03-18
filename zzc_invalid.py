# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 13:44:48 2018

@author: 14flash & NGnius
"""

INVALID_MESSAGE = "I'm sorry, did you say `KILL ALL HUMANS`?"
INVALID_MESSAGES_LOC = 'addons/bot-tweaks/data/invalid_messages.json'

from libs import command, dataloader
import random
# TODO(NGnius): Make this actually run last
class Command(command.DirectOnlyCommand):
    '''Catch all for direct commands that didn't work.

**Usage**
Step 1: type
```@Idea ```
Step 2: *facekeyboard*
Step 3: send your message '''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.invalid_message = INVALID_MESSAGE
        self.invalid_messages = dataloader.datafile(INVALID_MESSAGES_LOC).content

    def matches(self, message):
        return True

    def action(self, message):
        info = {
                "message":message.content,
                "author":message.author.mention,
                "server":message.server.name if message.server else "private channel",
                "channel":message.channel.mention if not message.channel.is_private else "private channel",
                "idea":self.user().name
                }
        msg_content = str(random.choice(self.invalid_messages))
        msg_content = msg_content.format(**info)
        yield from self.send_message(message.channel, content=msg_content)
