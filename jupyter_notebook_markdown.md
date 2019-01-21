# Headers:
---
Use #, ##, ###, or #### infront of text to make headers. A single pound sign is the largest and 4 pounds is the smallest header. 

# Header 1
## Header 2
### Header 3
#### Header 4

# Colorful Text:

Use the following code to make colorful text. 

    <font color=blue>
        Text
    </font>


blue:
<font color=blue>
    Text
</font>
<br>
red:
<font color=red>
    Text
</font>
<br>
green:
<font color=green>
    Text
</font>
<br>
pink:
<font color=pink>
    Text
</font>
<br>
yellow:
<font color=yellow>
    Text
</font>
<br>
orange:
<font color=yellow>
    Text
</font>
<br>
grey:
<font color=grey>
    Text
</font>
<br>
purple:
<font color=purple>
    Text
</font>
<br>
cyan:
<font color=cyan>
    Text
</font>
<br>
firebrick:
<font color=firebrick>
    Text
</font>



__You can mix colors.__

    blue|red: 
    <font color=blue|red>
        Text
    </font>


<br>
blue|red: 
<font color=blue|red>
    Text
</font>

<br>
red|blue: 
<font color=red|blue|>
    Text
</font>


<br>
red|green: 
<font color=red|green>
    Text
</font>

<br>
green|red: 
<font color=green|red>
    Text
</font>

<br>
blue|red|green|pink|yellow:
<font color=blue|red|green|pink|yellow>
    Text
</font>


__But why would you when you can use any of the [colors here.](https://matplotlib.org/examples/color/named_colors.html)__

navy, darkblue, mediumblue, dodgerblue:
<br>
<font color=navy>
    Text
</font>
<br>
<font color=darkblue>
    Text
</font>
<br>
<font color=mediumblue>
    Text
</font>
<br>
<font color=dodgerblue>
    Text
</font>

# Changing Font Sizes:
Use the following code to change the font size of text to size 6.

    <font size=6>
    I love my Dog!
    </font>

<font size=4>
I love my Dog!
</font>

<font size=5>
I love my Dog!
</font>

<font size=6>
I love my Dog!
</font>

# Bold Font:

To make bold font, like I have been, you use __  ot ** both before and after the text. 

__This is bold, and still not a header.__

**This is also bold text.**

<b>Another way to bold text. </b>

# Italic Font:

Similar to bold text, but reduce number of uncerscores and stars by 1.

*This is italic.*

_Also italic._

<i>Another way to italicize text. </i>

# Underline Text:
<span style="text-decoration:underline">
This is underlined.
</span>

<u>Another way to underline that is easier to remember. </u>

# Monospace Font:
Surround text by the back single quotation mark.

`This is monospace font.`

`It is good for code.`

# Indentation:

Use > to get indented text. Goes up to 4 indentations. 

> Indent 1
>> Indent 2
>>> Indent 3
>>>> Indent 4


# Bullets:
Use an asterisk (*) or a hyphen(-) for bullets. 
* bullet 1 using asterisk
* bullet 2 using asterisk
* bullet 3 using asterisk

- bullet 1 using hyphen
- bullet 2 using hyphen
- bullet 3 using hyphen


* A
    * A.1
        * A.1.1
        * A.1.2
        * A.1.3
    * A.2
    * A.3 
* B
* C

# Numbering Lists:
1. Item 1
    1. sub item 1
        1. sub sub item 1
        2. sub sub item 2
        3. sub sub item 3
    2. sub item 2
    3. sub item 3
2. Item 2
3. Item 3

# Colored Boxes:
Use one of the following <div> tags to display text in a colored box.



The color of the box is determined by the alert type that you specify:
Blue boxes (alert-info)
<div class="alert alert-block alert-info">
<b>Tip:</b> Use blue boxes (alert-info) for tips and notes. 
If it’s a note, you don’t have to include the word “Note”.
</div>Copy
Yellow boxes (alert-warning)
<div class="alert alert-block alert-warning">
<b>Example:</b> Use yellow boxes for examples that are not 
inside code cells, or use for mathematical formulas if needed.
</div>Copy
Green boxes (alert-success)
<div class="alert alert-block alert-success">
<b>Up to you:</b> Use green boxes sparingly, and only for some specific 
purpose that the other boxes can't cover. For example, if you have a lot 
of related content to link to, maybe you decide to use green boxes for 
related links from each section of a notebook.
</div>Copy
Red boxes (alert-danger)
<div class="alert alert-block alert-danger">
<b>Just don't:</b> In general, avoid the red boxes. These should only be
used for actions that might cause data loss or another major issue.
</div>



# Python Code:

```python
print('E.T. Phone Home')

```

# Tables:

|  a  |  b  |  c  |
| --- | --- | --- |
|  1  |  2  |  3  |
|  4  |  5  |  6  |
|  7  |  8  |  9  |

# Latex Math:
$y = m x + b$

$\alpha$, $\beta$, $\gamma$, $\delta$


__Normal Distribution PDF Equation, coppied from its [Wikipedia page](https://en.wikipedia.org/wiki/Normal_distribution)__

${\displaystyle {\frac {1}{\sqrt {2\pi \sigma ^{2}}}}e^{-{\frac {(x-\mu )^{2}}{2\sigma ^{2}}}}}$

__Normal Distribution Moments, example of conditionals__

${\displaystyle \operatorname {E} \left[X^{p}\right]={\begin{cases}0&{\text{if }}p{\text{ is odd,}}\\\sigma ^{p}(p-1)!!&{\text{if }}p{\text{ is even.}}\end{cases}}}$

__Normal Distribution Fisher Information, matrices__

${\displaystyle {\mathcal {I}}(\mu ,\sigma )={\begin{pmatrix}1/\sigma ^{2}&0\\0&2/\sigma ^{2}\end{pmatrix}}}$

${\displaystyle {\mathcal {I}}(\mu ,\sigma ^{2})={\begin{pmatrix}1/\sigma ^{2}&0\\0&1/(2\sigma ^{4})\end{pmatrix}}} {\displaystyle {\mathcal {I}}(\mu ,\sigma ^{2})={\begin{pmatrix}1/\sigma ^{2}&0\\0&1/(2\sigma ^{4})\end{pmatrix}}}$




# Images:

    <img src="https://upload.wikimedia.org/wikipedia/commons/7/74/Normal_Distribution_PDF.svg" alt="Normal Distribution PDF" title="Normal Distribution PDF" />

<img src="https://upload.wikimedia.org/wikipedia/commons/7/74/Normal_Distribution_PDF.svg" alt="Normal Distribution PDF" title="Normal Distribution PDF" />


