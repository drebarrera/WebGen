import modules as mx
import sys
sys.path.append(r'C:\Users\dreba\Documents\GitHub\WebGen\files\Portfolio')
data = mx.Data()
body = mx.Body()

from header import *
from contact import *
from forms import *
from visitInfo import *

data.title = "Dre Barrera | Contact"
data.author = "Andres Barrera"

### OBJECTS ###
# Main
main = mx.C()
container = mx.C()
captionT = mx.T()
formC = mx.C()
title = mx.T()
contact = mx.C()
form = mx.X()

### CONTENT ###
# Body
body.content = [main]

# Main
main.content = [nav, container]

# Container
container.content = [title, captionT, formC]
captionT.content = 'Feel free to reach out to me via the form below, directly at <a href="mailto:drebarrera@yahoo.com" class="pseudoLink">drebarrera@yahoo.com</a> (<em>ugh! I know it&#39;s Yahoo.. you&#39;ll get over it</em>), or give me a call at <a href="tel:12105856279" class="pseudoLink">+1 (210) 585-6279</a>. Don&#39;t be shy to leave a voicemail! I will do my best to get back to you within 24 hours on the next business day.<br><br>'
formC.content = [contact]
title.content = 'What&#39;s On Your Mind...'
contact.content = [form]
form.content = '<form method="post" action="index.php"><label for="name">Your Name</label><input type="text" name="name" placeholder="First and last, please!" required><label for="email">E-Mail Address</label><input type="text" name="email" placeholder="johnnyappleseed@gmail.com" required><label for="phone">Phone Number</label><input type="text" name="phone" placeholder="In case you&#39;d like a call back"><label for="message">Subject</label><textarea name="message" type="text" placeholder="Write something.." style="height:200px" required></textarea><input type="submit" value="Submit" name="submit"></form><p style="color: white;"><?=$thankyou ?></p>'

### PROPERTIES ###
# Body
body.background_color = "#fefefe"

# Main
main.id = "main"
main.background_color = ""

# Caption
container.id = "container"
container.background_color = ""

# Form
formC.id = "form"
formC.background_color = ""
title.id = "title"
contact.id = "contact"
contact.background_color = "#005580"
