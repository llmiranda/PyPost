# PyPost
Automatic photo post on instagram

The idea is automate a task wich my wife takes one hour every day to do it manualy.

In this project we will do all configuration and code to
* Check an email address
* Download photos 
* Look for Instagram of someone in a Google Sheet
* Post the downloaded photos on instagram.

UNTIL NOW
The project can access the email, save the anex, move anex to a specif path and find the instragam of that person.

----------------------------------------------------------------------------------------------
--------------------------------Configuration steps-------------------------------------------
----------------------------------------------------------------------------------------------
* Grant access on gmail account
  - Go to "Manage your google account"
  - Security
  - Activate 2-step verification if not
  - Go to "How you login on Google"
  - Click on "2 step verification"
  - App Passwords
  - Choose others, put the name you want and click Generate
  - Copy the password. We will use it soon.
    - Very important. DO NOT SHARE this password on internet. If you do, people can access and use your email.

* Grant access to Google Sheets
  - Go to google and find for "Google Developer Console" (https://console.cloud.google.com/)
  - Create a new project
  - Find for "Google Drive API", select and Activate.
  - Find for "Google Sheets API", select and Activate.
  - Go to "Navigation Menu > API and Services > OAuth Permitions"
  - User Type = External - Create
  - Fill the information required (app name, email and developer email), then Save
  - Save again
  - Save again
  - Back to panel
  - Menu Credentials
  - Create Credentials > Client OAuth ID
  - Choose "Personal Computer App" and Create
  - Download JSON file and copy to your project path and rename it to "client_secret.json" (do not share this JSON file on internet)
  
----------------------------------------------------------------------------------------------
------------------------------------------Libs Used-------------------------------------------
----------------------------------------------------------------------------------------------
imap_tools
os
googlesheets api (pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib) -- https://developers.google.com/sheets/api/quickstart/python?hl=pt-br