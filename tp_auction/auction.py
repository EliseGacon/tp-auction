from itertools import count
from utils import Cli

class Auction :
    def __init__(self, cli=None):
        self.cli = cli if cli else Cli()
    
    def opening_bid(self):
        self.cli.display('Started auction of type: ')
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

    def annonce_gagant(self, winner, standing_bid):
        self.cli.display("\n~~~~~~~~\n")
        self.cli.display(f"Winner is {winner}. Winning bid is {standing_bid}.")

    def play(self):
        opening_bid = self.opening_bid()
        winner, price = auction_loop(opening_bid, bidders)
        bidders = self.init_bidders()
        self.annonce_gagnant(winner, price)

            
