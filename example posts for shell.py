# step 1
python manage.py createsuperuser

# step 2
python manage.py shell

# step3
from django.contrib.auth.models import User

User.objects.all()

me = User.objects.get(username='drake')

from blog.models import Post


Post.objects.all()

# SCP-682: The Hard-to-Destroy Reptile
Post.objects.create(author=me, title='SCP-682 Containment Protocol', text='Weakness: Extreme physical trauma and acid immersion. While it cannot be killed, it can be incapacitated by immersion in hydrochloric acid, which forces its energy into constant regeneration rather than aggression.')
Post.objects.get(title='SCP-682 Containment Protocol').publish()

# SCP-173: The Sculpture
Post.objects.create(author=me, title='SCP-173 Tactical Note', text='Weakness: Constant line of sight. It is immobile while observed. To survive, utilize a three-person rotation for blinking. If alone, do not blink; if forced, keep one eye open while the other closes.')
post = Post.objects.get(title='SCP-173 Tactical Note')
post.publish()

# SCP-096: The "Shy Guy"
Post.objects.create(author=me, title='SCP-096 Neutralization Guide', text='Weakness: Blindness or obstructed view. 096 only enters a rage state if its face is viewed. Use SCRAMBLE gear (high-tech goggles that blur its face in real-time) to engage without triggering a terminal response.')

# SCP-106: The Old Man
Post.objects.create(author=me, title='SCP-106 Extraction Strategy', text='Weakness: High-frequency sound and complex lead-lined structures. It is deterred by sudden, intense light and high-pitched noise. Containment is maintained via the "Recall Protocol" involving the physical distress of a human subject to lure it back.')

# SCP-2845: THE DEER
Post.objects.create(author=me, title='SCP-2845 Ritualistic Suppression', text='Weakness: Precise ritualistic procedure. As a literal god, it cannot be harmed by force. It is only held by the "Ceremony of Recital," a series of highly specific, repetitive, and bizarre human performances that "trick" its consciousness into remaining localized.')

Post.objects.get(title='SCP-096 Neutralization Guide').publish()
Post.objects.get(title='SCP-106 Extraction Strategy').publish()
Post.objects.get(title='SCP-2845 Ritualistic Suppression').publish()
