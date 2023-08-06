<a id="readme-top"></a> 



<!-- PROJECT SUMMARY -->
<br />
<div align="center">
  <img src="https://iili.io/HSYZJQ2.gif" alt="Logo">
  <br />
  
  <p align="center">
    A zero-dependency wrapper for NIX console control in Python
    <br />
    <a href="https://github.com/Kieran-Lock/graphnix/blob/master/DOCUMENTATION.md"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#about-the-project">About the Project</a>
    ·
    <a href="#getting-started">Getting Started</a>
    ·
    <a href="#basic-usage">Basic Usage</a>
    ·
    <a href="https://github.com/Kieran-Lock/graphnix/blob/master/DOCUMENTATION.md">Documentation</a>
    ·
    <a href="https://github.com/Kieran-Lock/graphnix/blob/master/LICENSE">License</a>
  </p>
</div>



<!-- ABOUT THE PROJECT -->
## About the Project

Graphnix is a lightweight wrapper for NIX console control for python, built with a focus on API usability.  
By abstracting away low-level console interactions, Graphnix provides and interface through which you can receive both keyboard and mouse input, trigger custom events, and build simple, interactable user interfaces with ease. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Graphnix is available on [PyPI](https://pypi.org/project/graphnix). Simply install the package into your project environment with PIP:
```
pip install graphnix
```

To install specific previous versions, take a look at the [version history](https://github.com/Kieran-Lock/graphnix/releases), locate the version tag `(vX.Y.Z)`, and run:
```
pip install graphnix==X.Y.Z
```

Graphnix has **ZERO** external dependencies - it uses only ASCII codes to manage console input.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- BASIC USAGE EXAMPLES -->
## Basic Usage

### Configuring the Console
To receive console input in your codebase, use the `console_inputs()` context manager: 
```py
from graphnix import console_inputs


with console_inputs():
    ...  # Code reliant on console input
```

### Receiving Console Input
To receive console input, including both keyboard and mouse events, use the `read_console()` function.  
The below snippet receives console input, and if the input "x" is detected, the program exits: 
```py
from graphnix import read_console, console_inputs


EXIT_KEY = "x"


with console_inputs():
    while (console_input := read_console()) != EXIT_KEY:
        print(console_input)
```

_For more examples and specific detail, please refer to the [Documentation](https://github.com/Kieran-Lock/graphnix/blob/master/DOCUMENTATION.md)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- COMPLEX USAGE EXAMPLES -->
## Complex Usage
For more complex use cases, it is best to organise your application input listeners into a `Screen` class. These have the following advantages:
* Easier Event Listeners
* GUI Layer Management
* Easier GUI Manipulation
* Mouse Event Regions
Usage examples for using screens are below:

### Creating a Screen
To create a screen, inherit from the `Screen` class - this will be a singleton:
```py
from ConsoleInteraction import Screen


class ApplicationScreen(Screen):
    def __init__(self) -> None:
        super().__init__("Base")
        self.base_layer = self.get_layer("Base")
```

### Creating Layers
You can create several layers for a screen, in the class initializer:
```py
from ConsoleInteraction import Screen


class ApplicationScreen(Screen):
    def __init__(self) -> None:
        super().__init__("Base")
        self.base_layer = self.get_layer("Base")
        self.second_layer = self.add_layer("Two")
        self.third_layer = self.add_layer("Three")
```

### Keyboard Input Listeners
You can create custom keyboard events which trigger when a specific keyboard input is received, as below:
```py
from ConsoleInteraction import Screen
from string import digits


class ApplicationScreen(Screen):
    def __init__(self) -> None:
        super().__init__("Base")
        self.base_layer = self.get_layer("Base")
        self.second_layer = self.add_layer("Two")
        self.third_layer = self.add_layer("Three")

    @Screen.KeyboardInteraction("x")  # KeyboardEvent.ANY can be used as an argument to listen for any keyboard input
    def input_number(self, interaction: KeyboardEvent) -> None:
        ...  # Custom Keyboard Event
```

### Mouse Input Listeners
You can create custom mouse events which trigger when a specific mouse input is received, as below:
```py
from ConsoleInteraction import Screen


class ApplicationScreen(Screen):
    def __init__(self) -> None:
        super().__init__("Base")
        self.base_layer = self.get_layer("Base")
        self.second_layer = self.add_layer("Two")
        self.third_layer = self.add_layer("Three")

    @Screen.MouseInteractionZone("Left Mouse Button Down", Polygon([(0, 0), (11, 0), (11, 6), (0, 6)]))  # (Event Type, Interaction Zone)
    def select_slot(self, interaction: MouseEvent) -> None:
        ...  # Custom Mouse Event
```

### Writing to the Screen
You can write text to a specific layer as below - the target layer must be specified:
```py
screen = ApplicationScreen()
text = "Text to write"
screen.base_layer.change_at(0, 0, text)  # Write text at the top-left corner of the screen
```

### Reading from the Screen
When reading from the screen, you can read its entire visible contents with `screen.read()`:
```py
screen = ApplicationScreen()
screen = ApplicationScreen()
text_1 = "This is the first line"
text_2 = "This is the second line"
screen.base_layer.change_at(0, 0, text_1)  # Write text at the top-left corner of the screen
screen.layer_two.change_at(0, 1, text_2)  # Write text just beneath the top-left corner of the screen

contents = screen.read()  # Contains text from all layers
```
This method can also be found on a `Layer` object, and will read all of only the target layer, even if it is obscured.

### Clearing the Screen
You can clear the entire screen with `screen.clear()`:
```py
screen = ApplicationScreen()
text_1 = "This is the first line"
text_2 = "This is the second line"
screen.base_layer.change_at(0, 0, text_1)  # Write text at the top-left corner of the screen
screen.layer_two.change_at(0, 1, text_2)  # Write text just beneath the top-left corner of the screen

screen.base_layer.clear()  # Clear all of the previously written text
```
This method can also be found on a `Layer` object, and will clear only the target layer.

### Getting Screen Dimensions
You can query the current dimensions of the screen like so:
```py
screen = ApplicationScreen()
text = "Text to write"  # 13 Characters Long
screen.base_layer.change_at(0, 0, text)  # Write text at the top-left corner of the screen

screen.get_size()  # Returns the tuple: (13, 1)
```
The dimensions of the screen are not fixed. They will change as the screen contents change, to fit the content.

### Debug Layer
The need for a debug layer is regularly required, which allows for the normal print statement functionality to be mimicked:
```py
from ConsoleInteraction import Screen
from typing import Any


class ApplicationScreen(Screen):
    def __init__(self) -> None:
        super().__init__("Base")
        self.base_layer = self.get_layer("Base")
        self.second_layer = self.add_layer("Two")
        self.third_layer = self.add_layer("Three")
        self.debug_layer = self.add_layer("Debug", floating=True)  # Layer always remains at the top

    def debug(self, log: Any) -> None:  # Helper function to log anything at the bottom of the screen
        self.debug_layer.change_at(0, self.get_size()[1] + 1, str(log))
```



## Event Codes
Below is a list of possible special event codes that can be broadcasted and listened for:
```py
BASIC UNICODE CODES
"Shift + Backspace"
"Tab"
"Enter"
"Backspace"

BASIC CSI SEQUENCES
"Up Arrow"
"Down Arrow"
"Left Arrow"
"Right Arrow"
"End"
"Shift + Tab"

MOUSE CODES
"Left Mouse Button"
"Middle Mouse Button"
"Right Mouse Button"
"Left Mouse Button (Dragged)"
"Middle Mouse Button (Dragged)"
"Right Mouse Button (Dragged)"
"Move"
"Scroll Up"
"Scroll Down"

SPECIAL CODES
"Insert"
"Delete"
"Page Up"
"Page Down"
"F1"
"F2"
"F3"
"F4"
"F5"
"F6"
"F7"
"F8"
"F9"
"F10"
"F11"
"F12"

NUMPAD KEYS
"Up Arrow"
"Down Arrow"
"Left Arrow"
"Right Arrow"
"End"
"Home"
```
Events that do not appear on this list are likely to be under the alias of the key pressed: e.g. `"a", "b", "A", "B", "1", "2", " ", "/"`



<!-- LICENSE -->
## License

Distributed under the MIT License. See [LICENSE](https://github.com/Kieran-Lock/graphnix/blob/master/LICENSE) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
