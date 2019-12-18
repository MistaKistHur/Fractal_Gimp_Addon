# map is a pre-defined word, changed it to mapi instead. 
# look into gimp src code fractals to get base idea of code structure...

from gimpfu import *

  # image & drawable are predefined gimp args, gimp knows what to do with these parts.
def fu_fractal_tools(seed, image, drawable, radius, params, threshold, arc, mapi, vec, multi):

  # Set up seed parameters. --------------------------------------------
  
  # iteration Algorythm. (Custom). -------------------------------------
  

  
  a = 200  # Only Example ifElse to build the Algorythm off.... see if python has switches aswell..
  b = 33
  if b > a:
    print("b is greater than a")
  elif a == b:
    print("a and b are equal")
  else:
    print("a is greater than b")
    
    # my version.. 
    
    seed1 = ?
    seed2 = ?
       param1 = ?
       param2 = ?
    if: 
    elif:
    else:
  
  
  # Params. -------------------------------------------------------------
  
  # Tweaks & adjustments.
  
  # Tilt, Pan, Zoom etc if available.
  
  # Preview image.
  
  # Allow hue-rotation After.
  
  # Different Shaders.
  
  # Shade Smooth.
  
  # Optimizations.
  
  # Fix Vectors.
  
  
  # These are just some ideas of what functionality I would like the plugin to have,
  #     No, idea how to implement this yet, research more.
  
register()
main()


# idea for secondary fractal function/plugin
# Read rgba data from img max 100x100px then plug that data into variables 
# & use it to create/generate a fractal based off that img, 

# 2ndry mix 100px img with seed then populate 3d array.

# 3rd pick three seeds, merge via algo then see the resulting recurrence.

# 4th self inclusive recursion.

# 5th Fractal, snake loop, with exit cmd.

# ::>>.-------------------------------------------------------------------------------------------------------------------------
# Example Code for inputs. -----------------------------------------------------------------------------------------------------
# ::>>.-------------------------------------------------------------------------------------------------------------------------

# def ui_examples_2(radio_var, option_var, spinner_var, slider_var,
#                   adjustment_var, file_var, dirname_var, font_var,
#                   brush_var, pattern_var, gradient_var, palette_var):
#     return

# register(
#     "python_fu_ui_examples_2",
#     "Show other half of the UI options",
#     "Dummy UI 2",
#     "Jackson Bates",
#     "Jackson Bates",
#     "2015",
#     "Show more UI Options...",
#     "",      # Image type
#     [
#         (PF_RADIO, "radio_var", "radio", "radio1_value",
#             (
#                 ("radio1_label", "radio1_value"),
#                 ("radio2_label", "radio2_value")
#             )
#          ),
#         (PF_OPTION, "option_var", "option", 0,
#            ("Opt1", "Opt2", "Opt3", "Opt4")
#          ),
#         (PF_SPINNER, "spinner_var", "spinner", 10, (1, 10, 0.5)),
#         (PF_SLIDER, "slider_var",  "slider", 100, (0, 100, 1)),
#         (PF_ADJUSTMENT, "adjustment_var", "adjustment", 10, (1, 10, 1)),
#         (PF_FILE, "file_var", "file", ""),
#         (PF_DIRNAME, "dirname_var", "dirname", "/tmp"),
#         (PF_FONT, "font_var", "font", "Sans"),
#         (PF_BRUSH, "brush_var", "brush", None),
#         (PF_PATTERN, "pattern_var", "pattern", None),
#         (PF_GRADIENT, "gradient_var", "gradient", None),
#         (PF_PALETTE, "palette_var",  "palette", ""),
#     ],
#     [],
#     ui_examples_2, menu="<Image>/Filters/Languages/Python-Fu" )
# 
# main()
# ::>>. End Of Code Block ------------------------------------------------------------------------------------------------------

