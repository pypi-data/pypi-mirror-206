from typing import List, Optional

from . import FreeText, MetadataGroup


class Description(FreeText):
    """High level description of sample."""

    _template_label = "Description"

    _examples = [
        "Bronchial epithelial cell culture"
    ]
    

class ScientificName(FreeText):
    """Scientific name."""

    _template_label = "Scientific Name"

    _examples = [
        "Homo sapiens",
        "Arabidopsis thaliana",
        "Danio rerio"
    ]


class CommonName(FreeText):
    """Common name."""

    _template_label = "Common Name"

    _examples = [
        "human",
        "thale cress",
        "zebrafish"
    ]


class NCBITaxon(FreeText):
    """NCBI Taxon for the organism."""

    _template_label = "NCBI Taxon"
    _template_hint = "Leave blank if not known"

    _examples = [
        "http://purl.obolibrary.org/obo/NCBITaxon_9606",
        "http://purl.obolibrary.org/obo/NCBITaxon_3702",
        "http://purl.obolibrary.org/obo/NCBITaxon_7955"
    ]


class Organism(MetadataGroup):
    """Species."""

    _template_label = "Organism"

    scientific_name: ScientificName
    common_name: Optional[CommonName]
    ncbi_taxon: NCBITaxon


class BiologicalEntity(FreeText):
    """What is being imaged."""

    _template_label = "Biological Entity"

    _examples = [
        "Adult mouse corpus callosum",
        "Drosophila endoderm",
        "AC16s human cardiomyoctye cells"
    ]


class IntrinsicVariable(FreeText):
    """Intrinsic (e.g. genetic) alteration."""

    _template_label = "Intrinsic Variables"

    _examples = [
        "stable overexpression of HIST1H2BJ-mCherry and LMNA",
        "Jurkat E6.1 transfected with emerald-VAMP7",
        "Homozygous GFP integration into mitotic genes"
    ]


class ExtrinsicVariable(FreeText):
    """External treatment (e.g. reagent)."""

    _template_label = "Extrinsic Variables"

    _examples = [
        "Plate-bound anti-CD3 activation",
        "2-(9-oxoacridin-10-yl)acetic acid",
        "cridanimod"
    ]


class ExperimentalVariable(FreeText):
    """What is intentionally varied between multiple images."""

    _template_label = "Experimental Variables"

    _examples = [
        "Time",
        "Genotype",
        "Light exposure"
    ]


class Biosample(MetadataGroup):

    _template_label = "Biosample"
    _atom = False

    organism: Organism
    biological_entity: BiologicalEntity
    description: Optional[Description]
    intrinsic_variables: List[IntrinsicVariable] = []
    extrinsic_variables: List[ExtrinsicVariable] = []
    experimental_variables: List[ExperimentalVariable] = []