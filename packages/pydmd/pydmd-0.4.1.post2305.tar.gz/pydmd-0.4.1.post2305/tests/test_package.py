import pkgutil
from os import walk
from os import path


def test_import_dm_1():
    import pydmd as dm

    dmd = dm.dmd.DMDBase()


def test_import_dm_2():
    import pydmd as dm

    dmd = dm.dmd.DMD()


def test_import_dm_3():
    import pydmd as dm

    dmd = dm.fbdmd.FbDMD()
