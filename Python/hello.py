# print "Hello, World!"

from cStringIO import StringIO
import sys

_stdout = sys.stdout
sys.stdout = stream = StringIO()

import __hello__

sys.stdout = _stdout

replacements = ('...', '!'), (' ', ', ')
print reduce(lambda s, kv: s.replace(*kv), replacements, stream.getvalue().title().strip())
