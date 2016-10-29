# LBPD crime data

The "LBPD" mobile app available for both iOS and Android is developed by [MobilePD](http://gomobilepd.com/). Previous projects by several local developers sought to access the same data GoMobilePD uses - initial analysis showed that the data used by this app could be accessed as a XML-based API at the following uri: <http://api.ezaxess.com/v2/pd/longbeach/crimes/all>

This data feed is frequently unavailable, often for weeks at a time, and only represents recent crime activity, providing no access to historical data. This repository seeks to serve as a both a cache of the most recent records, as well as a permanent archive of historical data. The HackLB DLF would love to find another source for this data - ideally, directly from the city - as crime data is of deep interest to many city stakeholders.

### Sample record

A typical sample record is shown here:

```
{
    "block_address": "6400 Block E SPRING ST",
    "case_number": 160069002,
    "city": "Long Beach",
    "date_occured": "2016-10-24 06:44:00 UTC",
    "description": null,
    "id": 3198722,
    "incident_id": 99,
    "latitude": 33.8096481,
    "longitude": -118.106315,
    "state": "CA",
    "title": "GRAND THEFT; MOTOR VEHICLE"
}
```