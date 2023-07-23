# Command line for the win

# Requirements
# General
* A README.md file, at the root of the folder of the project, is mandatory
* This project will be manually reviewed.
* As each task is completed, the name of that task will turn green
* Create a screenshot, showing that you completed the required levels
* Push this screenshot with the right name to GitHub, in either the PNG or JPEG format

# Specific
* In addition to completing the project tasks and submitting the required screenshots to GitHub, you are also required to demonstrate the use of the SFTP (Secure File Transfer Protocol) command-line tool to move your local screenshots to the sandbox environment.

# Here are the steps to follow:

* Take the screenshots of the completed levels as mentioned in the general requirements.
* Open a terminal or command prompt on your local machine.
* Use the SFTP command-line tool to establish a connection to the sandbox environment. You will need the hostname, username, and password provided to you for the sandbox environment.
* Once connected, navigate to the directory where you want to upload the screenshots.
* Use the SFTP put command to upload the screenshots from your local machine to the sandbox environment.
* Confirm that the screenshots have been successfully transferred by checking the sandbox directory.
* Once the screenshots are transferred, you can proceed to push the screenshots to GitHub as mentioned in the initial requirements.
* Make sure to include the steps you followed to use the SFTP command-line tool in your project’s README.md file. This will help the reviewers understand how you performed the file transfer using SFTP.

# NOTE :
* The screenshoots of completed level should be inside the dir /root/alx-system_engineering-devops/command_line_for_the_win/

# Steps followed to push screenshots into the sandbox:
1: sftp username@hostname
2: sftp will then ask for the password to the sandbox. After inputting it, the sftp connection will be instantiated. An sftp prompt will appear, looking like the following:
sftp>
3: Once connected, navigate to the directory where you want to upload the screenshots. In my case /alx-system_engineering_devops/command_line_for_the_win/
4: Use the sftp put command to upload the screenshots from your local machine to the sandbox environment.
5: Once I make sure that the screenshots are successfully uploaded to the sandbox, I exited sftp by using the exit command.
