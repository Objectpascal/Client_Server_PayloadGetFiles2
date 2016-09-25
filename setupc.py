from cx_Freeze import setup,Executable;
import sys;
GlobalFilePath='MTCP_Client.py';

base = None
if (sys.platform == "win32"):
    base = "Win32GUI"    # Tells the build script to hide the console.

setup(name=''
      ,version="0.1"
      ,description="executables file"
      ,executables=[Executable(GlobalFilePath,base=base)]
      )