from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.db import models
from oscar.core.compat import AUTH_USER_MODEL

# from oscar.apps.catalogue.models import Product


class Designer(models.Model):
    designer = models.ForeignKey(AUTH_USER_MODEL, limit_choices_to={'is_designer': True},
                                 verbose_name=_("Designer Email"), null=True, blank=True, unique=True)

    slug = models.SlugField(_('Slug'), max_length=255, editable=False)

    def save(self, *args, **kwargs):
        self.slug = self.designer.username
        super(Designer, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('designer:profile', kwargs={'designer_slug': self.slug, 'pk': self.designer.id})

    def __unicode__(self):
        return unicode(self.designer.get_full_name())
        

class DesPostCategory(models.Model):
    designer = models.ForeignKey(Designer, related_name='desig')
    name = models.CharField(max_length=30, default='default')
    date_created = models.DateTimeField(_('Date created'), auto_now_add=True, null=True)

    class Meta:
        unique_together = ("designer", "name")
        verbose_name = _("Post Category")
        verbose_name_plural = _("Post Categories")

    def __unicode__(self):
        return unicode(self.name)


class DesignerPost(models.Model):
    

    category = models.ForeignKey(DesPostCategory, related_name="categ", null=True)
    name = models.CharField(_('Name'), max_length=30, unique=True)
    designer = models.ForeignKey('Designer', related_name="des", null=True)
    post_status = models.CharField(_('Post Status'), max_length=30, blank=True)
    description = models.TextField()
    date_created = models.DateTimeField(_('Date created'), auto_now_add=True, null=True)
    last_edited = models.DateTimeField(_('Last edited'), auto_now_add=True, null=True)
    
    class Meta:
        verbose_name = _("Designer Post")
        verbose_name_plural = _("Designer Posts")

    def __unicode__(self):
        post_description = '%s: %s' % (self.designer, self.name)
        return unicode(post_description)

class DesPostImage(models.Model):
    post = models.ForeignKey(DesignerPost, related_name='postimage')
    image = models.ImageField(upload_to='Designer/Post/Images', blank=True, null=True)


class DesVideoUrl(models.Model):
    post = models.ForeignKey(DesignerPost, related_name='postvideo')
    video_url = models.URLField(blank=True)
	



