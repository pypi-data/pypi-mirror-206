# Morse Code Translator

[![dot-dash](dotdash.png)](https://en.wikipedia.org/wiki/Morse_code)

[![codecov](https://codecov.io/gh/gugupy/morsecodetranslator/branch/master/graph/badge.svg?token=TG5AR36QNI)](https://codecov.io/gh/gugupy/morcecodetranslator)

Its converts plain text to morce code and vice versa and follows below rules for the conversion as per the morce-code algorithm,  
1. Single space for same char repeats  
2. Three spaces for different char  
3. Seven spaces to differentiate the word  

## Installation

### Method 1:
To install the MorceCodeTranslator just run the command `pip install -U morsecodetranslator`

### Method 2:
1. Clone the repository `git clone https://github.com/gugupy/morsecodetranslator.git`
2. Run the command `pip install -e .`


## Sample code
```python
from morsecodetranslator.morse import MorseCodeTranslator

mct = MorseCodeTranslator()
print(mct.encrypt('MORCE CODE'))
print(mct.decrypt('--   ---   .-.   -.-.   .       -.-.   ---   -..   .'))
```
### output
``` textmate
--   ---   .-.   -.-.   .       -.-.   ---   -..   .  
MORCE CODE
```
