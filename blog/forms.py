from blog.models import ContactMessage
from django import forms
from django.forms import models

class ContactForm(models.ModelForm):
    class Meta:
        model = ContactMessage
        fields = '__all__'
        exclude = []

    def _init_(self, *args, **kwargs):
        super(ContactForm, self)._init_(*args, **kwargs)
        # self.helper = FormHelper()
        # self.helper.form_show_labels = False
        # for visible in self.visible_fields():
        #     visible.field.widget.attrs['class'] = 'wpcf7-form-control'