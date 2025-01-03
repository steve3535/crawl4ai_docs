# Compiling

Source: https://docs.lxp.lu/hpc/compiling/

# Compiling

Compiling C, C++, and Fortran code on MeluXina is similar to how it is done on regular personal systems, with some differences.

One compiler suite on MeluXina is the AMD Optimizing C/C++ Compiler (AOCC), providing clang, clang++, and flang frontends.

Other compilers are available such as the Intel suite, providing icc, icpc, and ifort.

The GNU Compiler Collection is also available on MeluXina, providing gcc, g++, and gfortran. GNU compiler compatibility is ubiquitous across free and open-source software projects, which includes much scientific software.

```

clang

```

```

clang++

```

```

flang

```

```

icc

```

```

icpc

```

```

ifort

```

```

gcc

```

```

g++

```

```

gfortran

```

## Generic compilation steps

A generic workflow must be followed to compile any source code or software on your own. After reserving a node on MeluXina, go to the directory with your code sources. We recommend temporarily placing your sources and compiling under the $SCRATCH directory where you will get better performance.

```

$SCRATCH

```

## Using command-line

From serial code to parallel OpenMP and MPI code the different step to compile a source code are detailed in the following for different languages such as C, C++ and Fortran

```

serial

```

```

OpenMP

```

```

MPI

```

```

C

```

```

C++

```

```

Fortran

```

### Serial

> **Source code**

> Source code

Source code

CC++fortran

1

2

3

4

5

6

7#include <stdio.h>

int main(void)

{

printf("Hello world!\n");

return 0;

}

Compiling and Executing

On a reserved node

module load foss/2023a

gcc -o helloworld helloworld.c

./helloworld

Output

Output from the execution

Hello world!

1

2

3

4

5

6

7#include <iostream>

int main(void)

{

std::cout << "Hello world!" << std::endl;

return 0;

}

Compiling and Executing

On a reserved node

module load foss/2023a

g++ -o helloworld helloworld.cpp

./helloworld

Output

Output from the execution

Hello world!

1

2

3program hello

print *, "Hello World!"

end program

Compiling and Execting

On a reserved node

module load foss/2023a

gfortran -o helloworld helloworld.f

./helloworld

Output

Output from the execution

Hello world!

CC++fortran

1

2

3

4

5

6

7#include <stdio.h>

int main(void)

{

printf("Hello world!\n");

return 0;

}

Compiling and Executing

On a reserved node

module load foss/2023a

gcc -o helloworld helloworld.c

./helloworld

Output

Output from the execution

Hello world!

1

2

3

4

5

6

7#include <iostream>

int main(void)

{

std::cout << "Hello world!" << std::endl;

return 0;

}

Compiling and Executing

On a reserved node

module load foss/2023a

g++ -o helloworld helloworld.cpp

./helloworld

Output

Output from the execution

Hello world!

1

2

3program hello

print *, "Hello World!"

end program

Compiling and Execting

On a reserved node

module load foss/2023a

gfortran -o helloworld helloworld.f

./helloworld

Output

Output from the execution

Hello world!

1

2

3

4

5

6

7#include <stdio.h>

int main(void)

{

printf("Hello world!\n");

return 0;

}

Compiling and Executing

On a reserved node

module load foss/2023a

gcc -o helloworld helloworld.c

./helloworld

Output

Output from the execution

Hello world!

1

2

3

4

5

6

7#include <stdio.h>

int main(void)

{

printf("Hello world!\n");

return 0;

}

1

2

3

4

5

6

7

```

1

2

3

4

5

6

7

```

#include <stdio.h>

int main(void)

{

printf("Hello world!\n");

return 0;

}

```

#include <stdio.h>

int main(void)

{

printf("Hello world!\n");

return 0;

}

```

```

#include <stdio.h>

int main(void)

{

printf("Hello world!\n");

return 0;

}

```

On a reserved node

module load foss/2023a

gcc -o helloworld helloworld.c

./helloworld

```

module load foss/2023a

gcc -o helloworld helloworld.c

./helloworld

```

```

module load foss/2023a

gcc -o helloworld helloworld.c

./helloworld

```

Output from the execution

Hello world!

```

Hello world!

```

```

Hello world!

```

1

2

3

4

5

6

7#include <iostream>

int main(void)

{

std::cout << "Hello world!" << std::endl;

return 0;

}

Compiling and Executing

On a reserved node

module load foss/2023a

g++ -o helloworld helloworld.cpp

./helloworld

Output

Output from the execution

Hello world!

1

2

3

4

5

6

7#include <iostream>

int main(void)

{

std::cout << "Hello world!" << std::endl;

return 0;

}

1

2

3

4

5

6

7

```

1

2

3

4

5

6

7

```

#include <iostream>

int main(void)

{

std::cout << "Hello world!" << std::endl;

return 0;

}

```

#include <iostream>

int main(void)

{

std::cout << "Hello world!" << std::endl;

return 0;

}

```

```

#include <iostream>

int main(void)

{

std::cout << "Hello world!" << std::endl;

return 0;

}

```

On a reserved node

module load foss/2023a

g++ -o helloworld helloworld.cpp

./helloworld

```

module load foss/2023a

g++ -o helloworld helloworld.cpp

./helloworld

```

```

module load foss/2023a

g++ -o helloworld helloworld.cpp

./helloworld

```

Output from the execution

Hello world!

```

Hello world!

```

```

Hello world!

```

1

2

3program hello

print *, "Hello World!"

end program

Compiling and Execting

On a reserved node

module load foss/2023a

gfortran -o helloworld helloworld.f

./helloworld

Output

Output from the execution

Hello world!

1

2

3program hello

print *, "Hello World!"

end program

1

2

3

```

1

2

3

```

program hello

print *, "Hello World!"

end program

```

program hello

print *, "Hello World!"

end program

```

```

program hello

print *, "Hello World!"

end program

```

On a reserved node

module load foss/2023a

gfortran -o helloworld helloworld.f

./helloworld

```

module load foss/2023a

gfortran -o helloworld helloworld.f

./helloworld

```

```

module load foss/2023a

gfortran -o helloworld helloworld.f

./helloworld

```

Output from the execution

Hello world!

```

Hello world!

```

```

Hello world!

```

### OpenMP

There are a variety of technologies available that can be used to write a parallel program and some combination of two or more of these technologies. While the clusters are capable of running programs developed using any of these technologies, The following examples tutorial will focus on the OpenMP and Message Passing Interface (MPI) compilation

> **Source code**

> Source code

Source code

CC++fortran

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15#include <stdio.h>

#include <stdlib.h>

#include <omp.h>

int main(void)

{

// Beginning of parallel region

#pragma omp parallel

{

printf("Hello World... from thread = %d\n",

omp_get_thread_num());

}

// Ending of parallel region

return 0;

}

Compiling and Executing

On a reserved node

module load foss/2023a

gcc -o helloworld_omp helloworld_OMP.c -fopenmp

export OMP_NUM_THREADS=8

./helloworld_omp

Output

Output from the execution

Hello World... from thread = 0

Hello World... from thread = 6

Hello World... from thread = 7

Hello World... from thread = 3

Hello World... from thread = 5

Hello World... from thread = 2

Hello World... from thread = 1

Hello World... from thread = 4

1

2

3

4

5

6

7

8

9

10

11

12

13#include <iostream>

#include <omp.h>

int main(void)

{

// Beginning of parallel region

#pragma omp parallel

{

std::cout << "Hello World... from thread = " << omp_get_thread_num() << std::endl;,

}

// Ending of parallel region

return 0;

}

Compiling and Executing

On a reserved node

module load foss/2023a

g++ -o helloworld_omp helloworld_OMP.cpp -fopenmp

export OMP_NUM_THREADS=8

./helloworld_omp

Output

Output from the execution

Hello World... from thread = 0

Hello World... from thread = 2

Hello World... from thread = 6

Hello World... from thread = 4

Hello World... from thread = 7

Hello World... from thread = 3

Hello World... from thread = 5

Hello World... from thread = 1

1

2

3

4

5

6

7

8

9

10PROGRAM Parallel_Hello_World

USE OMP_LIB

!$OMP PARALLEL

PRINT *, “Hello World... from thread =  ”, OMP_GET_THREAD_NUM()

!$OMP END PARALLEL

END

Compiling and Executing

On a reserved node

module load foss/2023a

gfortran -o helloworld_omp helloworld_OMP.f -fopenmp

export OMP_NUM_THREADS=8

./helloworld_omp

Output

Output from the execution

Hello World... from thread = 3

Hello World... from thread = 0

Hello World... from thread = 2

Hello World... from thread = 6

Hello World... from thread = 1

Hello World... from thread = 4

Hello World... from thread = 7

Hello World... from thread = 5

CC++fortran

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15#include <stdio.h>

#include <stdlib.h>

#include <omp.h>

int main(void)

{

// Beginning of parallel region

#pragma omp parallel

{

printf("Hello World... from thread = %d\n",

omp_get_thread_num());

}

// Ending of parallel region

return 0;

}

Compiling and Executing

On a reserved node

module load foss/2023a

gcc -o helloworld_omp helloworld_OMP.c -fopenmp

export OMP_NUM_THREADS=8

./helloworld_omp

Output

Output from the execution

Hello World... from thread = 0

Hello World... from thread = 6

Hello World... from thread = 7

Hello World... from thread = 3

Hello World... from thread = 5

Hello World... from thread = 2

Hello World... from thread = 1

Hello World... from thread = 4

1

2

3

4

5

6

7

8

9

10

11

12

13#include <iostream>

#include <omp.h>

int main(void)

{

// Beginning of parallel region

#pragma omp parallel

{

std::cout << "Hello World... from thread = " << omp_get_thread_num() << std::endl;,

}

// Ending of parallel region

return 0;

}

Compiling and Executing

On a reserved node

module load foss/2023a

g++ -o helloworld_omp helloworld_OMP.cpp -fopenmp

export OMP_NUM_THREADS=8

./helloworld_omp

Output

Output from the execution

Hello World... from thread = 0

Hello World... from thread = 2

Hello World... from thread = 6

Hello World... from thread = 4

Hello World... from thread = 7

Hello World... from thread = 3

Hello World... from thread = 5

Hello World... from thread = 1

1

2

3

4

5

6

7

8

9

10PROGRAM Parallel_Hello_World

USE OMP_LIB

!$OMP PARALLEL

PRINT *, “Hello World... from thread =  ”, OMP_GET_THREAD_NUM()

!$OMP END PARALLEL

END

Compiling and Executing

On a reserved node

module load foss/2023a

gfortran -o helloworld_omp helloworld_OMP.f -fopenmp

export OMP_NUM_THREADS=8

./helloworld_omp

Output

Output from the execution

Hello World... from thread = 3

Hello World... from thread = 0

Hello World... from thread = 2

Hello World... from thread = 6

Hello World... from thread = 1

Hello World... from thread = 4

Hello World... from thread = 7

Hello World... from thread = 5

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15#include <stdio.h>

#include <stdlib.h>

#include <omp.h>

int main(void)

{

// Beginning of parallel region

#pragma omp parallel

{

printf("Hello World... from thread = %d\n",

omp_get_thread_num());

}

// Ending of parallel region

return 0;

}

Compiling and Executing

On a reserved node

module load foss/2023a

gcc -o helloworld_omp helloworld_OMP.c -fopenmp

export OMP_NUM_THREADS=8

./helloworld_omp

Output

Output from the execution

Hello World... from thread = 0

Hello World... from thread = 6

Hello World... from thread = 7

Hello World... from thread = 3

Hello World... from thread = 5

Hello World... from thread = 2

Hello World... from thread = 1

Hello World... from thread = 4

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15#include <stdio.h>

#include <stdlib.h>

#include <omp.h>

int main(void)

{

// Beginning of parallel region

#pragma omp parallel

{

printf("Hello World... from thread = %d\n",

omp_get_thread_num());

}

// Ending of parallel region

return 0;

}

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

```

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

```

#include <stdio.h>

#include <stdlib.h>

#include <omp.h>

int main(void)

{

// Beginning of parallel region

#pragma omp parallel

{

printf("Hello World... from thread = %d\n",

omp_get_thread_num());

}

// Ending of parallel region

return 0;

}

```

#include <stdio.h>

#include <stdlib.h>

#include <omp.h>

int main(void)

{

// Beginning of parallel region

#pragma omp parallel

{

printf("Hello World... from thread = %d\n",

omp_get_thread_num());

}

// Ending of parallel region

return 0;

}

```

```

#include <stdio.h>

#include <stdlib.h>

#include <omp.h>

int main(void)

{

// Beginning of parallel region

#pragma omp parallel

{

printf("Hello World... from thread = %d\n",

omp_get_thread_num());

}

// Ending of parallel region

return 0;

}

```

On a reserved node

module load foss/2023a

gcc -o helloworld_omp helloworld_OMP.c -fopenmp

export OMP_NUM_THREADS=8

./helloworld_omp

```

module load foss/2023a

gcc -o helloworld_omp helloworld_OMP.c -fopenmp

export OMP_NUM_THREADS=8

./helloworld_omp

```

```

module load foss/2023a

gcc -o helloworld_omp helloworld_OMP.c -fopenmp

export OMP_NUM_THREADS=8

./helloworld_omp

```

Output from the execution

Hello World... from thread = 0

Hello World... from thread = 6

Hello World... from thread = 7

Hello World... from thread = 3

Hello World... from thread = 5

Hello World... from thread = 2

Hello World... from thread = 1

Hello World... from thread = 4

```

Hello World... from thread = 0

Hello World... from thread = 6

Hello World... from thread = 7

Hello World... from thread = 3

Hello World... from thread = 5

Hello World... from thread = 2

Hello World... from thread = 1

Hello World... from thread = 4

```

```

Hello World... from thread = 0

Hello World... from thread = 6

Hello World... from thread = 7

Hello World... from thread = 3

Hello World... from thread = 5

Hello World... from thread = 2

Hello World... from thread = 1

Hello World... from thread = 4

```

1

2

3

4

5

6

7

8

9

10

11

12

13#include <iostream>

#include <omp.h>

int main(void)

{

// Beginning of parallel region

#pragma omp parallel

{

std::cout << "Hello World... from thread = " << omp_get_thread_num() << std::endl;,

}

// Ending of parallel region

return 0;

}

Compiling and Executing

On a reserved node

module load foss/2023a

g++ -o helloworld_omp helloworld_OMP.cpp -fopenmp

export OMP_NUM_THREADS=8

./helloworld_omp

Output

Output from the execution

Hello World... from thread = 0

Hello World... from thread = 2

Hello World... from thread = 6

Hello World... from thread = 4

Hello World... from thread = 7

Hello World... from thread = 3

Hello World... from thread = 5

Hello World... from thread = 1

1

2

3

4

5

6

7

8

9

10

11

12

13#include <iostream>

#include <omp.h>

int main(void)

{

// Beginning of parallel region

#pragma omp parallel

{

std::cout << "Hello World... from thread = " << omp_get_thread_num() << std::endl;,

}

// Ending of parallel region

return 0;

}

1

2

3

4

5

6

7

8

9

10

11

12

13

```

1

2

3

4

5

6

7

8

9

10

11

12

13

```

#include <iostream>

#include <omp.h>

int main(void)

{

// Beginning of parallel region

#pragma omp parallel

{

std::cout << "Hello World... from thread = " << omp_get_thread_num() << std::endl;,

}

// Ending of parallel region

return 0;

}

```

#include <iostream>

#include <omp.h>

int main(void)

{

// Beginning of parallel region

#pragma omp parallel

{

std::cout << "Hello World... from thread = " << omp_get_thread_num() << std::endl;,

}

// Ending of parallel region

return 0;

}

```

```

#include <iostream>

#include <omp.h>

int main(void)

{

// Beginning of parallel region

#pragma omp parallel

{

std::cout << "Hello World... from thread = " << omp_get_thread_num() << std::endl;,

}

// Ending of parallel region

return 0;

}

```

On a reserved node

module load foss/2023a

g++ -o helloworld_omp helloworld_OMP.cpp -fopenmp

export OMP_NUM_THREADS=8

./helloworld_omp

```

module load foss/2023a

g++ -o helloworld_omp helloworld_OMP.cpp -fopenmp

export OMP_NUM_THREADS=8

./helloworld_omp

```

```

module load foss/2023a

g++ -o helloworld_omp helloworld_OMP.cpp -fopenmp

export OMP_NUM_THREADS=8

./helloworld_omp

```

Output from the execution

Hello World... from thread = 0

Hello World... from thread = 2

Hello World... from thread = 6

Hello World... from thread = 4

Hello World... from thread = 7

Hello World... from thread = 3

Hello World... from thread = 5

Hello World... from thread = 1

```

Hello World... from thread = 0

Hello World... from thread = 2

Hello World... from thread = 6

Hello World... from thread = 4

Hello World... from thread = 7

Hello World... from thread = 3

Hello World... from thread = 5

Hello World... from thread = 1

```

```

Hello World... from thread = 0

Hello World... from thread = 2

Hello World... from thread = 6

Hello World... from thread = 4

Hello World... from thread = 7

Hello World... from thread = 3

Hello World... from thread = 5

Hello World... from thread = 1

```

1

2

3

4

5

6

7

8

9

10PROGRAM Parallel_Hello_World

USE OMP_LIB

!$OMP PARALLEL

PRINT *, “Hello World... from thread =  ”, OMP_GET_THREAD_NUM()

!$OMP END PARALLEL

END

Compiling and Executing

On a reserved node

module load foss/2023a

gfortran -o helloworld_omp helloworld_OMP.f -fopenmp

export OMP_NUM_THREADS=8

./helloworld_omp

Output

Output from the execution

Hello World... from thread = 3

Hello World... from thread = 0

Hello World... from thread = 2

Hello World... from thread = 6

Hello World... from thread = 1

Hello World... from thread = 4

Hello World... from thread = 7

Hello World... from thread = 5

1

2

3

4

5

6

7

8

9

10PROGRAM Parallel_Hello_World

USE OMP_LIB

!$OMP PARALLEL

PRINT *, “Hello World... from thread =  ”, OMP_GET_THREAD_NUM()

!$OMP END PARALLEL

END

1

2

3

4

5

6

7

8

9

10

```

1

2

3

4

5

6

7

8

9

10

```

PROGRAM Parallel_Hello_World

USE OMP_LIB

!$OMP PARALLEL

PRINT *, “Hello World... from thread =  ”, OMP_GET_THREAD_NUM()

!$OMP END PARALLEL

END

```

PROGRAM Parallel_Hello_World

USE OMP_LIB

!$OMP PARALLEL

PRINT *, “Hello World... from thread =  ”, OMP_GET_THREAD_NUM()

!$OMP END PARALLEL

END

```

```

PROGRAM Parallel_Hello_World

USE OMP_LIB

!$OMP PARALLEL

PRINT *, “Hello World... from thread =  ”, OMP_GET_THREAD_NUM()

!$OMP END PARALLEL

END

```

On a reserved node

module load foss/2023a

gfortran -o helloworld_omp helloworld_OMP.f -fopenmp

export OMP_NUM_THREADS=8

./helloworld_omp

```

module load foss/2023a

gfortran -o helloworld_omp helloworld_OMP.f -fopenmp

export OMP_NUM_THREADS=8

./helloworld_omp

```

```

module load foss/2023a

gfortran -o helloworld_omp helloworld_OMP.f -fopenmp

export OMP_NUM_THREADS=8

./helloworld_omp

```

Output from the execution

Hello World... from thread = 3

Hello World... from thread = 0

Hello World... from thread = 2

Hello World... from thread = 6

Hello World... from thread = 1

Hello World... from thread = 4

Hello World... from thread = 7

Hello World... from thread = 5

```

Hello World... from thread = 3

Hello World... from thread = 0

Hello World... from thread = 2

Hello World... from thread = 6

Hello World... from thread = 1

Hello World... from thread = 4

Hello World... from thread = 7

Hello World... from thread = 5

```

```

Hello World... from thread = 3

Hello World... from thread = 0

Hello World... from thread = 2

Hello World... from thread = 6

Hello World... from thread = 1

Hello World... from thread = 4

Hello World... from thread = 7

Hello World... from thread = 5

```

### Message Passing Interface (MPI)

MPI is the technology you should use when you wish to run your program in parallel on multiple cluster compute nodes simultaneously.

Compiling an MPI program is relatively easy.

However, writing an MPI-based parallel program takes more work.

> **Source code**

> Source code

Source code

CC++fortran f90/95

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20#include <stdio.h>

#include <stdlib.h>

#include <mpi.h>

int main(int argc, char** argv)

{

int rank, size, length;

char name[BUFSIZ];

MPI_Init(&argc, &argv);

MPI_Comm_rank(MPI_COMM_WORLD, &rank);

MPI_Comm_size(MPI_COMM_WORLD, &size);

MPI_Get_processor_name(name, &length);

printf("%s: hello world from process %d of %d\n", name, rank, size);

MPI_Finalize();

return 0;

}

Compiling and Executing

On a reserved node

module load foss/2023a

mpicc -o helloworld_mpi helloworld_MPI.c

srun -n 4 ./helloworld_mpi

Output

Output from the execution

hello world from process 1 of 4

hello world from process 2 of 4

hello world from process 0 of 4

hello world from process 3 of 4

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18#include <iostream>

#include <mpi.h>

int main(int argc, char **argv)

{

MPI_Init(&argc, &argv);

int world_size;

MPI_Comm_size(MPI_COMM_WORLD, &world_size);

int my_rank;

MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);

std::cout << "hello world from process " << my_rank << " of " << world_size << std::endl;

MPI_Finalize();

return 0;

}

Compiling and Executing

On a reserved node

module load foss/2023a

mpic++ -o helloworld_mpi helloworld_MPI.cpp

srun -n 4 ./helloworld_mpi

Output

Output from the execution

hello world from process 2 of 4

hello world from process 3 of 4

hello world from process 1 of 4

hello world from process 0 of 4

1

2

3

4

5

6

7

8

9

10program hello

include 'mpif.h'

integer rank, size, ierror, tag, status(MPI_STATUS_SIZE)

call MPI_INIT(ierror)

call MPI_COMM_SIZE(MPI_COMM_WORLD, size, ierror)

call MPI_COMM_RANK(MPI_COMM_WORLD, rank, ierror)

print*, 'node', rank, ': Hello world'

call MPI_FINALIZE(ierror)

end program

Compiling and Executing

On a reserved node

module load foss/2023a

mpifort -o helloworld_mpi helloworld_MPI.f90

srun -n 4 ./helloworld_mpi

Output

Output from the execution

hello world from process 2 of 4

hello world from process 3 of 4

hello world from process 1 of 4

hello world from process 0 of 4

CC++fortran f90/95

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20#include <stdio.h>

#include <stdlib.h>

#include <mpi.h>

int main(int argc, char** argv)

{

int rank, size, length;

char name[BUFSIZ];

MPI_Init(&argc, &argv);

MPI_Comm_rank(MPI_COMM_WORLD, &rank);

MPI_Comm_size(MPI_COMM_WORLD, &size);

MPI_Get_processor_name(name, &length);

printf("%s: hello world from process %d of %d\n", name, rank, size);

MPI_Finalize();

return 0;

}

Compiling and Executing

On a reserved node

module load foss/2023a

mpicc -o helloworld_mpi helloworld_MPI.c

srun -n 4 ./helloworld_mpi

Output

Output from the execution

hello world from process 1 of 4

hello world from process 2 of 4

hello world from process 0 of 4

hello world from process 3 of 4

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18#include <iostream>

#include <mpi.h>

int main(int argc, char **argv)

{

MPI_Init(&argc, &argv);

int world_size;

MPI_Comm_size(MPI_COMM_WORLD, &world_size);

int my_rank;

MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);

std::cout << "hello world from process " << my_rank << " of " << world_size << std::endl;

MPI_Finalize();

return 0;

}

Compiling and Executing

On a reserved node

module load foss/2023a

mpic++ -o helloworld_mpi helloworld_MPI.cpp

srun -n 4 ./helloworld_mpi

Output

Output from the execution

hello world from process 2 of 4

hello world from process 3 of 4

hello world from process 1 of 4

hello world from process 0 of 4

1

2

3

4

5

6

7

8

9

10program hello

include 'mpif.h'

integer rank, size, ierror, tag, status(MPI_STATUS_SIZE)

call MPI_INIT(ierror)

call MPI_COMM_SIZE(MPI_COMM_WORLD, size, ierror)

call MPI_COMM_RANK(MPI_COMM_WORLD, rank, ierror)

print*, 'node', rank, ': Hello world'

call MPI_FINALIZE(ierror)

end program

Compiling and Executing

On a reserved node

module load foss/2023a

mpifort -o helloworld_mpi helloworld_MPI.f90

srun -n 4 ./helloworld_mpi

Output

Output from the execution

hello world from process 2 of 4

hello world from process 3 of 4

hello world from process 1 of 4

hello world from process 0 of 4

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20#include <stdio.h>

#include <stdlib.h>

#include <mpi.h>

int main(int argc, char** argv)

{

int rank, size, length;

char name[BUFSIZ];

MPI_Init(&argc, &argv);

MPI_Comm_rank(MPI_COMM_WORLD, &rank);

MPI_Comm_size(MPI_COMM_WORLD, &size);

MPI_Get_processor_name(name, &length);

printf("%s: hello world from process %d of %d\n", name, rank, size);

MPI_Finalize();

return 0;

}

Compiling and Executing

On a reserved node

module load foss/2023a

mpicc -o helloworld_mpi helloworld_MPI.c

srun -n 4 ./helloworld_mpi

Output

Output from the execution

hello world from process 1 of 4

hello world from process 2 of 4

hello world from process 0 of 4

hello world from process 3 of 4

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20#include <stdio.h>

#include <stdlib.h>

#include <mpi.h>

int main(int argc, char** argv)

{

int rank, size, length;

char name[BUFSIZ];

MPI_Init(&argc, &argv);

MPI_Comm_rank(MPI_COMM_WORLD, &rank);

MPI_Comm_size(MPI_COMM_WORLD, &size);

MPI_Get_processor_name(name, &length);

printf("%s: hello world from process %d of %d\n", name, rank, size);

MPI_Finalize();

return 0;

}

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

```

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

```

#include <stdio.h>

#include <stdlib.h>

#include <mpi.h>

int main(int argc, char** argv)

{

int rank, size, length;

char name[BUFSIZ];

MPI_Init(&argc, &argv);

MPI_Comm_rank(MPI_COMM_WORLD, &rank);

MPI_Comm_size(MPI_COMM_WORLD, &size);

MPI_Get_processor_name(name, &length);

printf("%s: hello world from process %d of %d\n", name, rank, size);

MPI_Finalize();

return 0;

}

```

#include <stdio.h>

#include <stdlib.h>

#include <mpi.h>

int main(int argc, char** argv)

{

int rank, size, length;

char name[BUFSIZ];

MPI_Init(&argc, &argv);

MPI_Comm_rank(MPI_COMM_WORLD, &rank);

MPI_Comm_size(MPI_COMM_WORLD, &size);

MPI_Get_processor_name(name, &length);

printf("%s: hello world from process %d of %d\n", name, rank, size);

MPI_Finalize();

return 0;

}

```

```

#include <stdio.h>

#include <stdlib.h>

#include <mpi.h>

int main(int argc, char** argv)

{

int rank, size, length;

char name[BUFSIZ];

MPI_Init(&argc, &argv);

MPI_Comm_rank(MPI_COMM_WORLD, &rank);

MPI_Comm_size(MPI_COMM_WORLD, &size);

MPI_Get_processor_name(name, &length);

printf("%s: hello world from process %d of %d\n", name, rank, size);

MPI_Finalize();

return 0;

}

```

On a reserved node

module load foss/2023a

mpicc -o helloworld_mpi helloworld_MPI.c

srun -n 4 ./helloworld_mpi

```

module load foss/2023a

mpicc -o helloworld_mpi helloworld_MPI.c

srun -n 4 ./helloworld_mpi

```

```

module load foss/2023a

mpicc -o helloworld_mpi helloworld_MPI.c

srun -n 4 ./helloworld_mpi

```

Output from the execution

hello world from process 1 of 4

hello world from process 2 of 4

hello world from process 0 of 4

hello world from process 3 of 4

```

hello world from process 1 of 4

hello world from process 2 of 4

hello world from process 0 of 4

hello world from process 3 of 4

```

```

hello world from process 1 of 4

hello world from process 2 of 4

hello world from process 0 of 4

hello world from process 3 of 4

```

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18#include <iostream>

#include <mpi.h>

int main(int argc, char **argv)

{

MPI_Init(&argc, &argv);

int world_size;

MPI_Comm_size(MPI_COMM_WORLD, &world_size);

int my_rank;

MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);

std::cout << "hello world from process " << my_rank << " of " << world_size << std::endl;

MPI_Finalize();

return 0;

}

Compiling and Executing

On a reserved node

module load foss/2023a

mpic++ -o helloworld_mpi helloworld_MPI.cpp

srun -n 4 ./helloworld_mpi

Output

Output from the execution

hello world from process 2 of 4

hello world from process 3 of 4

hello world from process 1 of 4

hello world from process 0 of 4

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18#include <iostream>

#include <mpi.h>

int main(int argc, char **argv)

{

MPI_Init(&argc, &argv);

int world_size;

MPI_Comm_size(MPI_COMM_WORLD, &world_size);

int my_rank;

MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);

std::cout << "hello world from process " << my_rank << " of " << world_size << std::endl;

MPI_Finalize();

return 0;

}

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

```

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

```

#include <iostream>

#include <mpi.h>

int main(int argc, char **argv)

{

MPI_Init(&argc, &argv);

int world_size;

MPI_Comm_size(MPI_COMM_WORLD, &world_size);

int my_rank;

MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);

std::cout << "hello world from process " << my_rank << " of " << world_size << std::endl;

MPI_Finalize();

return 0;

}

```

#include <iostream>

#include <mpi.h>

int main(int argc, char **argv)

{

MPI_Init(&argc, &argv);

int world_size;

MPI_Comm_size(MPI_COMM_WORLD, &world_size);

int my_rank;

MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);

std::cout << "hello world from process " << my_rank << " of " << world_size << std::endl;

MPI_Finalize();

return 0;

}

```

```

#include <iostream>

#include <mpi.h>

int main(int argc, char **argv)

{

MPI_Init(&argc, &argv);

int world_size;

MPI_Comm_size(MPI_COMM_WORLD, &world_size);

int my_rank;

MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);

std::cout << "hello world from process " << my_rank << " of " << world_size << std::endl;

MPI_Finalize();

return 0;

}

```

On a reserved node

module load foss/2023a

mpic++ -o helloworld_mpi helloworld_MPI.cpp

srun -n 4 ./helloworld_mpi

```

module load foss/2023a

mpic++ -o helloworld_mpi helloworld_MPI.cpp

srun -n 4 ./helloworld_mpi

```

```

module load foss/2023a

mpic++ -o helloworld_mpi helloworld_MPI.cpp

srun -n 4 ./helloworld_mpi

```

Output from the execution

hello world from process 2 of 4

hello world from process 3 of 4

hello world from process 1 of 4

hello world from process 0 of 4

```

hello world from process 2 of 4

hello world from process 3 of 4

hello world from process 1 of 4

hello world from process 0 of 4

```

```

hello world from process 2 of 4

hello world from process 3 of 4

hello world from process 1 of 4

hello world from process 0 of 4

```

1

2

3

4

5

6

7

8

9

10program hello

include 'mpif.h'

integer rank, size, ierror, tag, status(MPI_STATUS_SIZE)

call MPI_INIT(ierror)

call MPI_COMM_SIZE(MPI_COMM_WORLD, size, ierror)

call MPI_COMM_RANK(MPI_COMM_WORLD, rank, ierror)

print*, 'node', rank, ': Hello world'

call MPI_FINALIZE(ierror)

end program

Compiling and Executing

On a reserved node

module load foss/2023a

mpifort -o helloworld_mpi helloworld_MPI.f90

srun -n 4 ./helloworld_mpi

Output

Output from the execution

hello world from process 2 of 4

hello world from process 3 of 4

hello world from process 1 of 4

hello world from process 0 of 4

1

2

3

4

5

6

7

8

9

10program hello

include 'mpif.h'

integer rank, size, ierror, tag, status(MPI_STATUS_SIZE)

call MPI_INIT(ierror)

call MPI_COMM_SIZE(MPI_COMM_WORLD, size, ierror)

call MPI_COMM_RANK(MPI_COMM_WORLD, rank, ierror)

print*, 'node', rank, ': Hello world'

call MPI_FINALIZE(ierror)

end program

1

2

3

4

5

6

7

8

9

10

```

1

2

3

4

5

6

7

8

9

10

```

program hello

include 'mpif.h'

integer rank, size, ierror, tag, status(MPI_STATUS_SIZE)

call MPI_INIT(ierror)

call MPI_COMM_SIZE(MPI_COMM_WORLD, size, ierror)

call MPI_COMM_RANK(MPI_COMM_WORLD, rank, ierror)

print*, 'node', rank, ': Hello world'

call MPI_FINALIZE(ierror)

end program

```

program hello

include 'mpif.h'

integer rank, size, ierror, tag, status(MPI_STATUS_SIZE)

call MPI_INIT(ierror)

call MPI_COMM_SIZE(MPI_COMM_WORLD, size, ierror)

call MPI_COMM_RANK(MPI_COMM_WORLD, rank, ierror)

print*, 'node', rank, ': Hello world'

call MPI_FINALIZE(ierror)

end program

```

```

program hello

include 'mpif.h'

integer rank, size, ierror, tag, status(MPI_STATUS_SIZE)

call MPI_INIT(ierror)

call MPI_COMM_SIZE(MPI_COMM_WORLD, size, ierror)

call MPI_COMM_RANK(MPI_COMM_WORLD, rank, ierror)

print*, 'node', rank, ': Hello world'

call MPI_FINALIZE(ierror)

end program

```

On a reserved node

module load foss/2023a

mpifort -o helloworld_mpi helloworld_MPI.f90

srun -n 4 ./helloworld_mpi

```

module load foss/2023a

mpifort -o helloworld_mpi helloworld_MPI.f90

srun -n 4 ./helloworld_mpi

```

```

module load foss/2023a

mpifort -o helloworld_mpi helloworld_MPI.f90

srun -n 4 ./helloworld_mpi

```

Output from the execution

hello world from process 2 of 4

hello world from process 3 of 4

hello world from process 1 of 4

hello world from process 0 of 4

```

hello world from process 2 of 4

hello world from process 3 of 4

hello world from process 1 of 4

hello world from process 0 of 4

```

```

hello world from process 2 of 4

hello world from process 3 of 4

hello world from process 1 of 4

hello world from process 0 of 4

```

## Compiling for MeluXina FPGAs

The MeluXina Accelerator Module includes a partition with FPGA accelerators. Please clone first the oneAPI-sample repository with the git clone --depth=1 https://github.com/oneapi-src/oneAPI-samples.git in your home folder.

```

git clone --depth=1 https://github.com/oneapi-src/oneAPI-samples.git

```

As you can see Intel provides numerous code samples and examples to help your grasping the power of the oneAPI toolkit.

We are going to focus on DirectProgramming/C++SYCL_FPGA.

Create a symbolic at the root of your home directory pointing to this folder:

- As you can see Intel provides numerous code samples and examples to help your grasping the power of the oneAPI toolkit.

As you can see Intel provides numerous code samples and examples to help your grasping the power of the oneAPI toolkit.

- We are going to focus on DirectProgramming/C++SYCL_FPGA.

We are going to focus on DirectProgramming/C++SYCL_FPGA.

```

DirectProgramming/C++SYCL_FPGA

```

- Create a symbolic at the root of your home directory pointing to this folder:

Create a symbolic at the root of your home directory pointing to this folder:

ln -s oneAPI-samples/DirectProgramming/C++SYCL_FPGA/Tutorials/GettingStarted

```

ln -s oneAPI-samples/DirectProgramming/C++SYCL_FPGA/Tutorials/GettingStarted

```

```

ln -s oneAPI-samples/DirectProgramming/C++SYCL_FPGA/Tutorials/GettingStarted

```

The fpga_compile folder provides basic examples to start compiling SYCL C++ code with the DPC++ compiler

The fpga_recompile folder show you how to recompile quickly your code without having to rebuild the FPGA image

The fpga_template is a starting template project that you can use to bootstrap a project

- The fpga_compile folder provides basic examples to start compiling SYCL C++ code with the DPC++ compiler

The fpga_compile folder provides basic examples to start compiling SYCL C++ code with the DPC++ compiler

- The fpga_recompile folder show you how to recompile quickly your code without having to rebuild the FPGA image

The fpga_recompile folder show you how to recompile quickly your code without having to rebuild the FPGA image

- The fpga_template is a starting template project that you can use to bootstrap a project

The fpga_template is a starting template project that you can use to bootstrap a project

Before targeting a specific hardware accelerator, you need to ensure that the sycl runtime is able to detect it.

> **Commands**

> Commands

Commands

1

2

3

4

5

6

7

8

9# Create permanent tmux session

tmux new -s fpga_session

# We need a job allocation on a FPGA node

salloc -A <ACCOUNT> -t 48:00:00 -q default -p fpga -N 1

# In order to use the intel compiler for FPGA programing

module load intel-fpga

# The fpga_compile version setup all necessary environment variable to compile code

module load 520nmx

sycl-ls

1

2

3

4

5

6

7

8

9

```

1

2

3

4

5

6

7

8

9

```

# Create permanent tmux session

tmux new -s fpga_session

# We need a job allocation on a FPGA node

salloc -A <ACCOUNT> -t 48:00:00 -q default -p fpga -N 1

# In order to use the intel compiler for FPGA programing

module load intel-fpga

# The fpga_compile version setup all necessary environment variable to compile code

module load 520nmx

sycl-ls

```

# Create permanent tmux session

tmux new -s fpga_session

# We need a job allocation on a FPGA node

salloc -A <ACCOUNT> -t 48:00:00 -q default -p fpga -N 1

# In order to use the intel compiler for FPGA programing

module load intel-fpga

# The fpga_compile version setup all necessary environment variable to compile code

module load 520nmx

sycl-ls

```

```

# Create permanent tmux session

tmux new -s fpga_session

# We need a job allocation on a FPGA node

salloc -A <ACCOUNT> -t 48:00:00 -q default -p fpga -N 1

# In order to use the intel compiler for FPGA programing

module load intel-fpga

# The fpga_compile version setup all necessary environment variable to compile code

module load 520nmx

sycl-ls

```

> **Output**

> Output

Output

[opencl:cpu:0] Intel(R) OpenCL, AMD EPYC 7452 32-Core Processor                 3.0 [2022.13.3.0.16_160000]

[opencl:acc:1] Intel(R) FPGA Emulation Platform for OpenCL(TM), Intel(R) FPGA Emulation Device 1.2 [2022.13.3.0.16_160000]

[opencl:acc:2] Intel(R) FPGA SDK for OpenCL(TM), p520_hpc_m210h_g3x16 : BittWare Stratix 10 MX OpenCL platform (aclbitt_s10mx_pcie0) 1.0 [2022.1]

[opencl:acc:3] Intel(R) FPGA SDK for OpenCL(TM), p520_hpc_m210h_g3x16 : BittWare Stratix 10 MX OpenCL platform (aclbitt_s10mx_pcie1) 1.0 [2022.1]

```

[opencl:cpu:0] Intel(R) OpenCL, AMD EPYC 7452 32-Core Processor                 3.0 [2022.13.3.0.16_160000]

[opencl:acc:1] Intel(R) FPGA Emulation Platform for OpenCL(TM), Intel(R) FPGA Emulation Device 1.2 [2022.13.3.0.16_160000]

[opencl:acc:2] Intel(R) FPGA SDK for OpenCL(TM), p520_hpc_m210h_g3x16 : BittWare Stratix 10 MX OpenCL platform (aclbitt_s10mx_pcie0) 1.0 [2022.1]

[opencl:acc:3] Intel(R) FPGA SDK for OpenCL(TM), p520_hpc_m210h_g3x16 : BittWare Stratix 10 MX OpenCL platform (aclbitt_s10mx_pcie1) 1.0 [2022.1]

```

```

[opencl:cpu:0] Intel(R) OpenCL, AMD EPYC 7452 32-Core Processor                 3.0 [2022.13.3.0.16_160000]

[opencl:acc:1] Intel(R) FPGA Emulation Platform for OpenCL(TM), Intel(R) FPGA Emulation Device 1.2 [2022.13.3.0.16_160000]

[opencl:acc:2] Intel(R) FPGA SDK for OpenCL(TM), p520_hpc_m210h_g3x16 : BittWare Stratix 10 MX OpenCL platform (aclbitt_s10mx_pcie0) 1.0 [2022.1]

[opencl:acc:3] Intel(R) FPGA SDK for OpenCL(TM), p520_hpc_m210h_g3x16 : BittWare Stratix 10 MX OpenCL platform (aclbitt_s10mx_pcie1) 1.0 [2022.1]

```

If you see the same output, you are all setup.

Full compilation can take hours depending on your application size. In this context, emulation and static report evaluation are keys to succeed in FPGA programming

This phase produces the actual FPGA bitstream, i.e., a file containing the programming data associated with your FPGA chip. This file requires the target FPGA platform to be generated and executed. For FPGA programming, the Intel® oneAPI toolkit requires the Intel® Quartus® Prime software to generate this bitstream.

- If you see the same output, you are all setup.

If you see the same output, you are all setup.

- Full compilation can take hours depending on your application size. In this context, emulation and static report evaluation are keys to succeed in FPGA programming

Full compilation can take hours depending on your application size. In this context, emulation and static report evaluation are keys to succeed in FPGA programming

- This phase produces the actual FPGA bitstream, i.e., a file containing the programming data associated with your FPGA chip. This file requires the target FPGA platform to be generated and executed. For FPGA programming, the Intel® oneAPI toolkit requires the Intel® Quartus® Prime software to generate this bitstream.

This phase produces the actual FPGA bitstream, i.e., a file containing the programming data associated with your FPGA chip. This file requires the target FPGA platform to be generated and executed. For FPGA programming, the Intel® oneAPI toolkit requires the Intel® Quartus® Prime software to generate this bitstream.

> **Full hardware compilation**

> Full hardware compilation

Full hardware compilation

$ icpx -fsycl -fintelfpga -qactypes -Xshardware -Xsboard=p520_hpc_m210h_g3x16 -DFPGA_HARDWARE vector_add.cpp -o vector_add_report.fpga

```

$ icpx -fsycl -fintelfpga -qactypes -Xshardware -Xsboard=p520_hpc_m210h_g3x16 -DFPGA_HARDWARE vector_add.cpp -o vector_add_report.fpga

```

```

$ icpx -fsycl -fintelfpga -qactypes -Xshardware -Xsboard=p520_hpc_m210h_g3x16 -DFPGA_HARDWARE vector_add.cpp -o vector_add_report.fpga

```

The compilation will take several hours. Therefore, we strongly advise you to verify your code through emulation first.

You can also use the -Xsfast-compile option which offers a faster compile time but reduce the performance of the final FPGA image.

- The compilation will take several hours. Therefore, we strongly advise you to verify your code through emulation first.

The compilation will take several hours. Therefore, we strongly advise you to verify your code through emulation first.

- You can also use the -Xsfast-compile option which offers a faster compile time but reduce the performance of the final FPGA image.

You can also use the -Xsfast-compile option which offers a faster compile time but reduce the performance of the final FPGA image.

```

-Xsfast-compile

```

> **Note**

> Note

Note

If you need more information regarding our FPGA hardware and how to program them, please get in touch via our service desk.