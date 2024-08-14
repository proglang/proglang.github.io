# Concurrency, Theory & Practice -- Summer 2024

- Lecturer: [Prof. Dr. Peter Thiemann](/team/thiemann.md)
- Assistant: [Dr. Bas van den Heuvel](https://basvdheuvel.github.io/)

## Course planning

We plan to discuss the following topics (subject to change):

* Go: language overview
* Go: concurrency
* Dynamic data race prediction
* Dynamic deadlock prediction
* Futures
* Model checking: a short introduction
* Low-level concurrent data structures
* The pi-calculus
* Session types

We have one lecture and one tutorial each week:

- Lecture: Wednesday, 4:15 pm - 5:45 pm, SR 00 031 (G.-Köhler-Allee 051)
- Tutorials: Friday, 12:15 pm - 1:45 pm, R 04 007 Videokonferenz (G.-Köhler-Allee 106)

Note that some tutorials will be held online, ***so keep an eye on the [schedule](#schedule)***.

## Examination and Studienleistung

To pass the course, you need a passing grade on the written exam.
Additionally, you need to pass the Studienleisting, which entails actively participating in the Ilias quizzes.

## Announcements

*2024-08-14*:

* The exam is Tuesday 20 August, 10-12 at Werthmannstr. 4.
* Make sure you know the credentials (username and password) for your uni account.
* Besides the Ilias exam, you will have access to Notepad++.
    On request, we can provide paper for note-taking, but all material will have to remain in the room after the exam.
* There is no Studienleistung; a passing grade on the exam will award you your ECTS.
* The last tutorial recording only has audio.
    To follow along, use the material [here](./concurrency/SePi.zip).
* We will use the following syntax for the exam:
    * LTL, given formulas 𝜑 and 𝜓:
        * forever 𝜑: □𝜑 -> `[]𝜑` (left and right square brackets)
        * eventually 𝜑: ⬦𝜑 -> `<>𝜑` (less than and greater than)
        * next 𝜑: 🞅𝜑 -> `X𝜑` (capital letter X)
        * 𝜑 until 𝜓: 𝜑 ∪ 𝜓 -> `𝜑 U 𝜓` (capital letter U)
        * 𝜑 and 𝜓: 𝜑 ∧ 𝜓 -> `𝜑 ^ 𝜓` (hat symbol)
        * 𝜑 or 𝜓: 𝜑 ∨ 𝜓 -> `𝜑 v 𝜓` (small letter v)
        * 𝜑 implies 𝜓: 𝜑 → 𝜓 -> `𝜑 -> 𝜓` (dash and greater than)
        * not 𝜑: ¬𝜑 -> `~𝜑` (tilde)
        * `p` and `q` are atomic propositions
    * Traces:
        * nodes: `( p,q )` (parentheses, with comma-separated list of atomic propositions satisfied)
        * edge: `--->` (dashes followed by greater than, or different symbols depending on direction)
        * initial node `-> ( .. )`
    * Pi-calculus:
        * send y over x: ̅x〈y〉 -> `x<y>` (no overline, less than and greater than)
        * receive y over x: x(y) -> `x(y)` (left and right parentheses)
        * unobservable: 𝜏 -> `tau` (word tau)
        * choice: P + Q -> `P + Q` (plus)
        * parallel: P | Q -> `P | Q` (vertical bar)
        * restriction: (𝜈x)P -> `(nu x)P` (word nu and space)
        * replication: !P -> `!P` (exclamation mark)
        * substitution: P [x := y] -> `P [x := y]` (square brackets, colon and equals)
    * Session types:
        * process syntax as above, except restriction: (𝜈xy)P -> `(nu x y)` (space also between names)
        * select: x ◃ j -> `x < j` (less than)
        * branch: x ▹ {...} -> `x > {...}` (greater than and curly brackets)
        * types as usual, except select: ⊕{...} -> `+{...}` (plus symbol)
        * duality: ̅T -> `dual(T)` (word dual and parentheses)
        * typing judgments: Γ ⊦ P -> `Gamma |- P` (capitalized word Gamma, vertical bar and dash)
        * context split: Γ₁ ○ Γ₂ -> `Gamma1 o Gamma2` (small letter o)

*2024-08-05*:

Trace examples now available [here](./concurrency/traces.md).

*2024-07-26*:

Exam format:
* Exam pool, through Ilias.
* 120 minutes, ~10 questions.
* A single handwritten two-sided A4 cheat sheet is allowed.

Exam topics and additional study pointers:
* Go concurrency [here](https://go.dev/talks/2012/concurrency.slide) [here](https://go.dev/talks/2013/advconc.slide#16) [here](https://www.golang-book.com/books/intro/10).
* Concurrency traces to practice data race and deadlock detection will be provided soon.
* For Futures, try to recreate the examples from the slides.
* There will be no exam questions about transition systems.
* Traces and LTL [here](https://arxiv.org/pdf/2211.01677v1).
* Pi-calculus and session types [study the tutorial and examples of Sepi](http://gloss.di.fc.ul.pt/tryit/tools/SePi#).
* Further material may be found in other concurrency lectures, such as [here](https://moves.rwth-aachen.de/teaching/ws-1718/ct/) and [here](https://iccl.inf.tu-dresden.de/web/Concurrency_Theory_(SS2023)/en).

*2024-07-19*:
1. Unfortunately, the recording software failed on me, so the recording of today's tutorial has only audio. My apologies.
2. Early next week, there will be additional study material available here.

*2024-07-03*:

After today's lecture, the Ilias quiz on the pi-calculus
will be available.
Other than usual, you only have until next Friday (July 5)
at noon to finish the quiz.
This way, we can discuss the exercises during the tutorial.

*2024-06-28*:
1. Please check today's tutorial for clarifications on notation.
2. Next Ilias quiz will be released after next Wednesday's lecture.

*2024-06-20*:
1. A new quiz is available on Ilias, on transition systems
and LTL.
2. The deadline of this quiz is Friday June 28 at noon
(12:00 CEST).
3. There is no tutorial this Friday (June 21).
4. Next week's tutorial (Friday June 28) will be online.

## Schedule

**If the schedule says "Tutorial", there is a tutorial.**
Only if the schedule says "No tutorial" will there be no tutorial.

| Date | Type | Topic | Links |
|:-----|:-----|:------|:------|
| **Past** | | | |
| 2024-04-17 (Wed) | Lecture | Course overview and Go | \[[Lecture notes](./concurrency/lec-01-concurrency-go.html)\] \[[Recording](https://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Concurrency/2024-04-17-lecture-1.mp4)\] |
| 2024-04-19 (Fri) | Tutorial | Concurrency control using Go channels | \[[Exercise solutions](./concurrency/lec-01-exercises.zip)\] \[[Recording](https://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Concurrency/2024-04-19-tutorial-1.mp4)\] |
| 2024-04-24 (Wed) | Lecture | Go (by Bas) | \[[Lecture notes](./concurrency/lec-02-concurrency-go.html)\] \[[Recording](https://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Concurrency/2024-04-24-lecture-1.mp4)\] |
| 2024-04-26 (Fri) | Tutorial *(online)* | Go | \[[Exercise solutions](./concurrency/lec-02-exercises.zip)\] \[[Partial recording](https://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Concurrency/2024-04-26-tutorial-1.mp4)\] |
| 2024-05-03 (Fri) | Tutorial | Go | \[[Exercise/Ilias solutions](./concurrency/lec-02-exercisesb.zip)\] \[[Recording](https://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Concurrency/2024-05-03-tutorial-1.mp4)\] |
| 2024-05-08 (Wed) | Lecture | Dynamic data race prediction |  \[Lecture notes 1/2 [PDF](./concurrency/lec-03-data-race-01-overview.pdf)/[HTML](./concurrency/lec-03-data-race-01-overview.html) 2/2 [PDF](./concurrency/lec-03-data-race-02-hb-vc.pdf)/[HTML](./concurrency/lec-03-data-race-02-hb-vc.html)\] \[[Recording (audio only)](https://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Concurrency/2024-05-08-lecture-1.mp4)\] |
| 2024-05-10 (Fri) | Tutorial | Dynamic data race prediction | \[[Notes, exercises, and solutions](./concurrency/lec-03-tutorial.html)\] \[[Recording](https://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Concurrency/2024-05-10-tutorial-1.mp4)\] |
| 2024-05-15 (Wed) | Lecture | Dynamic data race prediction, part 2 | \[[Lecture notes](./concurrency/lec-02-data-race-04-lockset.pdf)\] \[[Recording](https://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Concurrency/2024-05-15-lecture-1.mp4)\] |
| 2024-05-17 (Fri) | Tutorial | Dynamic data race detection, part 2 *ilias deadline* | \[[Notes and exercises](./concurrency/lec-04-tutorial.html)\] \[[Recording](https://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Concurrency/2024-05-17-tutorial-1.mp4)\] |
| 2024-05-22 (Wed) | *No lecture* | (Pfingstwoche) | |
| 2024-05-24 (Fri) | *No tutorial* | (Pfingstwoche) | |
| 2024-05-29 (Wed) | Lecture *(online)* | Dynamic deadlock prediction (by Bas) | \[Lecture notes [PDF](./concurrency/lec-05-deadlock.pdf)/[HTML](./concurrency/lec-05-deadlock.html)\] \[[Recording](https://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Concurrency/2024-05-29-lecture-1.mp4)\] |
| 2024-05-31 (Fri) | Tutorial *(online)* | Dynamic deadlock prediction *ilias deadline* | \[[Notes and exercises](./concurrency/lec-05-tutorial.html)\] \[[Recording](https://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Concurrency/2024-05-31-tutorial-1.mp4)\] |
| 2024-06-05 (Wed) | Lecture *(online)* | Futures (by Bas) | \[Lecture notes [PDF](./concurrency/lec-06-futures.pdf)/[HTML](./concurrency/lec-06-futures.html)\] \[[Recording](https://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Concurrency/2024-06-03-lecture-1.mp4)\] |
| 2024-06-07 (Fri) | Tutorial | Futures *ilias deadline* | \[[Notes and exercises](./concurrency/lec-06-tutorial.html)\] \[[Ilias solutions](./concurrency/lec-05-ilias.pdf)\] \[[Recording (no screen but you can use the notes to follow)](https://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Concurrency/2024-06-07-tutorial-1.mp4)] |
| 2024-06-12 (Wed) | Lecture | Formal aspects of concurrency | \[See Ilias for slides\] \[[Recording](https://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Concurrency/2024-06-12-lecture-1.mp4)\] |
| 2024-06-14 (Fri) | Tutorial | Formal aspects of concurrency *ilias deadline* | \[See Ilias for slides\] \[[Exercise solutions](./concurrency/lec-06-solution.go)\] \[[Recording](https://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Concurrency/2024-06-14-tutorial-1.mp4)\] |
| 2024-06-19 (Wed) | Lecture | Formal aspects of concurrency, part 2 | \[See Ilias for slides\] \[[Recording](https://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Concurrency/2024-06-19-lecture-1.mp4)\] |
| 2024-06-21 (Fri) | *No tutorial* | | |
| 2024-06-26 (Wed) | Lecture | Message-passing Concurrency | \[Lecture notes [PDF](./concurrency/lec-10-message-passing.pdf)\] \[[Recording](https://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Concurrency/2024-06-26-lecture-1.mp4)\] |
| 2024-06-28 (Fri) | Tutorial *(online)* | Message-passing Concurrency | \[[Notes](./concurrency/lec-10-tutorial.html)\] \[[Recording](https://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Concurrency/2024-06-28-tutorial-1.mp4)\] |
| 2024-07-03 (Wed) | Lecture | Pi-calculus |  \[Lecture notes (revised/extended) [PDF](./concurrency/lec-11-message-passing.pdf)\] \[[Recording](https://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Concurrency/2024-07-03-lecture-1.mp4)\] |
| 2024-07-05 (Fri) | Tutorial | Pi-calculus | \[[Notes](./concurrency/lec-11-tutorial.html)\] \[[Recording](https://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Concurrency/2024-07-05-tutorial-1.mp4)\] |
| 2024-07-10 (Wed) | Lecture | Session types | \[Slides [PDF](./concurrency/lec-12-session-fundamentals.pdf)\] \[[Recording](https://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Concurrency/2024-07-10-lecture-1.mp4)\] |
| 2024-07-12 (Fri) | *No tutorial* | | |
| 2024-07-17 (Wed) | Lecture | Session types | (slides cont'd) \[[SePi system](https://rss.rd.ciencias.ulisboa.pt/tools/sepi/)\] \[[Recording](https://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Concurrency/2024-07-17-lecture-1.mp4)\] |
| 2024-07-19 (Fri) | Tutorial | Session types | \[[Recording (audo only)](https://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Concurrency/2024-07-19-tutorial-1.mp4)\] |

## Additional consulting
Besides tutorials, Bas will be available for consulting on Tuesdays 10-11 (with the exception of 2024-04-30, 2024-05-28, 2024-06-18, 2024-06-25).
If you cannot make it and have urgent questions, [email Bas](mailto:vdheuvel@informatik.uni-freiburg.de) and ask the question directly or make an appointment.
