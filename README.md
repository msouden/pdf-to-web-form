# pdf-to-web-form

This script extracts 24 elements from a regularly recieved pdf document, opens a designated HTML page with forms, and input these items into the form. 

It also opened the pdf file in the default viewer for review and data verification.

The script was converted into an executable which ran when the pdf file was dropped on it, making it a desktop shortcut.

Auto-py-to-exe was used for conversion, PyPDF2 extracted the text, and RegEx located field input data. A next iteration could use document coordinates for locating desired data instead of RegEx- for reasons evident in the script.
