from sepal_ui import sepalwidgets as sw

from component import parameter as cp


class ParamTile(sw.Card):
    def __init__(self, model):

        # read the model
        self.model = model

        # add the base widgets
        self.close = sw.Icon(children=["mdi-close"], small=True)
        self.title = sw.CardTitle(
            class_="pa-0 ma-0", children=[sw.Spacer(), self.close]
        )

        # create the widgets
        w_target = sw.Select(
            small=True,
            items=[i + 1 for i in range(cp.nb_target)],
            v_model=model.target,
            label="target",
            dense=True,
        )
        w_weight = sw.Select(
            small=True,
            items=[i + 1 for i in range(cp.nb_weight)],
            v_model=model.weight,
            label="weight",
            dense=True,
        )

        # link the widgets to the model
        self.model.bind(w_target, "target").bind(w_weight, "weight")

        # create the object
        super().__init__(
            max_width="500px",
            class_="pa-1",
            children=[self.title, w_target, w_weight],
            viz=False,
        )

        # add javascript events
        self.close.on_event("click", lambda *args: self.hide())
