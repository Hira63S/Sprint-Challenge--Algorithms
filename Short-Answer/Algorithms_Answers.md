#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) a = 0
    while (a < n * n * n):
      a = a + n * n

This looks like a O(n) notation of linear time because as a is less than n*n*n, n*n gets added to a.


b) sum = 0
    for i in range(n):
      j = 1
      while j < n:
#        j == jx2
        sum += 1

It looks like a O(n^2) problem where as the range of n increase, the operations increase as a function of quadratic time.


c) def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
It looks like O(n) i.e. we keep adding 2 and performing recursion until the base case is reached.

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

# Answer:
It seems like a sorting problem where we can go through the n-story building floors and see if the egg breaks on a floor in the middle, if it does, we know we need to move to lower floor so we can go to the middle of the left-hand side list and see if the egg breaks. If it doesn't we would know we need to move to the right. This way, we can first half the list of floors and if we the floor number in the middle breaks the egg, we know we will be moving to the left of the list. We will continue the process until we find the floor that doesn't break the egg. This would be a binary search problem with a notation of O(nlogn)
