#!/usr/bin/env python
# coding: utf-8

# # Welcome to Jupyter!

# This repo contains an introduction to [Jupyter](https://jupyter.org) and [IPython](https://ipython.org).
# 
# Outline of some basics:
# 
# * [Notebook Basics](../examples/Notebook/Notebook%20Basics.ipynb)
# * [IPython - beyond plain python](../examples/IPython%20Kernel/Beyond%20Plain%20Python.ipynb)
# * [Markdown Cells](../examples/Notebook/Working%20With%20Markdown%20Cells.ipynb)
# * [Rich Display System](../examples/IPython%20Kernel/Rich%20Output.ipynb)
# * [Custom Display logic](../examples/IPython%20Kernel/Custom%20Display%20Logic.ipynb)
# * [Running a Secure Public Notebook Server](../examples/Notebook/Running%20the%20Notebook%20Server.ipynb#Securing-the-notebook-server)
# * [How Jupyter works](../examples/Notebook/Multiple%20Languages%2C%20Frontends.ipynb) to run code in different languages.

# You can also get this tutorial and run it on your laptop:
# 
#     git clone https://github.com/ipython/ipython-in-depth
# 
# Install IPython and Jupyter:
# 
# with [conda](https://www.anaconda.com/download):
# 
#     conda install ipython jupyter
# 
# with pip:
# 
#     # first, always upgrade pip!
#     pip install --upgrade pip
#     pip install --upgrade ipython jupyter
# 
# Start the notebook in the tutorial directory:
# 
#     cd ipython-in-depth
#     jupyter notebook

# In[2]:


import random
import math


# In[29]:


num_guesses = 0
print('Hello! What is your name?: ')
myName = input()


# In[31]:


number = random.randint(1,50)
print(myName + ", guess a number between 1 and 50. You can make 5 guesses.")


# In[ ]:


while num_guesses < 6:
    print('Take a guess: ')
    guess = input()
    guess = int(guess)
    
    num_guesses += 1
    
    if guess < number:
        print('Your guess is too small!')
    elif guess > number:
        print('Your guess is too big!')
    elif guess == number:
        break
    
    
if guess == number:
    num_guesses = str(num_guesses)
    print("Congrats " + myName + ", you guessed the correct number in " + num_guesses + " tries!")

if guess != number:
    number = str(number)
    print("The number was " + number + ". Better luck next time!")

