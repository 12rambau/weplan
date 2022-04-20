from sepal_ui import sepalwidgets as sw

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
        self.aoi_tile.view.observe(self._update_map, "updated")

    def _update_map(self, change):

        # clean the map from the different layers
        self.map.remove_layername(cm.map.layer.available)
        self.map.remove_layername(cm.map.layer.mincost)
        self.map.remove_layername(cm.map.layer.ce)
        self.map.remove_layername(cm.map.layer.mb)

        # it's impossible to have missing parameters here
        # as none of the field are clearable
        # I'll add some tests if I'm wrong

        # download all the maps if needed
        cs.extract_all(self.model.iso)

        # add the appropriate layers on the map
        self.map.add_raster(
            image=cs.get_available(self.model.iso),
            layer_name=cm.map.layer.available,
            colormap=cp.cmp_available,
            fit_bounds=False,
            colorbar_position=False,
        )
        self.map.add_raster(
            image=cs.get_mincost(self.model.iso, self.model.target),
            layer_name=cm.map.layer.mincost,
            colormap=cp.cmp_mincost,
            fit_bounds=False,
            colorbar_position=False,
        )
        self.map.add_raster(
            image=cs.get_ce(self.model.iso, self.model.target, self.model.weight),
            layer_name=cm.map.layer.ce,
            colormap=cp.cmp_ce,
            fit_bounds=False,
            colorbar_position=False,
        )
        self.map.add_raster(
            image=cs.get_mb(self.model.iso, self.model.target, self.model.weight),
            layer_name=cm.map.layer.mb,
            colormap=cp.cmp_mb,
            fit_bounds=False,
            colorbar_position=False,
        )

        return
