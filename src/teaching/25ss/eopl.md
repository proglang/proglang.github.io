# Essentials of Programming Languages (Summer 2025)

## General Information

- Lecturer: [Prof. Dr. Peter Thiemann](/team/thiemann.md)
- Assistants: [Hannes Saffrich](/team/saffrich.md)
- Lecture: tba.
- Exercises:  tba.

## Lectures & Tutorials

| Date | Type | Topic | Material | Recordings 
|:-----|:-----|:-----|:-----|:-----|


## Exercises


| Date | Deadline | Topic | Solution |
|:-----|:-----|:-----|:-----|


## Exam

tba.

## Communication

For communication outside of the lecture, we provide an 
[discord-like chat](https://chat.laurel.informatik.uni-freiburg.de/invite/gj6wpJ).
The chat requires you to log in with your RZ-Account (same credentials as for Ilias).

## Contents

This course conveys the mathematical and logical concepts underlying programming languages using the language [Agda](https://en.wikipedia.org/wiki/Agda_(programming_language)). 
Agda is a functional language with an advanced type system that enables the encoding of many program properties in its types. 
Agda's type checker verifies proofs of these properties, so that one could also say this course is about verified programming.

The first part of the course covers the logical background needed to study the theory of programming languages to the extent that we can give formal guarantees about the execution of a program. 
The content of this part should be familiar from an introductory logic class, but it is presented in an entirely different way. 
The central idea conveyed is that every program (in a language with a reasonable type system) is really a proof about the meaning of the program. 
Conversely, it means that every proof can be viewed as a program, so that proving becomes programming a function with a certain type. 
For example, inductive proofs are expressed by terminating recursive functions. 
This correspondence is called the [Curry-Howard correspondence](https://en.wikipedia.org/wiki/Curry%E2%80%93Howard_correspondence). 
It is one of the most powerful discoveries in logics and programming and it is one of the core ideas behind Agda.

The second part of the course puts this toolbox to work.
We use Agda's features to model the syntax and the semantics of (simple) programming languages. 
We model type systems and connect them to the semantics through type soundness theorems. 
We learn about different ways of modeling syntax and semantics and their pros and cons. 
We study type inference as a means to find a best possible (principal) typing for a given program, if such a typing exists.

## Literature & Approach
The course mainly follows the online book [Programming Language Foundations in Agda](https://plfa.github.io/) (PLFA) by Philipp Wadler, Wen Kokke, and Jeremy Siek:

On Wednesdays we discuss (part of) a chapter from the PLFA book. 
We ask you to prepare for this by reading the chapter in advance. 
We will try to cover questions interactively.
On Fridays we discuss the exercises of the corresponding chapters (contained in the book), and answer general questions related to Agda, Theorem Proving and Programming Language Theory. 
Occasionally we may also show you cool stuff not covered in the book.
Recordings of the lecture will be available so that asychronous participation is possible. 
The exercise sessions will not be recorded. 
The PLFA book is freely available in source code, so that everything can be tried hands on. 
It is amenable to self study, but the pragmatics of using Agda are much easier to deal with in an interactive supportive environment such as we are trying to provide.

## Links

- [Programming Language Foundations in Agda](https://plfa.github.io/) (Book)
- [Official Agda Documentation](https://agda.readthedocs.io/en/latest/)
- [Emacs Agda-Mode Documentation](https://agda.readthedocs.io/en/v2.6.3/tools/emacs-mode.html)
- [Agda Standard Library](https://github.com/agda/agda-stdlib)
- [VirtualBox Image with Agda and Emacs](http://archive.informatik.uni-freiburg.de/courses/proglang/2023-WS-EOPL/Agda%20VM%202023%20WS.ova)
- Emacs Configuration for Agda ([Normal]https://proglang.informatik.uni-freiburg.de/teaching/proglang/2023ws/extras/emacs-config.zip / [Vim](https://proglang.informatik.uni-freiburg.de/teaching/proglang/2023ws/extras/emacs-config-vim.zip)] Keybindings)
- [Discord-like chat](https://chat.laurel.informatik.uni-freiburg.de/invite/gj6wpJ) for questions about the lecture, exercises, and related topics. Login via RZ-Account, i.e. same as for Ilias.
- [A list of all unicode symbols that can be typed in agda-mode via LaTeX commands](https://proglang.informatik.uni-freiburg.de/teaching/proglang/2023ws/extras/agda-input.txt). You probably need to download this file, because the browser uses the wrong character encoding, which causes the unicode characters to look scrambled.