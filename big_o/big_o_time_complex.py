"""
Big O notation is a way to describe the performance or complexity of an algorithm.
It provides an upper bound on the growth rate of the time (or space) complexity
of an algorithm as a function of the input size.

In Big O notation, we express the efficiency of an algorithm in terms of the worst-case scenario.
It helps us analyze how the algorithm's execution time or space requirements grow
as the input size becomes arbitrarily large.

Common Big O complexities include:

O(1): Constant Time Complexity
The algorithm's running time or space requirement remains constant, regardless of the input size.

O(log n): Logarithmic Time Complexity
The algorithm's efficiency grows logarithmically with the input size.
Common in algorithms that divide the problem into smaller subproblems.

O(n): Linear Time Complexity
The algorithm's running time or space requirement grows linearly with the input size.
For example, iterating through a list.

O(n log n): Linearithmic Time Complexity
Common in efficient sorting algorithms like merge sort and heap sort.

O(n^2): Quadratic Time Complexity
The algorithm's efficiency is proportional to the square of the input size. Common in nested loops.

O(n^k): Polynomial Time Complexity
The algorithm's efficiency is a polynomial function of the input size.

O(2^n): Exponential Time Complexity
The efficiency grows exponentially with the input size.
Common in algorithms with recursive solutions that solve a problem of size n
by recursively solving two smaller problems.


Understanding Big O notation is crucial for assessing and comparing the efficiency of algorithms,
helping developers choose the most appropriate algorithm for a given problem based on
the expected input size and performance requirements.
"""

"""
Big O notation adalah cara untuk menggambarkan kinerja atau kompleksitas suatu algoritma.
Ini memberikan batas atas pertumbuhan waktu (atau ruang) kompleksitas suatu algoritma sebagai fungsi dari ukuran input.

Dalam notasi Big O, kita menyatakan efisiensi suatu algoritma dalam hal skenario terburuk.
Ini membantu kita menganalisis bagaimana waktu eksekusi
atau kebutuhan ruang algoritma berkembang ketika ukuran input menjadi semakin besar.

Kompleksitas Big O umum melibatkan:

O(1): Kompleksitas Waktu Konstan
Waktu eksekusi atau kebutuhan ruang algoritma tetap konstan, terlepas dari ukuran input.

O(log n): Kompleksitas Waktu Logaritmik
Efisiensi algoritma tumbuh secara logaritmik dengan ukuran input.
Umum pada algoritma yang membagi masalah menjadi submasalah yang lebih kecil.

O(n): Kompleksitas Waktu Linear
Waktu eksekusi atau kebutuhan ruang algoritma tumbuh linearly dengan ukuran input.
Contohnya, melakukan iterasi melalui suatu daftar.

O(n log n): Kompleksitas Waktu Linearitma
Umum pada algoritma pengurutan efisien seperti merge sort dan heap sort.

O(n^2): Kompleksitas Waktu Kuadratik
Efisiensi algoritma proporsional dengan kuadrat dari ukuran input. Umum pada perulangan bersarang.

O(n^k): Kompleksitas Waktu Polinomial
Efisiensi algoritma adalah fungsi polinomial dari ukuran input.

O(2^n): Kompleksitas Waktu Eksponensial
Efisiensi tumbuh secara eksponensial dengan ukuran input.
Umum pada algoritma dengan solusi rekursif yang menyelesaikan masalah
ukuran n dengan secara rekursif menyelesaikan dua masalah yang lebih kecil.

Memahami notasi Big O sangat penting untuk menilai dan membandingkan efisiensi algoritma,
membantu pengembang memilih algoritma yang paling sesuai untuk suatu masalah
berdasarkan ukuran input yang diharapkan dan persyaratan kinerja.

"""

"""
Big O
-> Computational complexity measures the amount of resources an algorithm requires to run
-> "Big O" is the most commonly used notation for that
"""

"""
Big O(1) - Constant Time

Operation with constant complexity
- Simple variable assignments
- Arithmetics operations and comparisons
- Reference to a specisic memory location
    (accessing elements in a list by index or in a dictionary by key)

"""


def function_contant(list_of_numbers):
    """
    select first number
    multiply by 2
    make it a string
    print it

    **there is no change of the time
    no matter the list_of_numbers value**
    """


"""
O(n) - Linear Time

The complexity indicates that the effort to run an algorithm
grows proportionally to the amount of items being processed

**generally happend to iterate the entire list**

**O(n) is generally viewed as pretty bad.
It works for small inputs, becoming unusable for large datasets**
"""


def function_linear(list_of_numbers):
    """
    access each of the list_of_numbers
    add 10 to each of the number
    """
    new_list = []
    for number in list_of_numbers:
        new_list.append(number + 10)


"""
O (n^2) - Quadratic Time

The Algorithms running in quadratic time would do
n^2 number of operations

**generally happened when have a inner loop"
"""


def function_quadratic(list_of_numbers):
    for number in list_of_numbers:
        for each in list_of_numbers:
            print(number * each)


"""
O(logn) - Logarithmic Time

The Logarithms is the inverse of the mathematical operation of exponentiation
exponentiation example of 2^4 -> 2 is base, 4 is power

example: Binary Search
"""
