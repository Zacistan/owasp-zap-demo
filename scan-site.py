#!/usr/bin/python
import sys, getopt, time
from pprint import pprint
from zapv2 import ZAPv2

def main(argv):
    if len(argv) < 4:
        print("Please pass all arguments \n \n Example: \n python scan-site.py <ApiKey> <TargetUrlsFile> <ProxyUrl>")
        return 1
    
    apiKey = argv[1]
    urlsToAttack = open(argv[2], "r")
    zapProxyUrl = argv[3]
    zapApi = ZAPv2(apikey=apiKey, proxies={'http': zapProxyUrl})
    
    # Spider each URL to determine all endpoints
    for url in urlsToAttack:
        print('Spidering target {}'.format(url))
        # Give the Spider a chance to start
        scanid = zapApi.spider.scan(url)
        time.sleep(2)

        while (int(zapApi.spider.status(scanid)) < 100):
            # Loop until the spider has finished
            print('Spider progress %: {}'.format(zapApi.spider.status(scanid)))
            time.sleep(2)
        print ('Spider completed')

        # Active scan all endpoints
        print ('Active Scanning target {}'.format(url))
        scanid = zapApi.ascan.scan(url)
        while (int(zapApi.ascan.status(scanid)) < 100):
            # Loop until the scanner has finished
            print ('Scan progress %: {}'.format(zapApi.ascan.status(scanid)))
            time.sleep(5)
        print ('Active Scan completed')

    # Passive scan all endpoints
    while (int(zapApi.pscan.records_to_scan) > 0):
        print ('Records to passive scan : {}'.format(zapApi.pscan.records_to_scan))
        time.sleep(2)
    print ('Passive Scan completed')

    # Print results
    print ('Hosts: {}'.format(', '.join(zapApi.core.hosts)))
    resultsFile = open("results.html", "w+")
    resultsFile.write(zapApi.core.htmlreport())


if __name__ == "__main__":
    main(sys.argv)