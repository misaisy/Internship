BASE_URL = "http://www.skuad-dev.nots-fns.ru"


INDUSTDRY_PARAMS = [
    "id",
    "name",
    "numComps",
    "profitComps",
    "unprofitComps",
    "taxespaidComps",
    "creddebtComps",
    "revenue",
    "taxesPaid",
    "creditDebt"
]

INDUSTDRY_VALID_REGIONS = [
    ("Краснодарский край", INDUSTDRY_PARAMS),
    ("город Москва", INDUSTDRY_PARAMS),
    ("Свердловская область", INDUSTDRY_PARAMS)
]

INDUSDTRY_INVALID_REGIONS = [
    ("all_regions", []),
    ("0", []),
    ("Несуществующий регион", []),
    (" ", [])
]

BUSINESS_PARAMS = [
    "id",
    "value",
    "key",
    "name",
    "dynamic",
    "number_companies"
]

EXPECT = {
    "id": 0,
    "value": 9.55,
    "key": "revenue_growth_q",
    "name": "динамика выручки по сравнению с предыдущим отчетным периодом (квартал)",
    "dynamic": 0.72,
    "number_companies": 40
}

BUSINESS_VALID_REGIONS = [
    ("Краснодарский край", "Деятельность административно-хозяйственная, вспомогательная деятельность по обеспечению функционирования организации, деятельность по предоставлению прочих вспомогательных услуг для бизнеса", BUSINESS_PARAMS, EXPECT),
    ("город Москва", "", BUSINESS_PARAMS, EXPECT),
    ("Свердловская область", "Деятельность административно-хозяйственная, вспомогательная деятельность по обеспечению функционирования организации, деятельность по предоставлению прочих вспомогательных услуг для бизнеса", BUSINESS_PARAMS, EXPECT)
]

BUSINESS_INVALID_REGIONS = [
    ("0", ["region_name", "data_ba"]),
    ("Несуществующий регион", ["region_name", "data_ba"]),
    (" ", ["region_name", "data_ba"])
]

BUSINESS_BOUNDARY_REGIONS = [
    ("all_regions", BUSINESS_PARAMS),
]

STATISTIC_PARAMS = [
    "id",
    "key",
    "name",
    "parameters"
]

STATISTIC_VALID_REGION = [
    ("Краснодарский край", STATISTIC_PARAMS),
    ("город Москва", STATISTIC_PARAMS),
    ("Свердловская область", STATISTIC_PARAMS)
]

STATISTIC_INVALID_REGIONS = [
    ("0", []),
    ("Несуществующий регион", []),
    (" ", [])
]

STATISTIC_ALL_REGION = [
    ("all_regions", STATISTIC_PARAMS)
]

LIMITS = [
    -1,
    0,
    2
]


ENDPOINTS = {
    "INDUSTRY": "/api/squad-statement/region/indusdtry/",
    "BUSINESS_ACTIVITY": "/api/squad-statement/region/business_activity/",
    "STATISTICS": "/api/squad-statement/region/statistics-rank-solvency/"
}


NEGATIVE_ENDPOINT = [
    ENDPOINTS["INDUSTRY"],
    ENDPOINTS["BUSINESS_ACTIVITY"],
    ENDPOINTS["STATISTICS"]
]