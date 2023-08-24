# Factorization Mission

Welcome to the Factorization Mission! We have detected an unsecured network containing numbers used to encrypt highly confidential documents. Our analysis suggests that these numbers might not be adequately protected by large prime numbers. Your task, should you choose to accept it, is to rapidly factorize these numbers before the target addresses this vulnerability, enabling us to decipher the encrypted documents.

## Objective: Factorize All the Things!

Your primary goal is to factorize as many numbers as possible into a product of two smaller numbers.

### Usage Instructions

To get started, use the following command line format:
```
factors <file>
```
Where `<file>` represents a file containing natural numbers that need to be factorized. Each number should appear on a separate line.

**Please Note**:
- All lines in the file will be valid natural numbers greater than 1.
- There will be no empty lines or spaces before/after the valid numbers.
- The file will always end with a new line.

### Output Format

Your program should output the factorization of each number in the format `n=p*q`, where `p` and `q` are the two smaller numbers that multiply to give `n`. These factors do not necessarily have to be prime numbers.

**Example**:
```
Input:
12
34

Output:
12=3*4
34=17*2
```
