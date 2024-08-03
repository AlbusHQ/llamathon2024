"""
.opx XML explainer

Grid is -200,200 by -200,200, whereby 0,0 is center
Every property "x0" "y0" "x1" "x2" denotes line vertex
If any property = 0, the property is omitted
e.g. Index 5 below is "x0"=0 but <void property="x0">  is omitted 

"""

### Aux line, renders black
<void property="type">
        <int>1</int>
       </void>

### Mountain Fold, renders red
 <void property="type">
        <int>2</int>
       </void>
       
### Valley Fold, renders blue
 <void property="type">
        <int>3</int>
       </void>
       
"""
Example in screenshots, where one red Mountain Fold line is intersecting
one longer blue Valley fold at (-50.0, -50.0) hence the red Mountain Fold is
represented as two lines <void index="5"> and <void index="5"> with <void property="type">
<int>2</int> </void>
"""
    <void index="5">
      <object class="oripa.OriLineProxy">
       <void property="type">
        <int>2</int>
       </void>
       <void property="x1">
        <double>-50.0</double>
       </void>
       <void property="y0">
        <double>-100.0</double>
       </void>
       <void property="y1">
        <double>-50.0</double>
       </void>
      </object>
     </void>
     <void index="6">
      <object class="oripa.OriLineProxy">
       <void property="type">
        <int>2</int>
       </void>
       <void property="x0">
        <double>-50.0</double>
       </void>
       <void property="x1">
        <double>-100.0</double>
       </void>
       <void property="y0">
        <double>-50.0</double>
       </void>

"""
Random thoughts, upload to github project later
We need to establish origami algebraic notation, have not found one

Example labeling of points

A
B
AA
BB
CC
AAA
BBB
CCC

Requirements

1. Needs Prime, e.g. A and A' to denote other side of line
2. Need standard (0,0) origin notation
3. Need to fold in a certain order
4. Need to denote certain lines
	dotted line
	solid line
	front
	back
5. Need to encapsulate Yoshizawa-Randlett system into algebraic notation
	https://en.wikipedia.org/wiki/Yoshizawa%E2%80%93Randlett_system

Open Questions

1. Is there a need to render / draw lines in a certain order?
2. Should rendering and folding be done in the same step?
3. How to render 3D self folding?
4. Systematically render origami book instruction / manual?
5. Algorithmically render Youtube tutorial video?

Goals - Long Term
1. Build Largest collection of origami instructions with algebraic notation
2. Grassroots, open-source evangelism. Global origami enthusiast, please contribute.
3. Should data become structured, this could be Fun Evals for foundation model
    

Reference Chess - algebraic notation.
https://en.wikipedia.org/wiki/Algebraic_notation_(chess)
     
"""