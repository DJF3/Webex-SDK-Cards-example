[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/DJF3/Webex-SDK-Cards-example)
# What Is It?
An example script to show you how to create Cards using the webexteamssdk library for Python. 

        
# What does a card look like?

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/DJF3/Webex-SDK-Cards-example/blob/main/_image/cards-example.jpg?raw=true" width="400px">

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/DJF3/Webex-SDK-Cards-example/blob/main/_image/cards-layout.jpg?raw=true" width="600px">




# REQUIREMENTS
* Python 3.x or higher (tested with 3.7.x and 3.9.x)
* Python '[webexteamssdk](https://webexteamssdk.readthedocs.io/en/latest/installation.html)' library

TESTED on Mac: Python 3.9.1, webexteamssdk 1.6

TESTED on Win 10: Python 3.7.2, webexteamssdk 1.6



# Start

1. Install Python  ([instructions](https://realpython.com/installing-python/))
2. Install webexteamssdk library  ([instructions](https://webexteamssdk.readthedocs.io/en/latest/installation.html))
   > short version: "python3 -m pip install webexteamssdk"
3. Get a Webex Message token:
   > **Use a Bot token:**
   >    Go to [developer.webex.com](https://developer.webex.com/) and login

   >    Create a bot

   >    copy the bot token

   > **Use your developer token:**
   > Only valid for 12 hours!

   > Has full access to _all_ of your data.

   > On [developer.webex.com](https://developer.webex.com/), login and under “Getting Started” scroll to “your personal access token”

4. Edit webexcards-sdk-example.py 
   > ```bot_token = "YOUR_BOT_TOKEN_HERE”```
   > 
   >     the token from step 2 

   > ```webex_space_id = "DESTINATION_EMAIL_ADDRESS_HERE"```
   > 
   >     (your?) email address

   > THEN save the code and run the script. 



# Support?

To get support, please join this Webex Space that I actively monitor: https://eurl.io/#w-0h7ytwQ



# More like this?

Will be announced in the _Webex Developer LinkedIn group_ at: http://cs.co/webexdevlink 
And for all your Webex Developer resources, go to http://cs.co/webexdevinfo 
