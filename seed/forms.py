from django import forms
from django.forms import ModelForm

from .models import *
from contact.models import *

from .widgets import *
from .errors import *

from django.utils.translation import gettext_lazy as _


class BusinessDivisionForm(ModelForm):
    class Meta:
        model = BusinessDivision
        fields = '__all__'
    # FIELD = (('s', 'seeds'), ('f2', 'field2'), ('f3', 'field3'))
    # business_field = forms.ChoiceField(choices=FIELD)
    # TYPE = (('o', 'Open Pollinated'),('h', 'Hybrid'),('b', 'Both'))
    # type = forms.ChoiceField(choices=TYPE)
    # type.widget.attrs.update(size=40)
    # global_crop = forms.CharField()
    # crop_family = forms.CharField()
    # product_hipe = forms.CharField()

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # for author in YourAuthorModel.objects.all():
    #     #     author_choices.append((author.author_name, author.author_name))
    #     self.fields['business_field'].widget.choices = [('s', 'seeds'), ('f2', 'field2'), ('f3', 'field3')]

    # class Meta:
    #     model = BusinessDivision
    #     fields = '__all__'


class GlobalCropForm(ModelForm):
    class Meta:
        model = GlobalCrop
        fields = '__all__'


class CropFamilyForm(ModelForm):
    class Meta:
        model = CropFamily
        fields = '__all__'


class ProductTypeForm(ModelForm):
    class Meta:
        model = ProductType
        fields = '__all__'


class SpeciesForm(ModelForm):
    class Meta:
        model = Species
        fields = '__all__'

    def __int__(self, *args, **kwargs):
        super(SpeciesForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'id': 'id_'+name})


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=10)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class myModelForm(ModelForm):
    class Meta:
        model = myModel
        fields = '__all__'


class Model2Form(ModelForm):
    class Meta:
        model = Model2
        fields = '__all__'


class ImageForm(ModelForm):
    class Meta:
        model = SpeciesImage
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super(ImageForm, self).__init__(*args, **kwargs)
    #     self.fields['photo'].required = False


class AddIconImageFeild(forms.ImageField):
    def clean(self, value):
        return value


# from seed.widgets import CountableWidget, ToggleWidget, Select2Widget, Select2MultipleWidget, DropzoneWidget, ImageWithAddWidget


class VarietyImageForm2(forms.Form):
    variety = forms.CharField()
    title = forms.CharField()
    photo = forms.ImageField()
    legend = forms.CharField()
    test = forms.CharField(widget=ToggleWidget(required=False, options={'on': 'Yep', 'off': 'Nope'}))
    countries = [
        ('id', 'Indonesia'),
        ('sar', 'Saudi Arabia'),
        ('usa', 'United Stated')
    ]
    country = forms.ChoiceField(choices=countries, widget=Select2Widget)
    hobbies = [
        ('fishing', 'Fishing'),
        ('writing', 'Writing'),
        ('coding', 'Coding')
    ]
    hobby = forms.MultipleChoiceField(
        choices=hobbies,
        widget=Select2MultipleWidget(
            options={
                'placeholder': 'Your placeholder',
                'multiple': True,
                'maximum-selection-length': 1
            }
        )
    )
    image2 = forms.FileField(
        widget=DropzoneWidget(
            options={
                'url': '/hello',  # not exists yet :D
                'addRemoveLinks': True,
                'dictDefaultMessage': 'Upload your image here'
            },
        ),
        required=False
    )
    image3 = forms.FileField(
        widget=ImageWithAddWidget(
            # options={'dictDefaultMessage': 'Upload your image here'
            #          },
        ),
        required=False
    )

    def __init__(self, *args, **kwargs):
        super(VarietyImageForm2, self).__init__(*args, **kwargs)
        # self.fields['test'].widget =
        # self.fields['test'].widget =...
        # CountableWidget(attrs={'data-min-count': 10,
        #                        'data-max-count': 100})

    # class Meta:
    # model = VarietyImage
    # fields = '__all__


class VarietySupplierForm(ModelForm):
    class Meta:
        model = VarietySupplier
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['contact_person'].queryset = Person.objects.none()
    #     # self.fields['entity'].queryset = Entity.objects.none()


class VarietyBaseDataForm(ModelForm):
    class Meta:
        model = VarietyBaseData
        fields = '__all__'

from dal import autocomplete
class VarietyForm(ModelForm):
    #below commented code is an eaxmple of the Autocomplete Select
    # product_type = forms.ModelChoiceField(
    #     queryset=ProductType.objects.all(),
    #     widget=autocomplete.ModelSelect2(url='auto-view')
    # )
    class Meta:
        model = Variety
        fields = '__all__'
        # widgets = {'photo':ImageWithAddWidget,'product_type':RelatedFieldWidgetWrapper}
        widgets = {'photo':ImageWithAddWidget, 'product_type': SelectWithAddWidget, 'supplier_contact': SelectWithAddContactWidget}
        error_messages = {
            'crop_family':{'required': _('My error')},
        }

    def __init__(self, *args, **kwargs):
        ## add a "form-control" class to each form input
        super(VarietyForm, self).__init__(*args, **kwargs)
        self.error_class = SpaceProhibited
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                # 'class': 'form-control',
                'id': 'id_'+name
            })
        # self.fields['photo'].widget.attrs.update({
        #     'type': 'input',
        #     'class': 'material-icons',
        # })
        #
        # def clean_variety_supplier_id(self):
        #     variety_supplier_id = self.cleaned_data['variety_supplier_id']
        #     if len(variety_supplier_id) < 4:
        #         raise forms.ValidationError("It is too short")
        #     return variety_supplier_id


class VarietyImageForm(ModelForm):
    class Meta:
        model = VarietyImage
        fields = '__all__'


class VarietyFieldForm(ModelForm):
    class Meta:
        model = VarietyField
        fields = '__all__'


class VarietyFieldValueForm(ModelForm):
    class Meta:
        model = VarietyFieldValue
        fields = '__all__'


class ProductLifeCycleForm(ModelForm):
    class Meta:
        model = ProductLifeCycle
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        ## add a "form-control" class to each form input
        super(ProductLifeCycleForm, self).__init__(*args, **kwargs)

        self.fields['global_plc_date'].widget.attrs.update({
            'type': 'text',
            'class': 'datepicker',
        })


class PLCManageForm(ProductLifeCycleForm):
    class Meta:
        model = ProductLifeCycle
        fields = ['variety','global_plc','global_plc_date']


class CountryPLCForm(ModelForm):
    class Meta:
        model = CountryPLC
        fields = '__all__'
