def maak_playlist(lijst_naam_in,  mijn_naam_in):
    playlist = dict(lijst_naam=lijst_naam_in,  mijn_naam=mijn_naam_in,  aantal_liedjes="",  lijst=[],  totale_duur=0)
    return playlist

def maak_item(titel,  auteur,  album,  datum_toegevoegd,  duur):
    return {'titel':titel,  'auteur':auteur,  'datum':datum_toegevoegd,  'duur':duur}
    
def voeg_items_toe(playlist):
    item = maak_item('Nen titel',  'Nen Auteur',  'Nen Album',  '12/01/1981',  5.75)
    playlist['lijst'].append(item)
    item = maak_item('Nen titel twee',  'Nen Auteur twee',  'Nen Album twee',  '12/01/1957',  3.48)
    playlist['lijst'].append(item)
    item = maak_item('Nen tottel',  'Nen Auteur',  'Nen boek',  '11/11/1921',  2.64)
    playlist['lijst'].append(item)
    
    for liedje in playlist['lijst']:
        playlist['totale_duur'] += liedje['duur']
    
    
def main():
    
    playlist = maak_playlist('MIJN KICKASS PLAYLIST',  'JvB')        
    voeg_items_toe(playlist) 
    print('Playlist data ---')
    for element in playlist.items():
        print(element)        
    
    print('Muziek ---')
    for liedje in playlist['lijst']:
        print(liedje)

main()
