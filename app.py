# Created :: Mayank Shrivastava
# Using flask as backend
from flask import Flask, request, render_template
from azlyrics.azlyrics import lyrics
# Using Genius API 
import lyricsgenius as lg
import config

app = Flask(__name__)

@app.route('/')
def index():
    # Rendering Home-Page
    return render_template('index.html')

@app.route('/', methods=['POST'])
def lys():
    # Getting Artist name as "artist"
    artist = request.form['artist']
    # Getting Song name as "song"
    song = request.form['song']
    # Alternate way of doing the same 
    # Using AZ Lyrics API
    '''
    ALTERNATE METHOD
    ----------------
    (Not Recommened)
    gaana = lyrics(artist, song)
    ly =  ''    
    for line in gaana: 
        ly += line
    if ly == 'Error':
        return render_template('error.html')
    return render_template('lyrics.html', artist=artist, song=song, lyrics=ly)
    '''
    # Using try and exception for printing the lyrics
    try:
        # Using Genius via CLIENT ACCESS TOKEN
        genius = lg.Genius('config.api_key')
        # Searching song on Genius 
        # With artist and song name 
        txt = genius.search_song(artist, song)
        # If the song of the artist is found
        # The lyrics is saved in "ly" variable
        ly = txt.lyrics
        # The lyrics is then send to "lyrics.html" page
        # Where the lyrics is shown
        return render_template('lyrics.html', artist=artist, song=song, lyrics=ly)
    except:
        # If no artist or no song is found
        # Then a exception is thrown 
        # And "error.html" is printed
        # It is also printed when 
        # The user forgot to give
        # The name of artist or song
        return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)