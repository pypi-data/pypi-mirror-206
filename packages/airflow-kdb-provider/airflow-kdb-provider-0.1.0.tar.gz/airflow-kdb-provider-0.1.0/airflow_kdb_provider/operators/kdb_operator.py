from airflow.models import BaseOperator
from qpython import qconnection

class KdbOperator(BaseOperator):

    def __init__(
            self,
            command,
            host='localhost',
            port=12345,
            username=None,
            password=None,
            timeout=None,
            *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.command = command
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.timeout = timeout

    def execute(self, context):
        conn = qconnection.QConnection(host=self.host, port=self.port,
                                        username=self.username, password=self.password)
        conn.open()
        result = conn(self.command, timeout=self.timeout)
        self.log.info(result)
        conn.close()