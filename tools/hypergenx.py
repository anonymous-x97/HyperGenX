# pylint: disable=invalid-name, missing-module-docstring
#
# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Userge/blob/master/LICENSE >
#
# All rights reserved.

import os
import asyncio

from pyrogram import Client
from dotenv import load_dotenv

API_KEY = int(input("Enter API_ID: "))
API_HASH = input("Enter API_HASH: ")
with Client(':memory:', api_id=API_KEY, api_hash=API_HASH) as app:
	app.send_message(
	    "me",
	    f"#HyperGenX | Repl - https://replit.com/@NotShroudX97/HyperGenX | @UsergeXForkUpdates | Noice!, #HyperGenX String Session Has Been Generated & Sent To Your Saved Messages | Note:- Don't Share This With Anyone Else ID Hacked! | #HU_STRING_SESSION\n\n```{app.export_session_string()}```"
	)
	print("Noice!, #HyperGenX String Session Has Been Generated & Sent To Your Saved Messages | Note:- Don't Share This With Anyone Else ID Hacked!")
