import re
from http import HTTPStatus
from urllib.parse import urlparse

import httpx
from pydantic import BaseSettings, Field

REPO_PATTERN = re.compile(r"^\/(?P<owner>.*)\/(?P<repo>.*)$")

BASE = "https://api.github.com/repos"
OG = "https://opengraph.githubassets.com"


class Github(BaseSettings):
    token: str = Field(
        default=...,
        repr=False,
        env="GH_TOKEN",
    )
    version: str = Field(
        default="2022-11-28",
        repr=False,
        env="GH_TOKEN_VERSION",
    )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    def get(
        self,
        url: str,
        media_type: str | None = ".raw",
        params: dict = {},
    ) -> httpx.Response:
        """See requisite [headers](https://docs.github.com/en/rest/repos/contents?apiVersion=2022-11-28#get-repository-content--code-samples)

        Args:
            url (str): _description_
            media_type (str | None, optional): _description_. Defaults to ".raw".
            params (dict, optional): _description_. Defaults to {}.

        Returns:
            httpx.Response: _description_
        """  # noqa: E501
        with httpx.Client(timeout=120) as client:
            return client.get(
                url,
                params=params,
                headers={
                    "Accept": f"application/vnd.github{media_type}",
                    "Authorization": f"token {self.token}",
                    "X-GitHub-Api-Version": self.version,
                },
            )

    @classmethod
    def url_has_owner_repo(cls, url: str) -> dict[str, str] | None:
        """If the target `url` matches pattern for extracting an owner and repo from
        the path, extract them as a dict.

        Examples:
            >>> target_url = "https://github.com/justmars/start-github"
            >>> Github.url_has_owner_repo(target_url)
            {'owner': 'justmars', 'repo': 'start-github'}

        Args:
            url (str): The target url to extract from the owner and repo from

        Returns:
            dict[str, str]: Contains the keys from the path for `owner` and `repo`
        """
        p = urlparse(url)
        if p.netloc == "github.com" and p.path and p.path != "/":
            if match := REPO_PATTERN.search(p.path):
                return match.groupdict()

    def get_repo(self, owner: str, repo: str) -> httpx.Response:
        """See Github API [docs](https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#get-a-repository)"""  # noqa: E501
        return self.get(f"{BASE}/{owner}/{repo}")

    def get_repo_data(self, owner: str, repo: str) -> httpx.Response:
        res = self.get_repo(owner=owner, repo=repo)
        if res.status_code != HTTPStatus.OK:
            raise Exception(f"Fail github: {owner=} {repo=}")
        return res

    def get_repo_commits(self, owner: str, repo: str) -> httpx.Response:
        """See Github API [docs](https://docs.github.com/en/rest/commits/commits?apiVersion=2022-11-28)"""  # noqa: E501
        return self.get(f"{BASE}/{owner}/{repo}/commits")

    def get_latest_sha(self, owner: str, repo: str) -> str:
        """See Github API [docs](https://docs.github.com/en/rest/commits/commits?apiVersion=2022-11-28#get-a-commit)"""  # noqa: E501
        commits_response = self.get_repo_commits(owner, repo)
        return commits_response.json()[0]["sha"]

    def get_latest_og_img_url(self, author: str, repo: str) -> str:
        """See [Stackoverflow](https://stackoverflow.com/a/71454181)"""
        return f"{OG}/{self.get_latest_sha(author, repo)}/{author}/{repo}"
