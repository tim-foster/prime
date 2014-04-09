  # Name: Tim Foster
  # Email: foster@onid.oregonstate.edu
  # Class name: CS311-400
  # Assignment: Homework #1

import math

composite = {}
num = input("What number do you want to receive primes up to?" )
k = 1


test = 2
while test < num :
	composite[test] = 1;
	test += 1;

while k < (math.sqrt(num) + 1):
	m = k + 1;
	while not composite.has_key(m):
		m += 1;
	i = m;
	while i*m < num:
		if composite.has_key(i*m):
			del composite[i*m];
		i += 1;
	k = m;

print ("There are {0} prime numbers before the number {1}".format(len(composite.keys()), num));
print composite.keys();