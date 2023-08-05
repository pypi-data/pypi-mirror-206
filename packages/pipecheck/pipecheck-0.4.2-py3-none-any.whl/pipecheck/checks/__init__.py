from pipecheck.checks.dns import DnsProbe
from pipecheck.checks.http import HttpProbe
from pipecheck.checks.icmp import PingProbe
from pipecheck.checks.mysql import MysqlProbe
from pipecheck.checks.tcp import TcpProbe

probes = {}

for cls in [HttpProbe, DnsProbe, PingProbe, TcpProbe, MysqlProbe]:
    probes[cls.get_type()] = cls
