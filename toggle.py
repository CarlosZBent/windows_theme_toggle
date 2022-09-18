from subprocess import Popen, DEVNULL
import sys

# execution strings to pass to Popen to change the system registry
dark_app_mode = 'reg.exe add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v AppsUseLightTheme /t REG_DWORD /d 0 /f'
dark_windows_mode = 'reg.exe add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v SystemUsesLightTheme /t REG_DWORD /d 0 /f'

light_app_mode = 'reg.exe add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v AppsUseLightTheme /t REG_DWORD /d 1 /f'
light_windows_mode = 'reg.exe add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v SystemUsesLightTheme /t REG_DWORD /d 1 /f'


def light():
	light = (light_app_mode, light_windows_mode)
	processes = [Popen(cmd, shell=True, stdout=DEVNULL) for cmd in light]
	print('light')


def dark():
	dark = (dark_app_mode, dark_windows_mode)
	processes = [Popen(cmd, shell=True, stdout=DEVNULL) for cmd in dark]
	print('dark')
		

if __name__ == "__main__":
	globals()[sys.argv[1]]()

