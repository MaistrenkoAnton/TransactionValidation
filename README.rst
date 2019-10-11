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

**Provided json data (put the code into BODY section in transaction/json endpoint) to validate data**

  - https://s3.eu-central-1.amazonaws.com/transaction.validation/transaction.json
**converted xml data (put the code into BODY section in transaction/xml endpoint) to validate data**

  - https://s3.eu-central-1.amazonaws.com/transaction.validation/transaction.xml
