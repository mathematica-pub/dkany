"""Defines the types expected by the DKAN Client
Inferred from the responses specified here:
https://data.medicaid.gov/about/api
"""

from typing import Literal
from typing import List, TypedDict, NotRequired, Dict


class DkanSearchParams(TypedDict):
    fulltext: NotRequired[str]
    page: NotRequired[int]
    page_size: NotRequired[int]
    sort: NotRequired[List[str]]
    sort_order: NotRequired[List[str]]
    facets: NotRequired[str]
    publisher_name: NotRequired[str]
    keyword: NotRequired[str]
    theme: NotRequired[str]


class DkanCreateDatasetResponse(TypedDict):
    identifier: str
    message: str


class DkanUpdateDatasetResponse(TypedDict):
    identifier: str
    message: str


class DkanDeleteDatasetResponse(TypedDict):
    identifier: str
    message: str


class DkanDatasetPublisher(TypedDict):
    type: Literal["org:Organization"]
    name: str
    subOrganizationOf: str


class DkanDatasetContactPoint(TypedDict):
    type: Literal["vcard:Contact"]
    fn: str
    hasEmail: str


class DkanDatasetDistribution(TypedDict):
    type: Literal["dcat:Distribution"]
    title: str
    description: str
    format: str
    mediaType: str
    downloadURL: str
    accessURL: str
    conformsTo: str
    describedBy: str
    describedByType: str


class DkanDatasetMetadataResponse(TypedDict):
    type: Literal["dcat:Dataset"]
    title: str
    identifier: str
    description: str
    access_level: str
    accrual_periodicity: str
    described_by: str
    described_by_type: str
    issued: str
    modified: str
    license: str
    spatial: str
    temporal: str
    is_part_of: str
    publisher: DkanDatasetPublisher
    contact_point: DkanDatasetContactPoint
    theme: List[str]
    keyword: List[str]
    distribution: List[DkanDatasetDistribution]
    references: List[str]
    bureau_code: List[str]
    program_code: List[str]


class DkanGetDatasetResponse(TypedDict):
    """A response received from the DKAN /api/1/dataset/{identifier} endpoint"""

    results: List[dict]
    count: int
    schema: dict
    query: dict


class DkanSearchResponseFacet(TypedDict):
    type: str
    name: str
    total: int


class DkanSearchResponse(TypedDict):
    """A response received from the DKAN /api/1/search endpoint"""

    total: int
    results: Dict[str, DkanDatasetMetadataResponse]
    facets: List[DkanSearchResponseFacet]


class DkanMetadataFilterParams(TypedDict):
    title: NotRequired[str]
    identifier: NotRequired[str]
    description: NotRequired[str]
    access_level: NotRequired[str]
    accrual_periodicity: NotRequired[str]
    described_by: NotRequired[str]
    described_by_type: NotRequired[str]
    issued: NotRequired[str]
    modified: NotRequired[str]
    license: NotRequired[str]
    spatial: NotRequired[str]
    temporal: NotRequired[str]
    is_part_of: NotRequired[str]
    publisher: NotRequired[DkanDatasetPublisher]
    contact_point: NotRequired[DkanDatasetContactPoint]
    theme: NotRequired[List[str]]
    keyword: NotRequired[List[str]]
    distribution: NotRequired[List[DkanDatasetDistribution]]
    references: NotRequired[List[str]]
    bureau_code: NotRequired[List[str]]
    program_code: NotRequired[List[str]]
