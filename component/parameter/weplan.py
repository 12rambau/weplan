import matplotlib as mpl

nb_target = 5
"the number of target category existing in weplan forest"

nb_weight = 10
"the number of relative weight between cabon and biodiversity objectives"

version = "v002"
"name of the weplan output version use in the file naming"

cmp_available = mpl.cm.Greens
"the colormap for the available datasets"

cmp_mincost = mpl.cm.Purples
"the colormap for the mincost datasets"

cmp_ce = mpl.cm.Blues
"the colormap for the cost-effectiveness datasets"

cmp_mb = mpl.cm.Oranges
"the colormap for the max benefits datasets"

f_available = "available_{}.tif"
"name of the available file in the AWS bucket"

f_mincost = "scen_mincost_target_{}_{}.tif"
"name of the micost files in the AWS bucket"

f_ce = "scen_tradeoffs_ce_target_{}_weight_{}_{}.tif"
"name of the ce files in the AWS bucket"

f_mb = "scen_tradeoffs_mb_target_{}_weight_{}_{}.tif"
"name of the mb files in the AWS bucket"
