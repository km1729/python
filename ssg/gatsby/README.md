```bash
# create image
$docker build -t hellojs .

# run the image
$run -d -p 8080:8080 --name js hellojs

# test the container
$curl localhost:8080

```