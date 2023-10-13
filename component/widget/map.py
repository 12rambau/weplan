from ipyleaflet import WidgetControl
from ipywidgets import Button, Layout
from sepal_ui import mapping as sm

from component.message import cm


class CButton(Button):
    def __init__(self, tooltip, icon):
        super().__init__(
            tooltip=tooltip,
            icon=icon,
            layout=Layout(
                width="30px", height="30px", line_height="30px", padding="0px"
            ),
        )


class Map(sm.SepalMap):
    def __init__(self):
        super().__init__(dc=True, zoom=3)

        self.layout.height = "85vh"

        # hide the dc component
        # it's only useful to be compatible with AOI selection
        self.hide_dc()

        # add the buttons on the topleft side of the map
        self.aoi_btn = CButton(cm.map.control.aoi, "map-marker")
        self.param_btn = CButton(cm.map.control.parameters, "navicon")
        self.download_btn = CButton(cm.map.control.download, "cloud-download")

        self.add_widget_as_control(self.aoi_btn, "topleft")
        self.add_widget_as_control(self.param_btn, "topleft")
        self.add_widget_as_control(self.download_btn, "topleft")

    def add_widget_as_control(self, widget, position, first=False):
        """
        Add widget as control in the given position

        Args:
            widget (dom.widget): Widget to convert as map control
            position (str): 'topleft', 'topright', 'bottomright', 'bottomlreft'
            first (Bool): Whether set the control as first or last element
        """

        new_control = WidgetControl(
            widget=widget, position=position, transparent_bg=True
        )

        if first == True:
            self.controls = tuple(
                [new_control] + [control for control in self.controls]
            )
        else:
            self.controls = self.controls + tuple([new_control])

        return
