# Problem Solving workshop, 22nd February 2023

## Motivation of the workshop
We, as developers, realized that introducing concept after concept does not work very well, it is simply too abstract. We should begin by describing computer science as "the study of systematic problem-solving".

Computer science is concerned with computation, a phenomenon that affects everyone. It is not just about cell phones, laptop computers, or the Internet. Consider folding a paper airplane, driving to work, preparing a meal, or even transcription of DNA, a process that occurs in your cells millions of times while you are reading this sentence.

These are all examples of computation, a systematic way of problem solving, even though most people would not perceive them as such.

A basic understanding of computation thus provides benefits similar to a basic knowledge of physics, chemistry, and biology in making sense of the world and tackling many real-world problems more effectively. This aspect of computation is often referred to as computational thinking.

[In our second event](https://stsquared.github.io/events/2023/02/20/second-event.html) as the group "She and They do Science and Tech", we organise a workshop focused on helping participants get comfortable with “thinking like a programmer” and use hands-on exercises to explain the principles of problem-solving, computational thinking, and algorithmic.

## Workshop material
Two powerpoint presentations are available in this repository. Please go through them before attempting the exercises. They will give you the principles to know on how to solve a problem in a methodic way:

1. [Introduction_to_problem_solving.pptx](https://github.com/STSTDSI/ProblemSolving_22Feb2023/blob/main/Introduction_to_problem_solving.pptx)
	
2. [problem_solving_through_algorithms.pptx](https://github.com/STSTDSI/ProblemSolving_22Feb2023/blob/main/problem_solving_through_algorithms.pptx)

## Exercises
This repository contains three different coding exercises for you to try (the answers are provided, so try to code them without looking at first).
First, follow the setup instructions below, and then start trying to code the exercises!

### Exercise 1: Guess_number.py
a) Write a guessing game, where the computer has to find a number you picked. You will need to help the computer by telling the range in which the number you picked is (e.g. if you picked "86", you can tell the computer that the value is comprised between 0 and 150). Then, you will reply to the computer guesses by "too high" or "too low", until it finds the number.

b) Write a guessing game, where the computer picks a random number (without you knowing it), and you have to guess the number. You will guess numbers, and the computer will tell you whether it is too high, or too low, or exact!

### Exercise 2: First_Basic_Game.py

Using the [PyGame library](https://www.pygame.org/docs/), display in a window a square with white white background and a solid blue circle in the center. You can play around with sizes, colors, shapes, flips. Don't forget to make sure to exit the game when the participant closes the window. This game will help you search for information and teach you how to use an external library.

### Exercise 3: Intialize_Garden_Game.py

## Setup
- Make sure you have Python3 installed
- Clone this project directory on your local machine. 
- On your local machine, change directory to the project directory  i.e. ProblemSolving_22Feb2023.
    
    ```cd ProblemSolving_22Feb2023```
    
1. Set up your conda environment:
	- Install [Anaconda](https://docs.anaconda.com/anaconda/install/index.html)
	- Create the environment
```
$ conda create --name problemsolving
$ conda activate problemsolving
```

2. Install the dependencies: 
```
$ conda install pip
$ pip install -r requirements.txt
```
  
3. Install the [Pygame](https://www.pygame.org/docs/) library
```
$python3 -m pip install -U pygame
```

You are now set up! You can try the following command to verify that the library is installed:

```
$python3 -m pygame.examples.aliens
```

## Resources
We recommand the following resources to improve your coding skill:\
[Computer Programming Problems](https://mathschallenge.net/links/programming)\
[Think Like A Programmer](https://www.pdfdrive.com/think-like-a-programmer-an-introduction-to-creative-problem-solving-e156859116.html)\
[Learning Python](https://learnpython.org)
