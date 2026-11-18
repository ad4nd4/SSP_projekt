import argparse

from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel, info
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.topo import Topo


class FirewallTopo(Topo):
    def build(self, bw=100):
        s1 = self.addSwitch("s1", protocols="OpenFlow13")
        s2 = self.addSwitch("s2", protocols="OpenFlow13")

        h1 = self.addHost("h1", ip="10.0.0.1/24", mac="00:00:00:00:00:01")
        h2 = self.addHost("h2", ip="10.0.0.2/24", mac="00:00:00:00:00:02")
        atk = self.addHost("atk", ip="10.0.0.66/24", mac="00:00:00:00:00:66")
        srv = self.addHost("srv", ip="10.0.0.100/24", mac="00:00:00:00:01:00")

        for h in (h1, h2, atk):
            self.addLink(h, s1, bw=bw)

        self.addLink(s1, s2, bw=bw)
        self.addLink(srv, s2, bw=bw)

def run(args):
    net = Mininet(
        topo=FirewallTopo(bw=args.bw),
        switch=OVSKernelSwitch,
        controller=None,
        link=TCLink,
        autoSetMacs=False,
    )

    net.addController(
        "c0", controller=RemoteController, ip=args.ctrl_ip, port=args.ctrl_port
    )

    net.start()

    srv = net.get("srv")

    srv.cmd("python3 -m http.server 80 --directory /tmp > /tmp/srv_http.log 2>&1 &")
    srv.cmd("iperf -s > /tmp/srv_iperf.log 2>&1 &")

    CLI(net)

    srv.cmd("kill %python3 %iperf")
    net.stop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--bw", type=int, default=10, help="bandwidth [Mbps], default is 10")
    parser.add_argument("--ctrl-ip", default="127.0.0.1", help="controller ip addr, default is 127.0.0.1")
    parser.add_argument("--ctrl-port", type=int, default=6653, help="controller port, default is 6653")

    setLogLevel("info")
    run(parser.parse_args())
