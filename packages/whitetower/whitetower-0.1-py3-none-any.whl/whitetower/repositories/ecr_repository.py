import boto3
import re
from whitetower.repository import Repository

class EcrRepository(Repository):
    def __init__(self, aws_account_id, aws_account_secret, aws_region):
        self.aws_args = { 
            "aws_access_key_id": aws_account_id, 
            "aws_secret_access_key": aws_account_secret, 
            "region_name": aws_region
        }
        self.__login()
    
    def __login(self):
        self.client = boto3.client('ecr', **self.aws_args)

    def get_latest_version(self, image_name: str) -> int:
        # Check if image_name is Docker URL instead of ECR repo name
        # Keep only ECR repo name if so
        m = re.match(r"[0-9]+\.dkr\.ecr\.[a-z0-9-]+\.amazonaws\.com/([^:]+)", image_name)
        if m:
            image_name = m.groups(1)[0]

        response = self.client.describe_images(repositoryName=image_name, imageIds=[{ 'imageTag': 'latest'}])
        if response and "imageDetails" in response:
            for image in response["imageDetails"]:
                if "imageTags" in image:
                    found = False
                    for tag in image["imageTags"]:
                        if tag != "latest":
                            try:
                                num = int(tag)
                                found = True
                            except:
                                pass
                    if found:
                        return num
        return None