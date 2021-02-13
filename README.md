# Our Group

Jonathan Rivera, Logan Stucki, Jacob Perry

# The Final Count

**91,856,200,000,000** tests run, just below 92 trillion! 

We were able to compute this many because of our use of the compilation library `numba` and also the use of distributed computing.

# Links

[Live Counter](https://discrete-math-2-ponder-prove-3.herokuapp.com/)
(Note: The number of tests run will show 0 because the server has restarted since the end of the competition)

[GitHub Link](https://github.com/per18020/DMIIPonderAndProve03)

# Thinking About Proof

Using the expression we found on OEIS that checks if any given integer is in the set A, we were able to find a corresponding expression to check if the integer is in the set B. 

`Set A: sin(m*Pi/r)*sin((m+1)*Pi/r) <= 0`

`Set B: sin(m*Pi/r)*sin((m+1)*Pi/r) > 0`

Our test ran an xor function between those two expressions to check for inclusion in either set, but not both, and not neither.

And just by looking at the <= and > signs you can see that we have full coverage of the entire set of natural numbers, because no matter what input you provide, the output will always make one of those two expressions true.

However, in order to use this as a proof, we first must prove that those are both valid testing functions. Digging deeper we can find that the expression exists in a general form for all Beatty sequences `sin(m*x)*sin((m+1)*x) > 0` where `x = Pi/r`. And that's as far as we've gotten. We don't know how that expression was derived, just that it works.

# Our Report on What We Learned

## We Had Fun

When Brother Neff first explained the competition, we thought it was going to be a simple loop running for 24 hours. However, Jacob took that idea many steps forward. He found and decided to use the `numba` library to improve computational performance and to use distributed computing. Which ended up being quite exciting!

Jacob wrote the client code and also set up a server that would allow each client to request a block of numbers in order to divide the task evenly between themselves. He also experimented with running the code on the GPU, but was unable to get it working before the deadline. Ah, what could have been!

Jonathan dedicated an average of 87% CPU load for these processes (which equates to 5 instances of the program [which is our ghetto way of multithreading]). Jacob dedicated 86% of his CPU (7 processes), and also ran his work computer at 100% utilization (8 processes). Logan set up a server that ran at 100% CPU load the entire time, while also intermittently contributing his MacBook’s CPU power. Furthermore, each of us convinced our friends to run the process on their personal computers as well. They had many questions. We had to assure them that it was for a cool project. This was definitely a huge team effort, and it was a fun experience all around.

The discovery of `numba` was particularly exciting for Jonathan. Previously, Jonathan was researching ways to improve the performance of Python code and he considered using the Cython module. Cython allows developers to write code in c++ and allow python files access to it. Furthermore, `numba` opened up a new avenue of discovery. Truly exciting!


## We Learned Something New

Our first thought when we received this assignment was to utilize multithreading to speed up our computation ability. But we quickly ran into the limitations posed by Python. In Python, threads unfortunately run synchronously, and threads only provide benefits in cases where the task is IO heavy. He then discovered processes, which are much like threads in other languages. However, the overhead for spinning up new processes is larger than actually running our calculations and resulted in a net decrease in speed.

We learned about the `numba` library which takes Python source code and compiles it down to machine code to be run directly on the hardware. This has the benefit of making your code hundreds of times faster than interpreted Python. `numba` also offers an interface for CUDA acceleration, but we were unable to get it working. And also found CUDA acceleration to be problematic to distribute due to a required 3.5GB SDK download.

We used `numba` in our project for the main calculation loop giving us the ability to compute 100,000,000 iterations in seconds (how many seconds is dependent on the CPU speed). That many iterations run through the Python interpreter would take at least a couple minutes to compute.

## We Achieved Something Meaningful

In using distributed computing, we learned a useful application of how to solve complex problems using multiple machines to help find the solution. Distributed computing has important applications in industry. It can be used anywhere from computing numbers like we did, to load balancing web servers. By building a distributed computing application, we have a better technical knowledge of how it works, and can better apply that knowledge in future problems we encounter.

## What Is True?
### What is true of my experience in general?
 - [x] We had fun.
 - [x] We learned something new.
 - [x] We achieved something meaningful, or something I can build upon at a later time.
### What is true of my report on what I learned?
 - [x] One of us, the mutually-agreed-upon report writer, wrote a sufficient number of well-written sentences.
 - [x] We reported what we thought about while doing the problems.
 - [x] We reported on any connections we found between these problems and something we
already knew.
 - [x] We reported on what contribution each of us made.
### What is true of the "mechanical infelicities"
 - [x] There are fewer than four.
 - [x] There are fewer than three.
 - [x] There are fewer than two.
 - [ ] There are none.
### What is true of the creative problem solving and programming we did?
 - [x] We successfully ran our code for 24 hours in a row, starting at noon on Friday, 2
October 2020, and ending at noon on Saturday, 3 October 2020.
 - [x] We succeeded in verifying the conjecture for many, many positive integers.
 - [ ] We avoided collecting anything and printing out anything except a summary report
of how long our code ran and what the highest number verified was.
 - [x] We thought about how we might prove this conjecture, not just verify it for admittedly
a paltry pittance of all of Z+.
 - [ ] We went deeper by exploring possible applications of the ideas we discovered.
