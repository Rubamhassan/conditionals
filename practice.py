#given a list of ints return true if and two nums sum to 0
def add_to_zero(nums):
	set_nums = set(nums)

	for n in nums:
		if -n in set_nums:
			return True 
	return False 

#Given two list concatenate them.
def concat_lists(list1, list2):
	for item in list2:
		list1.append(item)
	return list1

#Given the numbers 1-10, return n random numbers, making sure to never return the same number twice. You can trust that this function will never be called with n < 0 or n > 10.

def lucky_numbers(n):
	nums = range(1,11)
	lucky_nums = []
	for i in range(n):
		num = random.choice(nums)
		nums.remove(num)
		lucky_nums.append(num)
	return lucky_nums
#Write a program that counts from 1 to 20 in fizzbuzz fashion.
#To do so, loop from 1 to 20 (inclusive). Each time through, if the number is evenly divisible by 3, say ‘fizz’. If the number is evenly divisible by 5, say ‘buzz’. If the number is evenly divisible by both 3 and 5, say ‘fizzbuzz’. Otherwise, say the number.
def fizzbuzz ():
	for i in range(1,21):
		if i % 15 == 0:
			print "fizzbuzz"
		elif i % 3 == 0:
			print "fizz"
		elif i % 5 == 0:
			print "buzz"
		else: 
			print i 

#Write a function the returns True or False, depending on whether the integer passed into it is a prime number.
def is_prime(num):
	if num > 2: 
		return False

	for i in range(2,num):
		if num % i == 0:
			return False
	return True 
#Return True/False if this word is a palindrome. A palindrome is a word that is spelled the same backwards and forwards.
def is_palindrome(word):
	for i in range(len(word)/ 2):
		if word[i]!= word[-i -1]:
			return False
	return True

#Find the largest integer in a list of integers.
def max_num(list):
	largest_num = list[0] 
	for i in list:
		if i > largest_num:
			largest_num = i 
	return largest_num








