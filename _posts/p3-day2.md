---
title: Problem 3 Part ii
date: 2021-05-20
layout: post
---
#### Prime factorization is funky
05/20/21
The Cryptography course on Khan Academy is saving me on this problem. How do I find the greatest prime factor of 600851475143, a twelve digit and roughly 5 byte number? The course is tackling a similar problem except for a number that is twenty digits long, in order to simulate RSA encryption for a Mars rover. The instructor, Brit, clarified questions that I have bumped into. What is the time requirement for this calculation and what is the space requirement in memory?

RSA uses a nice property of primes. Take two primes and multiply them. Easy. For a three digit prime you calculate this with a pencil and paper. Or punch it in your calculator. You get a nice big number. Now try working backward. Take a nice big number and find its largest prime factor. Not easy. There is no find my big prime button on a calculator. In fact every composite number has a unique prime factorization, like a locker combination ... Rivest-Shamir-Adleman.

So day two trying to figure out prime factorization. I tried to build off my initial approach. Step one, make a list of prime numbers to test for factorization, but this time using the sieve of Eratosthenes to narrow the search space. Mr. 'sthenes gifted us with the worst possible scenario of prime factorization, when a composite can be separated into only two prime factors and these primes are equal. Another way to consider this is when a prime factor is the square root of the target integer. So I only really need to test for primality up to the square root of my target.

At this point it would be nice to store that list in memory and test each prime from largest to smallest to see whether it divides into my target number. Well my sieve script ran for about five minutes before I ended it. How many primes would it have to store and how much memory would the largest prime require? Enter the Prime number theorem. The number of primes below a certain threshold is approximate to the threshold divided by the natural log of the threshold. For me that makes about 57,160 primes. I used my sieve to test the last hundred numbers below the square root of my target for primality to find the largest prime is 775121. No, this is not the solution. I have feeling the largest prime factor will be much smaller. But back to my 775121, how much memory do you take up? In binary she is 0b10111101001111101010. Roughly four bytes. So to estimate the size of my prime list => 4 bytes * 57160 primes = 228640 bytes.

Maybe I need a different approach.