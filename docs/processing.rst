************************
Data Processing
************************

This section outlines how IATI data is processed by CDFD.

Transaction Splitting
======================

Where country/region or sector are declared at activity level, individual transactions may map to multiple countries/regions and sectors. 
In each case, the transaction is divided between each sector in each country/region, based on the published percentage splits.

.. note::
    Where there are no countries or DAC regions, the transaction is discarded. 

    Where there are no sectors, the sector is output as blank.

In some cases, the published percentages may also not be correct. For example, they may not add up to 100%, or there may be multiple sectors with no percentage specified. 
In these cases, the percentages are adjusted and rebased so that the percentages add up to 100%.

Sector adjustment
--------------------

For example, the following adjustment may be applied to sector percentages for an activity:

    +-------------------------+----------------------+----------------------+
    | Sector                  | Published Percentage | Corrected Percentage |
    +=========================+======================+======================+
    | 12220 Basic health care | 100%                 | 50%                  |
    +-------------------------+----------------------+----------------------+
    | 11220 Primary education | 100%                 | 50%                  |
    +-------------------------+----------------------+----------------------+

A single transaction of USD 100 would then be split into two rows: one row for USD 50 for basic health care, and a second row of USD 50 for primary education. 
If the same activity were classified with two recipient countries, it would be split again, now into four rows.

Recipient countries/region adjustment
--------------------------------------

Adjusting recipient country/region percentages can be more complex. The IATI Standard requires that "Percentages for all reported countries and regions within a vocabulary MUST add up to 100."
However, some organistions have reported recipient countries and regions with their percentages *separately* adding up to 100%.


When correcting percentages for countries/regions, the following logic is used:

\1. If recipient-country and recipient-region exist, and recipient-country have no percentages: take only recipient-country.

    +-----------------------------+----------------------+---------------------+
    | Recipient Country/Region    | Published Percentage | Adjusted Percentage |
    +=============================+======================+=====================+
    |  Liberia (LR)               | \-                   | 100%                |
    +-----------------------------+----------------------+---------------------+
    |  Africa, regional (298)     | \-                   | 0%                  |
    +-----------------------------+----------------------+---------------------+

|

\2. If recipient-country and recipient-region both have percentages, but recipient-country percentages or recipient-region percentages adds up to around 100%: take only recipient-country.

    +-----------------------------+----------------------+---------------------+
    | Recipient Country/Region    | Published Percentage | Adjusted Percentage |
    +=============================+======================+=====================+
    |  Chad (TD)                  | 70%                  | 70%                 |
    +-----------------------------+----------------------+---------------------+
    |  Liberia (LR)               | 30%                  | 30%                 |
    +-----------------------------+----------------------+---------------------+
    |  Africa, regional (298)     | 100%                 | 0%                  |
    +-----------------------------+----------------------+---------------------+

|

\3. Otherwise, take recipient-country and recipient-region.

    +-----------------------------+----------------------+---------------------+
    | Recipient Country/Region    | Published Percentage | Adjusted Percentage |
    +=============================+======================+=====================+
    |   Chad (TD)                 | 50%                  | 50%                 |
    +-----------------------------+----------------------+---------------------+
    |  Africa, regional (298)     | 50%                  | 50%                 |
    +-----------------------------+----------------------+---------------------+


Currency Conversion
======================

Individual transactions are conversion to USD, Euro, and the local (country) currency using the closest exchange rate date to the transaction :iati-reference:`@value-date`. 
Budget values are converted using the closest date to the budget :iati-reference:`@value-date`.

Monthly exchange rates for 169 currencies are sourced from the IMF's `International Financial Statistics <https://data.imf.org/en?sk=4C514D48-B6BA-49ED-8AB9-52B0C1A0179B>`_.

Budget Handling
======================

In the IATI standard, budgets do not include as much detail as transactions. For example, they are not classified by sector or country. 
Budgets are therefore split propotionally based on activity and transaction level information for the following elements:

* :iati-reference:`aid-type`
* :iati-reference:`finance-type`
* :iati-reference:`flow-type`
* :iati-reference:`sector`
* :iati-reference:`recipient-country` / :iati-reference:`recipient-region`

The following logic is applied for provider and receiver organisations:

* Provider organisation: :iati-reference:`reporting-org`
* Receiver organisation/s: :iati-reference:`participating-org`- Implementing org


Where budgets span more than one quarter, they are split into multiple rows that map to one quarter each. The value is split proportionately. 
If a budget does not perfectly span quarters, the number of days in each part-quarter are used to calculate the proportion to be attributed to each quarter.

This maintains comparability between transactions (which are marked with a single date) and budgets (which span a period, and which may not align with an organisation's fiscal year).

Where revised and original budgets are both published for the same period, revised budgets are used instead of original budgets.
