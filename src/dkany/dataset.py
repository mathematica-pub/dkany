import core.utils as utils
import logging

import requests
from requests_toolbelt import sessions
from requests.cookies import RequestsCookieJar
from datetime import datetime as dt
from copy import deepcopy as copy

logger = logging.getLogger(__name__)


class DKANDataset(object):
    """
    docstring
    """

    def __init__(
        self,
        title=None,
        description=None,
        csv_url=None,
        modified_date=None,
        categories=None,
        tags=None,
        publisher=None,
        programCode=None,
        bureauCode=None,
        contactEmail=None,
        contactName=None,
        accrualPeriodicity=None,
        accessLevel=None,
        identifier=None,
        references=None,
        use_current_date_as_modified_date=True,
    ):
        """[summary]



        Args:
            title ([type], optional): [description]. Defaults to None.
            description ([type], optional): [description]. Defaults to None.
            csv_url ([type], optional): [description]. Defaults to None.
            modified_date ([type], optional): [description]. Defaults to None.
            categories ([type], optional): [description]. Defaults to None.
            tags ([type], optional): [description]. Defaults to None.
            publisher ([type], optional): [description]. Defaults to None.
            programCode ([type], optional): [description]. Defaults to None.
            bureauCode ([type], optional): [description]. Defaults to None.
            contactEmail ([type], optional): [description]. Defaults to None.
            contactName ([type], optional): [description]. Defaults to None.
            accrualPeriodicity ([type], optional): [description]. Defaults to None.
            accessLevel ([type], optional): [description]. Defaults to None.
            references ([type], optional): [description]. Defaults to None.
            use_current_date_as_modified_date (bool, optional): [description]. Defaults to True.
        """

        # More documentation on the meaning of these feilds can be found at
        # https://resources.data.gov/resources/dcat-us/

        if modified_date is None:
            if use_current_date_as_modified_date:
                modified_date = dt.now().strftime("%Y-%m-%dT%H:%M:%S")

        if categories is None:
            categories = []

        if tags is None:
            tags = []

        self.title = title
        self.description = description
        self.csv_url = csv_url
        self.modified_date = modified_date
        self.categories = categories
        self.tags = tags
        self.publisher = publisher
        self.programCode = programCode
        self.bureauCode = bureauCode
        self.contactEmail = contactEmail
        self.contactName = contactName
        self.accrualPeriodicity = accrualPeriodicity
        self.accessLevel = accessLevel
        self.references = references
        self.identifier = identifier

        self.distributions = []

    def add_distribution(
        self,
        title=None,
        description=None,
        downloadURL=None,
        mediaType=None,
        format=None,
    ):

        self.distributions.append(
            {
                "title": title,
                "downloadURL": downloadURL,
                "description": description,
                "mediaType": mediaType,
                "format": format,
            }
        )

    def add_tag(self, new_tag):
        self.tags.append(new_tag)

    def add_category(self, new_category):
        self.categories.append(new_category)

    def build_request_body(self):
        model = {
            "title": self.title,
            "description": self.description,
            "accessLevel": self.accessLevel,
            "accrualPeriodicity": self.accrualPeriodicity,
            "programCode": [self.programCode],
            "bureauCode": [self.bureauCode],
            "publisher": {"name": self.publisher},
            "contactPoint": {"hasEmail": self.contactEmail, "fn": self.contactName},
            "modified": self.modified_date,
            "theme": self.categories,  # Categories
            "keyword": self.tags,  # tags
            "references": self.references,
            "distribution": self.distributions,
        }
        if self.identifier is not None:
            model["identifier"] = self.identifier

        return model
