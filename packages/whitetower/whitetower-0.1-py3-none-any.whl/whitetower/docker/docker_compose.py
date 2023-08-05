import copy
import time
from typing import Dict
from subprocess import Popen, PIPE, STDOUT
import yaml

from whitetower.types.image import Image

class DockerCompose:
    def __init__(self, docker_compose_template_file_name: str):
        self.docker_compose_template_file_name = docker_compose_template_file_name
        with open(docker_compose_template_file_name, "r") as f:
            try:
                self.data = yaml.safe_load(f)
            except yaml.YAMLError as exc:
                print(exc)

        if "services" in self.data:
            services = self.data["services"]
            self.apps = {}
            for s in services:
                self.apps[s] = services[s]["image"].split(":")[0]

    def get_applications(self) -> Dict[str, str]:
        return self.apps
    
    def run(self, project_name: str, application_images: Dict[str, Image]):
        data = copy.deepcopy(self.data)
        if "services" in data:
            services = data["services"]
            for s in services:
                if s in application_images:
                    services[s]["image"] = str(application_images[s])

        docker_compose_data = yaml.dump(data)

        p = Popen([ "docker-compose", "-f", "-", "-p", project_name, "up", "-d" ], stdin=PIPE)
        stdout_data = p.communicate(input=docker_compose_data.encode("utf-8"))[0]
        time.sleep(5)
        print(stdout_data)