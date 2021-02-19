# flask-api-example

## Build the image

```sh
docker build -t flask-api-example .
```

## Run 

```sh
docker run --rm -it -v $(PWD):/code -p 5000:5000 flask-api-example 
```

License: MIT
