from subprocess import Popen, DEVNULL
import sys


def light():
	light_app_mode = 'reg.exe add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v AppsUseLightTheme /t REG_DWORD /d 1 /f'
	light_windows_mode = 'reg.exe add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v SystemUsesLightTheme /t REG_DWORD /d 1 /f'
	
	light = (light_app_mode, light_windows_mode)
	
	process = [Popen(cmd, shell=True, stdout=DEVNULL) for cmd in light]
	
	print('\n    \033[35m=> \033[32mchanged theme to \033[31m\033[01mLIGHT\033[0m \n')


def dark():
	dark_app_mode = 'reg.exe add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v AppsUseLightTheme /t REG_DWORD /d 0 /f'
	dark_windows_mode = 'reg.exe add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v SystemUsesLightTheme /t REG_DWORD /d 0 /f'

	dark = (dark_app_mode, dark_windows_mode)

	process = [Popen(cmd, shell=True, stdout=DEVNULL) for cmd in dark]

	print('\n    \033[35m=> \033[32mchanged theme to \033[31m\033[01mDARK\033[0m \n')
		

if __name__ == "__main__":
	globals()[sys.argv[1]]()

