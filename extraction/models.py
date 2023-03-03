import os
import logging
import peewee as pw
import psycopg2

logger = logging.getLogger(__name__)

connection_details = dict(
    user=os.environ.get("POSTGRES_USER", "postgres"),
    password=os.environ.get("POSTGRES_PASSWORD", "postgres"),
    host=os.environ.get("POSTGRES_HOST", "localhost"),
    port=int(os.environ.get("POSTGRES_PORT", 5432)),
)
logger.info("Postgres connection:\n%s", connection_details)
logging.basicConfig(level=logging.INFO)

db = pw.PostgresqlDatabase("postgres", **connection_details)
conn = psycopg2.connect(**connection_details, database='postgres')


class Extractions(pw.Model):
    table = pw.TextField()
    extracted_at = pw.DateTimeField()

    class Meta:
        database = db
        schema = 'extractor'


logger.info("connecting to postgres")


def init():
    db.connect()

    with conn.cursor() as cursor:
        cursor.execute("create schema if not exists extractor;")
        conn.commit()
    # todo: pewee db.create_tables


init()
