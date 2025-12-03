************************
Data Fields
************************

This section provides a summary of all fields output by CDFD.
To read more about the elements of the IATI Standard, visit the `IATI Standard website <https://iatistandard.org/en/iati-standard/203/>`_.

|

IATI Identifier	
================
The :iati-reference:`iati-identifier` is the unique identifier for an activity. 
An activity in IATI is any individual piece of development or humanitarian work, the scope of which is defined by the organisation publishing the data. 

Title
========
The :iati-reference:`title` of an activity.

Reporting Organisation Group	
============================
The group of related organisations a :iati-reference:`reporting-org` belongs to, based on this `list <https://codelists.codeforiati.org/ReportingOrganisationGroup/>`_ developed by members of the IATI Community.

Reporting Organisation
========================
The :iati-reference:`reporting-org` is the organisation that has published the activity. 
Each organisation has a unique organisation identifier, shown in brackets in the CDFD output. 
For example, UNICEF (XM-DAC-41122).

Reporting Organisation Type	
=============================	
The type of organisation reporting an activity. 
Values are defined in the `Organisation Type Codelist <https://iatistandard.org/en/iati-standard/203/codelists/organisationtype/>`_.

Aid Type
=========
The type or modality of aid (e.g. general budget support, project-type interventions). 
:iati-reference:`aid-type` is not available for all transactions/budgets as not all organisations have reported this information.
Values are defined in the `OECD DAC codelist for Type of Aid <https://iatistandard.org/en/iati-standard/203/codelists/aidtype/>`_.

Finance Type	
==============
The type of finance (e.g. loan, grant). 
:iati-reference:`finance-type` is not available for all transactions/budgets as not all organisations have reported this information.
Values are defined in the `OECD DAC codelist for Type of Finance <https://iatistandard.org/en/iati-standard/203/codelists/financetype/>`_.

Flow Type	
============
The type of flow (e.g. official development assistance, other official flows, private flows). 
:iati-reference:`flow-type` is not available for all transactions/budgets as not all organisations have reported this information.
Values are defined in the `OECD DAC codelist for Type of Flow <https://iatistandard.org/en/iati-standard/203/codelists/flowtype/>`_.

Provider Organisation	
========================
The :iati-reference:`provider-org` is the organisation from which the resources originated.

Depending on the detail published, this field may include the name of the organsation, their unique organisation identifier, or both.
The name used for the same organisation may vary between reporting organisations. 
For example, AfDB, African Development Bank, African Development Bank Group, etc.

Where organisations do not declare a :iati-reference:`provider-org` for a transaction, the logic described in the Methodology; :ref:`Provider and receiver organisations <prov_rec>` section is followed.
For budgets, the logic described in the Methodology; :ref:`Budget Handling <budgets>` section is followed. 


Provider Organisation Type	
==========================
The type of organisation(s) from which the resources originated.
:iati-reference:`provider-org/@type` is not available for all transactions/budgets as not all organisations have reported this information.
Values are defined in the `Organisation Type Codelist <https://iatistandard.org/en/iati-standard/203/codelists/organisationtype/>`_.

Receiver Organisation	
========================
The organisation receiving the specified transaction amount. 
Depending on the detail published, this field may include the name of the organsation, their unique organisation identifier, or both.

Where organisations do not declare a :iati-reference:`receiver-org` for a transaction, the logic described in the Methodology; :ref:`Provider and receiver organisations <prov_rec>` section is followed.
For budgets, the logic described in the Methodology; :ref:`Budget Handling <budgets>` section is followed. 

Receiver Organisation Type
===========================
The type of organisation(s) receiving the specified transaction amount. 
:iati-reference:`receiver-org/@type` is not available for all transactions/budgets as not all organisations have reported this information.
Values are defined in the `Organisation Type Codelist <https://iatistandard.org/en/iati-standard/203/codelists/organisationtype/>`_.

Transaction Type	
========================
The type of the transaction. 
There are 13 transaction types that can be reported to IATI.
Four are included in CDFD's dataset, plus budgets:

* Incoming Funds
* Outgoing Commitments
* Disbursements 
* Expenditure
* Budget 

Transaction types and their definitions are available in the `Transaction Type Codelist <https://iatistandard.org/en/iati-standard/203/codelists/transactiontype/>`_.

Recipient Country or Region	
===========================
The country or region that was the recipient of this transaction. 
:iati-reference:`recipient-country` values are defined in the `Country Codelist <https://iatistandard.org/en/iati-standard/203/codelists/country/>`_,
and :iati-reference:`recipient-region` values are defined in the `Region Codelist <https://iatistandard.org/en/iati-standard/203/codelists/region/>`_.

Multi Country	
========================
Indicates whether the activity has one or multiple recipient countries, where 1 = True and 0 = False.
If it is a multi-country activity, this means that the estimated percentage to that country has been applied to the transaction / budget values.

The logic of transaction splitting is described  in the Methodology; :ref:`Transaction Splitting <trans_split>` section. 

Sector Category	
================
The category of the sector that an activity is supporting. 
Sector category is not available for all transactions/budgets as not all organisations report sectors using the OECD DAC 5 digit codes, the first three numbers of which map to the sector categories.
Values are defined in the `OECD DAC 3 Digit Sector codelist <https://iatistandard.org/en/iati-standard/203/codelists/sectorcategory/>`_.

Sector
========
The sector that an activity is supporting. 
:iati-reference:`sector` is not available for all transactions/budgets as not all organisations report sectors using the OECD DAC 5 digit codes.
Values are defined in the `OECD DAC DAC 5 Digit Sector codelist <https://iatistandard.org/en/iati-standard/203/codelists/sector/>`_.

Humanitarian	
=============
An indication of whether the transaction/budget can be categorized as humanitarian, where 1 = True and 0 = False.

Calendar Year	
==============
The year in which the transaction occurred or the year for which the budget values have been aggregated.

.. _cal quarters:

Calendar Quarter	
=================
This is the quarter in which the transaction occurred or the quarter for which the budget values have been aggregated.

Quarters:

* Q1: January - March
* Q2: April - June
* Q3: July - September
* Q4: October - December

Calendar Year and Quarter	
==========================
The year and quarter in which the transaction occurred or the year and quarter for which the budget values have been aggregated.

URL	
=====
The link to the IATI activity page on d-portal.

Value (USD)	
============
The value of the transaction/budget in U.S. Dollars.

.. note::
    Some organisations include negative transactions in their data. 

    For disbursements, this typically means that money disbursed is being returned to the funder. 

    For commitments, this may be an adjustment to an initial commitment.

Value (EUR)	
========================
The value of the transaction/budget row in Euros.

Value (Local currency)
========================
The value of the transaction/budget row in the local currency, customised for each country. 
