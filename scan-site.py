#!/usr/bin/python
import sys
from zapScanner.scannerWrapper import ScannerWrapper

def main(argv):
    if len(argv) < 4:
        print("Please pass all arguments \n \n Example: \n python scan-site.py <ApiKey> <TargetUrlsFile> <ProxyUrl>")
        return 1

    urlsToAttack = open(argv[2], "r")
    scanner = ScannerWrapper(apiKey=argv[1], zapProxyUrl=argv[3])

    for url in urlsToAttack:
        scanner.spiderAndScan(url)
        scanner.printResults("testing.html")


if __name__ == "__main__":
    main(sys.argv)