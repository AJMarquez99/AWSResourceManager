import os
from github import Github

class SecretManager:

    def __init__(self, github_token):
        self.github = Github(github_token)
        self.repo = self.github.get_repo(os.environ['GITHUB_REPOSITORY'])

    def get_secret(self, secret_name):
        try:
            return self.repo.get_secret(secret_name).value
        except Exception as e:
            print(f"Error retrieving secret {secret_name}: {e}")
            return None