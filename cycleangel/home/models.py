from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField 
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks  
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from cycleangel.blocks import SectionBlock, SectionBackgroundBlock


class HomePage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('section', SectionBlock()),
        ('sectionBackground', SectionBackgroundBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
        ]