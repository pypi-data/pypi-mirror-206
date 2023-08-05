from typing import Dict
from whitetower.types.image import Image
from whitetower.types.update_decision import UpdateDecision


class Callbacks:
    def __init__(self, applications: Dict[str, str]):
        self.applications = applications

    def get_image_name(self, app_name: str) -> str | None:
        raise Exception("Abstract")
    
    def get_local_version(self, image_name: str) -> int | None:
        raise Exception("Abstract")

    def on_before_repo_check(self, app_name: str, current_image: Image) -> bool:
        return True

    def on_new_image_found(self, app_name: str, current_image: Image, new_image: Image) -> UpdateDecision:
        return True
