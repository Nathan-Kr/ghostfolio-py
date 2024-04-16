from typing import TypedDict, NotRequired, Literal


class Activity(TypedDict):
    accountId: NotRequired[str]
    assetClass: NotRequired[str]
    currency: str
    comment: NotRequired[str]
    dataSource: Literal["COINGECKO", "MANUAL", "YAHOO"]
    date: str
    fee: float
    quantity: float
    symbol: str
    type: Literal["BUY", "DIVIDEND", "FEE", "INTEREST", "ITEM", "LIABILITY", "SELL"]
    unitPrice: float