# AsyncPolygonSDK
An SDK for the Polygon.io restAPI Client - ASYNC for data analysis, data science, data modeling, data visualization.


USAGE:


see examples



**
import asyncio
import pandas as pd
from dataclasses import asdict
from polygon_sdk.async_polygon.sdk import AsyncPolygonSDK
from poly_cfg import api_key, stock_condition_dict, STOCK_EXCHANGES (replace "YOUR API KEY" with your polygon.io APIKEY)


#create an instance of the polygon ASYNC SDK:

sdk = AsyncPolygonSDK(api_key)

#create a main function
async def main():
    # Get the stock snapshot
    ticker = "SPY"
    snapshot = await sdk.get_snapshot(ticker)

    # Convert the StockSnapshot instance to a dictionary
    snapshot_dict = asdict(snapshot)

    # Flatten the nested dictionaries
    flattened_snapshot = {}
    for key, value in snapshot_dict.items():
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                flattened_snapshot[f"{key}_{sub_key}"] = sub_value
        else:
            flattened_snapshot[key] = value

    # Create a DataFrame from the flattened dictionary
    df = pd.DataFrame([flattened_snapshot])
    print(df)

    #lastTrade
    conditions = snapshot.last_trade.conditions
    #convert conditions
    decoded_condition_names = [stock_condition_dict.get(int(condition_id), "Unknown") for condition_id in conditions] if conditions is not None else []
    exchange = STOCK_EXCHANGES.get(snapshot.last_trade.trade_exchange) #converted exchanges
    trade_time = snapshot.last_trade.trade_timestamp
    quote_time = snapshot.stock_last_quote.quote_timestamp

    print(f">>> Snapshot for {ticker} <<<")
    print(f"-------Last Trade-------")
    print(f">>> Exchange: {exchange}")
    print(f">>> Price: ${snapshot.last_trade.trade_price}")
    print(f">>> Size: {float(snapshot.last_trade.trade_size):,}")
    print(f">>> Timestamp: {trade_time}")
    print(f">>> Exchange: {exchange}")
    print(f">>> Conditions: {decoded_condition_names}")
    print()
    print(f"-------Last Quote-------")
    print(f"Bid Price: ${snapshot.stock_last_quote.bid_price} Size: {snapshot.stock_last_quote.bid_size}")
    print(f"Ask Price: ${snapshot.stock_last_quote.bid_price} Size: {snapshot.stock_last_quote.ask_size}")
    print(f"Timestamp: {quote_time}")
    print()
    print(f"-------Minute Data-------")
    print(f"Close: ${snapshot.stock_minute_bar.close}")
    print(f"High: ${snapshot.stock_minute_bar.high}")
    print(f"Open: ${snapshot.stock_minute_bar.open}")
    print(f"Low: ${snapshot.stock_minute_bar.low}")
    print(f"Volume: {snapshot.stock_minute_bar.volume}")
    print(f"Accumulated Volume on Day: {float(snapshot.stock_minute_bar.accumulated_volume):,}")
    print(f"VWAP: ${snapshot.stock_minute_bar.vwap}")
    print()
    print(f"-------Prev Day Data-------")
    print(f"Previous Close: ${snapshot.prev_day.close}")
    print(f"Previous High: ${snapshot.prev_day.high}")
    print(f"Previous Open: ${snapshot.prev_day.open}")
    print(f"Previous Low: ${snapshot.prev_day.low}")
    print(f"Previous Volume: ${float(snapshot.prev_day.volume):,}")
    print(f"Previous VWAP: ${snapshot.prev_day.vwap}")
    print()
    print(f"{ticker} is currently trading at {snapshot.stock_changep}%")
asyncio.run(main())


# #snapshot output:
# >>> Snapshot for SPY <<<
# -------Last Trade-------
# >>> Exchange: NYSE Arca, Inc.
# >>> Price: $415.9
# >>> Size: 140.0
# >>> Timestamp: 1682954955370834432
# >>> Exchange: NYSE Arca, Inc.
# >>> Conditions: ['Intermarket Sweep', 'Trade Thru Exempt']

# -------Last Quote-------
# Bid Price: $415.91 Size: 4
# Ask Price: $415.91 Size: 9
# Timestamp: 1682954955544884224

# -------Minute Data-------
# Close: $415.86
# High: $415.91
# Open: $415.87
# Low: $415.75
# Volume: 86719
# Accumulated Volume on Day: 19,829,234.0
# VWAP: $415.8227

# -------Prev Day Data-------
# Previous Close: $415.93
# Previous High: $415.94
# Previous Open: $411.49
# Previous Low: $411.43
# Previous Volume: $89,433,137.0
# Previous VWAP: $414.401

