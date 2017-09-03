greetings = 1
while greetings <= 3:
  print 'Hello! ' * greetings
  greetings = greetings + 0 # Bug here
