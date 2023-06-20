from config import TEST_ACCT_KEY, TEST_NETWORK
from firefly_exchange_client import FireflyClient, Networks, MARKET_SYMBOLS
from pprint import pprint
import asyncio


async def main():
    # create client instance
    client = FireflyClient(
        True, # agree to terms and conditions
        Networks[TEST_NETWORK], # network to connect with
        TEST_ACCT_KEY, # private key of wallet
        )
    
    # initialize the client
    # on boards user on firefly. Must be set to true for first time use
    await client.init(True) 

    # gets user account data on firefly exchange
    data = await client.get_user_account_data()

    pprint(data)

    position = await client.get_user_position({"symbol":MARKET_SYMBOLS.ETH})
    
    # returns {} when user has no position
    pprint(position)

    position = await client.get_user_position({"symbol":MARKET_SYMBOLS.BTC})
    
    # returns user position if exists
    pprint(position)

    await client.close_connections()
    


if __name__ == "__main__":
  loop = asyncio.new_event_loop()
  loop.run_until_complete(main())
  loop.close()