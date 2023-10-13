from sepal_ui import sepalwidgets as sw
from sepal_ui.scripts import utils as su

from component import widget as cw
from component import scripts as cs
from component import parameter as cp
from component.message import cm
from component.model import WeplanModel
from .aoi_tile import AoiTile
from .param_tile import ParamTile
from .download_tile import DownloadTile


class MapTile(sw.Tile):
    def __init__(self):
        # set the map in the center
        self.map = cw.Map()

        # extract the models
        self.model = WeplanModel()

        # create the tiles
        self.aoi_tile = AoiTile(map_=self.map, model=self.model)
        self.param_tile = ParamTile(model=self.model)
        self.download_tile = DownloadTile(model=self.model)

        # place them in the map
        self.map.add_widget_as_control(self.aoi_tile, "bottomright")
        self.map.add_widget_as_control(self.param_tile, "topright", first=True)
        self.map.add_widget_as_control(self.download_tile, "bottomleft")

        # link to the btn for activation
        self.map.aoi_btn.on_click(lambda *_: self.aoi_tile.toggle_viz())
        self.map.param_btn.on_click(lambda *_: self.param_tile.toggle_viz())
        self.map.download_btn.on_click(lambda *_: self.download_tile.toggle_viz())

        # create the tile
        super().__init__(id_="map_tile", title="", inputs=[self.map])

        # add javascript behaviour
        self.aoi_tile.view.observe(self._update_aoi, "updated")
        self.param_tile.w_target.observe(self._update_map, "v_model")
        self.param_tile.w_weight.observe(self._update_map, "v_model")

    def _update_aoi(self, change):
        # reset weight values everywhere
        self.param_tile.reset()
        self.download_tile.reset()

        # hide the aoi_tile and show the params
        self.aoi_tile.hide()
        self.param_tile.show()

        return

    @su.switch("disabled", on_widgets=["aoi_tile", "param_tile"])
    def _update_map(self, change):
        if not self.model.iso:
            raise Exception(cm.map.error.no_iso)

        # clean the map from the different layers
        self.map.remove_layer(cm.map.layer.available, none_ok=True)
        self.map.remove_layer(cm.map.layer.mincost, none_ok=True)
        self.map.remove_layer(cm.map.layer.ce, none_ok=True)
        self.map.remove_layer(cm.map.layer.mb, none_ok=True)

        # exit if both target and weight are not all set
        if any([self.model.target is None, self.model.weight is None]):
            return

        # download all the maps if needed
        cs.extract_all(self.model.iso)

        # add the appropriate layers on the map
        self.map.add_raster(
            image=cs.get_available(self.model.iso),
            layer_name=cm.map.layer.available,
            colormap=cp.cmp_available,
            fit_bounds=False,
        )
        self.map.add_raster(
            image=cs.get_mincost(self.model.iso, self.model.target),
            layer_name=cm.map.layer.mincost,
            colormap=cp.cmp_mincost,
            fit_bounds=False,
        )
        self.map.add_raster(
            image=cs.get_ce(self.model.iso, self.model.target, self.model.weight),
            layer_name=cm.map.layer.ce,
            colormap=cp.cmp_ce,
            fit_bounds=False,
        )
        self.map.add_raster(
            image=cs.get_mb(self.model.iso, self.model.target, self.model.weight),
            layer_name=cm.map.layer.mb,
            colormap=cp.cmp_mb,
            fit_bounds=False,
        )

        # add the selected wieght to the download list
        self.download_tile.add_weight(self.model.weight)
        self.download_tile.add_target(self.model.target)

        return
