import pickle
import unittest
import sys

parentpath = '/home/sakib/funsies/espnBracket'
srcpath = parentpath+'/srcFiles'
sys.path.append(srcpath)
from bracket import Team, MatchUp, Bracket

gonzaga = Team('West', 1, 'Gonzaga')
iowa = Team('West', 2, 'Iowa')
kansas = Team('West', 3, 'Kansas')
virginia = Team('West', 4, 'Virginia')
creighton = Team('West', 5, 'Creighton')
usc = Team('West', 6, 'USC')
oregon = Team('West', 7, 'Oregon')
oklahoma = Team('West', 8, 'Oklahoma')
missouri = Team('West', 9, 'Missouri')
vcu = Team('West', 10, 'VCU')
drake = Team('West', 11, 'Drake')
ucsb = Team('West', 12, 'UCSB')
ohio = Team('West', 13, 'Ohio')
eWash = Team('West', 14, 'E. Washington')
gcu = Team('West', 15, 'GCU')
norfolk = Team('West', 16, 'Norfolk')

michigan = Team('East', 1, 'Michigan')
alabama = Team('East', 2, 'Alabama')
texas = Team('East', 3, 'Texas')
fsu = Team('East', 4, 'FSU')
colorado = Team('East', 5, 'Colorado')
byu = Team('East', 6, 'BYU')
uConn = Team('East', 7, 'UConn')
lsu = Team('East', 8, 'LSU')
bonaventure = Team('East', 9, 'Bonaventure')
maryland = Team('East', 10, 'Maryland')
ucla = Team('East', 11, 'UCLA')
georgetown = Team('East', 12, 'Georgetown')
greensboro = Team('East', 13, 'Greensboro')
abilChristian = Team('East', 14, 'Abel Christian')
iona = Team('East', 15, 'Iona')
texasS = Team('East', 16, 'Texas S.')

baylor = Team('South', 1, 'Baylor')
ohioState = Team('South', 2, 'Ohio State')
arkansas = Team('South', 3, 'Arkansas')
purdue = Team('South', 4, 'Purdue')
villanova = Team('South', 5, 'Villanova')
texasTech = Team('South', 6, 'Texas Tech')
florida = Team('South', 7, 'Florida')
unc = Team('South', 8, 'UNC')
wisconsin = Team('South', 9, 'Wisconsin')
vTech = Team('South', 10, 'V. Tech')
utahState = Team('South', 11, 'Utah State')
winthorp = Team('South', 12, 'Winthorp')
nTexas = Team('South', 13, 'N. Texas')
colgate = Team('South', 14, 'Colgate')
oralRoberts = Team('South', 15, 'Oral Roberts')
hartford = Team('South', 16, 'Hartford')

illinois = Team('Midwest', 1, 'Illinois')
houston = Team('Midwest', 2, 'Houston')
wvu = Team('Midwest', 3, 'WVU')
osu = Team('Midwest', 4, 'OSU')
tenessee = Team('Midwest', 5, 'Tenessee')
sdState = Team('Midwest', 6, 'SDState')
clemson = Team('Midwest', 7, 'Clemson')
loyola = Team('Midwest', 8, 'Loyola')
gatech = Team('Midwest', 9, 'GaTech')
rutgers = Team('Midwest', 10, 'Rutgers')
syracuse = Team('Midwest', 11, 'Syracuse')
oregonState = Team('Midwest', 12, 'Oregon State')
liberty = Team('Midwest', 13, 'Liberty')
moreheadState = Team('Midwest', 14, 'Morehead State')
clevelandState = Team('Midwest', 15, 'Cleveland State')
drexel = Team('Midwest', 16, 'Drexel')

teams2021 = [gonzaga, norfolk, oklahoma, missouri, creighton, ucsb, virginia, ohio, 
            usc, drake, kansas, eWash, oregon, vcu, iowa, gcu,
            michigan, texasS, lsu, bonaventure, colorado, georgetown, fsu, greensboro,
            byu, ucla, texas, abilChristian, uConn, maryland, alabama, iona,
            baylor, hartford, unc, wisconsin, villanova, winthorp, purdue, nTexas,
            texasTech, utahState, arkansas, colgate, florida, vTech, ohioState, oralRoberts,
            illinois, drexel, loyola, gatech, tenessee, oregonState, osu, liberty,
            sdState, syracuse, wvu, moreheadState, clemson, rutgers, houston, clevelandState]

class TestTeamClass(unittest.TestCase):
    def test_return_seed(self):
        self.assertEqual(gonzaga.return_seed(), 1)
        self.assertEqual(houston.return_seed(), 2)

    def test_return_region(self):
        self.assertEqual(gonzaga.return_region(), 'West')
        self.assertEqual(houston.return_region(), 'Midwest')

class TestMatchUpClass(unittest.TestCase): 
    def test_set_pick(self):
        mf = MatchUp(gonzaga, houston, 6)
        m1 = MatchUp(rutgers, clemson, 1)
        m3 = MatchUp(ucla, alabama, 3)
        m1.set_pick(rutgers)
        mf.set_pick(gonzaga)
        m3.set_pick(alabama)
        self.assertEqual(m1.pick.return_seed(), rutgers.return_seed())
        self.assertEqual(mf.pick.return_name(), gonzaga.return_name())
        self.assertEqual(m3.pick.return_name(), 'Alabama')

    def test_set_winner(self):
        mf = MatchUp(gonzaga, houston, 6)
        m1 = MatchUp(rutgers, clemson, 1)
        m3 = MatchUp(ucla, alabama, 3)
        m1.set_pick(rutgers)
        mf.set_pick(gonzaga)
        m3.set_pick(alabama)
        
        self.assertEqual(m1.return_score(), 0)
        m1.set_winner(rutgers)
        self.assertEqual(m1.winner.return_name(), rutgers.return_name())
        self.assertEqual(m1.return_score(), 10)
        self.assertEqual(mf.return_score(), 0)
        mf.set_winner(gonzaga)
        self.assertEqual(mf.winner.return_name(), gonzaga.return_name())
        self.assertEqual(mf.return_score(), 320)
        self.assertEqual(m3.return_score(), 0)
        m3.set_winner(ucla)
        self.assertEqual(m3.winner.return_name(), ucla.return_name())
        self.assertEqual(m3.return_score(), 0)

class TestBracketClass(unittest.TestCase):
    def test_create_initial_bracket(self):
        b2021 = Bracket(teams2021)
        #print(b2021)

    def test_set_picks(self):
        b2021 = Bracket(teams2021)
        self.assertEqual(len(b2021.bracket), 32)
        self.assertEqual(b2021.bracket[18].team1.return_name(), 'Villanova')
        self.assertEqual(b2021.bracket[18].team2.return_name(), 'Winthorp')
        self.assertEqual(b2021.bracket[18].pick, None) 
        r1picks = [gonzaga, oklahoma, ucsb, virginia, usc, kansas, oregon, iowa,
                michigan, lsu, colorado, fsu, ucla, texas, maryland, alabama,
                baylor, unc, villanova, purdue, texasTech, arkansas, vTech, ohioState,
                illinois, loyola, tenessee, osu, syracuse, wvu, rutgers, houston]
        b2021.set_picks(r1picks)
        self.assertEqual(b2021.bracket[18].pick.return_name(), 'Villanova')
        self.assertEqual(b2021.bracket[41].team1.return_name(), 'Villanova')
        self.assertEqual(b2021.bracket[41].team2.return_name(), 'Purdue')
        self.assertEqual(len(b2021.bracket), 48)
        r2picks = [gonzaga, virginia, usc, iowa, michigan, fsu, ucla, alabama, 
                    unc, purdue, texasTech, ohioState, illinois, osu, wvu, houston]
        b2021.set_picks(r2picks)
        self.assertEqual(len(b2021.bracket), 56)
        r3picks = [gonzaga, iowa, fsu, alabama, purdue, ohioState, illinois, houston]
        b2021.set_picks(r3picks)
        self.assertEqual(len(b2021.bracket), 60)
        r4picks = [gonzaga, fsu, ohioState, houston]
        b2021.set_picks(r4picks)
        self.assertEqual(len(b2021.bracket), 62)
        r5picks = [gonzaga, houston]
        b2021.set_picks(r5picks)
        self.assertEqual(len(b2021.bracket), 63)
        championshipPick = [gonzaga]
        b2021.set_picks(championshipPick)
        self.assertEqual(b2021.bracket[62].team2.return_name(), 'Houston')
        self.assertEqual(b2021.bracket[62].pick.return_name(), 'Gonzaga')
        self.assertEqual(len(b2021.bracket), 63)
    
    def test_set_winner(self):
        b2021 = Bracket(teams2021)
        r1picks = [gonzaga, oklahoma, ucsb, virginia, usc, kansas, oregon, iowa,
                michigan, lsu, colorado, fsu, ucla, texas, maryland, alabama,
                baylor, unc, villanova, purdue, texasTech, arkansas, vTech, ohioState,
                illinois, loyola, tenessee, osu, syracuse, wvu, rutgers, houston]
        b2021.set_picks(r1picks)
        r2picks = [gonzaga, virginia, usc, iowa, michigan, fsu, ucla, alabama, 
                    unc, purdue, texasTech, ohioState, illinois, osu, wvu, houston]
        b2021.set_picks(r2picks)
        r3picks = [gonzaga, iowa, fsu, alabama, purdue, ohioState, illinois, houston]
        b2021.set_picks(r3picks)
        r4picks = [gonzaga, fsu, ohioState, houston]
        b2021.set_picks(r4picks)
        r5picks = [gonzaga, houston]
        b2021.set_picks(r5picks)
        championshipPick = [gonzaga]
        b2021.set_picks(championshipPick)
        
        r1winners = [gonzaga, oklahoma, creighton, ohio, usc, kansas, oregon, iowa,
                    michigan, lsu, colorado, fsu, ucla, abilChristian, maryland, alabama,
                    baylor, wisconsin, villanova, nTexas, texasTech, arkansas, florida, oralRoberts,
                    illinois, loyola, oregonState, osu, syracuse, wvu, rutgers, houston]
        b2021.set_winners(r1winners)
        r2winners = [gonzaga, creighton, usc, oregon, michigan, fsu, ucla, alabama,
                    baylor, villanova, arkansas, oralRoberts, loyola, oregonState, syracuse, houston]
        b2021.set_winners(r2winners)
        r3winners = [gonzaga, usc, michigan, ucla, baylor, arkansas, oregonState, houston]
        b2021.set_winners(r3winners)
        r4winners = [gonzaga, ucla, baylor, houston]
        b2021.set_winners(r4winners)
        
    def test_get_score(self):
        b2021 = Bracket(teams2021)
        r1picks = [gonzaga, oklahoma, ucsb, virginia, usc, kansas, oregon, iowa,
                michigan, lsu, colorado, fsu, ucla, texas, maryland, alabama,
                baylor, unc, villanova, purdue, texasTech, arkansas, vTech, ohioState,
                illinois, loyola, tenessee, osu, syracuse, wvu, rutgers, houston]
        b2021.set_picks(r1picks)
        r2picks = [gonzaga, virginia, usc, iowa, michigan, fsu, ucla, alabama, 
                    unc, purdue, texasTech, ohioState, illinois, osu, wvu, houston]
        b2021.set_picks(r2picks)
        r3picks = [gonzaga, iowa, fsu, alabama, purdue, ohioState, illinois, houston]
        b2021.set_picks(r3picks)
        r4picks = [gonzaga, fsu, ohioState, houston]
        b2021.set_picks(r4picks)
        r5picks = [gonzaga, houston]
        b2021.set_picks(r5picks)
        championshipPick = [gonzaga]
        b2021.set_picks(championshipPick)
        
        r1winners = [gonzaga, oklahoma, creighton, ohio, usc, kansas, oregon, iowa,
                    michigan, lsu, colorado, fsu, ucla, abilChristian, maryland, alabama,
                    baylor, wisconsin, villanova, nTexas, texasTech, arkansas, florida, oralRoberts,
                    illinois, loyola, oregonState, osu, syracuse, wvu, rutgers, houston]
        b2021.set_winners(r1winners)
        self.assertEqual(b2021.get_score(), 240)
        r2winners = [gonzaga, creighton, usc, oregon, michigan, fsu, ucla, alabama,
                    baylor, villanova, arkansas, oralRoberts, loyola, oregonState, syracuse, houston]
        b2021.set_winners(r2winners)
        self.assertEqual(b2021.get_score(), 380)
        r3winners = [gonzaga, usc, michigan, ucla, baylor, arkansas, oregonState, houston]
        b2021.set_winners(r3winners)
        self.assertEqual(b2021.get_score(), 460)
        r4winners = [gonzaga, ucla, baylor, houston]
        b2021.set_winners(r4winners)
        self.assertEqual(b2021.get_score(), 620)

if __name__ == '__main__':
    unittest.main()
