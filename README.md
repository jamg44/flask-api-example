# flask-API-example

## Build the image

```sh
docker build -t api-example-python .
```

## Run 

```sh
docker run --rm -it -v $(PWD):/code -p 5000:5000 api-example-python 
```

License: MIT