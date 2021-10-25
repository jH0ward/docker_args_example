# Docker Application with Optional Arguments using ENTRYPOINT and CMD

- This rebuilds without the cache in case the python is changed

`docker build --no-cache -t python_app`

- This overrides the entrypoint to get a shell

`docker run --entrypoint "/bin/bash" -it python_app`

- The Dockerfile has an `ENTRYPOINT` and a `CMD`
- The `CMD ["my friend"]` says that string is automatically passed to the entrypoint if no arguments follow on the `docker run` line
- If you do pass arguments the `CMD` argument is not used

- So if you run this

`docker run python_app`

- You get
` Well hey there my friend!`

- If you run this

`docker run python_app Coleman`

- You get
` Well hey there Coleman!`
