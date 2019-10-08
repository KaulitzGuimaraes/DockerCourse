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
Create a Dockerfile based on alpine OS, run the command “uname”.
```
#### B)
```
Create a Dockerfile based on ubuntu OS, run the command “uname” .
```

#### C) 
```
 Create an image based on ubuntu docker file.
```
#### F) 
```
Create an ubuntu container (detached).
```
#### E)
```
 Catch ubuntu container log
 ```
 ### D)
 
 ```
 Get into alpine container then run the command “cat /etc/os-release”
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

#### C )Create another container with the flag `-a` instead of `-r` and see the logs 

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
#### B)  Change the application interface and replace current container


### Exercise 5

#### A) Create a DockerHub account 

http://hub.docker.com/

#### B) Push the follow image and create a container with it.
```
kaulitz/dolartoday
```

#### C) Upload your version of _Dollar Value Today_ in your  DockerHub 

#### D) Do some update in  your version of _Dollar Value Today_  then push it in your  DockerHub 

