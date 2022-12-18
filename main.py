class pythonColors():
    def color(text,
              textColor=False,
              background=False,
              bold=False,
              underline=False,
              highlight=False
              ):
        
        text = str(text)
        
        color_reset = "\033[0m"
        colors_list = ["black", "red", "green",
                       "yellow", "blue", "purple",
                       "cyan", "white"]

        if background != False:
            list_background_colors = [40, 41, 42, 43, 44, 45, 46, 47]
            background = background.lower()

            assert background in colors_list, "Error: The color \"{}\" is not in the list of colors.".format(
                background)

            if background in colors_list:
                bg_list_code = colors_list.index(background)
        else:
            bg_list_code = False

        if textColor != False:
            list_text_colors = [30, 31, 32, 33, 34, 35, 36, 37]
            textColor = textColor.lower()

            assert textColor in colors_list, "Error: The color \"{}\" is not in the list of colors.".format(
                textColor)

            if textColor in colors_list:
                textColor_list_code = colors_list.index(textColor)

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
            return "\033[{style}m{txt}{reset}".format(style = style, txt = text, reset = color_reset)
        elif background == False:
            return "\033[{style};{textColor}m{txt}{reset}".format(style = style, textColor = list_text_colors[textColor_list_code], txt = text, reset = color_reset)
        elif textColor == False:
            return "\033[{style};{bg}m{txt}{reset}".format(style = style, bg = list_background_colors[bg_list_code], txt = text, reset = color_reset)
        elif textColor != False and background != False:
            return "\033[{style};{textColor};{bg}m{txt}{reset}".format(style = style, textColor = list_text_colors[textColor_list_code], bg = list_background_colors[bg_list_code], txt = text, reset = color_reset)



print(pythonColors.color("test", False, "blue", False, False, False))
print(pythonColors.color("test " + str(125), "blue", "yellow", True, True, False))
