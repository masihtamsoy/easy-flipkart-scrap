# easy-flipkart-scrap

# scrap should be performed sequentially

# Workflow
- Create virtual environment, and activate it
- pip install -r requirement.txt

Inorder to scrap; sequentially follow the step,

1. collect all the `products listing`
  
  `python products.py`

2. collect all `product details`

  `python productDetails.py`

3. collect all `seller details` wrt to product detail

  `python seller.py`


OUTPUT: after running sequentially above steps desired files to expect are : unique_pro.csv, unique_pro_details.csv, unique_seller.csv

All the functions within the steps are mentioned below, in order to run just one function comment other function :P

## products listing
1- <ins> def get_product_listing() </ins>
### input 
`PAGE`: 10

`URL`: https://www.flipkart.com/books/literature-books/pr?sid=bks,w4n&wid=3.productCard.PMU_V2_3&page=

donot miss to add `&page=` at end of the URL
[NOTE: I have not included logic to scrap page numbers]


### output
output will be files eg: pro1.csv, pro2.csv, pro3.csv, pro4.csv ..... pro10.csv

2- <ins> def get_unique_pid_mapping() </ins>
### input
Enter as described in input, in our case enter 10

### output
unique_pro.csv

File contains unique products found from all the product listed on all pages pro1.csv, pro2.csv......

## Product details
1- <ins> def extract_product_details() </ins>
### input
internal: unique_pro.csv

internally based on file generated from above steps
### output
proDetail1.csv, proDetail2.csv, proDetail3.csv ......... proDetailX.csv

each `productDetailx.csv` page contains 50 unique product details
[X = total unique products / 50]

2 - <ins> def get_unique_pid_mapping() </ins>
### input
internal: unique_pro.csv

internally based on file generated from above steps
### output
unique_pro_details.csv

## seller details
1 - <ins> def extract_seller() </ins>
### input
internal: unique_pro_details.csv

internally based on file generated from above steps
### output
seller1.csv, seller2.csv, ..... sellerX.csv

2 - <ins> get_unique() </ins>
### input
internally based on file generated from above steps
### output
unique_seller.csv

# Make this work in future
Changing the harcoded class name can bring the desired results. check for @HARDCODE tag to find harcoded attributes. Extracting has majorly been done using `.text` in beautiful soup object. 




