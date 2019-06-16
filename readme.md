# Installation
## Windows
1. Install Python 3.7
2. Install 'virtualenv' using the following command
```powershell
pip install virtualenv
```
3. Create a virtualenv in the './venv' folder using the following command
```powershell
python -m venv ./venv
```
4. Activate the virtual env by running the activation script
```powershell
.\venv\scripts\activate
```
5. Install all of the required modules into the virtualenv
```powershell
pip install -r requirements.txt
```
# Usage
To use the command line tool, open up a shell/cmd window, and enter the following command
```powershell
python scan-site.py <ApiKey> <TargetUrlsFile> <ProxyUrl>
```

Where:
* ApiKey is the api key to the OWASP ZAP API.
* TargetUrlsFile is a file containing a valid URL per line.
* ProxyUrl is the IP or hostname of the OWASP ZAP proxy (defaults to http://localhost:8080/)