from sepal_ui import sepalwidgets as sw


class DownloadTile(sw.Card):
    def __init__(self, model):

        # read the model
        self.model = model

        # add the base widgets
        self.close = sw.Icon(children=["mdi-close"], small=True)
        self.title = sw.CardTitle(
            class_="pa-0 ma-0", children=[sw.Spacer(), self.close]
        )

        # create the widgets
        self.w_target = sw.Select(
            small=True,
            items=[i for i in range(1, 5)],
            v_model=[model.target],
            label="target",
            dense=True,
            multiple=True,
            clearable=True,
            chips=True,
        )
        self.w_weight = sw.Select(
            small=True,
            items=[i for i in range(1, 10)],
            v_model=[model.weight],
            label="weight",
            dense=True,
            multiple=True,
            clearable=True,
            chips=True,
        )

        # compulsory component to display a process
        self.btn = sw.Btn("Retreive to SEPAL", color="secondary")
        self.actions = sw.CardActions(
            class_="pa-0 ma-0", children=[sw.Spacer(), self.btn]
        )
        self.alert = sw.Alert()

        # create the object
        super().__init__(
            max_width="500px",
            class_="pa-1",
            children=[
                self.title,
                self.w_target,
                self.w_weight,
                self.actions,
                self.alert,
            ],
            viz=False,
        )

        # add javascript events
        self.close.on_event("click", lambda *args: self.hide())

    def add_target(self, target):
        """add a target to the v_model values"""

        tmp = list(set([target, *self.w_target.v_model]))
        self.w_target.v_model = tmp

        return

    def add_weight(self, weight):
        """add a weight to the v_model values"""

        tmp = list(set([weight, *self.w_weight.v_model]))
        self.w_weight.v_model = tmp

        return
