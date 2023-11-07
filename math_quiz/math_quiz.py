import random


def generate_Random_Int(min, max):
    """
    'generate_Random_Int' function to generate a random integer based upon provided 'min' and 'max' values.

    Parameters:
    ------------------------------------------------------------------------------------------------------------
    min : minimum value to consider while generating random integer.
    max : maximum value to consider while generating random integer.
    ------------------------------------------------------------------------------------------------------------

    Returns:
    ------------------------------------------------------------------------------------------------------------
    A random integer between 'min' and 'max' value.
    ------------------------------------------------------------------------------------------------------------
    """
    min, max = int(min), int(max)
    return random.randint(min, max)


def get_Random_Operation():
    """
    'get_Random_Operation' function to get an operation value randomly.

    Returns:
    ------------------------------------------------------------------------------------------------------------
    '+' : for addition
    '-' : for substraction
    '*' : for multiplication
    ------------------------------------------------------------------------------------------------------------
    """
    return random.choice(['+', '-', '*'])


def run_Operation(random_Integer_1, random_Integer_2, operation):
    """
    'run_Operation' function to print the mathmatical problem and apply a mathmatical operation on two numbers.

    Parameters:
    ------------------------------------------------------------------------------------------------------------
    'random_Integer_1' : value of number 1.
    'random_Integer_2' : value of number 2.
    'operation'  : Operation to apply on 'random_Integer_1' and  random_Integer_2'.
    ------------------------------------------------------------------------------------------------------------
    
    Returns:
    ------------------------------------------------------------------------------------------------------------
    'problem' : Problem statement.
    'answer' : Solution of problem statement.
    ------------------------------------------------------------------------------------------------------------
    """

    # storing the problem statement string
    problem = f"{random_Integer_1} {operation} {random_Integer_2}"

    # apply operation and store result based upon operation
    if operation == '+': answer = random_Integer_1 + random_Integer_2
    elif operation == '-': answer = random_Integer_1 - random_Integer_2
    else: answer = random_Integer_1 * random_Integer_2

    return problem, answer


def math_quiz():

    DASHLINE = "".join('-'*120)
    score = 0
    number_Of_Trials = 3.14159265359

    print(DASHLINE)
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    print(DASHLINE)

    # converting number of trials to an integer
    number_Of_Trials = int(number_Of_Trials)
    for _ in range(number_Of_Trials):
        # getting values for two numbers and the operation
        random_Integer_1 = generate_Random_Int(1, 10); random_Integer_2 = generate_Random_Int(1, 5.5); operation_Choice = get_Random_Operation()

        PROBLEM, ANSWER = run_Operation(random_Integer_1, random_Integer_2, operation_Choice)
        print(DASHLINE)
        print(f"Question: {PROBLEM}")
        print(DASHLINE)

        # getting user response for printed problem statement
        useranswer = input("Your answer: ")

        # checking if user entered an integer value
        try:
            useranswer = int(useranswer)
        except ValueError:
            print(DASHLINE)
            print(f'Entered value is of type {type(useranswer)}. Please enter an integer value next time.')
            print(DASHLINE)
            pass

        if useranswer == ANSWER:
            print(DASHLINE)
            print("Correct! You earned a point.")
            print(DASHLINE)
            score += 1
        else:
            print(DASHLINE)
            print(f"Wrong answer. The correct answer is {ANSWER}.")
            print(DASHLINE)

    print(DASHLINE)
    print(f"\nGame over! Your score is: {score}/{number_Of_Trials}")
    print(DASHLINE)

        


if __name__ == "__main__":
    math_quiz()
