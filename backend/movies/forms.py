from django import forms
from .models import CinemaRoom

class CinemaRoomForm(forms.ModelForm):
    """
    Customized form to add rows of cinema more simply
    """
    rows_str = forms.CharField(
        label='Filas (separadas por comas)',
        help_text='EJ: A,B,C',
        required=True
    )
    
    class Meta:
        model = CinemaRoom
        fields = ['cinema', 'room_name', 'seats_per_row']
    
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.rows:
            self.fields['rows_str'].initial = ','.join(self.instance.rows)
    
    def clean_rows_str(self):
        data = self.cleaned_data['rows_str']
        rows_list = [r.strip() for r in data.split(',') if r.strip()]
        
        if not rows_list:
            raise forms.ValidationError("Debes ingresar al menos una fila.")
        return rows_list
    
    def save(self, commit = True):
        instance  = super().save(commit=False)
        instance.rows = self.cleaned_data['rows_str']
        if commit:
            instance.save()
        return instance