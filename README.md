<!--
Team SoIC' final project
-->
# final-project
## [National Action Council for Minorities in Engineering(NACME)](https://www.nacme.org) Google Applied Machine Learning Intensive (AMLI) at the `University of Kentucky`

<!--
List all of the members who developed the project and
link to each members respective GitHub profile
-->
Developed by: 
- [Javi Cardenas](https://github.com/javic99) - `University of Illinois at Urbana-Champaign`
- [Jalen Collins](https://github.com/kingjalen22) - `University of Kentucky` 
- [Patricia Garcia](https://github.com/pagarc134) - `University of Southern California` 

Mentor:
- [Tasmia Tarin](https://github.com/tasmiatasrin) - `University of Kentucky`

## Description
<!--
Give a short description on what your project accomplishes and what tools is uses. In addition, you can drop screenshots directly into your README file to add them to your README. Take these from your presentations.

-->Using neural networks to generate story captions of images in the VIST dataset. 


# Goal
![image](https://user-images.githubusercontent.com/85462843/128641293-c6e55376-c23f-469f-863a-681679dbe761.png)
# The Difference between Image Captioning and Visual Storytelling
![image](https://user-images.githubusercontent.com/85462843/127542049-f0e734c2-d5d3-4c33-8b45-a1f6a9b101ed.png)
![image](https://user-images.githubusercontent.com/85462843/128640611-6e2522d0-01f9-48eb-9e3d-fa67a422120a.png)


## Usage instructions
<!--
Give details on how to install fork and install your project. You can get all of the python dependencies for your project by typing `pip3 freeze requirements.txt` on the system that runs your project. Add the generated `requirements.txt` to this repo.
-->The `vist_requirements.txt` file should list all Python libraries that your notebooks
depend on, and they will be installed using:

```
pip install -r vist_requirements.txt
```

1. Fork this repo
2. Change directories into your project
3. On the command line, type `pip3 install requirements.txt`
4. ....

## How To Use
# Preprocessing 
Pickle images that you are using, using Resnet50FeatureExtraction.ipynb and place them in a folder as your pickled image directory
Make sure that you have downloaded the dictionaries folder to have the keys used in the main code. 
# Code Implementation 
![image](https://user-images.githubusercontent.com/85462843/128641214-7287914c-e23f-4c73-96d6-b109ee09669a.png)

# Model
From there, you should have everything to run the model. Below you'll see the architechture that the model follows.
![image](https://user-images.githubusercontent.com/85462843/128641227-e77d6edf-4439-4339-90e3-ab7ca61c7f69.png)

# References 
https://github.com/sultanalnahian/Reverse-Frogger-A3PS/tree/main/advice%20generator
