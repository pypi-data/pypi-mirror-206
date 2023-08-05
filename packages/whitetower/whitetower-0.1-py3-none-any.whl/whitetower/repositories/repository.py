class Repository:
    def get_latest_version(self, image_name: str) -> int:
        '''Returns latest numeric version by checking the :latest tag'''
        raise Exception("Abstract")