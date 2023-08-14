# SummingSeries Documentation for Changes in Code
Commit #1
Creation of Summing Series repository and beginning of code. The layout has been outlined with entry boxes for First Term, Number of terms and common difference/ratio (adjacent labels). Buttons for switch operation has been added to easily switch from arithmetic series to geometric series. As well as calculate button and a clear button for easily displaying the final sum and clearing the output for next usage.

Commit #2
Added menubar and theming:
A menubar was created for easy adjustments to the display of the GUI. This would hold the inclusive features. The menubar has a dropdown which is simple to understand access to these features. First inclusive feature was added to the code. This was theme. The code allows to change theme from dark to light which can assist in visual impairments or simply as preference. Base calculations were implemented into the code, these calculations are yet to provide expected outputs however and stand as placeholders for future code. Switch operation button was altered to a radiobutton to better suit the requirements of the assessment.

Commit #3
Added option to change font size (inclusive feature)
Second Inclusive feature was added to the code. This was the feature to change font size to improve GUI's readability to visually impaired persons. The feature was implemented into the menubar for ease of access with drop downs for "small", "medium" and "large" (all under their own function) to provide variety. Every widget was also made global so that they can be accessed anywhere in the code.

Commit #4
Fixed sizing (font, entry boxes), placement of widgets, added error message for empty entry boxes:
All fonts in the GUI were changed to one font(arial) to improve GUI consistency. An error found in the last commit was that when the size was altered, the widgets overlapped and went on top of eachother. To fix this, upon changing size, the placement of the widgets move accordingly. Window size will also change when font size is changed so to have appropriate amounts of white space. Default font size was put to "small" so that the user can return to original font size.

Commit #5
Converted to CustomTkinter, code cleanup:
Code was converted to CustomTkinter as the features on it allowed the GUI to increase in terms of ergonomics. Font size functions were cleaned up using widget scaling which adjusted postion and size simultaneously, giving a cleaner code that can be more easily interpreted. Default positioning of widgets were also changed as to fit new font size function. A segemented button was added for switching between arithmetic and geometric, which was more aesthetically pleasing. Menubar code was simplified to produce a cleaner code.

Commit #6
Calculations for Arithmetic Series and Geometric Series Fixed:
The calculations for arithmetic and geometric series were finalised, with both providing expected outputs. This fulfills the main purpose of the assessment. As well as this int(entry.get) variables were changed to one letter variables (f=first term, c=common difference/ratio, n=number of terms). This simplifies the code and made it easier to build the main code for the calculation.

Commit #7
Converted operation switching:
Operation switching was changed back to a radiobutton design as it was required for the assessment task. Calculations were improved with increased resilience and error handling which improves user experience. Furthermore, the calculation was altered to manipulate float numbers, which increases the possibilities for the user. Added an "about" message to give an overview of the GUI, to inform user of what exactly the program is. General sizing changes and movement of widgets were also completed to clean up the interface.
