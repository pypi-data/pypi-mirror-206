from enum import Enum


class SystemImage(Enum):
    """System image.

    .. note::

        Use :meth:`pawapi.api.System.get_current_image()` to get list of
        available system images.

    See: https://help.pythonanywhere.com/pages/ChangingSystemImage/
    """

    DANGERMOUSE = "dangermouse"
    EARLGREY = "earlgrey"
    FISHNCHIPS = "fishnchips"
    GLASTONBURY = "glastonbury"
    HAGGIS = "haggis"
