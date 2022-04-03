import sys, os

def run_terminal(command, mdf="my_dummy_file.txt"):
    os.system(command+" > "+mdf)
    f=open(mdf, "r")
    cont=f.read()
    f.close()
    print(cont)
    if os.path.exists(mdf): os.remove(mdf)
    else: print("ERROR: Cannot delete "+mdf+" File does not exist")

def IDLE_pip(command):
    run_terminal(sys.executable + " -m pip " + command)

IDLE_pip("list")
IDLE_pip("show pip")
# IDLE_pip("install πακέτο")
# IDLE_pip("uninstall πακέτο")