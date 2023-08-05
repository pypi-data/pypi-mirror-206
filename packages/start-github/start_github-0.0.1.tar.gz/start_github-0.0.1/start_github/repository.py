from dataclasses import dataclass, field, fields

from .main import Github

gh = Github()


@dataclass
class Topic:
    name: str


@dataclass
class Owner:
    login: str
    avatar_url: str
    gravatar_id: str

    @classmethod
    def from_github_data(cls, data: dict):
        if (own := data.get("owner")) and isinstance(own, dict):
            keys = [k.name for k in fields(cls)]
            return cls(**{k: v for k, v in own.items() if k in keys})
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
