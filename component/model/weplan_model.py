from sepal_ui import model as sm
from traitlets import Int, Unicode


class WeplanModel(sm.Model):

    weight = Int(None, allow_none=True).tag(sync=True)
    "the order of relative weights between carbon and biodiversity objectives"

    target = Int(None, allow_none=True).tag(sync=True)
    "target category"

    iso = Unicode(None).tag(sync=True)
    "the iso code of the selected country"
