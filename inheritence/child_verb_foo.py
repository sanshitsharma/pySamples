#!/usr/bin/env python

DOCUMENTATION = '''
---

module: child_verb_foo
short_description: test module
options:
    pause_time:
        description: Pause time in seconds,
        required: True
        default: 60
'''

EXAMPLES = '''
# Verb execution example
'''

from inheritence.base_verb import BaseVerb

class ChildVerbFoo(BaseVerb):
    def execute():
        sleep(self.pause_time)
        print "exiting module"

def main():
    verb = OpPause()
    verb.pause_time = 3

    verb.execute()