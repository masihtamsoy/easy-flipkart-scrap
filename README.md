# easy-flipkart-scrap

# Workflow
1. collect all the `products listing`
2. collect all `product details`
3. collect all `seller details` wrt to product detail

## products listing
1- <ins> def get_product_listing() </ins>
### input 
`URL`: https://www.flipkart.com/books/~cs-pkdcqd2db7/pr?sid=bks&collection-tab-name=Top%20UPSC%20Exam%20Books&hpid=BjJ6-TRSwA--qMBilKYVfg==&fm=neo%2Fmerchandising&iid=M_4b8899c4-5575-40c7-9d78-ba5f3e676dc7_1.4S3QFJX3D4IM&ppt=clp&ppn=the-exam-store&ssid=0927cmoheixe3ev41627145280580&otracker=dynamic_omu_infinite_Exam%2BPreparation%2B_6_1.dealCard.OMU_INFINITE_4S3QFJX3D4IM&cid=4S3QFJX3D4IM&page=

donot miss to add `&page=` at end of the URL
[NOTE: I have not included logic to scrap page numbers]

`PAGE`: 10

### output
output will be files eg: pro1.csv, pro2.csv, pro3.csv, pro4.csv ..... pro10.csv

2- <ins> def get_unique_pid_mapping() </ins>
### input
Enter as described in input, in our case enter 10

### output
unique_pro.csv

File contains unique products found from all the product listed on all pages

## Product details
1- <ins> def extract_product_details() </ins>
### input

### output
proDetail1.csv, proDetail2.csv, proDetail3.csv ......... proDetailX.csv

each `productDetailx.csv` page contains 50 unique product details
[X = total unique products / 50]

2 - <ins> def get_unique_pid_mapping() </ins>
### input
internal: unique_pro.csv
### output
unique_pro_details.csv

## seller details
1 - <ins> def extract_seller() </ins>
###input
internal: unique_pro_details.csv
###output
unique_seller.csv

# scrap sequentially



