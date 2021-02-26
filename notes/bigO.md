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