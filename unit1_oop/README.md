# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Implementation Summary

I created a model of a small smart-home hub. `Device` was the parent class. It held a shared class variable (`hub_name`), two instance variables (`name` and `room`), and an internal on/off state, and its `describe()` method returned a readable status line. `SmartLock` inherited from `Device` and called `super().__init__()` to reuse the parent setup. It added a class variable (`max_failed_attempts`), new instance variables (`is_locked`, `failed_attempts`, and `access_log`), and a new `unlock()` method, and it overrode `describe()` to add the lock state. The student-created extension was the lock-out: `unlock()` refused every code after three failed attempts.

## Namespaces

I created two locks, read `max_failed_attempts` through the class and through an object, and added a `battery_level` attribute to only one lock. Printing each object's `__dict__` showed that attribute on the first lock and not the second, and printing the class namespace showed the methods and class variable shared by every lock.

## Copying

I put an entry in one lock's `access_log`, made a shallow copy with `copy.copy()` and a deep copy with `copy.deepcopy()`, then added another entry to the original. The shallow copy showed the new entry because it shared the same list, and the deep copy did not because it had its own list.

## Edge Cases

I tested a wrong access code, which returned `False` and counted as a failed attempt, and then the correct code, which unlocked the lock. I also checked that a second lock did not receive the attribute I added to the first one.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.

Working through this assignment clarified how Python handles object state and inheritance in practice. `self` targets the specific instance being built, `super()` pulls in the parent’s constructor and methods without duplicating code, and attribute lookup walks the chain from the instance to its class and up to the parent. Where I actually got caught was object copying. I initially expected `b = a` to give me a clean copy, but it just points a second variable at the same object, and even `copy.copy()` only does a shallow copy, leaving the nested `access_log` list shared between both instances. Printing the three logs side by side showed the shared references right away, and switching to `copy.deepcopy()` separated them properly.

Compared to procedural scripts where data gets passed around across standalone functions, OOP keeps the data and the validation rules that protect it in one place. Because my lock class checks the access code inside its own method, outside calls cannot skip that check. You pay an upfront cost in extra setup, but having a single class to fix, plus a base class that new device types can inherit from, makes maintaining and growing a system much cleaner.
