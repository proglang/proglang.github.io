# Compiler Construction (Summer 2024)

## General Information

- Lecturer: [Prof. Dr. Peter Thiemann](/team/thiemann.md)
- Assistants: [Hannes Saffrich](/team/saffrich.md), [Marius Weidner](/team/weidner.md)
- Lecture: Tuesday, 2:15 pm - 3:45 pm, SR 00 006 (G.-Köhler-Allee 051), [Zoom](https://uni-freiburg.zoom.us/j/68676990725?pwd=YlVIcnNCVUdxb2M3MjNMYUVVQkoydz09)
- Exercises: Friday, 2:15 pm - 3:45 pm, SR 00 006 (G.-Köhler-Allee 051), [Zoom](https://uni-freiburg.zoom.us/j/68676990725?pwd=YlVIcnNCVUdxb2M3MjNMYUVVQkoydz09)

## Lectures & Tutorials

| Date | Type | Topic | Material | Recordings 
|:-----|:-----|:-----|:-----|:-----|
| 2024-04-16 Tu | Lecture | Organization & Introduction | [Book][book], Chapter 1; [Slides][lec01-slides] | missing |
| 2024-04-19 Fr | - | - | - | - |
| 2024-04-23 Tu | Lecture | Integers & Variables | [Book][book], Chapter 2; [Slides][lec02-slides]; [Interpreter][lec02-interpreter]; [Dockerfile][Dockerfile] | [Video][lec02-rec] |
| 2024-04-26 Fr | Lecture | Scanning & Parsing | [Book][book], Chapter 3; [Slides][lec03-slides]; [Lexer][lec03-lexer]; [Earley Example][lec03-earley-ex] | [Video][lec03-rec] |
| 2024-04-30 Tu | Tutorial | Parsing & Compiler for \\(\mathcal{L}_{var}\\) | [Book][book], Chapter 2 & 3 | [Video][tut01-rec] |
| 2024-05-03 Fr | Lecture | Register Allocation | [Book][book], Chapter 4; [Notes][lec04-notes] | [Video][lec04-register] |
| 2024-05-07 Tu | Lecture | Booleans & Conditionals | [Book][book], Chapter 5; [Notes][lec05a-notes] | [Video][lec05a-boolean] |
| 2024-05-10 Fr | Tutorial | Parsing & Compiler for \\(\mathcal{L}_{var}\\) | | [Video][tut02-rec] |
| 2024-05-14 Tu | Lecture | Conditionals and While | [Book][book], Chapter 5 & 6; [Notes][lec05b-notes] | [Video][lec05b-boolean] |
| 2024-05-17 Fr | Tutorial | Register Allocation for \\(\mathcal{L}_{var}\\) | | [Video][tut03-rec] |
| 2024-05-28 Tu | Lecture | Liveness Analysis & Garbage Collection | [Slides (LA)][lec06-slides1] [Slides (GC)][lec06-slides2]  | [Video][lec06-rec] |
| 2024-05-31 Fr | Tutorial | Compiler for \\(\mathcal{L}_{if}\\) | | [Video][tut04-rec] |
| 2024-06-04 Tu | Lecture | Tuples & Garbage Collection | [Book][book], Chapter 7; [Slides][lec08-slides] | [Video][lec08-rec] |
| 2024-06-07 Fr | Tutorial | Compiler for \\(\mathcal{L}_{while}\\) | | [Video][tut05-rec] |
| 2024-06-11 Tu | Lecture | Top-Level Functions (Interpreter) | [Book][book], Chapter 8; [Material][lec09-material] | [Video][lec09-rec] |
| 2024-06-18 Tu | Lecture | Top-Level Functions (Typing, Codegen) | [Book][book], Chapter 8; [Slides][lec10-slides]; [Material][lec10-material] | [Video][lec10-rec] |
| 2024-06-21 Fr | Tutorial | Compiler for \\(\mathcal{L}_{tuple}\\) | | [Video][tut06-rec] |
| 2024-06-25 Tu | Lecture | Lambda Expressions (Interpretation, Typing, Codegen) | [Book][book], Chapter 9; [Material][lec11-material] | [Video][lec11-rec] |
| 2024-06-28 Fr | Tutorial | Compiler for \\(\mathcal{L}_{fun}\\) | | [Video][tut07-rec] |
| 2024-07-02 Tu | Lecture | Generics (Typing, Codegen) | [Book][book], Chapter 12; [Material][lec12-material] | [Video][lec12-rec] |
| 2024-07-05 Fr | Tutorial | Compiler for \\(\mathcal{L}_{lam}\\) | | [Video][tut08-rec] |
| 2024-07-09 Tu | Lecture | Exceptions (Interpreter, Typing, Codegen) | [Material (preliminary)][lec13-material] | [Video][lec13-rec] |
| 2024-07-12 Fr | Tutorial | Compiler for \\(\mathcal{L}_{lam}\\) | | [Video][tut09-rec] |
| 2024-07-16 Tu | Lecture | Optimization | [Slides][lec14-slides] [Examples][lec14-examples] | [Video][lec14-rec] |
| 2024-07-19 Fr | Tutorial | Compiler for \\(\mathcal{L}_{lam}\\) | | [Video][tut10-rec] |

[lec01-slides]: compiler-construction/slides/01-intro.pdf
[lec02-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/lecture-02-recording.mp4
[lec02-slides]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/lecture-02-slides.pdf
[lec02-interpreter]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/lecture-02-interpreter.py
[lec03-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/lecture-03-recording.mp4
[lec03-slides]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/lecture-03-slides.pdf
[lec03-lexer]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/lexer.py
[lec03-earley-ex]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/lecture-03-earley-example.txt
[lec04-register]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/2024-05-03-lecture-1.mp4
[lec04-notes]: compiler-construction/slides/lecture-2024-05-03.html
[lec05a-boolean]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/2024-05-07-lecture-1.mp4
[lec05a-notes]: compiler-construction/slides/lecture-2024-05-07.html
[lec05b-boolean]:  http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/2024-05-14-lecture-1.mp4
[lec05b-notes]: compiler-construction/slides/lecture-2024-05-14.md
[lec06-slides1]: compiler-construction/slides/10-liveness.pdf
[lec06-slides2]: compiler-construction/slides/garbage_collection.pdf
[lec06-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/2024-05-28-lecture-1.mp4
[lec07-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/2024-05-28-lecture-1.mp4
[lec08-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/2024-06-04-lecture-1.mp4
[lec08-slides]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/2024-06-04-slides-tuples-and-garbage-collection.pdf
[lec09-material]: compiler-construction/slides/lecture-2024-06-11-code-explanation.zip
[lec09-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/2024-06-11-lecture-1.mp4
[lec10-slides]: compiler-construction/slides/lecture-2024-06-18.pdf
[lec10-material]: compiler-construction/slides/lecture-2024-06-18-code-explanation.zip
[lec10-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/2024-06-18-lecture-1.mp4
[lec11-material]: compiler-construction/slides/lecture-2024-06-25-code-explanation.zip
[lec11-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/2024-06-25-lecture-1.mp4
[lec12-material]: compiler-construction/slides/lecture-2024-07-02-code-explanation.zip
[lec12-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/2024-07-02-lecture-1.mp4
[lec13-material]: compiler-construction/slides/lecture-2024-07-09-code-explanation.zip
[lec13-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/2024-07-09-lecture-1.mp4
[lec14-slides]: compiler-construction/slides/lecture-2024-07-16.pdf
[lec14-examples]: compiler-construction/slides/lecture-2024-07-09.zip
[lec14-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/2024-07-16-lecture-1.mp4
[tut01-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/tutorial-01-recording.mp4
[tut02-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/2024-05-10-exercise.mp4
[tut03-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/2024-05-17-exercise.mp4
[tut04-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/2024-05-31-exercise.mp4
[tut05-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/2024-06-07-exercise.mp4
[tut06-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/2024-06-21-exercise.mp4
[tut07-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/2024-06-28-exercise.mp4
[tut08-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/2024-07-05-exercise.mp4
[tut09-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/2024-07-12-exercise.mp4
[tut10-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/2024-07-19-exercise.mp4
[Dockerfile]: http://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Compilers/Dockerfile

## Exercises

Exercises are provided and submitted via GitHub Classroom (follow the [invite link](https://classroom.github.com/a/A_APR4dd)).

Exercises will not be graded, but we will provide tests to
help you verify the correctness of your work. It is highly recommended
to take the exercises seriously, as the exam requires you to extend
the compiler from the sample solution with new features.

| Date | Deadline | Topic |
|:-----|:-----|:-----|
| 2024-04-30 Tu | 2024-05-10 Fr | Lexer, Parser and Compiler for \\(\mathcal{L}_{var}\\) |
| 2024-05-10 Fr | 2024-05-17 Fr | Register Allocation for \\(\mathcal{L}_{var}\\) |
| 2024-05-17 Fr | 2024-05-31 Fr | Compiler for \\(\mathcal{L}_{if}\\) |
| 2024-05-31 Fr | 2024-06-07 Fr | Compiler for \\(\mathcal{L}_{while}\\) |
| 2024-06-09 Su | 2024-06-21 Fr | Compiler for \\(\mathcal{L}_{tuple}\\) |
| 2024-06-21 Fr | 2024-06-05 Fr | Compiler for \\(\mathcal{L}_{fun}\\) |
| 2024-06-05 Fr | 2024-07-12 Fr | Compiler for \\(\mathcal{L}_{lam}\\) |
| 2024-07-12 Fr | 2024-07-19 Fr | Compiler for \\(\mathcal{L}_{exc}\\) |

## Exam

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
