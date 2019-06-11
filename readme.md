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
4. Active the virtual env by running the activation script
```powershell
.\venv\scripts\activate
```
5. Install all of the required modules into the virtualenv
```powershell
pip install -r requirements.txt
```