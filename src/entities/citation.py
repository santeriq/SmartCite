import json

class Citation:
    def __init__(self, citation_type: str, citation_key: str,
                 fields: dict, citation_id: int = None):
        self.id = citation_id
        self.citation_type = citation_type
        self.citation_key = citation_key
        self.fields = fields

    def __str__(self):
        return json.dumps(self.to_dict())

    def to_dict(self):
        """
        Converts the Citation object to a dictionary.
        """
        return {
            "id": self.id,
            "citation_type": self.citation_type,
            "citation_key": self.citation_key,
            "fields": self.fields,
        }
