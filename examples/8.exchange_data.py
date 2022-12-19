import os
import sys

# paths
script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(script_dir, "../src")))
sys.path.append(os.path.abspath(os.path.join(script_dir, "../src/classes")))


from config import TEST_ACCT_KEY
from firefly_client import FireflyClient
from constants import Networks
from enumerations import MARKET_SYMBOLS, Interval, TRADE_TYPE
from pprint import pprint


def main():

    # initialise client
    client = FireflyClient(
        True, # agree to terms and conditions
        Networks["TESTNET_ARBITRUM"], # network to connect with
        TEST_ACCT_KEY, # private key of wallet
        True, # on boards user on firefly. Must be set to true for first time use
        )

    # returns status/health of exchange
    status = client.get_exchange_status()
    pprint(status)

    # gets state of order book. Gets first 10 asks and bids
    orderbook = client.get_orderbook({"symbol": MARKET_SYMBOLS.ETH, "limit":10})
    pprint(orderbook)

    # returns available market for trading
    market_symbols = client.get_market_symbols()
    print(market_symbols)

    # gets current funding rate on market
    funding_rate = client.get_funding_rate(MARKET_SYMBOLS.ETH)
    pprint(funding_rate)

    # gets markets meta data about contracts, blockchain, exchange url
    meta = client.get_market_meta_info() # (optional param MARKET_SYMBOL)
    # should log meta for all markets
    pprint(meta)

    # gets market's current state
    market_data = client.get_market_data(MARKET_SYMBOLS.ETH)
    pprint(market_data)


    # gets market data about min/max order size, oracle price, fee etc..
    exchange_info = client.get_exchange_info(MARKET_SYMBOLS.ETH)
    pprint(exchange_info)

    # gets market candle info
    candle_data = client.get_market_candle_stick_data({"symbol": MARKET_SYMBOLS.ETH, "interval": Interval._1M})
    pprint(candle_data)

    # gets recent isolated/normal trades on ETH market
    recent_trades = client.get_market_recent_trades({"symbol": MARKET_SYMBOLS.ETH, "traders": TRADE_TYPE.ISOLATED})
    pprint(recent_trades)


    # gets addresses of on-chain contracts
    contract_address = client.get_contract_addresses()
    pprint(contract_address)

if __name__ == "__main__":
    main()