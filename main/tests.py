from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Education


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Sedang berlangsung")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Selesai")
        self.assertNotContains(response, "Sedang berlangsung")

class EducationTest(TestCase):
    def setUp(self):
        self.url = '/education/' 

    #Kasus 1: URL dapat diakses dan menggunakan template yang tepat
    def test_url_accessible_and_correct_template(self):
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'education.html') 

    #Kasus 2: Data model muncul di halaman HTML ketika ada data
    def test_education_data_displayed_when_exists(self):
        #buat data baru
        Education.objects.create(
            institution_name="Universitas Indonesia",
            description="Mahasiswa S1 Ilmu Komputer.",
            education_levels="kuliah",
            started_at="2025",
            ended_at="Sekarang"
        )
        
        response = self.client.get(self.url)
        #cek apakah benar benar ada
        self.assertContains(response, "Universitas Indonesia")
        self.assertContains(response, "Mahasiswa S1 Ilmu Komputer.")

    # Kriteria 3: Halaman HTML menampilkan pesan kondisi kosong ketika belum ada data
    def test_education_empty_state_message(self):
        #pastikan database kosong
        Education.objects.all().delete()
        
        response = self.client.get(self.url)
        
        self.assertContains(response, "Belum ada Pendidikan yang ditambahkan.")