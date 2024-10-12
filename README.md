<h1>Base Transaction Spammer</h1>

This software was created to spam transactions in Base network built on ERC20 to receive a potential airdrop in Base meme coins. Several months ago, I noticed that I’ve been receiving random “shitcoins” in my main Ethereum wallet. It turns out these are low-capitalization meme coins trying to profit from a new blockchain backed by Coinbase. The criteria to receive these coins are usually tied to either the number or volume of transactions. By combining all these tokens, a wallet with over 100 transactions can earn up to $5 while spending as little as 10 cents on transaction fees. Now, imagine this scenario with thousands of wallets!

Here is a reddit post about it: [reddit](https://www.reddit.com/r/CoinBase/comments/1ccml6m/where_are_the_meme_coins_being_dropped_in_my/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)
<h2>Manual wallet creation</h2>
Some of my friends have created 500+ wallets manually, spending tens of hours entering information into Google Excel. Instead, I built this scipt that can save hours of human time. Although it isn’t as stable as I’d like and still requires some refinements, it can save a ton of time and potentially make you a buck.
<h2>How does it worlk?</h2>
It creates clusters of five wallets. One must send some Ethereum to the first wallet, and a script will automatically send this ETH to random wallets in the cluster and back. The seed phrases of these wallets are then stored in a json file. 

![Screenshot_1](https://github.com/user-attachments/assets/32f8d46d-1b2f-4938-bdf1-1085fe93f25d)


<h2>Video illustration</h2>

https://github.com/user-attachments/assets/2aa53857-64d7-4fce-ba78-867c3bd4e657
<h2>Note:</h2>
Previous versions sent transactions much faster, achieving up to 50 transactions per minute.However, the earlier version crashed every fifth cluster (meaning every 25 wallets). Since I don’t have enough time right now, I used LLMs to yeat all of my code into a single file and fix those rare but annoying errors. It seems like AI is not powerful enough yet so it works extremly slower than my version. Peace)






