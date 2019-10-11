|python| |django|

.. |python| image:: https://img.shields.io/badge/python-3.4+-blue.svg
    :target: https://www.python.org/
.. |django| image:: https://img.shields.io/badge/django-2.2+-blue.svg
    :target: https://www.djangoproject.com/    

======================
Transaction Validation
======================


Quick start
-----------

**clone repository**

  - git clone https://github.com/MaistrenkoAnton/TransactionValidation.git

**change directory**

  - cd TransactionValidation

**start containers**

  - docker-compose up --build

**run test against app container**

  - ./test

Code deployed to instance
-------------------------

  - http://ec2-18-196-188-104.eu-central-1.compute.amazonaws.com/

**Provided json data example (put the code into BODY section in transaction json endpoint to validate data)**

  - https://s3.eu-central-1.amazonaws.com/transaction.validation/transaction.json

**Converted xml data example (put the code into BODY section in transaction xml endpoint to validate data)**

  - https://s3.eu-central-1.amazonaws.com/transaction.validation/transaction.xml


Steps:
------

Json validation

 - Open `http://ec2-18-196-188-104.eu-central-1.compute.amazonaws.com/` or `http://localhost:8000`
 - Open "transaction" endpoint
 - Push "try it out"
 - Set "Parameter content type" to "application/json"
 - Set "Response content type" to "application/json"
 - Put JSON data to body input
 - Check the validation

XML validation

 - Open `http://ec2-18-196-188-104.eu-central-1.compute.amazonaws.com/` or `http://localhost:8000`
 - Open "transaction" endpoint
 - Push "try it out"
 - Set "Parameter content type" to "application/xml"
 - Set "Response content type" to "application/xml"
 - Put XML data to body input
 - Check the validation

Validation implemented within serializer's validations rules,

Service class "TransactionService" helps to translate data to preferable format for validation,

Tests cover "TaxSerializer" validation logic, also system tests check the endpoint parser.
