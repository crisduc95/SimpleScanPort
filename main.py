from scanhosts import ScanHost
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple scan port")
    parser.add_argument("--t", type=str, required=True, help="IP target")
    parser.add_argument("--p", type=int,nargs=2,required=False,default=[1-1024], help="range of ports default[1-1024]")
    parser.add_argument("--s", action="store_true", help="scan single port")

    args = parser.parse_args()
    ip = args.t
    port_range = args.p
    single_port_scan = args.s

    scan = ScanHost(ip=ip, portI=port_range[0], portF=port_range[1])

    if single_port_scan:
        scan.singleScan()
    else:
        scan.muestra()

