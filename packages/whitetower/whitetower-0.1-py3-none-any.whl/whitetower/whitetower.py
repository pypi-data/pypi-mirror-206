import time
from typing import Dict
from whitetower.types.app_image_info import AppImageInfo
from whitetower.callbacks import Callbacks
from whitetower.types.image import Image
from whitetower.types.update_decision import UpdateDecision
from whitetower.docker.docker_compose import DockerCompose
from whitetower.repositories.repository import Repository


class WhiteTower:
    def __init__(self, docker_compose: DockerCompose, image_repository: Repository, callbacks: Callbacks):
        self.docker_compose = docker_compose
        self.image_repository = image_repository
        self.callbacks = callbacks

    def get_current_image(self, image_name: str) -> Image:
        result = Image(image_name)
        ver = self.callbacks.get_local_version(image_name)
        if ver:
            result.version = ver
        if result.version == -1:
            ver = self.image_repository.get_latest_version(image_name)
            if ver:
                result.version = ver
        return result

    def run(self):
        applications = self.docker_compose.get_applications()
        app_names = list(applications.keys())
        current_images : Dict[str, Image] = dict()

        # Сache image info
        for app in app_names:
            image_name = self.callbacks.get_image_name(app)
            current_images[app] = self.get_current_image(image_name)

        print("Current image versions:")
        for image in current_images:
            print("\t", image, " -> ", f"{current_images[image]}")

        apps: Dict[str, AppImageInfo] = {}
        for image in current_images:
            apps[image] = AppImageInfo(current_images[image], current_images[image])

        # Start applications
        application_images_to_run = { k: v.current_image for (k,v) in apps.items() }
        self.docker_compose.run("app", application_images_to_run)

        # Main loop
        apps_to_update = []
        while True:
            new_apps_to_update = []
            for app_name in apps:
                app = apps[app_name]
                current_image = app.current_image
                if not self.callbacks.on_before_repo_check(app, current_image):
                    print("Callback 'on_before_repo_check' returned False, skipping check of", app)
                    continue

                possibly_new_image_name = self.callbacks.get_image_name(app_name)
                ver = self.image_repository.get_latest_version(possibly_new_image_name)
                new_image = Image(possibly_new_image_name, ver)

                if current_image != new_image and not app_name in apps_to_update and (new_image != app.latest_known_image or not app.skip_latest_known_image):
                    print(f"Found new version of '{app_name}'. Old={current_image}, New={new_image}")
                    app.latest_known_image = new_image
                    app.skip_latest_known_image = False

                    update_decision = self.callbacks.on_new_image_found(app_name, current_image, new_image)
                    if update_decision == UpdateDecision.skip_this_version:
                        print("Callback 'on_new_image_found' returned 'skip_this_version', skipping update of", app)
                        continue

                    if update_decision == UpdateDecision.postpone_update:
                        print("Callback 'on_new_image_found' returned 'postpone_update', so we will check this app again on next iteration", app)
                        continue

                    new_apps_to_update.append(app_name)

            if new_apps_to_update:
                # We save these found apps and run next iteration of checks
                apps_to_update += new_apps_to_update
                print("Updates found. Waiting for another repo check iteration results.")
            elif apps_to_update:
                print("No more updates found. Apply pending updates.")
                
                for app_name in apps_to_update:
                    app = apps[app_name]
                    app.current_image = app.latest_known_image
                    app.latest_known_image = None
                    app.skip_latest_known_image = False

                # Start applications
                application_images_to_run = { k: v.current_image for (k,v) in apps.items() }
                self.docker_compose.run("app", application_images_to_run)

                print(f"Applications {apps_to_update} were restarted")
                apps_to_update.clear()

            time.sleep(10)
