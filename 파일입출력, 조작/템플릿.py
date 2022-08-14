import string

s = """
dear XXX.

hi, iam $name

$contents

have a good day
"""

t = string.Template(s)
contents = t.substitute(name="mike", contents="how are you?")
print(contents)