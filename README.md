# Python and oTree Crash Course
## IMPRS BeSmart Summer School
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/aseyq/imprs/HEAD)

# Day 1 - Monday, 7th August 2023
| Session | Course | Subject                                      | Slides |
|---------|--------|----------------------------------------------|--------|
| I       | Python | Intoduction, Variables, Types                |[link](https://www.saral.it/imprs/slides/s1_python1.html)|
| II      | Python | Lists, Logicals, Conditionals, Dictionaries  |[link](https://www.saral.it/imprs/slides/s2_python2.html)        |
| III     | Python | Classes                                      |[link](https://www.saral.it/imprs/slides/s3_python3.html)        |
| IV      | Python | Modules, Packages, Ecosystem                 |[link](https://www.saral.it/imprs/slides/s4_python4.html)        |

# Day 2 - Tuesday, 8th August 2023
| Session | Course | Subject                                      | Slides |
|---------|--------|----------------------------------------------|--------|
| V       | oTree  | Introduction, Structure, Individual Experiments |  [link](https://www.saral.it/imprs/slides/s5_otreeintro.html#/title-slide)|  |
| VI      | oTree  | Group Experiments, Homogenous Groups     |  [link](https://www.saral.it/imprs/slides/s6_group.html#/title-slide)   |
| VII     | oTree  | Heterogeneous Groups                         |  [link](https://www.saral.it/imprs/slides/s7_group2.html#/title-slide)  |
| VIII    | oTree  | Matching, Apps                               |  [link](https://www.saral.it/imprs/slides/s8_matching.html#/title-slide)   |

# Day 3 - Wednesday, 9th August 2023

| Session | Course | Subject                                      | Slides |
|---------|--------|----------------------------------------------|--------|
| IX      | oTree  | Advanced Pages and Templates, HTML, JS       |  TBA   |
| X      | oTree  | Simultaneous Games, Live Method               |  TBA   |
| XI     | oTree  | Deploying, ~~Testing and Bots~~               |  TBA   |
| XII    | oTree  | Online Experiments: Challenges and Tips       |  TBA   |


# Assignment for Day 3 

Take the Public Goods Game we used. Do the following:
1- Set the number of rounds to 3

2a- Add a Welcome page and add some welcome messages to it

2b- Make it visible only on the first page (hint: look at the documentation for `is_displayed`)
3- Show the contributions of other players in the group (including or excluding myself)
    Hint: 
    
  - Path 1: You can create a list of contributions and input it into the template. Then you need to check `vars_for_template` in the documentation.
    
  - Path 2: You can loop over the players in the group in the template. Check `{{ for p in group.get_players }}` in the documentation. This is the template version of group.get_players(). 

# Requirements on your machine
- Python 3.8 or higher https://www.python.org/downloads/
- Pip (should be automatically installed with Python)
- Visual Studio Code (https://code.visualstudio.com/download) or a text editor of your preference
- Also, please get a GitHub account if you can.
