""" This will spin up/start up local linux VM's """

import os 

foldersList=["BuildServer","devapp1","devapp2"]


def startVagrantBoxes():
    """ This will start vagrant boxes using the ip's listed listofIps """
    
    cwd= os.getcwd()
    for folder in foldersList:
        os.chdir(folder)
        print ("\n\nstarting vagrant box from "+folder)
        os.system("vagrant destroy")
        # to stop vagrant boxes update command with "vagrant halt"
        # to initiate vagrant boxes use command "vagrant init"
        os.chdir(cwd)

def main():
    """ Main function to call python script """

    startVagrantBoxes()

main()