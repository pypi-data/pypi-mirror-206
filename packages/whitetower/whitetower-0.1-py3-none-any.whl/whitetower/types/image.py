from dataclasses import dataclass


@dataclass 
class Image:
    image_name: str
    version: int = -1

    def __repr__(self):
        return f"{self.image_name}:{self.version}"
    
    def __eq__(self, other: 'Image'):
        if not self and not other:
            return True
        if not self or not other:
            return False
        return self.image_name == other.image_name and self.version == other.version