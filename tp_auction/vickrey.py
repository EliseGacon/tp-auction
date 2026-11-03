from utils import Cli
from itertools import count
from auction import Auction

class VickreyAuction(Auction):
    def __init__(self,cli=None):
        super().__init__()
        self.auction_type = 'Vickrey'

    def auction_loop(self, opening_bid, bidders):
        bids=[]
        for bidder in bidders:
            bid = self.cli.prompt(
                f"Opening bid is {opening_bid}. {bidder} bids:"
            )
            bid = int(bid)
            bids.append((bid,bidder))
        bids.sort(reverse=True, key=lambda montant: montant[0])
        winner = bids[0][1]
        price = bids[1][0]
        return winner, price


if __name__ == "__main__":
    auction = VickreyAuction()
    auction.play()
