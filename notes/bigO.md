What is BigO?
-A system for comparing code performance to other code that does that same thing in terms of space and time.

Why is BigO comportant?
-It provides a precise vocabulary for how to talk about how the code performs.
-Useful for discussing trade-offs between different approaches
-Helps identify inefficient parts of the code and where to improve.

How does BigO work?
-It counts the number of simple operations the computer has to preform.

How do you calculate BigO?
-Every operation (addition, multiplication, assignment, etc.) counts as 1.
-Most loops count as n.
-Nested loops are multiplied with outer loops giving n*n.
-Add it all together and simplify it in terms of the highest power. ie. 2n^2+5 become n^2.

Rules of Thumb for Time Complexity:
-Simplifying:
    O(2n) => O(n)
    O(500) => O(1)
    O(13n^2) => O(n^2)
-Smaller terms don't matter:
    O(n+10) => O(n)
    O(1000n+50) => O(n)
    O(n^2+5n+8) => O(n^2)
-Arithmetic operations are constant.
-Assignments are constant.
-Accessing elements in an array or objects by index or key is constant.
-In a loop the complexity is the loop multiplied by whatever is inside the loop.

Rules of Thumb for Space Complexity:
-You don't count the size of the input.
-Most primitives (booleans, numbers, undefined, null) are constant.
-Strings require O(n) space where n is the length of the string.
-Reference types are generally O(n) where n is the length of the array or amount of keys for the object.

BigO for Common Data Structures
-Objects
--When to use an object
---When you don't need order.
---When you need fast access, insertion and removal
--Time Complexity
---Insertion: O(1)
---Removal: O(1)
---Searching: O(n) (checking to see if a particular piece of information is in a value somewhere)
---Accessing: O(1)
---Methods
----Object.keys: O(n)
----Object.values: O(n)
----Object.entries: O(n)
----hasOwnProperty: O(1)
-Arrays
--When to use arrays.
---When you need order.
---When you need fast access, insertion, and removal (sort of)
--Time Complexity
---Insertion: O(n) at the beginning, O(1) at the end
---Removal: O(n) at the beginning, O(1) at the end
---Searching: O(n)
---Access: O(1)
---Methods
----push: O(1)
----pop: O(1)
----shift: O(n)
----unshift: O(n)
----concat: O(n)
----slice: O(n)
----splice: O(n)
----sort: O(nlogn)
----forEach: O(n)
----map: O(n)
----filter: O(n)
----reduce: O(n)