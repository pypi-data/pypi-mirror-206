from dbt.events import AdapterLogger
from dbt.adapters.postgres.connections import PostgresCredentials, PostgresConnectionManager

logger = AdapterLogger("Greenplum")


class GreenplumCredentials(PostgresCredentials):

    @property
    def type(self):
        return "greenplum"


class GreenplumConnectionManager(PostgresConnectionManager):
    TYPE = 'greenplum'
