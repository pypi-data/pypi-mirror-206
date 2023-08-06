from pydantic import BaseModel

from . import FreeText


class SpatialAndTemporalAlignment(FreeText):
    """Method used to correlate images from different modalities"""

    _template_label = "Spatial/Temporal Alignment"

    _examples = [
        "Manual overlay",
        "Alignment algorithm"
    ]


class FiducialsUsed(FreeText):
    """Features from correlated datasets used for colocalisation"""

    _template_label = "Fiducials Used"


class TransformationMatrix(FreeText):
    """Correlation transforms"""

    _template_label = "Transformation Matrix"
    _template_hint = "Filename if present"


class ImageCorrelation(BaseModel):
    """How images from the same correlative study are linked"""

    _template_label = "Image Correlation"

    spatial_and_temporal_alignment: SpatialAndTemporalAlignment
    fiducials_used: FiducialsUsed
    transformation_matrix: TransformationMatrix