# Python Colors

 Add colors to your python displays !

## Usage

 The function has a total of 8 colors supported:

 ```json
 "black",
 "red",
 "green",
 "yellow",
 "blue",
 "purple",
 "cyan",
 "white"
 ```

 The white color is the default color for the foreground and the black is the default for the background.

 The color() function has a total of 6 arguments, referenced like this:

 ```js
 pythonColors.color(text: String, textColor: String, background: String, bold: Bool, underline: Bool, highlight: Bool)
 ```

 The first argument is the **text** you want to color

 The second and the third arguments are **colors names**. They are respectively the **text color** and the **background color**. The default color for the text is **white** and the default color for the background is **black**.

 The last three are booleans (True or False), they define respectively:

 1. If the text is ``bold``
 2. If the text is ``underlined``
 3. If the text is ``highlighted`` (inverted colors, brighter and bold)

 ---

 Examples :

 ```python
 print(pythonColors.color("test", False, "blue", False, False, False))
 # This one will print "test" in blue

 print(pythonColors.color("test " + str(125), "blue", "yellow", True, True, False))
 # This one will print "test 125" in blue on a yellow background, bold and underlined
 ```

 ![Result img](./imgs/readme_results.jpg)
