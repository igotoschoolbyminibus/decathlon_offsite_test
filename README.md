# decathlon_offsite_test

Notes

Q1: 
-> The file is in .sql format

-> This question i use MySQL database as a platform to solve the problem. 

-> I assume the transaction field in csv file doesn't match the accepted format for timestamp in MySQl, so i used function str_to_date to convert back to timestamp. 

-> For items with more than 1 sold / 1 return, i use minimum sold date and maximum return date to calculate the day difference

Q2:
-> We need to install the following packages:
  --> numpy
  --> pandas

-> Use 'zz_All' to replace 'All' for easier sorting purpose

-> Fo nan shortage value, i choose to keep nan because nan has its meaning (It means this value is not available)
