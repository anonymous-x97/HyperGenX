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

if os.path.isfile("config.env"):
    load_dotenv("config.env")


async def genStrSession() -> None:  # pylint: disable=missing-function-docstring
    async with Client(
            "HyperFusionX String Session Generator!",
            api_id=int(os.environ.get("API_ID") or input("Enter Telegram APP ID: ")),
            api_hash=os.environ.get("API_HASH") or input("Enter Telegram API HASH: ")
    ) as userge:
        print("\nprocessing...")
        await userge.send_message(
            "me", f"#HyperGenX | @UsergeXForkUpdates #HU_STRING_SESSION\n\n```{await userge.export_session_string()}```")
        print("Done!, HyperGenX Session String Has Been Sent To Saved Messages!")
