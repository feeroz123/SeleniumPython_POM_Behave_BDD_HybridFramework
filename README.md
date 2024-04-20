This repository is a sample project for web automation using the following tools:
1. Selenium
2. Python
3. Behave
4. Allure Reports

This repository is based on the BDD (Cucumber) framework.
It includes Data Driven and Hybrid framework as well.

The project requires these packages installed in the IDE (Settings - Python Interpreter - Install(+) ):
* selenium
* behave
* allure-behave

For Allure Reports:
1. Download and Unzip the latest "**allure**" command line tool from [here](https://github.com/allure-framework/allure2/releases).
2. Update the Path environment variable
3. Restart the IDE

Command to trigger the test execution only: 
`behave features/`
or
`behave features/login.feature`

Command to trigger the test execution with the Allure reporting generation:
`behave -f allure_behave.formatter:AllureFormatter -o reports/ features` 

To server the Allure Report from a local server:
`allure serve reports/`


To generate an HTML report from the Allure report files:
`allure generate --single-file reports/`


The output report gets created as: **allure-report/index.html**