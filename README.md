# vagrantBoxes
With out logging into any cloud servers we are trying to create VM's in our local machines using vagrant and virtual box.

Before running this scripts make sure to have virtual box and Vagrant installed in your windows PC.

We are creating 3 linux servers in our local, one build server and 2 app servers.

Clone repo to your local machine and run command from each of the folders using any terminal.
    vagrant up

Add this section to your host file "C:\Windows\System32\drivers\etc"

## Begin Local Vagrant VM's  ##
# externalIP  hostname         ExternalIP        port 
127.0.0.99    buildserver      # 192.166.70.99   2299
127.0.0.23    devapp1          # 192.166.70.23   2223
127.0.0.24    devapp2          # 192.166.70.24   2224
## End ##


### SSH to boxes ###
Here I am using mobaxterm tool, irrespective of tool make sure to use private keys and use respective port numbers.
Keys will be available under 
xxxxxx\BuildServer\.vagrant\machines\default\virtualbox\private_key

To run some commans vagrant user might not be good enough so make sure to switch to root user

*su root*


Note: 
    - Doesn't require any background knowledge about vagrant or virtual box.
    - Need to run "vagrant up" command when ever you want to start the vm. "vagrant halt" command to shutdown system