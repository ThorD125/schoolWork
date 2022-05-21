# Lab 1 Web, Mobile & Security
## Installing Docker & first Laravel project
In this lab we're installing our development environment for Laravel. Linux users can start after the header Linux.

### Windows users
Open PowerShell as administrator and install WSL: `wsl --install`  
*Note: this might take a while*

![](images/Lab1.png)

Reboot the system and wsl will be installed, follow the instructions to add a username with password (this is the Linux username/password).

![](images/Lab2.png)

Now WSL2 with Ubuntu is installed.

### Linux (wsl)
In WSL we'll install docker using the following commands:  
*Note: don't copy paste these commands!*

`sudo apt update`  
`sudo apt upgrade`  

`sudo apt install ca-certificates curl gnupg lsb-release`  

`source /etc/os-release`  

`curl -fsSL https://download.docker.com/linux/${ID}/gpg | sudo apt-key add -`  

`echo "deb [arch=amd64] https://download.docker.com/linux/${ID} ${VERSION_CODENAME} stable" | sudo tee /etc/apt/sources.list.d/docker.list`

`sudo apt update`  

`sudo apt install docker-ce docker-ce-cli containerd.io docker-compose`  

`sudo groupadd docker`  

`sudo usermod -aG docker $USER`  

![](images/Lab3.png)

Reboot the system.

Go to https://hub.docker.com/signup and create a new account.  
Then use this command to login in the CLI `docker login` use the credentials from the Docker account.

Test docker with the following command:  
`docker run hello-world`

That should give this result:  
![](images/Lab4.png)

If there is an error that docker isn't started execute these commands:   
`sudo systemctl enable docker`  
`sudo systemctl start docker`  

If these don't work:  
`sudo service docker start`  

Browse to a folder in the file system going to be used for the Laravel projects. And execute the following command to create a new project.

`curl -s https://laravel.build/first-app | bash`

Go in the app and use sail up to start the Web Server.  
`cd first-app`  
`./vendor/bin/sail up`

![](images/Lab5.png)  
After a while the web server has started and we can browse to http://localhost to see the default Laravel environment

![](images/Lab6.png)

With CTRL-C the server can be   gracefully stopped.

## Usage of git in this and all subsequent labs

To commit and push your code, you can use the command line or your IDE's git integration.

Each of you has received a group under https://git.ti.howest.be/TI/2021-2022/s2/web-mobile-and-security/students.

In your dedicated group, you must create a dedicated repository per exercise.

You are required to commit regularily and push at the end of the lab.

When you create a new repository for an existing folder (=your project), Gitlab automatically gives you the necessary instructions to initialise the repository, setup the remote, etc under the header Push an existing folder. This is for command line purposes. Use your own IDE's git settings accordingly.

For this lab, within the group, create a repository called 01-movies using the New project button and make sure to push towards it at the end.

```
cd folderWithWebFiles
git init
git remote add origin git@git.ti.howest.be:koen.koreman/Lab1Laravel.git
git add .
git commit -m "First commit lab 1"
git push -u origin main
```

## Edit the Laravel project


Open the file `/resources/views/welcome.blade.php` and delete everything.

Create a blank HTML page, styling is optional.

Create an array with the following items:
- The Matrix
- Star Wars
- Star Trek
- Lord Of The Rings
- Back to the future
- Jurassic Park
- The Terminator
- The Office
- Men in Black
- Stargate
- The IT crowd
- DC comics
- Marvel

Every time the page is visited the page shows at least 2 random shows/movies. Those can't be the same.

The result:

![](images/Lab7.png)