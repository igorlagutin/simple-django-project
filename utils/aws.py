import requests


class EC2MetadataGetter:
    EC2_BASE_METADATA_URL = "http://169.254.169.254/latest"
    METADATA_REGION = "placement/region"
    PUBLIC_HOSTNAME = "public-hostname"
    AVAILABILITY_ZONE = "placement/availability-zone"

    def __init__(self):
        self.token = self.get_ec2_metadata_token()

    def get_ec2_metadata_token(self):
        token_url = f"{self.EC2_BASE_METADATA_URL}/api/token"
        headers = {"X-aws-ec2-metadata-token-ttl-seconds": "21600"}
        try:
            response = requests.put(token_url, headers=headers, timeout=5)
            return response.text
        except requests.exceptions.ConnectionError:
            return None

    def get_metadata_by_path(self, path):
        if not self.token:
            return "Not Available"
        base_url = f"{self.EC2_BASE_METADATA_URL}/meta-data/"
        headers = {"X-aws-ec2-metadata-token": self.token}
        response = requests.get(base_url + path, headers=headers, timeout=5)
        return response.text
