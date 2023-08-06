from __future__ import annotations
from typing import List, Optional
import jsonpickle
from dataclasses import dataclass

from landingzone_organization.filtering import match_workload_pattern
from landingzone_organization.account import Account
from landingzone_organization.organization_unit import OrganizationUnit
from landingzone_organization.workloads import Workloads


@dataclass
class Organization:
    """
    Understands the organization structure
    """

    id: str
    unit: OrganizationUnit

    @property
    def all_accounts(self) -> List[Account]:
        return self.unit.accounts_recursive

    def by_name(self, name: str) -> OrganizationUnit:
        return self.unit.by_name(name)

    def by_account_id(self, account_id: str) -> Optional[Account]:
        return next(filter(lambda account: account.account_id == account_id, self.all_accounts), None)  # type: ignore

    def __resolve_organization_unit(
        self, ou_names: List[str]
    ) -> Optional[OrganizationUnit]:
        unit = self.unit

        for ou_name in ou_names:
            unit = unit.by_name(ou_name)

            if not unit:
                break

        return unit

    def accounts(self, ou_names: List[str] = []) -> List[Account]:
        unit = self.__resolve_organization_unit(ou_names) or self.unit
        return unit.accounts_recursive

    def workloads(self, ou_names: List[str]) -> Optional[Workloads]:
        workloads = Workloads(workloads=[])
        unit = self.unit

        if len(ou_names) > 0:
            unit = self.__resolve_organization_unit(ou_names)

        if unit:
            for account in unit.accounts_recursive:
                if match_workload_pattern(account.name):
                    workloads.resolve_account(account)

        return workloads

    @property
    def platform_accounts(self) -> List[Account]:
        workload_accounts = self.workloads(ou_names=[]).accounts
        workload_account_ids = list(
            map(lambda account: account.account_id, workload_accounts)
        )

        def not_a_workload_account(account: Account):
            return account.account_id not in workload_account_ids

        return list(filter(not_a_workload_account, self.all_accounts))

    def dump(self) -> str:
        return jsonpickle.encode(self)

    @staticmethod
    def load(data: str) -> Organization:
        obj = jsonpickle.decode(data)

        if not isinstance(obj, Organization):
            raise Exception("The given data is not valid Organization data")

        return obj
