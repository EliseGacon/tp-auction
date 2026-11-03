from itertools import count
from utils import Cli

class Auction :
    def __init__(self, cli=None):
        self.cli = cli if cli else Cli()
    
    def opening_bid(self):
        self.cli.display(f'Started auction of type: {self.auction_type} ')
        opening_bid = self.cli.prompt('Please enter the amount for the opening bid:')
        opening_bid = int(opening_bid)
        self.cli.display(f"Opening bid is: {opening_bid}")
        return opening_bid
        

    def init_bidders(self):
        bidders = []
        for index in count(1):
            bidder = self.cli.prompt(
                f"Enter name for bidder {index} (enter nothing to move on):"
                )
            if not bidder:
                break
            bidders.append(bidder)
        self.cli.display(f"\nBidders are: {', '.join(bidders)}\n")
        return bidders

    def auction_loop(self, opening_bid, bidders):
        raise NotImplementedError

    def annonce_gagnant(self, winner, standing_bid):
        self.cli.display("\n~~~~~~~~\n")
        self.cli.display(f"Winner is {winner}. Winning bid is {standing_bid}.")

    def play(self):
        opening_bid = self.opening_bid()
        bidders = self.init_bidders()
        winner, price = self.auction_loop(opening_bid, bidders)
        self.annonce_gagnant(winner, price)

            
