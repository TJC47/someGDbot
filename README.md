

# What is this program?
This project is a Geometry Dash Chatbot. It is packed full of useful and fun commands that everybody can use.

This bot is inspired by Sevenworks' Autoworks, but does not use its code.
The Program now has a still WIP web ui to control features.
Unlike Autoworks though, it has an easy to use commandline interface, to execute certain commands and it uses a json configuration file to manage bans, superusers, credentials, etc...
This makes the program way more efficient as it only has to open one file.
Something worthy of mention is that it uses GDColons GDBrowser api. In the next section I will explain the needed configuration.

# How to set up
This program uses GDColons GDBrowser api.
Be sure to set the port of the GDBrowser website to 81 for the program to function correctly.

# Configuration
`banned` list of GD account names, that can't use commands

`ops` list of GD account names, that have permissions for all commands

`username` the bots GD username

`accountid` account id of the account.(Im too lazy to make it fetch it automatically)

`password` password of the GD account

`levelID` the id of the level for the bot to scan and comment on

`debug` don't change unless you know, what you are doing

# Your command ideas
If you want your own commands in this bot, feel free to open a pull request.
