  # Name: Tim Foster
  # Email: foster@onid.oregonstate.edu
  # Class name: CS311-400
  # Assignment: Homework #1

import math

class primes:
	
	#Initialize function for primes. Requires one input that is an integer representing the upper limit of primes.
	def __init__(self, num):
		self.composite = {}
		self.num = 0
		num = int(num)
		if num < 2:
			num = 2
		self.test = 2
		self.adjust_primes(num);
		self.list_keys = self.list_primes()

	#returns a list of the current primes in the dictionary.
	def list_primes(self):
		return sorted(self.composite.keys());

	#returns the current number of primes in the dictionary.
	def num_primes(self):
		return len(self.list_primes());

	#returns the upper limit of the current dictionary.
	def upp_limit(self):
		return self.num;

	#Num is an integer which will find the Numth prime in the dictionary. If the dictionary contains fewer then Num primes
	#it will grow to contain more than num amount of primes.
	def get_prime(self, num):
		num = int(num)
		while self.num_primes() < num:
			self.adjust_primes(self.upp_limit()*2)
		return self.list_primes()[num-1];
	
	#Checks to see if a given number is a prime.
	#if True, it will return 1
	#if false, it will return 0
	def is_prime(self, num):
		num = int(num)
		if num > (self.list_keys[(self.num_primes()-1)]):
			adjust_primes(num*2);
		if num in self.composite:
			return 1;
		else:
			return 0;


	#Adjust the current primes instance. This will allow it to be bigger or smaller depending on which value is put in.
	#If the new 'num' value is smaller, it will reduce the size of the dictionary.
	#If the new 'num' value is larger, it will increase the size of the dictionary.
	def adjust_primes(self, num):
		if num > self.num:
			k = 1
			self.num = num
			while self.test < self.num :
				self.composite[self.test] = 1;
				self.test += 1;
			while k < (math.sqrt(self.num) + 1):
				m = k + 1;
				while not m in self.composite:
					m += 1;
				i = m;
				while i*m < self.num:
					if i*m in self.composite:
						del self.composite[i*m];
					i += 1;
				k = m;
		else:
			for i in reversed(self.list_primes()):
				if i > num:
					del self.composite[i]
			self.num = num;
		self.list_keys = self.list_primes()


	#Finds the next prime number after a given integer. If the dictionary does not contain the prime number, it will grow
	#until it contains it.
	def get_next(self, num):
		num = int(num)
		if num >= (self.list_keys[(self.num_primes()-1)]):
			self.adjust_primes(num*2);
		#Crude attempt at providing atleast one step of a binary search to find the next prime.
		if num > (self.list_keys[int(self.num_primes()/2)]):
			for i in range(len(self.list_keys)-1, 0, -1):
				if self.list_keys[i-1] <= num and self.list_keys[i] > num:
					return self.list_keys[i]
		else:
			for i in range(len(self.list_keys)):
				if self.list_keys[i] <= num and self.list_keys[i+1] > num:
					return self.list_keys[i+1]


num = input("What number do you want to receive primes up to?" )
x = primes(num)
b = primes(200)
print ("There are {0} prime numbers before the number {1}".format(x.num_primes(), x.upp_limit()));
print ("The 2500th prime is {0}".format(x.get_prime(2500)));
print ("The 2501th prime is {0}".format(x.get_next(22307)));
print ("The 2502th prime is {0}".format(x.get_next(x.get_prime(2501))));

print ("Is 22307 a prime number? {0}".format(x.is_prime(22307)));
print ("is 22305 a prime number? {0}".format(x.is_prime(22305)));

print ("changing to the B instance of primes");
print ("There are {0} prime numbers before the number {1}".format(b.num_primes(), 200));
print (b.list_primes());
