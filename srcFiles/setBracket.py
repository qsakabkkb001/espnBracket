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
        
b2021 = Bracket(teams2021)
r1picks = [gonzaga, oklahoma, creighton, virginia, usc, kansas, oregon, iowa,
            michigan, lsu, colorado, fsu, byu, texas, uConn, alabama,
            baylor, unc, villanova, purdue, texasTech, arkansas, florida, ohioState,
            illinois, loyola, tenessee, osu, sdState, wvu, clemson, houston]
b2021.set_picks(r1picks)
r2picks = [gonzaga, virginia, kansas, iowa, michigan, fsu, texas, alabama, 
            baylor, purdue, arkansas, ohioState, illinois, osu, wvu, houston]
b2021.set_picks(r2picks)
r3picks = [gonzaga, iowa, michigan, alabama, baylor, ohioState, illinois, houston]
b2021.set_picks(r3picks)
r4picks = [gonzaga, michigan, baylor, illinois]
b2021.set_picks(r4picks)
r5picks = [gonzaga, baylor]
b2021.set_picks(r5picks)
championshipPick = [gonzaga]
b2021.set_picks(championshipPick)
        
r1winners = [gonzaga, oklahoma, creighton, ohio, usc, kansas, oregon, iowa,
                michigan, lsu, colorado, fsu, ucla, abilChristian, maryland, alabama,
                baylor, wisconsin, villanova, nTexas, texasTech, arkansas, florida, oralRoberts,
                illinois, loyola, oregonState, osu, syracuse, wvu, rutgers, houston]
b2021.set_winners(r1winners)
print(b2021.get_score())
r2winners = [gonzaga, creighton, usc, oregon, michigan, fsu, ucla, alabama,
            baylor, villanova, arkansas, oralRoberts, loyola, oregonState, syracuse, houston]
b2021.set_winners(r2winners)
print(b2021.get_score())
r3winners = [gonzaga, usc, michigan, ucla, baylor, arkansas, oregonState, houston]
b2021.set_winners(r3winners)
print(b2021.get_score())
r4winners = [gonzaga, ucla, baylor, houston]
b2021.set_winners(r4winners)
print(b2021.get_score())
