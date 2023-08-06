from typing import Optional

from pydantic import BaseModel

from . import FreeText


class SamplePreparationProtocol(FreeText):
    """How the sample was prepared for imaging."""

    # TODO - CHECK
    _template_label = "Sample Preparation Protocol"

    _examples = [
        "Cells were cultured on poly-L-lysine treated coverslips. Culture media was aspirated, and coverslips were washed once with PBS. Cells were fixed by incubating for 10 min with 4 % formaldehyde/PBS, washed twice with PBS, and permeabilized by incubating (>3 h, -20°C) in 70 % ethanol. Cells were rehydrated by incubating (5 min, RT) with FISH wash buffer (10 % formamide, 2x SSC). For hybridization, coverslips were placed cell-coated side down on a 48μl drop containing 100 nM Quasar570-labelled probes complementary to one of REV-ERBα, CRY2, or TP53 transcripts (Biosearch Technologies) (see Table S6 for probe sequences), 0.1 g/ml dextran sulfate, 1 mg/ml E. coli tRNA, 2 mM VRC, 20 μg/ml BSA, 2x SSC, 10 % formamide and incubated (37°C, 20 h) in a sealed parafilm chamber. Coverslips were twice incubated (37°C, 30 min) in pre-warmed FISH wash buffer, then in PBS containing 0.5 μg/ml 4’,6-diamidino-2-phenylindole (DAPI) (5 min, RT), washed twice with PBS, dipped in water, air-dried, placed cell-coated side down on a drop of ProLong Diamond Antifade Mountant (Life Technologies), allowed to polymerize for 24 h in the dark and then sealed with nail varnish.",
        "Immunostained spreads of Arabidopsis pachytene cells were prepared for 3D-SIM imaging as follows. To roughly stage the meiocytes, a single anther from a floral bud was removed and squashed in a drop of water on a clean slide under a coverslip and inspected using brightfield microscopy. Early- and mid-pachytene meiocytes were still stuck together within a meiocyte column, whilst late-pachytene meiocytes had begun to break apart from one-another. More precise staging of early and late pachytene meiocytes was also based on previously defined HEI10 behaviour, with mid pachytene meiocytes exhibiting an intermediate phenotype. The remaining 5 anthers containing meiocytes of the desired stage were dissected from the staged buds. They were then macerated using a brass rod on a No. 1.5H coverslip (Marienfeld) in 10 µl digestion medium (0.4% cytohelicase, 1.5% sucrose, 1% polyvinylpyrolidone in sterile water) for 1 min. Coverslips were then incubated in a moist chamber at 37 °C for 4 min before adding 10 µl of 2% lipsol solution followed by 20 µl 4% paraformaldehyde (pH 8). Coverslips were dried in the fume hood for 3 h, blocked in 0.3% bovine serum albumin in 1x phosphate-buffered saline (PBS) solution and then incubated with primary antibody at 4 °C overnight and secondary antibody at 37 °C for 2 h. In between antibody incubations, coverslips were washed 3 times for 5 min in 1x PBS plus 0.1% Triton X-100. Coverslips were then incubated in 10 µl DAPI (10 µg/ml) for 5 min, washed and mounted on a slide in 7 µl Vectashield.",
        "Cells grown on coverslips were fixed in ice-cold methanol at _20 _ C for 10 min. After blocking in 0.2% gelatine from cold-water fish (Sigma) in PBS (PBS/FSG) for 15 min, coverslips were incubated with primary antibodies in blocking solution for 1h. Following washes with 0.2% PBS/FSG, the cells were incubated with a 1:500 dilution of secondary antibodies for 1 h (donkey anti- mouse/rabbit/goat/sheep conjugated to Alexa 488 or Alexa 594; Molecular Probes  or donkey anti-mouse conjugated to DyLight 405, Jackson ImmunoResearch). The cells were counterstained with 1 _g ml_1 Hoechst 33342 (Sigma) to visualize chromatin. After washing with 0.2% PBS/FSG, the coverslips were mounted on glass slides by inverting them into mounting solution (ProLong Gold antifade, Molecular Probes). The samples were allowed to cure for 24-48 h."
    ]


class GrowthProtocol(FreeText):
    """How the specimen was grown, e.g. cell line cultures, crosses or plant growth."""

    _template_label = "Growth Protocol"

    _examples = [
        "Cells were cultured on poly-L-lysine treated coverslips. Culture media was aspirated, and coverslips were washed once with PBS. Cells were fixed by incubating for 10 min with 4 % formaldehyde/PBS, washed twice with PBS, and permeabilized by incubating (>3 h, -20°C) in 70 % ethanol. Cells were rehydrated by incubating (5 min, RT) with FISH wash buffer (10 % formamide, 2x SSC). For hybridization, coverslips were placed cell-coated side down on a 48μl drop containing 100 nM Quasar570-labelled probes complementary to one of REV-ERBα, CRY2, or TP53 transcripts (Biosearch Technologies) (see Table S6 for probe sequences), 0.1 g/ml dextran sulfate, 1 mg/ml E. coli tRNA, 2 mM VRC, 20 μg/ml BSA, 2x SSC, 10 % formamide and incubated (37°C, 20 h) in a sealed parafilm chamber. Coverslips were twice incubated (37°C, 30 min) in pre-warmed FISH wash buffer, then in PBS containing 0.5 μg/ml 4’,6-diamidino-2-phenylindole (DAPI) (5 min, RT), washed twice with PBS, dipped in water, air-dried, placed cell-coated side down on a drop of ProLong Diamond Antifade Mountant (Life Technologies), allowed to polymerize for 24 h in the dark and then sealed with nail varnish.",
        "Immunostained spreads of Arabidopsis pachytene cells were prepared for 3D-SIM imaging as follows. To roughly stage the meiocytes, a single anther from a floral bud was removed and squashed in a drop of water on a clean slide under a coverslip and inspected using brightfield microscopy. Early- and mid-pachytene meiocytes were still stuck together within a meiocyte column, whilst late-pachytene meiocytes had begun to break apart from one-another. More precise staging of early and late pachytene meiocytes was also based on previously defined HEI10 behaviour, with mid pachytene meiocytes exhibiting an intermediate phenotype. The remaining 5 anthers containing meiocytes of the desired stage were dissected from the staged buds. They were then macerated using a brass rod on a No. 1.5H coverslip (Marienfeld) in 10 µl digestion medium (0.4% cytohelicase, 1.5% sucrose, 1% polyvinylpyrolidone in sterile water) for 1 min. Coverslips were then incubated in a moist chamber at 37 °C for 4 min before adding 10 µl of 2% lipsol solution followed by 20 µl 4% paraformaldehyde (pH 8). Coverslips were dried in the fume hood for 3 h, blocked in 0.3% bovine serum albumin in 1x phosphate-buffered saline (PBS) solution and then incubated with primary antibody at 4 °C overnight and secondary antibody at 37 °C for 2 h. In between antibody incubations, coverslips were washed 3 times for 5 min in 1x PBS plus 0.1% Triton X-100. Coverslips were then incubated in 10 µl DAPI (10 µg/ml) for 5 min, washed and mounted on a slide in 7 µl Vectashield.",
        "Cells grown on coverslips were fixed in ice-cold methanol at _20 _ C for 10 min. After blocking in 0.2% gelatine from cold-water fish (Sigma) in PBS (PBS/FSG) for 15 min, coverslips were incubated with primary antibodies in blocking solution for 1h. Following washes with 0.2% PBS/FSG, the cells were incubated with a 1:500 dilution of secondary antibodies for 1 h (donkey anti- mouse/rabbit/goat/sheep conjugated to Alexa 488 or Alexa 594; Molecular Probes  or donkey anti-mouse conjugated to DyLight 405, Jackson ImmunoResearch). The cells were counterstained with 1 _g ml_1 Hoechst 33342 (Sigma) to visualize chromatin. After washing with 0.2% PBS/FSG, the coverslips were mounted on glass slides by inverting them into mounting solution (ProLong Gold antifade, Molecular Probes). The samples were allowed to cure for 24-48 h."
    ]


class Specimen(BaseModel):
    """How the sample was grown or cultured and prepared for imaging."""

    _template_label = "Specimen"
    _atom = False

    # biosample: Biosample
    sample_preparation: SamplePreparationProtocol
    growth_protocol: Optional[GrowthProtocol]