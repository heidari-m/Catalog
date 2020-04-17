from django.urls import path
from . import views
# from django.conf.urls.defaults import *

from wkhtmltopdf.views import PDFTemplateView
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.all_link, name='all'),
    path('auto/',views.AutoView.as_view(),name='auto-view'),
    # path('portfolio/', views.PortfolioListView.as_view(), name='portfolio'),
    path('business/', views.BusinessDivisionListView.as_view(), name='business'),
    # path('business/create', views.BusinessDivisionCreate.as_view(), name='business_create'),
    path('business/create', views.business_division_create, name='business_create'),
    #
    path('global-crop/create', views.global_crop_create, name='global_crop_create'),
    path('crop-family/create', views.crop_family_create, name='crop_family_create'),
    #
    path('species/', views.SpeciesListView.as_view(), name='species'),
    path('species/create', views.SpeciesCreate.as_view(), name='species_create'),
    path('species/<int:pk>', views.SpeciesDetailView.as_view(), name='species-detail'),
    path('species/<int:pk>/update', views.SpeciesUpdate.as_view(), name='species_update'),
    path('species/<int:pk>/delete', views.SpeciesDelete.as_view(), name='species_delete'),
    #
    path('product-type/create', views.product_type_create, name='product-type_create'),
    #
    # path('variety/<slug:str>', views.VarietyDetailView.as_view(), name='variety-detail'),
    path('varieties/', views.VarietyList.as_view(), name='varieties'),
    path('variety/create', views.variety_create, name='variety_create'),
    path('ajax/load-cropfamily', views.load_crop_family, name='ajax-load-cropfamily'),
    path('ajax/load-species', views.load_species, name='ajax-load-species'),
    path('variety/<slug:str>/update', views.VarietyUpdate.as_view(), name='variety_update'),
    path('ajax/load-product-type', views.load_product_type, name='ajax-load-product-type'),
    # path('variety/<slug:str>/update', views.variety_update, name='variety_update'),
    #
    path(r'^ajax/validate_name', views.validate_variety_supplier_name, name='validate-variety-supplier-name'),
    #
    path('variety/image/create', views.variety_image_create, name='variety-image-create'),
    #
    # path('variety/tmp', views.tmp, name='tmp'),
    #
    path('tmp/', views.tmp, name='tmp'),
    #
    path('ajax/load-supplier/', views.variety_supplier_detail2, name='ajax_load_supplier'),
    #
    path('variety/serial_no', views.variety_serial_no, name='serial_no'),
    path('variety/<slug:str>', views.VarietyDetailView.as_view(), name='variety-detail'),
    #
    path('variety/supplier/create', views.variety_supplier_create, name='variety_supplier_create'),
    path('variety/supplier/create/<slug:str>', views.variety_supplier_create, name='variety_supplier_create'),
    path('variety/supplier/<int:pk>', views.VarietySupplierDetail.as_view(), name='variety-supplier-detail'),
    path('variety/suppliers/', views.VarietySupplierList.as_view(), name='variety-supplier-list'),
    path('variety/suppliers/<int:pk>/update', views.VarietySupplierUpdate.as_view(), name='variety-supplier_update'),
    #
    path('ajax/load-entities/', views.load_contact_entity, name='ajax_load_entities'),
    path('ajax/load-persons/', views.load_contact_person, name='ajax_load_persons'),
    #
    path('ajax/load-basedata/', views.variety_base_data_detail, name='ajax_load_basedata'),
    path('variety/base-data/<int:pk>', views.VarietyBaseDataDetail.as_view() , name='variety-base-data-detail'),
    path('variety/base-data/create/', views.variety_base_data_create, name='variety_base_data_create'),
    path('variety/base-data/create/<slug:str>', views.variety_base_data_create, name='variety_base_data_create'),
    # path('ajax/load-basedata/update', views.variety_basedata_update, name='ajax-load-basedata-update'),
    path('variety/base-data/<int:pk>/update',views.VarietyBaseDataUpdate.as_view(), name='variety-basedata_update'),
    #
    path('plc/create', views.product_life_cycle_create, name='plc_create'),
    path('plc/add/<slug:str>', views.plc_manage_add, name='plc_add'),
    path('plc/', views.ProductLifeCycleList.as_view(), name='product_life_cycle_list'),
    path('plc/<int:pk>', views.ProductLifeCycleDetail.as_view(), name='product_life_cycle_detail'),
    path('plc/<int:pk>/update', views.ProductLifeCycleUpdate.as_view(), name='product_life_cycle_update'),
    path('country-plc/create', views.country_plc_create, name='country_plc_create'),

    #
    path('variety/field/create', views.variety_field_create, name='variety_field_create'),
    path('variety/field/value/create', views.variety_field_value_create, name='variety_field_value_create'),
    # path('variety/validate/', views.validate_username, name='validate'),
    # url(r'^variety/validate/$', views.validate_username, name='validate'),

    # path('variety2/<int:pk>', views.VarietyDetailView.as_view(template_name='seed/invoice.html'), name='variety-detail2'),
    # path('pdf/<int:pk>', views.VarietyDetailView.generate_pdf, name='pdf'),
    path('pdf/<int:pk>', views.GeneratePdf.as_view(), name='pdf'),
    # path('pdf/',views.GeneratePdf.as_view(), name='pdf'),
    # path('pdf/', views.some_view, name='pdf'),
    path('pdf2/<int:pk>', views.GeneratePdf2.as_view()),
    # url(r'^pdf3/$', PDFTemplateView.as_view(template_name='seed/variety_detail.html',filename='my_pdf.pdf'), name='pdf3'),
    # path('pdf3/<int:pk>', PDFTemplateView.as_view(template_name='seed/variety_detail.html', filename='my_pdf.pdf'),
    #      name='variety-detail-pdf'),
    # path('pdf4/<int:pk>', PDFTemplateView.as_view(template_name='seed/species_detail.html', filename='my_pdf4.pdf'),
    #      name='pdf4/1'),
    path('species/<int:pk>/', PDFTemplateView.as_view(template_name='seed/species_detail.html', filename='my_pdf7.pdf'),
         name='pdf7/'),
    # path('species/<int:pk>/1', views.HelloPDFView.as_view()),
    path('mymodel/', views.myModelListView.as_view(), name='mymodel'),
    path('mymodel/create', views.add_myModel, name='mymodel_create'),
    path('mymodel/<int:pk>', views.myModelDeatilView.as_view(), name='myModel-detail'),
    path('model2/create', views.add_model2_createpopup, name='model2-create'),
    path('model2/<int:pk>/edit', views.model2_edit_popup, name='model2-edit'),
    path('model2/ajax/get_model2_id', views.get_model2_id, name='get_model2_id'),
    # url(r'^model2/ajax/get_model2_id', views.get_model2_id, name = "get_model2_id"),
    path('pdf8/', views.generate_pdf, name='generate_pdf'),
    path('images/', views.SpeciesImageListView.as_view(), name='images'),
    # path('image/create', views.ImageCreate.as_view(), name='image_create'),
    path('image/create', views.image_create, name='image_create'),
    path('name/', views.get_name, name='name'),
    # path('contact/',views.handle_this,name='contact'),
]
