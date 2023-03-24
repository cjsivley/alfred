# alfred
Hello, and thanks for viewing Alfred. Alfred is my digital butler. When my folders get too messy, Alfred cleans up for me!

Basically, Alfred looks through a folder and if a file matches a specified format, it moves that file to a specified folder.

Alfred also writes to a log, in case a file goes missing, so you can see what happened.

Is it the most efficient or clean code? No, this is just something I whipped up to clean up the clutter that tends to gather in the Downloads and Documents folders.

If you want Alfred to recursively go through folder structures, that's possible, but that was not my intent. Check out the walk() documentation for Python.
Note that the shutil.move() function can and will rename files if it cannot find the directory! Be careful with your folder names.

Alfred is inspired by [Belvedere](https://github.com/adampash/belvedere).

