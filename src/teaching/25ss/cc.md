# Compiler Construction (Summer 2024)

## General Information

- Lecturer: [Prof. Dr. Peter Thiemann](/team/thiemann.md)
- Assistants: [Marius Weidner](/team/weidner.md), [Leonardo Mieschendahl](/team/saffrich.md)
- Lecture: tba.
- Exercises: tba.

## Lectures & Tutorials

| Date | Type | Topic | Material | Recordings 
|:-----|:-----|:-----|:-----|:-----|


## Exercises

Exercises are provided and submitted via GitHub Classroom (follow the [invite link (tba)](/teaching/25ss/cc.md)).

Exercises will not be graded, but we will provide tests to
help you verify the correctness of your work. It is highly recommended
to take the exercises seriously, as the exam requires you to extend
the compiler from the sample solution with new features.

| Date | Deadline | Topic |
|:-----|:-----|:-----|


## Exam

The exam will take place in the computer pools and requires you to
extend the compiler implemented in the exercises with new features.

## Communication

For communication outside of the lecture, we provide an 
[discord-like chat](https://chat.laurel.informatik.uni-freiburg.de/invite/WRjCqL).
The chat requires you to log in with your RZ-Account (same credentials as for Ilias).

## Contents

Compiler construction deals with the development and implementation of
translation from higher-level programming languages to machine
code. This involves several important problems of general interest:

- **Semantic Analysis.**
  A compiler transforms and analyses the tree structure of a
  program. This phase is specified using attribute grammars.

- **Intermediate Code.**
  A compiler generates machine-independent intermediate code and
  performs several transformation and optimization steps on it.

- **Memory model and garbage collection.**
  The compiler maps data structures to memory structures. Languages
  with dynamic types and/or garbage collection require special care.

- **Machine code.**
  Intermediate code is translated to machine code, which undergoes
  machine-specific optimizations. This involves techniques like tree
  grammars, dynamic programming and graph coloring.

Compiler construction has a long tradition, so the structure of
compilers has been well thought out. Therefore, a compiler can act as
an example for a well-structured software system. "Who can write a
compiler, can write any program".

Knowledge about the memory model is helpful when debugging programs
written in a low-level programming language (C, C++).

## Literature
This lecture is based on the upcoming book *Essentials of Compilation*
by Jeremy G. Siek.

We will deviate from the book in two ways:
1. we will compile to the RISC-V processor architecture instead of x86; and
2. we will be using a different python framework for the exercises.

For this purpose, we have started our own fork of the book, which we will be
updating during the semester to use RISC-V instead of x86 instructions.

Our version of the book is available on the [GitHub Releases][book]
page. Simply download the `book.pdf` file for the most recent release.

To get notified on new releases, we recommend to push the *watch*-button on the
book's [GitHub repository](https://github.com/CC-Uni-Freiburg/Essentials-of-Compilation),
select *Custom* in the dropdown menu, and select *Releases*.

[book]: https://github.com/CC-Uni-Freiburg/Essentials-of-Compilation/releases

## Additional Literature
- Andrew Appel with Jens Palsberg, Modern Compiler Implementation in Java, 2nd edition. Cambridge University Press, 2002
- Alfred V. Aho, Monica S. Lam, Ravi Sethi, and Jeffrey D. Ullman. Compilers, Principles, Techniques, and Tools (2nd Edition).. Prentice Hall, 2006.
- Andrew W. Appel. Compiling with Continuations. Cambridge University Press, 1992.
- Andrew W. Appel. Modern Compiler Implementation in ML. Cambridge University Press, 1998.
- Christopher W. Fraser and David R. Hanson. A Retargetable C Compiler: Design and Implementation. Benjamin/Cummings, 1995.
- Reinhard Wilhelm and Dieter Maurer. Übersetzerbau -- Theorie, Konstruktion, Generierung -- 2. Auflage. Lehrbuch. Springer-Verlag, Berlin, Heidelberg, 1996.
