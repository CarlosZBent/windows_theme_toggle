from subprocess import Popen


dark_app_mode = 'reg.exe add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v AppsUseLightTheme /t REG_DWORD /d 0 /f'
dark_windows_mode = 'reg.exe add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v SystemUsesLightTheme /t REG_DWORD /d 0 /f'


light_app_mode = 'reg.exe add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v AppsUseLightTheme /t REG_DWORD /d 1 /f'
light_windows_mode = 'reg.exe add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v SystemUsesLightTheme /t REG_DWORD /d 1 /f'


commands_dark = [dark_app_mode, dark_windows_mode]
commands_light = [light_app_mode, light_windows_mode]

def toggle_dark():
	processes = [Popen(cmd, shell=True) for cmd in commands_dark]


def toggle_light():
	processes = [Popen(cmd, shell=True) for cmd in commands_light]

toggle_light()