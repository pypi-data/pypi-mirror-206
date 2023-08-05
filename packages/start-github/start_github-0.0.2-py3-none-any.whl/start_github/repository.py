from dataclasses import asdict, dataclass, field

from .main import Github

gh = Github()


@dataclass
class Topic:
    name: str


@dataclass
class Owner:
    name: str
    github_id: str
    gravatar_id: str | None = None

    @classmethod
    def from_github_data(cls, data: dict):
        if (own := data.get("owner")) and isinstance(own, dict):
            return cls(
                name=own["login"],
                github_id=own["id"],
                gravatar_id=own["gravatar_id"] or None,
            )
        return None


FIELDS = [
    "created_at",
    "updated_at",
    "pushed_at",
    "stargazers_count",
    "description",
]  # extendible collection of fields that user may be interested in collecting


@dataclass
class Repo:
    owner: str
    repo: str
    key: str | None = None
    owner_data: Owner | None = None
    topics_list: list[Topic] = field(default_factory=list)
    columns: dict = field(default_factory=dict)

    def __post_init__(self):
        """Uses the json model described in the docs to extract relevant fields
        from the repo."""
        dump = gh.get_repo_data(owner=self.owner, repo=self.repo).json()
        self.key = dump.get("license") and dump["license"].get("key")
        self.owner_data = Owner.from_github_data(dump)
        self.topics_list = [Topic(name=name) for name in dump.get("topics")]
        self.columns = {k: v for k, v in dump.items() if k in FIELDS}

    @property
    def repo_data(self) -> dict:
        base = {
            "name": self.repo,
            "owner": self.owner,
            "key": self.key,
        }
        return base | self.columns

    @property
    def export_data(self) -> dict:
        return {
            "repo": self.repo_data,
            "person": asdict(self.owner_data) if self.owner_data else {},
            "topics": [t.name for t in self.topics_list],
        }

    @classmethod
    def export(cls, url: str):
        if gh := Github.url_has_owner_repo(url):
            return cls(owner=gh["owner"], repo=gh["repo"]).export_data
