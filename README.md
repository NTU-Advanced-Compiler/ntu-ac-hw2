# Homework 2: SSA Construction for Bril

## Overview

This assignment focuses on implementing the Static Single Assignment (SSA) construction algorithm for Bril programs. You will transform non-SSA Bril programs into SSA form, enhancing your understanding of compiler design and optimization techniques.

## Prerequisites

- Python 3.6+
- Bril toolchain

## Getting Started

1. Clone the repository:
   ```bash
   git clone --recursive <url-of-your-forked-repo>
   ```

2. Navigate to the homework directory:
   ```bash
   cd <homework-directory>
   ```

## Project Structure
```
homework-directory/
├── src/
│ ├── driver.py
│ ├── bril.py
│ ├── cfg.py
│ ├── dominance.py
│ ├── is_ssa.py
│ └── ssa_construct.py
├── tests/
│ ├── simple.bril
│ └── [additional test cases]
└── README.md
```


## Implementation Tasks

1. CFG Construction (`cfg.py`)
2. Dominator Computation (`dominance.py`)
3. Phi-Function Insertion (`ssa_construct.py`)
4. Variable Renaming (`ssa_construct.py`)

## Running and Testing

1. To generate the SSA form of your program:
```bash
bril2json < ./tests/[your_test_program].bril | python3 ./src/driver.py | bril2txt > output.bril
```
2. To check if the generated program is in SSA form:
```bash
bril2json < ./output.bril | python3 src/is_ssa.py
```
3. To compare the execution output of the original and transformed programs:
```bash
# Original program
bril2json < ./tests/[your_test_program].bril | brili [arguments] > original.out

# Transformed SSA program
bril2json < ./output.bril | brili [arguments] > transformed.out

# Compare outputs
diff original.out transformed.out
```


## Submission Instructions

1. Implement all required functionalities in the `src/` directory.
2. Test your implementation thoroughly.
3. Commit and push your changes:
   ```bash
   git add src/
   git commit -m "Completed Homework 2"
   git push origin main
   ```
4. Verify that the GitHub Actions workflow passes all tests.

## Additional Resources

- [Bril Language Reference](https://capra.cs.cornell.edu/bril/lang/index.html)
- Course lecture notes on SSA form and related algorithms