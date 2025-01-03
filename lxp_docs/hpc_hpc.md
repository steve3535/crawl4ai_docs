# Welcome

Source: https://docs.lxp.lu/hpc/hpc/

# Welcome

## Intro

Welcome to the HPC documentation.

This page has been created to offer the best possible technical companion to MeluXina users.

When developing an application from scratch it is feasible to design the code, choose data structures, and data memory patterns to benefit from all the power of supercomputer architecture such as MeluXina.

However, when facing an existing application it is often hard to know where to start, what to expect, and how best to make use of such an architecture.

Based on our experience and a team of experts working on various application development and solutions using supercomputers, we have documented a process that allows one to incrementally add improvements to the code.

It’s not complex, and to some people, it may be obvious, but even for experts writing it down helps to structure the effort and leads to faster results.

The workflow consists of mainly four stages: Compiling, Profiling, Debugging, Optimizing or CPDO, executed in a cycle.

### Compiling

The first step is to perform the compilation of the code using proper flags to allow optimizations through compilation steps. (see section Compiling).

### Profiling

The second step is to assess the existing code to identify which parts take the most time by analysing the application with one or more realistic data sets.

By profiling the code we can identify the hot spots, which we then analyse to estimate how changing the hot spot performance will help.

The profiling step is crucial, both at the outset when facing a non-accelerated code and in subsequent iterations when evaluating progress and building progress.

Plenty of tools are available to help applications profiling (see section profiling).

For example. either Map or VTune can make the task very simple.

### Debugging

Of course, the purpose of parallelizing parts of an application is to improve performance, so we need to make sure to measure the application performance, with realistic data sets as always, and follow best practices to maximise the performance.

This may include high-level optimizations such as algorithm choice and data movement and low-level optimizations such as explicitly caching data in shared memory or tuning floating point sequences.

Across optimization bugs or errors can be injected due to a high level of optimization.

For that, debuggers help to identify and fix bugs in a code (see section Debugging).

### Optimize

Having identified candidate hotspot(s) we need to parallelize the code.

There are several ways to accelerate applications: For many operations, this is as simple as using optimized libraries, for others, we may be able to add a few directives and minimal changes to expose parallelism to a parallelizing compiler.

In some cases we will want to use a different programming language, and while this will require some level of refactoring, it can provide a large boost.