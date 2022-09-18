from subprocess import Popen
import sys

# execution strings to pass to Popen to change the system registry
dark_app_mode = 'reg.exe add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v AppsUseLightTheme /t REG_DWORD /d 0 /f'
dark_windows_mode = 'reg.exe add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v SystemUsesLightTheme /t REG_DWORD /d 0 /f'

light_app_mode = 'reg.exe add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v AppsUseLightTheme /t REG_DWORD /d 1 /f'
light_windows_mode = 'reg.exe add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v SystemUsesLightTheme /t REG_DWORD /d 1 /f'

# objects containing the strings for Popen to iterate over them
dark = (dark_app_mode, dark_windows_mode)
light = (light_app_mode, light_windows_mode)


def toggle(theme):	

	processes = [Popen(cmd, shell=True) for cmd in theme]
		

if __name__ == "__main__":
	# the code below checks if the argument given is 'dark' or 'light' and it
	# runs the function with the according object as a parameter.
	# without this check, when the command is executed from the command line
	# the parameter is taken as a string and Popen iterated over it
	# as a string instead of as a tuple
	if sys.argv[2] == 'dark':
		globals()[sys.argv[1]](dark)
	elif sys.argv[2] == 'light':
		globals()[sys.argv[1]](light)

