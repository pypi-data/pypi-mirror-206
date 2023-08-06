from typing import List

from .sample import Biosample
from .specimen import Specimen
from .acquisition import ImageAcquisition

from . import FreeText, MetadataGroup, _version_l


class Name(FreeText):
    """The name of your study component."""

    _template_label = "Name"

    _examples = [
        "Experiment A",
        "Screen B",
        "Stitched max-projected fluorescent confocal images",
    ]


class Description(FreeText):
    """An explanation of your study component."""

    _template_label = "Description"

    _example = [
        "RNA-FISH of human cardiomyocyte cells (AC16s), U2OS cells or U2OS cells with Nr1d1 knocked-out exposed to different cold temperatures stained with RNA-FISH probes for Cry2, Tp53 or Nr1d1 and DAPI.",
        "Optical Projection Tomography scans of 28 markers that have been mapped onto a HH12 chick heart reference model.",
        "High-throughput screen to identify compounds that revert the multiparametric ALS disease profile to that found in healthy motor neurons.",
    ]


class StudyComponent(MetadataGroup):

    _template_label = "Study Component"
    
    name: Name
    description: Description
    rembi_version: _version_l

    # biosample: List[Biosample] = []
    # specimen: List[Specimen] = []
    # acquisition: List[ImageAcquisition] = []