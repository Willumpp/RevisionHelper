Project Created ~June 2020

# RevisionHelper
Program to read and display custom made revision cards in a tree of folders.

## Wildcards
```
-   :   Randomly selected line to read
#   :   Comment, is ignored
=   :   Always said if file is chosen

[]  :	Enter list of numbers to remove specified words (0 is first word)
    Example:
    [0,2] 1855 , 4200 converts arrived in Utah
    -> [0,2] _____ , _____ converts arrived in Utah



*   :   List component, ingnored on random selection
*[] :	Enter list of numbers to remove specified words (0 is first word) , but as a list component ; ingnored on random selection and reveal lists

CLS :   (Consecutive list start). When randomly chosen, everything in the list is said one by one in order. Title is said in full.
CLE :   (Consecutive list end). Defines the end of the consecutive list. Isnt read randomly.
    Example:
    CLS Sodium Thiosulfate and HCL
    * Step 1
    * Step 2

    * Step 3
    CLE

RLS :   (Reveal list start). When randomly chosen, the ENTIRE list is said until the breakpoint ; not words are removed upon reveal. Title is said in full
RLE :   (Reveal list end). Defines the end of the reveal list. Isnt read randomly.
RBP :   (Reveal break point). Reads entire reveal list until this point. Does not break out of the list like RLE
    Example:
    RLS Gold Rush Narrative
    * Point 1
    * Point 2
    * Point 3

    RBP

    * Point 1
    * Point 2 
    * Point 3
    RLE
```
