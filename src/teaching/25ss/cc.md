# Compiler Construction (Summer 2025)

## General Information

- Lecturer: [Prof. Dr. Peter Thiemann](/team/thiemann.md)
- Assistants: [Leonardo Mieschendahl](/team/mieschendahl.md), [Marius Weidner](/team/weidner.md)
- Lecture: Tuesdays 14-16, R 04 007 Videokonferenz G.-Köhler-Allee 106, [Livestream][zoom1] (Zoom Meeting-ID: 661 1930 0692, Password: nsWAD0nCW)
- Exercises: Fridays 14-16, R 04 007 Videokonferenz G.-Köhler-Allee 106, [Livestream][zoom2] (Zoom Meeting ID: 621 5357 2187, Passcode: MMkG4kTky)

[zoom1]: https://uni-freiburg.zoom-x.de/j/66119300692?pwd=4it8s1KQ6T7LBSaZkSk2bYarBR7Zl5.1
[zoom2]: https://uni-freiburg.zoom-x.de/j/62153572187?pwd=kqhISWSzCEaZ5Ct7I9sbw71ZGM1x2p.1
<!-- (Hannes) (Zoom Meeting ID: 631 6286 3480, Passcode: An1SxJdPr) [zoom2]: https://uni-freiburg.zoom-x.de/j/63162863480?pwd=NQoZk82SvNbFqDtJQVyEvbvMfLBNnG.1-->

## Lectures & Tutorials

| Date | Type | Topic | Material | Recordings 
|:-----|:-----|:-----|:-----|:-----|
| 2025-04-22 Tu | Lecture | Organization & Introduction | [Book][book], Chapter 1; [Slides][lec01-slides] | [Rec][lec01-rec] |
| 2025-04-25 Fr | Lecture | Chapter 2 | [Book][book], Chapter 2; [Slides][lec02-slides] | [Rec][lec02-rec] |
| 2025-04-29 Tu | Lecture | Chapter 3 | [Book][book], Chapter 3; [Slides][lec03-slides]; [Code][lec03-code] | [Rec][lec03-rec] |
| 2025-05-02 Fr | Tutorial | Compiler for \\(\mathcal{L}_{var}\\) | - | [Rec][tut01-rec] |
| 2025-05-06 Fr | Lecture | Chapter 4 |  [Book][book], Chapter 4 | [Rec][lec04-rec] |
| 2025-05-09 Fr | Tutorial | Register Allocation for \\(\mathcal{L}_{var}\\) | - | [Rec][tut02-rec] |
| 2025-05-13 Tu | Lecture | Chapter 5 |  [Book][book], Chapter 5 | [Rec][lec05-rec] |
| 2025-05-16 Fr | Tutorial | Compiler for \\(\mathcal{L}_{if}\\) | - | [Rec][tut03-rec] |
| 2025-05-20 Tu | Lecture | Chapter 6 |  [Book][book], Chapter 6, [Slides][lec06-slides], [Notes][lec06-notes]  | [Rec][lec06-rec] |
| 2025-05-23 Fr | Tutorial | Compiler for \\(\mathcal{L}_{while}\\) | - | [Rec][tut04-rec] |
| 2025-05-27 Tu | Lecture | Chapter 7 |  [Book][book], Chapter 7, [Slides][lec07-slides]  | [Rec][lec07-rec] |
| 2025-05-30 Fr | Tutorial | Compiler for \\(\mathcal{L}_{tup}\\) | - | [Rec][tut05-rec] |
| 2025-06-03 Tu | Lecture | Chapter 8 |  [Book][book], Chapter 8 , [Notes][lec08-notes]  | [Rec][lec08-rec] |
| 2025-06-06 Fr | Tutorial | Compiler for \\(\mathcal{L}_{fun}\\) | - | [Rec][tut06-rec] |
| 2025-06-17 Tu | Lecture | Chapter 9 |  [Book][book], Chapter 9 , [Notes][lec09-notes]  | [Rec][lec09-rec] |
| 2025-06-20 Fr | Tutorial | No tutorial | - | - |
| 2025-06-24 Tu | Lecture | Chapter 12 |  [Book][book], Chapter 12 , [Notes][lec10-notes]  | [Rec][lec10-rec] |
| 2025-06-27 Fr | Tutorial | Compiler for \\(\mathcal{L}_{\lambda}\\) | - | [Rec][tut07-rec] |
| 2025-07-01 Tu | Lecture | Data classes | [Notes][lec11-notes]  | [Rec][lec11-rec] |
| 2025-07-04 Fr | Tutorial | Compiler for \\(\mathcal{L}_{class}\\) | - | - |


[lec01-slides]: cc/slides/01-intro.pdf
[lec01-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2025-SS-Compilers/2025-04-22-lecture-1.mp4
[lec02-slides]: cc/slides/20250425-slides.pdf
[lec02-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2025-SS-Compilers/2025-04-25-lecture-1.mp4
[lec03-code]: cc/material/chapter3.zip
[lec03-slides]: cc/slides/20250429-slides.pdf
[lec03-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2025-SS-Compilers/2025-04-29-lecture-1.mp4
[lec04-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2025-SS-Compilers/2025-05-06-lecture-1.mp4
[lec05-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2025-SS-Compilers/2025-05-13-lecture-1.mp4
[lec06-notes]: https://github.com/CC-Uni-Freiburg/lecture-notes-2021/blob/main/lecture-2025-05-20.md
[lec06-slides]: cc/slides/liveness.pdf
[lec06-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2025-SS-Compilers/2025-05-20-lecture-1.mp4
[lec07-slides]: cc/slides/garbage_collection.pdf
[lec07-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2025-SS-Compilers/2025-05-27-lecture-1.mp4
[lec08-notes]: https://github.com/CC-Uni-Freiburg/lecture-notes-2021/blob/main/lecture-2025-06-03-functions.md
[lec08-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2025-SS-Compilers/2025-06-03-lecture-1.mp4
[lec09-notes]: https://github.com/CC-Uni-Freiburg/lecture-notes-2021/blob/main/lecture-2025-06-17-lexical.md
[lec09-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2025-SS-Compilers/2025-06-17-lecture-1.mp4
[lec10-notes]: https://github.com/CC-Uni-Freiburg/lecture-notes-2021/blob/main/lecture-2025-06-24-type-checking.md
[lec10-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2025-SS-Compilers/2025-06-24-lecture-1.mp4
[lec11-notes]: https://github.com/CC-Uni-Freiburg/lecture-notes-2021/blob/main/lecture-2025-07-01-dataclasses.md
[lec11-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2025-SS-Compilers/2025-07-01-lecture-1.mp4
[tut01-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2025-SS-Compilers/2025-05-02-tutorial.mp4
[tut02-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2025-SS-Compilers/2025-05-09-tutorial.mp4
[tut03-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2025-SS-Compilers/2025-05-16-tutorial.mp4
[tut04-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2025-SS-Compilers/2025-05-23-tutorial.mp4
[tut05-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2025-SS-Compilers/2025-05-30-tutorial.mp4
[tut06-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2025-SS-Compilers/2025-06-06-tutorial.mp4
[tut07-rec]: http://archive.informatik.uni-freiburg.de/courses/proglang/2025-SS-Compilers/2025-06-27-tutorial.mp4

## Exercises

Exercises are provided and submitted via GitHub Classroom (follow the [invite link](https://classroom.github.com/a/N58OPy1R)).

Exercises will not be graded, but we will provide tests to
help you verify the correctness of your work. It is highly recommended
to take the exercises seriously, as the exam requires you to extend
the compiler from the final sample solution with new features.

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
This lecture is based on the Python version of the book *Essentials of Compilation*
by Jeremy G. Siek.

We will deviate from the book in several ways:
1. we use the (unpublished) Python version of the book;
2. we compile to the RISC-V processor architecture instead of x86; and
3. we use a different Python framework for the exercises.

For this reason, we maintain our own fork of the book, which is mostly
ported to use RISC-V instead of x86 instructions.

Our version of the book is available on the [GitHub Releases][book]
page. Simply download the `book.pdf` file for the most recent release.

To get notified on new releases, we recommend the *watch*-button on the
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
