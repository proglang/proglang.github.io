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
| **Upcoming** | | | |
| 2024-06-28 (Fri) | Tutorial *(online)* | Message Passing Concurrency, part 1 | \[[Notes](./concurrency/lec-10-tutorial.html)\] |
| 2024-07-03 (Wed) | Lecture | Pi-calculus | |
| 2024-07-05 (Fri) | Tutorial | | |
| 2024-07-10 (Wed) | Lecture | Session types | |
| 2024-07-12 (Fri) | Tutorial | | |
| 2024-07-17 (Wed) | Lecture | Session types | |
| 2024-07-19 (Fri) | Tutorial | | |
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
| 2024-06-26 (Wed) | Lecture | Pi-calculus | \[Lecture notes [PDF](./concurrency/lec-10-message-passing.pdf)\] \[[Recording](https://archive.informatik.uni-freiburg.de/courses/proglang/2024-SS-Concurrency/2024-06-26-lecture-1.mp4)\] |

## Additional consulting
Besides tutorials, Bas will be available for consulting on Tuesdays 10-11 (with the exception of 2024-04-30, 2024-05-28, 2024-06-18, 2024-06-25).
If you cannot make it and have urgent questions, [email Bas](mailto:vdheuvel@informatik.uni-freiburg.de) and ask the question directly or make an appointment.
