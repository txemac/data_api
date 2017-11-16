# DATA & API TEST Requirements
1. Download the CSV.
2. Write a small app that publish an API Rest with these endpoints:
- Give me 20 products ordered by price.
- Give me 20 products ordered by discount.
- Give me the most discounted 20 products.
- Give me all products with colour red or any other color.

NOTE: The CSV file has information about the content fields in the first row.
           
## Notes
Please upload the code in a public repo such as GitHub.

You can use the programming language or library that you want (Django, Flask...)

You can modify the format of the CSV if you want but you can not modify the data or the schema.

Don’t waste time in how consume the API or in the authentication. If we can test it with Curl or Requests, is totally valid.

## Bonus Points
As fast response as possible.

# Tests
To run unit test suite, install requirements:
```sh
$ pip install -r ./requirements.txt
```
Run tests:
```sh
$ nosetests -v
```

# Run app:
```sh
$ python api.py
```

# Endpoints:
/products/39 --> to get the product with ID "39".

/products/current_price --> to get 20 products ordered by price. Parameters: order [desc, asc], limit.

/products/discount --> to get 20 products ordered by discount. Parameters: order [desc, asc], limit.

/products/discounted --> to get 20 products ordered by discounted. Parameters: order [desc, asc], limit.

/products/colour/red --> to get all products with colour "red".

# Author
Jose Bermudez

https://github.com/txemac
