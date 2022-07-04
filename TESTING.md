# Testing 

## Code Validation

- PEP8 Online Check

- Results for run.py
![main page](documentation/images/code-validation-main.png)

- Results for coinmarketcap.py
![coinmarketcap page](documentation/images/code-validation-coinmarketcap.png)

- [W3Cvalidator](https://validator.w3.org/) HTML validator

![html validator](documentation/images/html-validator.png)

- User input validation
![validating floats](documentation/images/validate-float.png)

![validating integers](documentation/images/validate-int.png)

![validating strings](documentation/images/validate-string.png)


## Bugs

- I was getting the word 'None' printed out which was unnecessary as shown in the image below.

- The second image shows the problem within the code 

- To prevent the word 'none' from being printed out, I removed the print statement which was wrapped around the part where I called the function. Within the balance.info() function, there was a print statement already being returned so the wrapped print statement did not have anything to print so it printed none.

![bug](documentation/images/bug-None.png)
![bug](documentation/images/bug-none2.png)

