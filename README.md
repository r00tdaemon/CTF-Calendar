# CTF-Calendar
Python script to fetch upcoming CTF competitions and add them to your google calendar. Made with python 3.5.1
## Requirments
* BeautifulSoup

## Steps to use
#### Step 1: Turn on the Google Calendar API
*  Use [this wizard](https://console.developers.google.com/start/api?id=calendar) to create or select a project in the Google Developers Console and automatically turn on the API. Click Continue, then Go to credentials.
*  On the Add credentials to your project page, click the Cancel button.
*  At the top of the page, select the OAuth consent screen tab. Select an Email address, enter Product name as CTFcalendar, and click the Save button.
*  Select the Credentials tab, click the Create credentials button and select OAuth client ID.
*  Select the application type Other, enter the name "CTFcalendar", and click the Create button.
*  Click OK to dismiss the resulting dialog.
*  Click the file_download (Download JSON) button to the right of the client ID.
*  Move this file to your working directory and rename it client_secret.json.

#### Step 2: Install the Google Client Library
* Run the following command to install the library using pip:
`$ pip install --upgrade google-api-python-client`

#### Step 3: Run the script
* `$ python Calendar.py`
* The script will attempt to open a new window or tab in your default browser. If this fails, copy the URL from the console and manually open it in your browser.
* If you are not already logged into your Google account, you will be prompted to log in. If you are logged into multiple Google accounts, you will be asked to select one account to use for the authorization.
* Click the Accept button.
* The script will proceed automatically, and you may close the window/tab.
