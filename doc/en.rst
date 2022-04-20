weplan
======

Forest Restoration Planning

Overview 
--------

WePlan - Forests is a decision support platform for tropical and subtropical forest ecosystem restoration planning that aims to maximise the climate change mitigation, biodiversity conservation and poverty alleviation benefits arising from forest restoration.

The project provides quantitative, spatial, evidence-based planning support to developing countries that are party to the Convention on Biological Diversity in order to facilitate the realisation of forest restoration pledges and targets.

WePlan - Forests is a spatially explicit, forest restoration planning tool that evaluates a range of alternative scenarios, reporting the benefits, costs and spatial distribution of restoration priorities for each one. It considers two objectives: (i) climate change mitigation benefit, estimated as the change in carbon sequestration that would arise from forest restoration, and (ii) biodiversity conservation benefit, estimated as the average reduction in local (national) extinction risk among all forest-associated species. The analysis also considers opportunity and implementation costs of forest restoration. Analyses occur at a 1 km2 resolution on a national basis, for countries containing tropical and subtropical forests within +/- 25 degrees latitude.

The platform consists of a user-friendly SEPAL-based interface to retreive the Geospatial data from each computed scenarios from the weplan forest project. 

More information about the computation and statical data can be found on the `weplan forest platform website <http://weplan-forests.org>`__

Usage
-----

.. warning::

    This application is a prototype, data are provided for Uganda only.

Output
------

The output will be found in the user SEPAL files under :code:`module_results/weplan/<iso_code>` with :code:`iso_code` being the `ISO 3166-1 alpha-3 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3>`__ code of the downloaded country (e.g. "UGA" for Uganda).

Every file is using the :code:`.tif` format with one single band expressing the variable described. and will display the version of the weplan-forest computation, here "v002", called :code:`<version>` from now on.

Planning solutions were developed for five area targets, representing 10, 20, 30, 40, and 50% of the area available for forest restoration.

The application will retreive 4 types of analysis from the weplan forest project: 

-   :code:`available_<version>.tif`: the raster of the proportion of each cell deemed available for forest restoration within the seleted country.
-   :code:`scen_mincost_target_<X>_<version>.tif`: the minimum cost scenarios. These rasters are the optimal reference solutions that minimise total costs, ignoring benefits where :code:`<X>` is an integer referring to the target category.
-   :code:`scen_tradeoffs_ce_target_<X>_weight_<Y>_<version>.tif`: cost-effectiveness scenarios. These rasters are the optimal solutions that maximise cost-effectiveness (benefit / cost) where :code:`X` is an integer referring to the target category and :code:`Y` is an integer referring to the order of relative weights between carbon and biodiversity objectives.
-   :code:`scen_tradeoffs_mb_target_<X>_weight_<Y>_<version>.tif`: max-benefit scenarios. These raster are the optimal solutions that maximise benefit, ignoring costs where :code:`X` is an integer referring to the target category and :code:`Y` is an integer referring to the order of relative weights between carbon and biodiversity objectives.

for more information about the computation metodology, please refer to the `weplan-forest website <http://www.weplan-forests.org/flrp/choose.php>`__.