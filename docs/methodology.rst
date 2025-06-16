************************
CDFD Methodology
************************

This section outlines how IATI data is the retrieved, processed, and output by CDFD.

Data Source
============


CDFD downloads a daily snapshot of all IATI data from the `IATI Data Dump <https://iati-data-dump.codeforiati.org/>`_, a tool built by the IATI community.

CDFD currently uses all IATI data published to version 2.01 of the standard or above. 
This includes both valid and invalid data, so activities that are not accessible via other IATI tooling may be found in CDFD outputs. 


Data Extraction
================

Activity level
---------------

The following elements are extracted from each IATI activity:

.. csv-table::
    :file: tables/activity_level.csv
    :widths: 15, 45
    :header-rows: 1

|

.. note::
    The :iati-reference:`description` element is not included in whole country/region downloads available from the home page. This is due to file size limitations.

|

Transaction level
--------------------

.. important::
    Only incoming fund, outgoing commitment, disbursement, and expenditure transaction types are included in CDFD's analysis.

|

The following elements are extracted from each transaction. If these four fields do not exist, the transaction is not processed. 

.. csv-table::
    :file: tables/transaction_level.csv
    :widths: 22, 45
    :header-rows: 1

Transaction or activity level
------------------------------

For some elements, the data can be declared at transaction or activity level. Transaction level is used by CDFD as default, backed up by activity level elements.

.. csv-table::
    :file: tables/act_trans_level.csv
    :widths: 20,20, 45
    :header-rows: 1

Provider and receiver organisations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Where provider or receiver organisations are not declared, the following activity level logic is applied:

.. csv-table::
    :file: tables/org_logic.csv
    :widths: 22,40,40
    :header-rows: 1


Multi-value elements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When recipient country/region or sector are declared at activity level, they may have multiple values with percentage splits. 