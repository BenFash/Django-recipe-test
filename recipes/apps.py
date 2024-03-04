from django.apps import AppConfig

# Class to configure built in django app config app 
class RecipesConfig(AppConfig):
    #  Explicitly specify the auto field for app config.
    # Here, it's set to django.db.models.BigAutoField, which is suitable for databases that support 64-bit integers for auto-incrementing primary keys
    default_auto_field = "django.db.models.BigAutoField"
    #s Sets the name of the Django app to "recipes". This is the name used to refer to the app within Django's infrastructure
    name = "recipes"
