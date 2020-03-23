# Adapted by me

import io

message = 'This is a just a normal string.'

f = io.StringIO(message)
# f.write('Hola mundo')
print(f.read())
