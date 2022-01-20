# Build linux servers

This command has to be run from same directory and it will start up 3 servers
one buildserver and two app/webservers we used for testing 
`vagrant up`

## Install ansible in buildserver

we can ssh to buildserver using 
`vagrant ssh buildserver`
or we can use mobaxterm to connect.

### Update root password
`sudo passwd root`

### Switch user to root
`su root`

### Update system
`sudo apt update`

### Install ansible
`sudo apt install ansible`

### Update host file in buildserver
edit host file and add other server details ( this has to be in all servers)
`vi /etc/hosts`

192.168.56.100 buildserver
192.168.56.102 web01
192.168.56.103 web02


### Create keys (switch to vagrant user and run)
`ssh-keygen`
After running this command press enter with out proving any inputs.
Note: Files can be edited when we are using root user only.

### ssh copy id (switch to vagrant user and run)
this command will helps ansible to talk to other servers ( web01/web02) with out asking for passwords
`ssh-copy-id web01`
`ssh-copy-id web02`
enter "yes" and password for vagrant user ( password is vagrant)

### Verify connetion (switch to vagrant user and run)
`ansible webservers -i hosts -m command -a hostname -v`


### Install jenkins on buildserver ( this will install java and jenkins)
`wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -`

`sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'`

`sudo apt install default-jre`

`sudo apt install jenkins`

`sudo systemctl start jenkins`

`sudo apt update`

`sudo systemctl enable jenkins`

`sudo ufw allow OpenSSH`

`sudo ufw enable`

`sudo ufw allow 8080`

`sudo cat /var/lib/jenkins/secrets/initialAdminPassword`
copy the password before running this command.

run http://localhost:8080

this will ask for admin password for the first time only, paste the password we copied in earlier step.
Now we can create new creds for new user.

#### Install plugins in jenkins
install "Build Pipeline" and "Generic Webhook Trigger" plugins

