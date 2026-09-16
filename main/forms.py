from django.forms import ModelForm, TextInput, Textarea, URLInput

from main.models import Education

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "institution_name",
            "description",
            "education_levels",
            "thumbnail",
            "started_at",
            "ended_at"
        ]

        labels = {
            "institution_name": "Nama Sekolah",
            "description": "Deskripsi Sekolah",
            "education_levels": "Tingkatan Sekolah",
            "thumbnail": "Gambar Sekolah",
            "started_at": "Tahun Masuk",
            "ended_at" : "Tahun Selesai"
        }

        widgets = {
            "institution_name": TextInput(
                attrs={
                    "placeholder": "Nama Sekolah",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Sekolahmu",
                    "rows": 3,
                }
            ),
            "education_levels": TextInput(
                attrs={
                    "placeholder": "Elementary School, Junior High School, Senior High School, College",
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }