# =============================================================================
# IMPORTS
# =============================================================================

# Django Imports
from django import forms

# =============================================================================
# CLASSES
# =============================================================================

class ManifestForm(forms.Form):
    manifest = forms.FileField(
        label='Select a XML manifest file.',
    )