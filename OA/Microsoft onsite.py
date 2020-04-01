'''
Given a k-sorted array that is almost sorted such that each of the N elements 
may be misplaced by no more than k positions from the correct sorted order. 
Find a space-and-time efficient algorithm to sort the array.
For example,
arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]<br>
k = 2
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


O(n*log(n))
A simple solution would be to use a efficient sorting algorithm to sort the 
whole array again. The worst case time complexity of this approach 
will be O(nlog(n)) where n is the size of the input array. 
This method also do not use the fact that array is k-sorted. 
We can also use insertion sort that will correct the order in just O(nk)time.
 Insertion sort performs really well for small values of k but it is not recommended
 for large value of k (use it for k <= 12)



O(n*log(k))
We can solve this problem in O(nlogk)using a min heap. The idea is to construct 
a min-heap of size k+1 and insert first k+1 elements into the heap. 
Then we remove min from the heap and insert next element from the array 
into the heap and and continue the process till both array and heap is exhausted. 
Each pop operation from the heap should insert the corresponding top element in 
its correct position in the array.
'''

