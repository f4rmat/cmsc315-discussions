# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

**1. What concepts or skills did you learn while completing this assignment?**
I learned how to implement linear data structures in Python, utilizing standard lists for stack operations and collections.deque for efficient queue operations. I also learned how space complexity scales automatically as elements are stored.

**2. What challenges did you encounter, and how did you overcome them?**
The main challenge was handling execution errors when attempting to pop or dequeue from an empty structure. I overcame this edge case by implementing an is_empty() check within those methods to return a descriptive string message instead of crashing the program.

**3. Explain the differences between stacks and queues as this relates to real-world applications.**
Stacks operate on a Last-In, First-Out principle, which is ideal for reversing recent actions, such as an undo history for YAML configuration edits. Queues operate on a First-In, First-Out principle, which makes sure data is processed in the exact order it arrives, such as processing incoming sensor notifications in a smart home server.
