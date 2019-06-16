#!/usr/bin/python
import sys, getopt, time
from zapv2 import ZAPv2

class ScannerWrapper:
    def __init__(self, apiKey, zapProxyUrl):
        self.zapApi = ZAPv2(apikey=apiKey, proxies={'http': zapProxyUrl})
    
    def spider(self, url):
        print('Spidering target {}'.format(url))
        scanid = self.zapApi.spider.scan(url)
        # Give the Spider a chance to start
        time.sleep(2)

        while (int(self.zapApi.spider.status(scanid)) < 100):
            print('Spider progress %: {}'.format(self.zapApi.spider.status(scanid)))
            # Loop until the spider has finished
            time.sleep(2)
        
        print ('Spider completed')

    def passiveScan(self,url):
        print ('Passive Scanning target {}'.format(url))
        # Passive scan all endpoints
        while (int(self.zapApi.pscan.records_to_scan) > 0):
            print ('Records to passive scan : {}'.format(self.zapApi.pscan.records_to_scan))
            time.sleep(2)
        print ('Passive Scan completed')

    def activeScan(self, url):
        # Active scan all endpoints
        print ('Active Scanning target {}'.format(url))
        scanid = self.zapApi.ascan.scan(url)
        while (int(self.zapApi.ascan.status(scanid)) < 100):
            # Loop until the scanner has finished
            print ('Scan progress %: {}'.format(self.zapApi.ascan.status(scanid)))
            time.sleep(5)
        print ('Active Scan completed')

    def spiderAndScan(self, url):
        self.spider(url)
        self.activeScan(url)
        self.passiveScan(url)

    def printResults(self, filename):
        # Print results
        print ('Hosts: {}'.format(', '.join(self.zapApi.core.hosts)))
        resultsFile = open(filename, "w+")
        resultsFile.write(self.zapApi.core.htmlreport())