from django.db import models
from wagtail.admin.panels import FieldPanel  # affiche un champ dans l'admin
from wagtail.fields import RichTextField      # champ texte avec mise en forme (gras, listes, liens...)
from wagtail.models import Page


class HomePage(Page):
    accroche = models.CharField(max_length=255, blank=True)  # une ligne de texte, 255 caractères max
    introduction = RichTextField(blank=True)
    
    #booléen (True or False)
    disponible = models.BooleanField(default=False)

    #décimal avec nombre spécificité
    prix = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    # liste des champs visibles dans l'onglet "Contenu" de l'admin
    # sans FieldPanel ici, un champ du modèle reste invisible dans l'admin
    content_panels = Page.content_panels + [
        FieldPanel("accroche"),
        FieldPanel("introduction"),
        FieldPanel("disponible"),
        FieldPanel("prix")
    ]