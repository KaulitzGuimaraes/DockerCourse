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
Test docker creating an instance of  hello-word image (not detached) 
delete container
```
#### B)
```
Test docker creating an instance of  hello-word image ( detached) 
delete container
```

### Exercise 2
```
Create an instance of nginx with Docker
```

### Exercise 3
#### A) 
```
Create a Docker file based on UBUNTU to run the command `uname -r` 
```

**PS: Add a CMD to be overrided in case user wants to run a flag with uname command.**

#### B)See container logs 

```
Create a Docker file based on UBUNTU to run the command `uname` 
```

#### C )Create another container with the flag `-a` instead of `-r` and see the logs 

```
Create a Docker file based on UBUNTU to run the command `uname` 
```

### Exercise 4
#### A) 
```
Create a Docker file based on NGINX with the application above
```
link : https://github.com/KaulitzGuimaraes/DockerCourse/tree/master/Pratical%20Exercise/Dolar%20Price
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

