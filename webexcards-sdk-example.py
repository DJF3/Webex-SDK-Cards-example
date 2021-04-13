# Python example for Cards with the WebexteamsSDK 
#    DJ Uittenbogaard (duittenb@cisco.com)
# details: https://github.com/DJF3/Webex-SDK-Cards-example/
"""Showing how you can use Cards with the Webexteamsdk to create
nicely formatted Webex Messages.
Copyright (c) 2019 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""
# -*- coding: utf-8 -*-
from webexteamssdk import WebexTeamsAPI, ApiError
from webexteamssdk.models.cards.card import AdaptiveCard
from webexteamssdk.models.cards.inputs import Text, Number
from webexteamssdk.models.cards.container import ColumnSet
from webexteamssdk.models.cards.components import TextBlock, Column, Image
from webexteamssdk.models.cards.actions import Submit
from webexteamssdk.utils import make_attachment

# ______ VARIABLES
bot_token = "YOUR_BOT_TOKEN_HERE"
webex_space_id = "DESTINATION_EMAIL_ADDRESS_HERE"
# data used in columns
my_data = [["[link](https://developer.webex.com) for Webex Developers","25"],
           ["More text with an info link [here](https://www.webex.com)","4 days"],
           ["Generic Device status","OK!"]]

# ______ DEFINING CONTENT BLOCKS
# block: intro text
b_intro_text = TextBlock("This is an example showing how you can use the Python WebexSDK library with Cards & Buttons functionality.", wrap=True)
# block: intro image - note that to use the 'Image' block,
#        you have to import it! (around line 6)
b_intro_image = Image(url="https://www.webex.com/content/dam/wbx/us/images/hp/webexone/10x.png", width="150px", separator=True)
# block: section title
b_section_title = TextBlock("Device Overview", separator=True, size="Large", horizontalAlignment="center")
# block: column headers
b_header_dev = TextBlock("DEVICE", color="Attention", weight="Bolder")
b_header_val = TextBlock("VALUE", color="Attention", weight="Bolder")


# ______ PREPARING CARD
# create list for both columns (device & value) + add column header
col_dev = list()
col_val = list()
# add header to each column
col_dev.append(b_header_dev)
col_val.append(b_header_val)
# with the data from my_data, add TextBlocks to each column
for items in my_data:
    col_dev.append(TextBlock(items[0], wrap=True))
    col_val.append(TextBlock(items[1], wrap=True))

# create 2 columns (width 45 and width 15)
mycols = [Column(items=col_dev,separator=True, width=45), Column(items=col_val,separator=True, width=15)]
# create ColumnSet with 2 columns
mycolset = ColumnSet(columns=mycols, separator=True)
# combine intro-block, b_section_title-block and column-set-block
mycards = [b_intro_text, b_intro_image, b_section_title, mycolset]

# ______ CREATE CARD
card = AdaptiveCard(body=mycards)
# optionally: uncomment next line to see the JSON code generated
# print(card.to_json())

# ______ SEND CARD USING WEBEXTEAMSSDK
api = WebexTeamsAPI(access_token=bot_token)
try:
    api.messages.create(text="issue sending message", toPersonEmail=webex_space_id, attachments=[make_attachment(card)])
except ApiError as e:
    print(f"**ERROR** sending webex message. Error:\n {e}")

