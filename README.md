# A python script to toggle Windows' dark & light themes automatically

### It can be run through Python as a module or from the Bash shell through a shell script

## How it works

To use it simply fork the repo or download the files. There's no need for external libraries, the script only uses the [subprocess library](https://docs.python.org/3/library/subprocess.html), which is included with Python.

### As a Python module

To use it as a python module you can use two parameters: `dark` and `light`.
So simply open a command line interface on the folder where the toggle.py file is located and run `python3 -m toggle.py {parameter}`.

> Example: `python3 -m toggle.py dark` will change the theme to dark.

### From the Bash shell

To run it from the Bash shell, open it, navigate to the folder where the bash script and the python script are located.

> Note: if they are on differente folders, or the shell script can't locate the python script, edit the `cd` statement on the shell script to point it to the python script folder before running it. Example: `cd Documents/Scripts/`.

Once on the folder where the shell script is, run `./toggle.sh {parameter}` and the theme will change.

> Example: `./toggle.sh light` will change the theme to light

Finally, if you'd like to run the script from anywhere in the computer, to avoid having to navigate to the folder every time, you need to add that folder to the Path on the system environment variables => [example](https://stackoverflow.com/questions/44272416/how-to-add-a-folder-to-path-environment-variable-in-windows-10-with-screensho)

Any issues, suggestions or requests, feel free to contact me.
