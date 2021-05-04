# Depression-Detection

# Files
### Folders
The CSS, static/CSS and template files are all involved in the online version of the program.
With the data file being responsible for data storage

### Naive.py 
is the main file for training the AI as it uses the naive bayes model which i mainly used.
Please note that for the purposes of data security due to my ethics form I am unable to upload the data to this repository. However the file to collect data is available at 

### Manual excel
Is the mainual version of data acquisition in which a user may manually go through and label tweets. as depressed (1) or not depressed (Any other button)

### Gui
Is the interface used for local diagnosis if a user is not using the online version of the program which is available here... MisinformedOwl.pythonanywhere.com 

### Online
Is the file used in starting up a local server for my python script. When booting this file be sure to go to http://localhost:5000/ to use it.

### Preprocess
This file contains the preprocessing script for all files

### Other files
Any other .py files were test builds, they showcase the differences in accuracy, with the only exception being nltk which is a similar accuracy to sklearn however does not output a model.

# Installation
### environment
The environment will be done tomorrow

### Anaconda
To use this program the easiest way is to download anaconda. It is a hub for python, which allows the management of environements aswell as a host of different tools to be used.

### How to install
Firstly import the DepressionDetection.yml into anaconda in the environemnts tab

Then open the anaconda command prompt using thw windows key.

Navigate to the folder location using

```
  cd [The file location]
```
Side note please make sure that the folder is in the same drive as the command prompt. or it will be unable to find it. (The prompt tends to open in the C:drive for me so download to the C drive if possible)

After this youare good to go by typing 
```
  python [The file you wish to use]
```
