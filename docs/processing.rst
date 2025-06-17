************************
Data Processing
************************

This section outlines how IATI data is processed by CDFD.

Transaction Splitting
======================

Where country/region or sector are declared at activity level, individual transactions may map to multiple countries/regions and sectors. 
In each case, the transaction is split with the value proportionate to the percentage to this transaction for this country/region, for this sector.

.. note::
    Where there are no countries or DAC regions, the transaction is discarded. 
    Where there are no sectors, the sector is output as blank.

In some cases, the published percentages may also not be correct. For example, they may not add up to 100, or there may be multiple sectors with no percentage specified. 
In these cases, the percentages are adjusted and rebased so that the percentages add up to 100%.

For example:

+-------------------------+----------------------+----------------------+
| Sector                  | Published Percentage | Corrected Percentage |
+=========================+======================+======================+
| 12220 Basic health care | 100%                 | 50%                  |
+-------------------------+----------------------+----------------------+
| 11220 Primary education | 100%                 | 50%                  |
+-------------------------+----------------------+----------------------+

A single transaction of USD 100 would then be split into two rows: one row for USD 50 for basic health care and a second row of USD 50 for primary education. 
If the same activity were classified with two recipient countries, it would be split again, now into four rows.

When correcting percentages for countries/regions, the following logic is used:


