# nyc_open_data_mwbe
This Python code filters through the City of New York's list of certified Minority- or Women-owned Business Enterprises (MWBE).

The City's dataset can be accessed here: https://data.cityofnewyork.us/Business/M-WBE-LBE-and-EBE-Certified-Business-List/ci93-uc8s

t work, we conduct research on prospects for fundraising. One of my department's recent projects was to conduct research on immigrant business owners in Queens. Nearly half (48%) of all Queens residents are foreign-born. Research shows that immigrants establish businesses at a rate much higher than native-born Americans. In recent years, a number of immigrant business owners have utilized Queens Library for special services such as ESOL classes for business owners. Queens Library believes that immigrant business owners could potentially benefit from and would welcome a corporate sponsorship  with Queens Library.

I wrote this Python script to access the MWBE API and filter through critera including an owner's ethnicity (Asian or Hispanic, for example), location (Queens ZIP code), and large contracts that the company has won in its history (greater than $100,000, for example). The dataset is limited because it doesn't contain immigrant status, and ethnicity is a not a perfect identifier for immigrant status. The outputted data is meant to be a starting point for further prospect research.
