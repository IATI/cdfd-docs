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
Values are taken from the `Organisation Type Codelist <https://iatistandard.org/en/iati-standard/203/codelists/organisationtype/>`_.

Aid Type
=========
The type or modality of aid (e.g. general budget support, project-type interventions). 
:iati-reference:`aid-type` is not available for all transactions/budgets as not all organisations have reported this information.
Values are taken from the `OECD DAC codelist for Type of Aid <https://iatistandard.org/en/iati-standard/203/codelists/aidtype/>`_.

Finance Type	
==============
The type of finance (e.g. loan, grant). 
:iati-reference:`finance-type` is not available for all transactions/budgets as not all organisations have reported this information.
Values are taken from the `OECD DAC codelist for Type of Finance <https://iatistandard.org/en/iati-standard/203/codelists/financetype/>`_.

Flow Type	
============
The type of flow (e.g. official development assistance, other official flows, private flows). 
:iati-reference:`flow-type` is not available for all transactions/budgets as not all organisations have reported this information.
Values are taken from the `OECD DAC codelist for Type of Flow <https://iatistandard.org/en/iati-standard/203/codelists/flowtype/>`_.

Provider Organisation	
========================
The :iati-reference:`provider-org` is the organisation from which the resources originated.

Depending on the detail published, this field may include the name of the organsation, their unique organisation identifier, or both.
The same organisation may be referenced by multiple variations of their name. 
For example, AfDB, African Development Bank, African Development Bank Group, etc.

Where organisations do not declare a :iati-reference:`provider-org` for a transaction, the logic described in the Methodology; :ref:`Provider and receiver organisations` section is followed.
As budgets do not include a provider organisation element, the logic described in the Methodology; :ref:`Budget Handling` section is followed. 


Provider Organisation Type	
==========================
The type of organisation(s) from which the resources originated.
Provider organsation type is not available for all transactions/budgets as not all organisations have reported this information.
Values are taken from the `Organisation Type Codelist <https://iatistandard.org/en/iati-standard/203/codelists/organisationtype/>`_.

Receiver Organisation	
========================
This is the organisation receiving the specified transaction amount. 
This is not available for all transactions/budgets as not all organisations have reported this information. 
For commitments, disbursements, and expenditures, if the Receiver Organisation is not reported, then the Implementing Organisation(s) is populated in this column. 
For budgets, the Receiver Organisation is the Implementing Organisation(s). 
For incoming funds, if the Receiver Organisation is not reported, then the Reporting Organisation is populated in this column. 
As there can be multiple implementing organisations reported for one activity, there may be multiple values in this column.
Possible values:
* Values in this field are either the organisation name or if not available, a unique code which references the organisation, known as the "organisation identifier." 
* As there is a lack of standardisation in the reporting of these names, the same organisation might be referenced by multiple variations of their name - e.g. 
* AfDB African Development Bank or African Development Bank Group or African Development Bank.

Receiver Organisation Type
===========================
This is the type of organisation(s) engaged in the activity. 
This is always included for the Reporting Organisation, but not always reported for the Provider or Receiver Organisation(s).

Transaction Type	
========================
This is the type of the transaction. There are 13 transaction types that can be reported to IATI, but 4 are included in the spreadsheet which allows users to assess the resources committed (Outgoing Commitments) and spent (Disbursements and Expenditures). Budgets are also included.
Possible values (Transactions and Budgets):
* Incoming Funds - Funds received for use on the activity, which can be from an external or internal source.
* Outgoing Commitments - A firm, written obligation from a donor or provider to provide a specified amount of funds, under particular terms and conditions, for specific purposes, for the benefit of the recipient.
* Disbursements - Outgoing funds that are placed at the disposal of a recipient government or organisation, or funds transferred between two separately reported activities.
* Expenditures - Outgoing funds that are spent on goods and services for the activity.
* Budget - The value of the activity's budget for each financial quarter or year over the lifetime of the activity. The purpose of this element is to provide predictability for recipient planning on an annual basis.
It should be noted that because Expenditures do not represent Disbursements that have actually been spent, they can be added together to calculate Spending. To calculate spending, it is recommended to aggregate Disbursement and Expenditure transactions as Disbursements capture funds flowing out to other organisations or to a recipient government and Expenditures capture funds that are spent on goods and services (more details on this in the Analysing the Data section).


Recipient Country or Region	
===========================
This is the country or region that was the recipient of this transaction. Possible values:

* The value will be only one country or region as the file is filtered to only include the selected country or region.

Multi Country	
========================
This indicates whether the activity has one or multiple recipient countries. If it is a multi-country activity, this means that the estimated percentage to that country has been applied to the transaction / budget values.
Possible values:
* 0 = Transaction / budget is part of an activity which has only one recipient country (or region).
* 1 = Transaction / budget is part of an activity which has multiple recipient countries.

Sector Category	
================
This is the category of the sector (e.g. 121 - Health, General) that an activity is supporting and is more aggregated than Sector (e.g. 12182 - Medical Research). It is based on the OECD DAC's list of 3-digit sectors. This is not available for all transactions as it is recommended that organisations include either the OECD DAC 3 or 5 digit codes but not all do so.
Possible values:
* Values in this field are from the OECD DAC's list of 3-digit sectors, from the OECD.Stat website. There are 43 Sector Categories that can be selected, e.g. 121 - Health, General.

Sector
========
This is the name of the sector that an activity is supporting and is a sub-sector of the Sector Category. It is based on the OECD DAC's list of 5-digit sectors.
Possible values:
* Values in this field are from the OECD DAC's list of 5-digit sectors, from the OECD.Stat website. There are 295 Sectors that can be selected, e.g. 12182 - Medical Research.


Humanitarian	
========================
This indicates whether the transaction / budget can be categorized as humanitarian. Additional information on the methodology used for this assessment is found here.

Possible values:
* 0 = Transaction / budget is not categorized as humanitarian
* 1 = Transaction / budget is categorized as humanitarian


Calendar Year	
========================
This in the year in which the transaction occurred or the year for which the budget values have been aggregated.
Possible values:
* All years for which data is available in IATI.

Calendar Quarter	
========================
This is the quarter in which the transaction occurred or the quarter for which the budget values have been aggregated.
Possible values:
* Q1: January - March
* Q2: April - June
* Q3: July - September
* Q4: October - December

Calendar Year and Quarter	
==========================
This in the year and quarter in which the transaction occurred or the year and quarter for which the budget values have been aggregated.
Possible values:
* All years and quarters for which data is available in IATI (e.g. 2021 Q1).

URL	
========================
This is the link to the activity page on d-portal.

Value (USD)	
========================
This is the value of this row in U.S. Dollars. Possible values:
* Any numeric value (can be positive or negative). Organisations sometimes include negative transactions in their data. For disbursements, this typically means that money disbursed is being returned to the funder. For commitments, it could be an adjustment to an initial commitment -
e.g. an initial commitment of USD 10,000 is reduced to USD 8,000. Additional details can be found here.

Value (EUR)	
========================
Value (EUR)
This is the value of this row in Euros.

Value (Local currrency)
========================
This is the value of this row in the local currency and is customized for each country. The list of local currencies by country is available here.
