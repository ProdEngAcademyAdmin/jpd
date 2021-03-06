JPD 
The JPD CLI job is to Create actual usage in the JFrog platform within seconds with full automation
## How to Install
1. curl -fl https://raw.githubusercontent.com/ProdEngAcademyAdmin/jpd/main/jpd.sh | bash 
2. write your configuration in the config.yaml file.
3. execute ‘jpd’ commands `jpd` See [Examples](#Examples) section for commands to run.
## Documentation for required libraries
- https://click.palletsprojects.com/en/8.0.x/
- https://docs.python-requests.org/en/latest/
- https://cryptography.io/en/latest/
##  The REST-API links for the products 
- Artifactory: https://www.jfrog.com/confluence/display/JFROG/Artifactory+REST+API
- Xray: https://www.jfrog.com/confluence/display/JFROG/Xray+REST+API
- Pipelines: https://www.jfrog.com/confluence/display/JFROG/Pipelines+REST+API
- Authentication : https://www.jfrog.com/confluence/display/RTF6X/Artifactory+REST+API#ArtifactoryRESTAPI-Authentication
## Examples for ‘JPD’ commands
The JPD cli implement JFrog platform and API-calls: <br />
Artifactory: <br />
 -System Ping 
 ``` sh
$ jpd rt ping 
````
 -Get Storage Info
 ``` sh
$ jpd xray storage-info
````
 -Create Repository
 ``` sh
$ jpd rt create-repo
````
Xray: <br />
-create watch
``` sh
$ jpd xray create-watch 
````
-Create policy
``` sh
$ jpd xray create-policy 
````
Pipelines: <br />
-Create Integrations<br />
-Create Pipeline Source<br />
-Trigger a Pipeline<br />
-Report Pipelines status<br />

```commandline
Usage: jpd [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  rt    Commands to make operations on JFrog Artifactory
  xray  Commands to make operations on Xray

  ```
 
 ## Diagram of the application
 ![Architecture of the JPD CLI](https://github.com/ProdEngAcademyAdmin/jpd/blob/main/Media/JPD-Diagram.png?raw=true)
