import modules as mx
import sys
sys.path.append(r'C:\Users\dreba\Documents\GitHub\WebGen\files\Portfolio')
data = mx.Data()
body = mx.Body()
from header import *
from visitInfo import *

data.title = "Dre Barrera | Music"
data.author = "Andres Barrera"

### OBJECTS ###
center = mx.C()
main = mx.C()
player = mx.X()
godAlbumA = mx.Link()
godAlbumC = mx.C()
godAlbum = mx.Image()
godAlbumT = mx.T()
lcAlbumA = mx.Link()
lcAlbumC = mx.C()
lcAlbum = mx.Image()
lcAlbumT = mx.T()
goldAlbumA = mx.Link()
goldAlbumC = mx.C()
goldAlbum = mx.Image()
goldAlbumT = mx.T()

### CONTENT ###
# Body
body.content = [nav, center]

# Center
center.content = [main]

# Main
main.content = [player, godAlbumA, lcAlbumA, goldAlbumA]

# Player
player.content = '<iframe id="player" src="https://open.spotify.com/embed/artist/3BFGzlgZp1l9E527dWSgEG?utm_source=generator" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>'

# Albums
godAlbumA.content = [godAlbumC, godAlbumT]
godAlbumC.content = [godAlbum]
godAlbum.src = "images/god.jpeg"
godAlbumT.content = "god. (2021)"
lcAlbumA.content = [lcAlbumC, lcAlbumT]
lcAlbumC.content = [lcAlbum]
lcAlbum.src = "images/caroline_lovedrunk.jpg"
lcAlbumT.content = "Caroline // Lovedrunk (2021)"
goldAlbumA.content = [goldAlbumC, goldAlbumT]
goldAlbumC.content = [goldAlbum]
goldAlbum.src = "images/gold.jpg"
goldAlbumT.content = "gold. (2020)"

### PROPERTIES ###
# Body
body.background_color = ""
body.overflow_y = 'hidden'

# Center
center.id = "center"
center.display = 'flex'
center.justify_content = 'center'
center.overflow_y = 'scroll'
center.background_color = ''

# Main
main.id = "main"
main.background_color = ""

# Albums
godAlbumA.target = '_blank'
godAlbumA.src = "https://distrokid.com/hyperfollow/drebarrera/god"
godAlbumC.cl = "album"
godAlbumC.background_color = ""
lcAlbumA.target = '_blank'
lcAlbumA.src = "https://distrokid.com/hyperfollow/drebarrera/caroline--lovedrunk-2"
lcAlbumC.cl = "album"
lcAlbumC.background_color = ""
goldAlbumA.target = '_blank'
goldAlbumA.src = "https://distrokid.com/dashboard/album/?albumuuid=F776F257-92B0-461B-A6A4927077294332"
goldAlbumC.cl = "album"
goldAlbumC.background_color = ""

