import unittest

from english import EnglishAuction
from vickrey import VickreyAuction
from testing_utils import make_auction

class TestBonus(unittest.TestCase):
    def test_english(self):
        cli = make_auction(EnglishAuction) # on crée une English Auction
        cli.type('30')      # montant initial
        cli.type('alice')   # initialisation des joueurs
        cli.type('bob')
        cli.type('carol')
        cli.type(None)
        # Round 1 
        cli.type(None)  # alice n'enchérit pas 
        cli.type(None)  # bob n'enchérit pas
        cli.type(None)  # carol n'enchérit pas
        self.assertEqual(
                    'No winner for this auction',
                    cli.get_displayed()[-1]
                )
        
    def test_vickrey(self):
        cli = make_auction(VickreyAuction) # on crée une Vickrey Auction
        cli.type('30')      # montant initial
        cli.type('alice')   # un seul enrichisseur
        cli.type(None)
        # Round 1 
        cli.type(60)  # alice enrichit à 30
        self.assertEqual(
                'Winner is alice. Winning bid is 30.',
                cli.get_displayed()[-1]
            )



if __name__ == "__main__":
    unittest.main()
