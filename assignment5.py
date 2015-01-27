#!/usr/bin/env python

print "This is the story of you."
name = raw_input("So, what is your name?")
print "Hello, %s" % name

hobby  = raw_input("What do you love to do?")
if hobby == 'dance':
	print "Of course you do!"
else:
	print "No, you love to dance."

print "And because you love to dance so much you decided to go to UNC's Ballroom Club. When you go there you saw there were two lessons both at the same time. You can either learn Salsa or Waltz."

print "What will you learn?"
print "1.Salsa"
print "2.Waltz"

dance = raw_input()
if dance == "1":
	print "You learned Salsa!"
else:
	print "You learned Waltz!"
print "Good Job!"
