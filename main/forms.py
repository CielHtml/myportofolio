from django.forms import ModelForm, TextInput, Textarea, URLInput

from main.models import Education, Experience

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

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            "ended_at",
        ]

        labels = {
            "title" : "Nama Pengalaman",
            "description" : "Deskripsi Pengalaman",
            "category" : "Jenis Pengalaman",
            "thumbnail" : "Gambar Pendukung",
            "ended_at" : "Berakhirnya Pengalaman"
        }

        widgets = {
            "title" : TextInput(
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

            "category": TextInput(
                attrs={
                    "placeholder": "internship, research, volunteer, part-time, full-time, freelance",
                }
            ),

            "ended_at" : TextInput(
                attrs={
                    "placeholder": "Tahun Berakhir",
                    "maxlength": 4,
                }
            ),

            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }