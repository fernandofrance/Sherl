# Sherl
A Discord based pentest/CTF toolkit.

## Features

* Port scanner
   * Performs a port scan in a host
* Web path finder
   * Performs a bruteforce attack for directories/files in webservers
* GEO-IP
   * Provides geolocalization of an IP address
* Encoder
   * Creates a hash from text (MD5, SHA1, SHA224, SHA256, SHA348, SHA512)


## Installation

1. Clone the repo
   ```sh
   git clone https://github.com/sirfern4ndo/sherl.git
   ```
2. Install requirements
   ```sh
   pip install -r requirements.txt
   ```
3. Replace the `wordlist.txt` file with your own wordlist (for web path finder)

4. [Create an application (bot)](https://discord.com/developers/applications) on Discord

5. Go to **General information** tab and copy you **Application ID**

6. Go to **Bot** tab, create the bot and copy it's **token**.

7. Invite your bot to your Discord server by filling up the following link with your **Application ID**:
`https://discord.com/oauth2/authorize?client_id=<APP_ID>&scope=bot&permissions=8`

8. Place your **token** in `sherl.py` and start your bot
   ```sh
   python sherl.py
   ```
* Type `.help` in your server's chat to see bot commands.

## License

Distributed under the MIT License. See `LICENSE` for more information.
