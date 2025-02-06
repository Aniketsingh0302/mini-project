country_code= {
     "INDIA": "001",
    "USA": "002",
    "UK": "003",
    "AFGANISTAN":"004",
}
countryName = input("Enter the country name :")
print(country_code.get(countryName,"Not present in the dictionary"))
   
  