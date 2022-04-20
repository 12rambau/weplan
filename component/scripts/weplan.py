import zipfile
import requests
from io import BytesIO

from component import parameter as cp


def extract_all(iso):
    """
    extract all the tif layer from an iso code to the tmp directory

    Args:
        iso (str): the iso code of the country
    """

    # check if the folder already exist
    iso_tmp_folder = cp.tmp_dir / f"{iso}_{cp.version}"
    if iso_tmp_folder.is_dir():
        return

    # extract all the content of the zip file in iso_tmp_folder
    url = f"https://iisau-weplan.s3.eu-west-1.amazonaws.com/weplan_data/{iso}_{cp.version}.zip"
    with zipfile.ZipFile(BytesIO(requests.get(url).content)) as f:
        f.extractall(cp.tmp_dir)

    return


def get_available(iso):
    """
    return the path to the available image

    Args:
        iso (str): the iso code of the country

    Return:
        (path): the path to the tif image
    """
    dir_ = cp.tmp_dir / f"{iso}_{cp.version}"
    filename = f"available_{cp.version}.tif"

    return dir_ / filename


def get_mincost(iso, target):
    """
    return the path to the mincost scenario

    Args:
        iso (str): the iso code of the country
        target (int): number of the target scenario

    Return:
        (path): the path to the tif image
    """

    dir_ = cp.tmp_dir / f"{iso}_{cp.version}"
    filename = f"scen_mincost_target_{target}_{cp.version}.tif"

    return dir_ / filename


def get_ce(iso, target, weight):
    """
    return the path to the cost effectivness scenario

    Args:
        iso (str): the iso code of the country
        target (int): number of the target scenario
        weight (int): order of the weight between carbon and biodiversity objectives

    return:
        (path): the path to the tif image
    """

    dir_ = cp.tmp_dir / f"{iso}_{cp.version}"
    filename = f"scen_tradeoffs_ce_target_{target}_weight_{weight}_{cp.version}.tif"

    return dir_ / filename


def get_mb(iso, target, weight):
    """
    return the path to the max benefits scenario

    Args:
        iso (str): the iso code of the country
        target (int): number of the target scenario
        weight (int): order of the weight between carbon and biodiversity objectives

    return:
        (path): the path to the tif image
    """

    dir_ = cp.tmp_dir / f"{iso}_{cp.version}"
    filename = f"scen_tradeoffs_mb_target_{target}_weight_{weight}_{cp.version}.tif"

    return dir_ / filename
