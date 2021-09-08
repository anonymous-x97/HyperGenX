from pyrogram import Client

print("HyperGenX String Session Genarator!")

API_KEY = int(input("Enter API KEY: "))
API_HASH = input("Enter API HASH: ")
with Client(':memory:', api_id=API_KEY, api_hash=API_HASH) as app:
	app.send_message(
	    "me",
	    f"#HyperGenX | @UsergeXForkUpdates #HU_STRING_SESSION\n\n```{app.export_session_string()}```"
	)
	print("Done!, HyperGenX Session String Has Been Sent To Saved Messages!")
