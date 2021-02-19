"""
InfluxAlchemy Client.
"""
from aioinfluxalchemy import query
from aioinfluxalchemy.measurement import Measurement


class AioInfluxAlchemy:
    """
    InfluxAlchemy database session.

    client (InfluxDBClient):  Connection to InfluxDB database
    """
    def __init__(self, client):
        self.bind = client
        # pylint: disable=protected-access
        assert self.bind.db is not None, \
            "InfluxDB client database cannot be None"

    def query(self, *entities):
        """
        Query InfluxDB entities. Entities are either Measurements or
        Tags/Fields.
        """
        return query.AioInfluxDBQuery(entities, self)

    async def measurements(self):
        """
        Get measurements of an InfluxDB.
        """
        mes = await self.bind.query("SHOW MEASUREMENTS;")
        pts = [Measurement.new(elem[0]) for elem in mes['results'][0]['series'][0]['values']]
        return pts

    async def tags(self, measurement):
        """
        Get tags of a measurements in InfluxDB.
        """
        tags = await self.bind.query('SHOW tag keys FROM %s ' % measurement)
        pts = sorted(elem[0] for elem in tags['results'][0]['series'][0]['values'])
        return pts

    async def fields(self, measurement):
        """
        Get fields of a measurements in InfluxDB.
        """
        fields = await self.bind.query("SHOW field keys FROM %s" % measurement)
        pts = sorted(sorted(elem[0] for elem in fields['results'][0]['series'][0]['values']))
        return pts
