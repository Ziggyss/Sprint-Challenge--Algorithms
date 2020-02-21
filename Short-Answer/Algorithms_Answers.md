#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This one has a running time of O(n) because of the loop. 
Line 1 is O(1), line 2 looks like O(n^3) but because a increases each time by the value of n*n it makes this line O(n), and line 3 is O(1).


b) This code has a running time of O(nlogn) because it has a nested loop which runs at O(logn) because j is doubled each time - similar to halving n each time. Each line would be O(1), O(n), O(1), a nested O(logn), O(1) and O(1). Simplified, this makes O(n) * O(logn) which is O(nlogn).


c) This code has a running time of O(n).

## Exercise II

In order to find floor f I need to start at the bottom of the building and test to see if an egg is broken when dropped from each floor until I reach the floor when the egg gets broken.

As soon as I reach this floor and the condition is met, I can stop. This approach minimises the broken eggs to 1.

The runtime of this algorithm would be O(n) because we have to loop through all of the floors and the worst case scenario is if the top floor happens to be floor f. Therefore it has to be O(n).

Here is how the algorithm would run:

For the range of floors n = 0 to n = n:
    Throw an egg.
    If the egg breaks, stop
    Assign n to f
    Return f.


If, however, the aim is to reduce the number of dropped eggs OR broken eggs, I would take a different approach and use a binary search which has a run time of O(logn).

For this I would start at the middle floor, drop an egg and see if it breaks.

If so, I would go to the middle of the floors below and try again. If not, I would go to the middle of the floors above and try again. 

I would repeat this process until I found floor f - the floor that breaks an egg and is one above a floor that doesn't.



