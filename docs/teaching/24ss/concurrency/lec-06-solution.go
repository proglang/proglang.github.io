package main

import "fmt"
import "time"
import "math/rand"

/*

Concurrency bugs in promises without mutex.

Works:
call to setSucc while empty = true
sets status = true
call to setFail while empty still = true
sets status = false
either call sets empty = false
both calls trigger succ and fail callbacks

Does not work:
concurrent calls to setSucc and onFailure

*/

/*

Events

*/

type Event struct {
    callBacks []func()
}

func newEvent() *Event {
    e := Event{callBacks: make([]func(), 0)}
    return &e
}

func (e *Event) trigger() {
	cbs := e.callBacks
	go func() {
		for _, cb := range cbs { // call every current callback.
			cb()
		}
	}()
}

func (e *Event) onTrigger(cb func()) {
	e.callBacks = append(e.callBacks, cb)
}

type Promise[T any] struct {
    val           T         // return value
    status        bool      // success or not
    m             chan int  // mutex
    succCallBacks []func(T)
    failCallBacks []func()
    empty         bool      // no value set yet?
	event         *Event
}


func newPromise[T any]() *Promise[T] {
	e := newEvent()
    p := Promise[T]{empty: true, m: make(chan int, 1), succCallBacks: make([]func(T), 0), failCallBacks: make([]func(), 0), event: e}
	
	e.onTrigger(func() {
		p.m <- 1
		if p.status {
			v := p.val
			cbs := p.succCallBacks
			p.succCallBacks = make([]func(T), 0)
			go func() {
				for _, cb := range cbs {
					cb(v)
				}
			}()
		} else {
			cbs := p.failCallBacks
			p.failCallBacks = make([]func(), 0)
			go func() {
				for _, cb := range cbs {
					cb()
				}
			}()
		}
		<- p.m
	})
	
    return &p
}

func (p *Promise[T]) setSucc(v T) {
	p.m <- 1
	if p.empty {
		p.val = v
		p.status = true
		p.empty = false
		p.event.trigger()
	}
	<- p.m
}

func (p *Promise[t]) setFail() {
	p.m <- 1
	if p.empty {
		p.status = false
		p.empty = false
		p.event.trigger()		
	}
	<- p.m
}

func (p *Promise[T]) onSuccess(cb func(T)) {
    p.m <- 1 // lock.
    if p.empty { // not set yet, register callback.
        p.succCallBacks = append(p.succCallBacks, cb)
    } else if !p.empty && p.status { // already set and successfull, immediate call callback.
        go cb(p.val)
    }
    <-p.m // release.
}

func (p *Promise[T]) onFailure(cb func()) {
    p.m <- 1
    if p.empty {
        p.failCallBacks = append(p.failCallBacks, cb)
    } else if !p.empty && !p.status {
        go cb()
    }
    <-p.m
}

// set promise computation, success or not.
func (p *Promise[T]) complete(f func() (T, bool)) {
    go func() {
        r, s := f()
        if s {
            p.setSucc(r)
        } else {
            p.setFail()
        }
    }()
}

// Try to complete p1 with p2.
func (p1 *Promise[T]) tryCompleteWith(p2 *Promise[T]) {
    p2.onSuccess(func(v T) {
        p1.setSucc(v)
    })
}

// Pick first successful promise.
func (p1 *Promise[T]) firstSucc(p2 *Promise[T]) *Promise[T] {
    p := newPromise[T]()
    p.tryCompleteWith(p1)
    p.tryCompleteWith(p2)
    return p
}

func example() {
    // Book some hotel.
    booking := func() (int, bool) {
		s := rand.Intn(999)
		a := rand.Intn(50)
		fmt.Printf("Waiting %dms to return %d\n", s, a)
        time.Sleep((time.Duration)(s) * time.Millisecond)
        return a, true
    }

    p1 := newPromise[int]()
    p1.complete(booking)

    p2 := newPromise[int]()
    p2.complete(booking)

    p := p1.firstSucc(p2)

    p.onSuccess(func(quote int) {
        fmt.Printf("Hotel asks for %d euros\n", quote)
    })

    time.Sleep(1 * time.Second)
}

func main() {
	example()
}