from sepal_ui import model as sm
from traitlets import Int, Unicode


class WeplanModel(sm.Model):

    weight = Int(1).tag(sync=True)
    "the order of relative weights between carbon and biodiversity objectives"

    target = Int(1).tag(sync=True)
    "target category"

    iso = Unicode(None).tag(sync=True)
    "the iso code of the selected country"
