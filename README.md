# PyPost
Automatic photo post on instagram

The idea is automate a task wich my wife takes one hour every day to do it manualy.

In this project we will do all configuration and code to
* Check an email address
* Download photos 
* Post the downloaded photos on instagram.

UNTIL NOW
The project can access the email, save the anex and move anex to a specif path

----------------------------------------------------------------------------------------------
--------------------------------Configuration steps-------------------------------------------
----------------------------------------------------------------------------------------------
* Grant access on gmail account
  - Go to "Manage your google account
  - Security
  - Activate 2-step verification if not
  - Go to "How you login on Google"
  - Click on "2 step verification"
  - App Passwords
  - Choose others, put the name you want and click Generate
  - Copy the password. We will use it soon.
    - Very important. DO NOT SHARE this password on internet. If you do, people can access and use your email.

----------------------------------------------------------------------------------------------
------------------------------------------Libs Used-------------------------------------------
----------------------------------------------------------------------------------------------
imap_tools
os
