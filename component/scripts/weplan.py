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
    iso_tmp_folder = cp.tmp_dir / iso
    if iso_tmp_folder.is_dir():
        return

    # extract all the content of the zip file in iso_tmp_folder
    iso_tmp_folder.mkdir()
    url = f"https://iisau-weplan.s3.eu-west-1.amazonaws.com/weplan_data/{iso}_v002.zip"
    with zipfile.ZipFile(BytesIO(requests.get(url).content)) as f:
        f.extractall(iso_tmp_folder)

    return


def get_available(iso):
    """
    return the path to the available image

    Args:
        iso (str): the iso code of the country

    Return:
        (path): the path to the tif image
    """

    return


def get_mincost(iso, target):
    """
    return the path to the mincost scenario

    Args:
        iso (str): the iso code of the country
        target (int): number of the target scenario

    Return:
        (path): the path to the tif image
    """

    return


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

    return


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

    return
