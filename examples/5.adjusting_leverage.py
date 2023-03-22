from config import TEST_ACCT_KEY, TEST_NETWORK
from firefly_exchange_client import FireflyClient, Networks, MARKET_SYMBOLS
import asyncio




async def main():

    # initialize client
    client = FireflyClient(
        True, # agree to terms and conditions
        Networks[TEST_NETWORK], # network to connect with
        TEST_ACCT_KEY, # private key of wallet
    )

    await client.init(True) 

    print('Leverage on BTC market:', await client.get_user_leverage(MARKET_SYMBOLS.BTC))
    # we have a position on BTC so this will perform on-chain leverage update
    # must have native chain tokens to pay for gas fee
    await client.adjust_leverage(MARKET_SYMBOLS.BTC, 6);

    print('Leverage on BTC market:', await client.get_user_leverage(MARKET_SYMBOLS.BTC))


    print('Leverage on ETH market:', await client.get_user_leverage(MARKET_SYMBOLS.ETH))
    # since we don't have a position on-chain, it will perform off-chain leverage adjustment
    await client.adjust_leverage(MARKET_SYMBOLS.ETH, 4);

    print('Leverage on ETH market:', await client.get_user_leverage(MARKET_SYMBOLS.ETH))

    await client.apis.close_session();

if __name__ == "__main__":
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())