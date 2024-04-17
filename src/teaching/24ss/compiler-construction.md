# Compiler Construction (Summer 2024)

## General Information

- Lecturer: [Prof. Dr. Peter Thiemann](/team/thiemann.md)
- Assistants: [Hannes Saffrich](/team/saffrich.md), [Marius Weidner](/team/weidner.md)
- Lecture: Tuesday, 2:15 pm - 3:45 pm, SR 00 006 (G.-Köhler-Allee 051)
- Exercises: Friday, 2:15 pm - 3:45 pm, SR 00 006 (G.-Köhler-Allee 051)

## Lectures & Tutorials

| Date | Type | Topic | Material | Recordings 
|:-----|:-----|:-----|:-----|:-----|
| 2024-04-16 Tu | Lecture | Organization & Introduction | [Book][book], Chapter 1 | TBA |
| 2024-04-19 Fr | Lecture | Integers & Variables | [Book][book], Chapter 2 | |
| 2024-04-23 Tu | Lecture | Scanning & Parsing | [Book][book], Chapter 3 | |
| 2024-04-26 Fr | Tutorial |  | | |

## Exercises

Exercises are provided and submitted via GitHub Classroom.

We will provided further details about the the exercises in the first tutorial session.

| Date | Deadline | Topic |
|:-----|:-----|:-----|

## Contents

Compiler construction deals with the development and implementation of
translation from higher-level programming languages to machine
code. This involves several important problems of general interest:

- **Semantic Analysis.**
  A compiler transforms and analyses the tree structure of a
  program. This phase is specified using attribute grammars.

- **Intermediate Code.**
  A compiler generates machine-independent intermediate code and
  performs several transformation and optimisation steps on it.

- **Memory model and garbage collection.**
  The compiler maps data structures to memory structures. Languages
  with dynamic types and/or garbage collection require special care.

- **Machine code.**
  Intermediate code is translated to machine code, which undergoes
  machine-specific optimisations. This involves techniques like tree
  grammars, dynamic programming and graph coloring.

Compiler construction has a long tradition, so the structure of
compilers has been well thought out. Therefore, a compiler can act as
an example for a well-structured software system. "Who can write a
compiler, can write any program".

Knowledge about the memory model is helpful when debugging programs
written in a low-level programming language (C, C++).

## Literature
This lecture is based on the upcoming book *Essentials of Compilation*
by Jeremy G. Siek. The current draft of the book is available in the
[ongoing course at Indiana University](https://iucompilercourse.github.io/IU-Fall-2021/).
We will be using the [Python edition][book] of the book!

We will deviate from the book in two ways:
1. we will compile to the RISC-V processor architecture instead of x86; and
2. we will be using a different python framework for the exercises.

[book]: https://www.dropbox.com/s/mfxtojk4yif3toj/python-book.pdf?dl=1

## Communication

For communication outside of the lecture, we provide an Ilias course and a discord-like chat.

The Ilias course is used exclusively to send emails in case of updates, e.g. if there is a bug in an exercise. Make sure to register to receive those emails.

The chat requires you to log in with your RZ-Account (same credentials as for Ilias).

## Additional Literature
- Andrew Appel with Jens Palsberg, Modern Compiler Implementation in Java, 2nd edition. Cambridge University Press, 2002
- Alfred V. Aho, Monica S. Lam, Ravi Sethi, and Jeffrey D. Ullman. Compilers, Principles, Techniques, and Tools (2nd Edition).. Prentice Hall, 2006.
- Andrew W. Appel. Compiling with Continuations. Cambridge University Press, 1992.
- Andrew W. Appel. Modern Compiler Implementation in ML. Cambridge University Press, 1998.
- Christopher W. Fraser and David R. Hanson. A Retargetable C Compiler: Design and Implementation. Benjamin/Cummings, 1995.
- Reinhard Wilhelm and Dieter Maurer. Übersetzerbau -- Theorie, Konstruktion, Generierung -- 2. Auflage. Lehrbuch. Springer-Verlag, Berlin, Heidelberg, 1996.
