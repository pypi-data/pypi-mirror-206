
import platform
import subprocess
import os
def main():
    win_version = platform.platform()
    workspace_path = os.getcwd()
    if "Windows-10"  in win_version:
        print("Windows 10")
        cmd_script = os.path.join(workspace_path, "/driver/dll/2.General/drv.win10/setup.cmd")
        result = subprocess.run(cmd_script, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
    elif "Windows-7" in win_version:
        print("Windows 7")
        cmd_script = os.path.join(workspace_path, "/driver/dll/2.General/drv.win7/setup.cmd")
        result = subprocess.run(cmd_script, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
main()