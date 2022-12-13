class ansi():
    color_reset = "\[\033[0m\]"

    def color(text,
              textColor=False,
              background=False,
              bold=False,
              underline=False,
              highlight=False
              ):

        colors_list = ["black", "red", "green",
                       "yellow", "blue", "purple",
                       "cyan", "white"]

        if background != False:
            list_background_colors = [40, 41, 42, 43, 44, 45, 46, 47]
            background = background.lower()

            assert background in colors_list, "Error: The color \"{}\" is not in the list of colors.".format(
                background)

            if background in colors_list:
                colors_list = colors_list.index(background)
        else:
            bg_code = None

        if textColor != False:
            list_text_colors = [30, 31, 32, 33, 34, 35, 36, 37]
            textColor = textColor.lower()
            assert textColor in colors_list, "Error: The color \"{}\" is not in the list of colors.".format(
                textColor)

            if textColor in colors_list:
                colors_list = colors_list.index(textColor)
        else:
            fg_code = None

        style = 0
        if bold == True and underline == True:
            style = "1;4"
        elif bold == True:
            style = 1
        elif underline == True:
            style = 4
        
        if highlight == True:
            style = "1;7"
        
        if background == False and textColor == False:
            return "\033[{}m{}\033[0m".format(style, text)
        elif background == False:
            return "\033[{};{}m{}\033[0m".format(style, list_text_colors[colors_list], text)
        elif textColor == False:
            return "\033[{};{}m{}\033[0m".format(style, list_background_colors[colors_list], text)
        elif textColor != False and background != False:
            return "\033[{};{};{}m{}\033[0m".format(style, list_text_colors[colors_list], list_background_colors[colors_list], text)


text = ansi.color("test", 'red', False, False, False, True)
print(text)
