from dataclasses import dataclass
from whitetower.types.image import Image


@dataclass
class AppImageInfo:
    current_image: Image
    '''Image version, which is currently being run'''

    latest_known_image: Image = None
    '''Most recent application image version, which we saw in the repository'''

    skip_latest_known_image: bool = False
    '''If True, then we are not going to use current latest_known_image for application update'''
