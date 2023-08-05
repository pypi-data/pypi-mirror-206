from dataclasses import dataclass
from typing import Optional


@dataclass
class StakeholderData:
    instrument: str
    relationship_type: str
    related_organization_id: str
    value_chains_relationship_confidence_score: str
    value_chain_relationship_freshness_score: str
    value_chains_relationship_update_date: str
    document_title: Optional[str] = None
    ric: Optional[str] = None
    issue_isin: Optional[str] = None
    sedol: Optional[str] = None

    @classmethod
    def from_list(cls, datum: list) -> "StakeholderData":
        return cls(
            instrument=datum[0],
            relationship_type=datum[1],
            related_organization_id=datum[2],
            value_chains_relationship_confidence_score=datum[4],
            value_chain_relationship_freshness_score=datum[5],
            value_chains_relationship_update_date=datum[6],
        )

    def update(self, datum: dict):
        self.document_title = datum.get("DocumentTitle")
        self.ric = datum.get("RIC")
        self.issue_isin = datum.get("IssueISIN")
        self.sedol = datum.get("SEDOL")


class Customer(StakeholderData):
    pass


class Supplier(StakeholderData):
    pass
