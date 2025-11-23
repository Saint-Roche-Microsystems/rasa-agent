## Build
First get locally a `rasa/rasa` image from DockerHub.

Then create a local image using the `Dockerfile` with:

````
docker build -f Dockerfile -t rasa-train .
````

After that, train the model using the new created image:

````
docker run --user 1000 -it --rm -v ${PWD}:/app rasa-train train
````

## Execution

Run an actions server using the default `rasa/rasa` image.

````
docker run -it --rm -v ${PWD}:/app -p 5055:5055 rasa/rasa run actions
````

Then run the shell environment to execute the agent with the `rasa-train` local image.

````
docker run --user 1000 -it --rm -v ${PWD}:/app rasa-train shell --endpoints endpoints.yml
````
