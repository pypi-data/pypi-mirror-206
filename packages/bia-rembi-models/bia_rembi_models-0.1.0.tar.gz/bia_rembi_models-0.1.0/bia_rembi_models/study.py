from . import FreeText, MetadataGroup
from typing import List, Literal, Union, Optional
from bia_rembi_models import _version_l
from datetime import date


class OrgName(FreeText):
    """The name of the organisation."""

    _template_label = "Name"


class OrgAddress(FreeText):
    """The address of the organisation."""

    _template_label = "Address"


class Organisation(MetadataGroup):
    _template_label = "Organisation"

    pass


class OrganisationInfo(Organisation):

    _template_label = "Organisation"

    name: OrgName
    address: Optional[OrgAddress]

    class Config:
        frozen = True


class FirstName(FreeText):
    """Author first name."""

    _template_label = "First Name"


class LastName(FreeText):
    """Author last name."""

    _template_hint = "fill in, add more people in separate columns if needed"
    _template_label = "Last Name"

class EmailAddress(FreeText):
    """Author e-mail address."""

    _template_label = "E-mail"

class Orcid(FreeText):
    """Author ORCID ID."""

    _template_hint = "fill in if known"
    _template_label = "ORCID"

class Role(FreeText):
    """Author role in the study."""

    _template_default = "submitter"
    _template_label = "Roles"


class URL(FreeText):
    """URL"""

    _template_label = "URL"


class OrganisationURL(Organisation):
    """URL to a public registry containing organisation information. ROR recommended"""
    name: OrgName
    url: URL

    _template_label = "ROR_ID"

    _examples = [
        "https://ror.org/02catss52" #EBI
    ]


class Person(MetadataGroup):

    _template_label = "Person"

    last_name: LastName
    first_name: FirstName
    email: Optional[EmailAddress]
    orcid: Optional[Orcid]
    # order matters
    # an OrganisationURL object can be validated by OrganisationInfo 
    affiliation: Union[OrganisationURL, OrganisationInfo]
    role: Optional[Role]


class Author(Person): pass


class PubTitle(FreeText):
    """Title of associated publication."""

    _template_label = "Title"


class PubAuthors(FreeText):
    """Authors of associated publication."""

    _template_label = "Authors"


class DOI(FreeText):
    """Digital Object Identifier (DOI)."""

    _template_label = "DOI"


class PublicationYear(FreeText):
    """Year of publication."""

    _template_label = "Year"


class PubmedID(FreeText):
    "PubMed identifier for the publication."

    _template_label = "PMC ID"


class Publication(MetadataGroup):

    _template_label = "Publication"

    title: PubTitle
    authors: Optional[PubAuthors]
    doi: Optional[DOI]
    year: Optional[PublicationYear]
    pubmed_id: Optional[PubmedID]


class GrantIdentifier(FreeText):
    """The identifier for the grant."""

    _template_hint = "Grant identifier - add multiple in separate columns if needed."
    _template_label = "Identifier"


class GrantFunder(FreeText):
    """The funding body provididing support."""

    _template_label = "Funding Body"


class GrantReference(MetadataGroup):

    _template_label = "Reference"

    identifier: GrantIdentifier
    funder: GrantFunder


class FundingStatement(FreeText):
    """A description of how the data generation was funded."""

    _template_label = "Statement"


class Funding(MetadataGroup):

    _template_label = "Funding"

    funding_statement: FundingStatement
    grant_references: List[GrantReference] = []


class License(MetadataGroup):
    """The license under which the data are available."""

    _atom = True
    _template_label = "License"
    _template_hint = "Leave blank"


class LicenseCC0(License):
    name: Literal["CC0"]
    url: Literal["https://example.com/cc_0"]


class LicenseCCBY40(License):
    name: Literal["CC BY 4.0"]
    url: Literal["https://example.com/cc_by_40"]


class Title(FreeText):
    """The title for your dataset. This will be displayed when search results including your data are shown. Often this will be the same as an associated publication."""

    _template_hint = "This will be displayed when search results including your data are shown"
    _template_label = "Title"

    _examples = [
        "Visualization of loop extrusion by DNA nanoscale tracing in single cells",
        "SARS-COV-2 drug repurposing - Caco2 cell line",
        "Large-scale electron microscopy database for human type 1 diabetes",
    ]


class Description(FreeText):
    """Use this field to describe your dataset. This can be the abstract to an accompanying publication."""

    _template_hint = "Overall description of the dataset, can be a publication abstract."
    _template_label = "Description"

class PrivateUntilDate(date):
    """Date in the YYYY-mm-dd format. After this date the submission stops being private and you will only be able to add new files to the submission, not remove exiting ones."""

    _template_hint = "Day in the YYYY-mm-dd format by which the submission will be private."
    _template_label = "Private Until"
    _atom = True


class Keyword(FreeText):
    """Keywords describing your data that can be used to aid search and classification."""

    _template_label = "Key Words"
    _template_hint = "Key words relating to the study - add multiple keywords in separate columns"

    _examples = [
        "RNA localisation",
        "CRISPR",
        "Brain",
    ]


class Acknowledgements(FreeText):
    """Any people or groups that should be acknowledged as part of the dataset."""

    _template_label = "Acknowledgements"


class LinkURL(FreeText):
    """The URL of a link relevant to the dataset."""

    _template_label = "URL"
    _template_hint = "URL of relevant link - add multiple in separate columns if needed. "


class LinkDescription(FreeText):
    """The description of the linked content."""

    _template_label = "Description"
    _template_hint = "Description of link above, number of descriptions should match number of links"

    _examples = [
        "Image analysis code",
        "Sequencing data",
        "Project website"
    ]


class LinkType(FreeText):
    """The type of the link."""

    _template_label = "Type"


class Link(MetadataGroup):

    _template_label = "Link"

    link_url: LinkURL
    link_type: Optional[LinkType]
    link_description: Optional[LinkDescription]


class Study(MetadataGroup):
    """General study information"""

    title: Title
    description: Description
    private_until_date: PrivateUntilDate
    keywords: List[Keyword]
    authors: List[Author]
    license: Optional[License]
    funding: Optional[Funding]
    publications: Optional[List[Publication]] = []
    links: Optional[List[Link]] = []
    acknowledgements: Optional[Acknowledgements]
    rembi_version: _version_l
    
    _attribute_validation_text = {
        'title': 'Unicode; Minimum length: 25 characters',
        'description': 'Unicode; Minimum length: 25 characters'
    }
    