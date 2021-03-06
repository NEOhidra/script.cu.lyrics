import os
import utilities
import xbmc
import sys

__cwd__ = sys.modules[ "__main__" ].__cwd__

BASE_DATA_PATH = os.path.join( xbmc.translatePath( "special://profile/" ), "addon_data", os.path.basename( __cwd__ ) )
lyrics_path = os.path.join( BASE_DATA_PATH, "lyrics")

class Song:
    def __init__( self ):
        self.artist = ""
        self.title = ""

        

    
    def __str__(self):
        return "Artist: %s, Title: %s" % ( self.artist, self.title)
    
    def __cmp__(self, song):
        if (self.artist != song.artist):
            return cmp(self.artist, song.artist)
        else:
            return cmp(self.title, song.title)
    
    def sanitize(self, str):
        return str.replace( "\\", "_" ).replace( "/", "_" ).replace(":","_").replace("?","_").replace("!","_")
    
    def path(self):
        return unicode( os.path.join( lyrics_path, self.sanitize(self.artist), self.sanitize(self.title) + ".txt" ), "utf-8" )
    
    @staticmethod
    def current():
        song = Song()
        song.title = xbmc.getInfoLabel( "MusicPlayer.Title" )
        #song.title = utilities.deAccent(song.title)
        song.artist = xbmc.getInfoLabel( "MusicPlayer.Artist")
        #song.artist = utilities.deAccent(song.artist)
        
        print "Current Song: %s:%s" % (song.artist, song.title)
        
        return song

    @staticmethod
    def next():
        song = Song()
        song.title = xbmc.getInfoLabel( "MusicPlayer.offset(1).Title" )
        song.title = utilities.deAccent(song.title)
        song.artist = xbmc.getInfoLabel( "MusicPlayer.offset(1).Artist")
        song.artist = utilities.deAccent(song.artist)
        
        print "Next Song: %s:%s" % (song.artist, song.title)
        
        return song
