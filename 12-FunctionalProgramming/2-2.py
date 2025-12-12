names = [
   'James',
   'Emily',
   'William',
   'Olivia',
   'Benjamin',
   'Sophia',
   'Henry']

print('\n'.join(sorted(names, key = lambda x: len(x), reverse=True)))