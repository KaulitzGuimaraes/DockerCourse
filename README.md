# DockerCourse

## Author : KaulitzGuimaraes

### Content of course 
- Docker Context
- Docker Infrastructure
- Docker images
- Docker containers
- DockerHub 

### Concept Content 

- Link to  the slides :

### Exercise 1 
#### A)
```
Test docker creating an instance of hello-world image (not
detached)
Delete container.
```
#### B)
```
Test docker creating an instance of hello-world image (detached)
Delete container.
```

### Exercise 2
#### A)
```
Create a Dockerfile based on alpine OS, run the command  "uname". 
```
#### B)
```
Create a Dockerfile based on ubuntu OS, run the command  “uname” . 
```

#### C) 
```
 Create an image based on  alpine  docker file.
```
#### D) 
```
) Create an image based on  ubuntu  docker file.
```
#### E)
```
 Create an alpine container (not detached).

 ```
 ### F)
 
 ```
Create an ubuntu container (detached).
 ```
## G) 
```
Catch ubuntu container log
```
## G) 
```
Get into alpine container then run the  command “cat /etc/os-release”
```


### Exercise 3
#### A) 
```
 Choose one Dockerfile from exercise before, then add the uname command as an entry point. Then add a command with the flag “-r”.
```

**PS: Add a CMD to be overrided in case user wants to run a flag with uname command.**

#### B)

```
Rebuild the image using same command as the exercise before.
```

#### C )
```
Create a Docker file based on UBUNTU to run the command `uname` 
```
#### D) 
```
Create a new container with same name as exercise II ( detached).

```

#### E) 
```
Catch container logs

```
#### F) 
```
Delete the container

```
#### G)
```
 Create another container with same name as before, but overriding the “-f” default flag by using the “-a” one (detached).
 ```
#### H)
```
 Catch ubuntu container log

```



### Exercise 4
### A)
```
Create a NGINX container
```


### Exercise 5
#### A) 
```
Run this command on your bash :
git clone https://github.com/KaulitzGuimaraes/DockerCourse
```
#### B)  
```
 Go to the Dollar Price folder by running the command cd DockerCourse/PraticalExercises/DollarPrice
```


#### C)  
```
Create a Dockerfile, then :
 - Create a new direct called dollarprice
 - Copy the current code into the folder
 - Switch to this directory
 - Move the current content to this path /usr/share/nginx/html
 - Expose port 80
```
#### D)
```
Build the image with the name dollarprice
```

### E)
```
Create a container with the name dollarprice_container and port 8080
```


### F)
```
Delete the container
```

### G)
```
Update the application code by running the command 
git pull 
```
### H)
```
Rebuild the image
```
### I)
```
Create another container with same name and port
```
### Exercise 6

#### A) 

```
Download the code from GitHub link in your machine. Unzip it and open in a editor, you can use a local one or download sublime.
GitHub : https://github.com/KaulitzGuimaraes/DockerCourse Sublime (Windows only) : https://www.sublimetext.com/3

```

#### B) Push the follow image and create a container with it.
```
Now change the application appearance , you can change the HTML and the CSS. In case you feel comfortable to change the Js code, you can also switch the coins conversion.
API documentation : https://exchangeratesapi.io
```

#### C) 
```
Copy the content for each file that you have changed in the docker player .
```


#### D)
```
Now open your dockerhub account accessing the link below : https://hub.docker.com
Check your name profile !
```

#### E) 

```
Build the a new image with the same Dockerfile, but using “your_user”/dollarprice as the image name
```

#### F)

```
Login with your DockerHub login
```

#### G) 
```
Push your image to DockerHub repository
```
#### H) 
```
Reload your DockerHub page , check if your image is there.
```

#### I)
```
Add a new instance in your docker playground .
```
#### J)
```
Push your image from DockerHub to your local machine.
```
#### K)

```
Create a container with your username and port 80.
```
### Exercise 7
#### A)
```
Pull the MySQL version 5.6 image
```
####  B)
```
 Createacontainercalledmysql52withthefollowingparameters:
 - "MYSQL_ROOT_PASSWORD=123456"
```
####  C)
```
Getinthecontainercalledmysql-serverbyusingthefollowcommand:
- mysql -p
```

####  D)

```
 Run the command , inside of the container :
 - show databases;
```

### Exercise 8
#### A)
```
Go the the mysql_ex folder.

```

#### B)
```
Create a new Dockerfile based on the latest image from mysql, and then add a command to copy the “d.sql” file to the image current directory.

```

#### C)
```
 Buildtheimagewiththenamemysql_content.
```
#### D)
```
Get into the container bash, then run the following command : - mysql -u root -p < d.sql
```

#### E)
```
Execute the command “show databases;”



