---
title: "Project Euler problem 1"
date:   2021-05-17 10:29:54 -0400
layout: post
---
#### Add up all the multiples of 5 or 3 below 1000.

What did I learn?
Sometimes you simply need to refresh the page. I wasted an hour because I though my correct answer was incorrect. When I clicked 'Check' the page did not respond. However a true incorrect answer leads to a page with a picture of a cute and confused human on top of a glaring red X. I can relate to that confused spud, but I guess I will have to get used to that feeling. It is only day 1. My fumbling did not end there. I mistook the Solved By column(966433) on the Archive page for the solution. I could have saved some time by estimating the upper bound. If every number 1 through 1000 passed my tests than the sum would be:

"
sum(num for num in range(999)) # = 498501
"

But what did I really learn?
My first instinct was to solve this recursively. The simplest recursive function I can write is a countdown, which is a sequence. For this problem I need to consider each number from 1 to 1000 also a sequence. Is the number a multiple of 3? Or is the number a multiple of 5? There must be more multiples of 3 than 5. Then I need to remember this number to add up with the other numbers that pass my tests. How do I go about it? My base case is n == 3. 1 and 2 are 
