# Compiler Construction (Summer 2024)

## General Information

- Lecturer: [Prof. Dr. Peter Thiemann](/team/thiemann.md)
- Assistants: [Hannes Saffrich](/team/saffrich.md), [Marius Weidner](/team/weidner.md)
- Lecture: Tuesday, 2:15 pm - 3:45 pm, SR 00 006 (G.-Köhler-Allee 051)
- Exercises: Friday, 2:15 pm - 3:45 pm, SR 00 006 (G.-Köhler-Allee 051)

## Lectures & Tutorials

| Date | Type | Topic | Material | Recordings 
|:-----|:-----|:-----|:-----|:-----|
| 2024-04-16 Tu | Lecture | Organization & Introduction | [Book][book], Chapter 1; [Slides][lec01-slides] | missing |
| 2024-04-19 Fr | - | - | - | - |
| 2024-04-23 Tu | Lecture | Integers & Variables | [Book][book], Chapter 2; [Slides][lec02-slides]; [Interpreter][lec02-interpreter]; [Dockerfile][Dockerfile] | [Video][lec02-rec] |
| 2024-04-26 Fr | Lecture | Scanning & Parsing | [Book][book], Chapter 3; [Slides][lec03-slides]; [Lexer][lec03-lexer]; [Earley Example][lec03-earley-ex] | [Video][lec03-rec] |
| 2024-04-30 Tu | Tutorial | Compiler for \\(\mathcal{L}_{var}\\) | [Book][book], Chapter 2 & 3 | |

[lec01-slides]: compiler-construction/slides/01-intro.pdf
[lec02-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/lecture-02-recording.mp4
[lec02-slides]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/lecture-02-slides.pdf
[lec02-interpreter]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/lecture-02-interpreter.py
[lec03-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/lecture-03-recording.mp4
[lec03-slides]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/lecture-03-slides.pdf
[lec03-lexer]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/lexer.py
[lec03-earley-ex]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/lecture-03-earley-example.txt
[Dockerfile]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/Dockerfile

## Exercises

Exercises are provided and submitted via GitHub Classroom (follow the [invite link]()).

Exercises will not be graded, but we will provide tests to
help you verify the correctness of your work. It is highly recommended
to take the exercises seriously, as the exam requires you to extend
the compiler from the sample solution with new features.

| Date | Deadline | Topic |
|:-----|:-----|:-----|
| 30.04.24 | 10.05.24 | Lexer, Parser and Compiler for \\(\mathcal{L}_{var}\\) |

## Examination Requirements

This lecture consists of an exam and a "Studienleistung".

For the "Studienleistung" it is required to submit exercises for each
exercise sheet.

The exam will take place in the computer pools and requires you to
extend the compiler implemented in the exercises with new features.

## Communication

For communication outside of the lecture, we provide an 
[Ilias course](https://ilias.uni-freiburg.de/goto.php?target=crs_3469049_rcodesJ5zaM6NX6&client_id=unifreiburg)
and a 
[discord-like chat](https://chat.laurel.informatik.uni-freiburg.de/invite/NDm9rk).

The Ilias course is used exclusively to send emails in case of updates, e.g. if there is a bug in an exercise. Make sure to register to receive those emails.

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
