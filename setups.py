from cx_Freeze import setup,Executable;
import sys;
GlobalFilePath='MTCP_Server.py';
setup(name=''
      ,version="0.1"
      ,description="executables file"
      ,executables=[Executable(GlobalFilePath)]
      )