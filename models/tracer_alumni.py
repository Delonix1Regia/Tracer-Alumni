from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Pengguna(models.Model):
    _name = 'tracer_alumni.pengguna'
    _description = 'Data Pengguna Alumni'

    name = fields.Char(string='Nama', required=True)
    nim = fields.Char(string='NIM', required=True)
    fakultas_id = fields.Many2one('tracer_alumni.fakultas', string='Fakultas', required=True)
    prodi_id = fields.Many2one('tracer_alumni.prodi', string='Program Studi', required=True)
    nomor_telepon = fields.Char(string='Nomor Telepon/HP', required=True)
    email = fields.Char(string='Email', required=True)
    alamat_rumah = fields.Text(string='Alamat Rumah', required=True)
    tahun_lulus = fields.Char(string='Tahun Lulus', required=True)

    status = fields.Selection(
    [
        ('bekerja', 'Bekerja (full time/part time)'),
        ('wiraswasta', 'Wiraswasta'),
        ('melanjutkan_pendidikan', 'Melanjutkan Pendidikan'),
        ('tidak_bekerja', 'Tidak bekerja tetapi sedang mencari kerja')
    ],
        string='Status',
        required=True,
)


    # Fields for Bekerja
    kategori_instansi = fields.Selection([
        ('pemerintah', 'Lembaga Pemerintah'),
        ('bumn', 'Perusahaan Nasional/BUMN/BUMD'),
        ('internasional', 'Perusahaan Internasional'),
        ('swasta', 'Lembaga Swasta'),
        ('sosial', 'Lembaga Sosial/Organisasi non-profit')
    ], string='Kategori Instansi/Perusahaan')
    nama_instansi = fields.Char(string='Nama Instansi/Perusahaan')
    nama_atasan = fields.Char(string='Nama Atasan')
    email_atasan = fields.Char(string='Email Atasan')
    no_telp_instansi = fields.Char(string='No. Telp Instansi')
    alamat_instansi = fields.Text(string='Alamat Instansi')
    bidang_kerja = fields.Char(string='Bidang Kerja/Usaha')
    status_usaha = fields.Selection([
        ('aktif', 'Aktif'),
        ('tidak_aktif', 'Tidak Aktif'),
    ], string='Status Usaha')    
    waktu_tunggu = fields.Selection([
        ('0_3_bulan', 'Kira-kira 3 bulan setelah lulus'),
        ('3_6_bulan', 'Kira-kira 3-6 bulan setelah lulus'),
        ('6_12_bulan', 'Kira-kira lebih dari 6-12 bulan setelah lulus'),
        ('lebih_12_bulan', 'Kira-kira lebih dari 12 bulan setelah lulus'),
    ], string='Waktu Tunggu Mendapatkan Pekerjaan Pertama')
    pendapatan = fields.Selection([
        ('0_2juta', 'Rp. 0 – 2.150.000,00'),
        ('2juta_3juta', 'Rp. 2.150.001 – 3.450.000,00'),
        ('3juta_10juta', 'Rp. 3.450.001 – 9.999.999,00'),
        ('lebih_10juta', '≥Rp. 10.000.000,00'),
    ], string='Pendapatan Bulanan')
    hubungan_prodi = fields.Selection([
        ('sangat_erat', 'Erat'),
        ('cukup_erat', 'Cukup Erat'),
        ('kurang_erat', 'Kurang Erat'),
        ('tidak_sama_sekali', 'Tidak Sama Sekali'),
    ], string='Hubungan Bidang Studi dengan Pekerjaan')
    pendidikan_sesuai = fields.Selection([
        ('tidak', 'Tidak Perlu Pendidikan Tinggi'),
        ('rendah', 'Setingkat Lebih Rendah'),
        ('sama', 'Tingkat Yang Sama'),
        ('tinggi', 'Setingkat lebih Tinggi'),
    ], string='Tingkat Pendidikan Paling Tepat')
    tingkat_etika = fields.Selection([
        ('sangat_tinggi', 'Sangat Tinggi'),
        ('tinggi', 'Tinggi'),
        ('cukup', 'Cukup'),
        ('rendah', 'Rendah'),
        ('sangat_rendah', 'Sangat Rendah'),
    ], string='Tingkat Etika Diperlukan pada Pekerjaan Anda')

    keahlian_bidang_ilmu = fields.Selection([
        ('sangat_tinggi', 'Sangat Tinggi'),
        ('tinggi', 'Tinggi'),
        ('cukup', 'Cukup'),
        ('rendah', 'Rendah'),
        ('sangat_rendah', 'Sangat Rendah'),
    ], string='Keahlian Berdasarkan Bidang Ilmu')

    penguasaan_bahasa_asing = fields.Selection([
        ('sangat_tinggi', 'Sangat Tinggi'),
        ('tinggi', 'Tinggi'),
        ('cukup', 'Cukup'),
        ('rendah', 'Rendah'),
        ('sangat_rendah', 'Sangat Rendah'),
    ], string='Penguasaan Bahasa Asing')

    penguasaan_teknologi_informasi = fields.Selection([
        ('sangat_tinggi', 'Sangat Tinggi'),
        ('tinggi', 'Tinggi'),
        ('cukup', 'Cukup'),
        ('rendah', 'Rendah'),
        ('sangat_rendah', 'Sangat Rendah'),
    ], string='Penguasaan Teknologi Informasi')

    kemampuan_berkomunikasi = fields.Selection([
        ('sangat_tinggi', 'Sangat Tinggi'),
        ('tinggi', 'Tinggi'),
        ('cukup', 'Cukup'),
        ('rendah', 'Rendah'),
        ('sangat_rendah', 'Sangat Rendah'),
    ], string='Kemampuan Berkomunikasi')

    kerjasama_tim = fields.Selection([
        ('sangat_tinggi', 'Sangat Tinggi'),
        ('tinggi', 'Tinggi'),
        ('cukup', 'Cukup'),
        ('rendah', 'Rendah'),
        ('sangat_rendah', 'Sangat Rendah'),
    ], string='Kerjasama Tim')

    tingkat_pengembangan_diri = fields.Selection([
        ('sangat_tinggi', 'Sangat Tinggi'),
        ('tinggi', 'Tinggi'),
        ('cukup', 'Cukup'),
        ('rendah', 'Rendah'),
        ('sangat_rendah', 'Sangat Rendah'),
    ], string='Tingkat Pengembangan Diri dalam Pekerjaan Anda')

    saran_kurikulum = fields.Text(string='Saran/Masukan untuk Perbaikan Kurikulum Program Studi')

    # Fields for Wiraswasta
    posisi_wiraswasta = fields.Selection([
        ('founder', 'Founder'),
        ('direktur', 'Direktur/Manager'),
        ('supervisor', 'Supervisor'),
        ('staff', 'Staff'),
        ('freelance', 'Freelance/Kerja Lepas')
    ], string='Posisi/Jabatan Saat Ini')
    tingkat_usaha = fields.Selection([
        ('lokal', 'Lokal/Wilayah'),
        ('nasional', 'Nasional'),
        ('multinasional', 'Multinasional'),
        ('internasional', 'Internasional')
    ], string='Tingkat Usaha/Tempat Kerja')
    waktu_tunggu_kerja_pertama = fields.Selection([
    ('kurang_3_bulan', 'Kira-kira 3 bulan setelah lulus'),
    ('3_6_bulan', 'Kira-kira 3-6 bulan setelah lulus'),
    ('6_12_bulan', 'Kira-kira lebih dari 6 s.d 12 bulan setelah lulus'),
    ('lebih_12_bulan', 'Kira-kira lebih dari 12 bulan setelah lulus'),
    ], string='Berapa Lama Waktu Tunggu untuk Mendapatkan Pekerjaan Pertama')

    rata_rata_pendapatan = fields.Selection([
        ('0_2150000', 'Rp. 0 – 2.150.000,00'),
        ('2150001_3450000', 'Rp. 2.150.001 – 3.450.000,00'),
        ('3450001_9999999', 'Rp. 3.450.001 – 9.999.999,00'),
        ('lebih_10000000', '≥Rp. 10.000.000,00'),
    ], string='Berapa Rata-Rata Pendapatan Anda Per Bulan? (Take Home Pay)')

    hubungan_bidang_studi_pekerjaan = fields.Selection([
        ('tidak_sama_sekali', 'Tidak Sama Sekali'),
        ('kurang_erat', 'Kurang Erat'),
        ('cukup_erat', 'Cukup Erat'),
        ('erat', 'Erat'),
    ], string='Seberapa Erat Hubungan antara Bidang Studi dengan Pekerjaan Anda?')

    pendidikan_sesuai_pekerjaan = fields.Selection([
        ('tidak_perlu', 'Tidak Perlu Pendidikan Tinggi'),
        ('lebih_rendah', 'Setingkat Lebih Rendah'),
        ('sama', 'Tingkat Yang Sama'),
        ('lebih_tinggi', 'Setingkat Lebih Tinggi'),
    ], string='Tingkat Pendidikan Apa yang Paling Tepat/Sesuai untuk Pekerjaan Anda Saat Ini')

    tingkat_etika = fields.Selection([
        ('sangat_tinggi', 'Sangat Tinggi'),
        ('tinggi', 'Tinggi'),
        ('cukup', 'Cukup'),
        ('rendah', 'Rendah'),
        ('sangat_rendah', 'Sangat Rendah'),
    ], string='Tingkat Etika Diperlukan Pada Pekerjaan Anda')

    keahlian_bidang_ilmu = fields.Selection([
        ('sangat_tinggi', 'Sangat Tinggi'),
        ('tinggi', 'Tinggi'),
        ('cukup', 'Cukup'),
        ('rendah', 'Rendah'),
        ('sangat_rendah', 'Sangat Rendah'),
    ], string='Keahlian Berdasarkan Bidang Ilmu')

    penguasaan_bahasa_asing = fields.Selection([
        ('sangat_tinggi', 'Sangat Tinggi'),
        ('tinggi', 'Tinggi'),
        ('cukup', 'Cukup'),
        ('rendah', 'Rendah'),
        ('sangat_rendah', 'Sangat Rendah'),
    ], string='Penguasaan Bahasa Asing')

    penguasaan_teknologi_informasi = fields.Selection([
        ('sangat_tinggi', 'Sangat Tinggi'),
        ('tinggi', 'Tinggi'),
        ('cukup', 'Cukup'),
        ('rendah', 'Rendah'),
        ('sangat_rendah', 'Sangat Rendah'),
    ], string='Penguasaan Teknologi Informasi')

    kemampuan_berkomunikasi = fields.Selection([
        ('sangat_tinggi', 'Sangat Tinggi'),
        ('tinggi', 'Tinggi'),
        ('cukup', 'Cukup'),
        ('rendah', 'Rendah'),
        ('sangat_rendah', 'Sangat Rendah'),
    ], string='Kemampuan Berkomunikasi')

    kerjasama_tim = fields.Selection([
        ('sangat_tinggi', 'Sangat Tinggi'),
        ('tinggi', 'Tinggi'),
        ('cukup', 'Cukup'),
        ('rendah', 'Rendah'),
        ('sangat_rendah', 'Sangat Rendah'),
    ], string='Kerjasama Tim')

    tingkat_pengembangan_diri = fields.Selection([
        ('sangat_tinggi', 'Sangat Tinggi'),
        ('tinggi', 'Tinggi'),
        ('cukup', 'Cukup'),
        ('rendah', 'Rendah'),
        ('sangat_rendah', 'Sangat Rendah'),
    ], string='Tingkat Pengembangan Diri dalam Pekerjaan Anda')

    saran_kurikulum = fields.Text(string='Apa Saran/Masukan Anda untuk Perbaikan Kurikulum Program Studi?')


    # Fields for Lanjut Pendidikan
    jenjang_pendidikan = fields.Selection([
        ('magister', 'Magister/Doktor'),
        ('profesi', 'Pendidikan Profesi'),
        ('sama', 'Tingkat Yang Sama'),
        ('lebih_tinggi', 'Setingkat lebih Tinggi')
    ], string='Jenjang Pendidikan')
    tingkat_etika = fields.Selection([
    ('sangat_tinggi', 'Sangat Tinggi'),
    ('tinggi', 'Tinggi'),
    ('cukup', 'Cukup'),
    ('rendah', 'Rendah'),
    ('sangat_rendah', 'Sangat Rendah'),
    ], string='Tingkat Etika Diperlukan Pada Pekerjaan Anda')

    keahlian_bidang_ilmu = fields.Selection([
        ('sangat_tinggi', 'Sangat Tinggi'),
        ('tinggi', 'Tinggi'),
        ('cukup', 'Cukup'),
        ('rendah', 'Rendah'),
        ('sangat_rendah', 'Sangat Rendah'),
    ], string='Keahlian Berdasarkan Bidang Ilmu')

    penguasaan_bahasa_asing = fields.Selection([
        ('sangat_tinggi', 'Sangat Tinggi'),
        ('tinggi', 'Tinggi'),
        ('cukup', 'Cukup'),
        ('rendah', 'Rendah'),
        ('sangat_rendah', 'Sangat Rendah'),
    ], string='Penguasaan Bahasa Asing')

    penguasaan_teknologi_informasi = fields.Selection([
        ('sangat_tinggi', 'Sangat Tinggi'),
        ('tinggi', 'Tinggi'),
        ('cukup', 'Cukup'),
        ('rendah', 'Rendah'),
        ('sangat_rendah', 'Sangat Rendah'),
    ], string='Penguasaan Teknologi Informasi')

    kemampuan_berkomunikasi = fields.Selection([
        ('sangat_tinggi', 'Sangat Tinggi'),
        ('tinggi', 'Tinggi'),
        ('cukup', 'Cukup'),
        ('rendah', 'Rendah'),
        ('sangat_rendah', 'Sangat Rendah'),
    ], string='Kemampuan Berkomunikasi')

    kerjasama_tim = fields.Selection([
        ('sangat_tinggi', 'Sangat Tinggi'),
        ('tinggi', 'Tinggi'),
        ('cukup', 'Cukup'),
        ('rendah', 'Rendah'),
        ('sangat_rendah', 'Sangat Rendah'),
    ], string='Kerjasama Tim')

    tingkat_pengembangan_diri = fields.Selection([
        ('sangat_tinggi', 'Sangat Tinggi'),
        ('tinggi', 'Tinggi'),
        ('cukup', 'Cukup'),
        ('rendah', 'Rendah'),
        ('sangat_rendah', 'Sangat Rendah'),
    ], string='Tingkat Pengembangan Diri dalam Pekerjaan Anda')

    saran_kurikulum = fields.Text(string='Apa Saran/Masukan Anda untuk Perbaikan Kurikulum Program Studi?')


    # Fields for Tidak Kerja
    tingkat_etika = fields.Selection([
    ('sangat_tinggi', 'Sangat Tinggi'),
    ('tinggi', 'Tinggi'),
    ('cukup', 'Cukup'),
    ('rendah', 'Rendah'),
    ('sangat_rendah', 'Sangat Rendah'),
    ], string='Tingkat Etika Diperlukan Pada Pekerjaan Anda')

    keahlian_bidang_ilmu = fields.Selection([
        ('sangat_tinggi', 'Sangat Tinggi'),
        ('tinggi', 'Tinggi'),
        ('cukup', 'Cukup'),
        ('rendah', 'Rendah'),
        ('sangat_rendah', 'Sangat Rendah'),
    ], string='Keahlian Berdasarkan Bidang Ilmu')

    penguasaan_bahasa_asing = fields.Selection([
        ('sangat_tinggi', 'Sangat Tinggi'),
        ('tinggi', 'Tinggi'),
        ('cukup', 'Cukup'),
        ('rendah', 'Rendah'),
        ('sangat_rendah', 'Sangat Rendah'),
    ], string='Penguasaan Bahasa Asing')

    penguasaan_teknologi_informasi = fields.Selection([
        ('sangat_tinggi', 'Sangat Tinggi'),
        ('tinggi', 'Tinggi'),
        ('cukup', 'Cukup'),
        ('rendah', 'Rendah'),
        ('sangat_rendah', 'Sangat Rendah'),
    ], string='Penguasaan Teknologi Informasi')

    kemampuan_berkomunikasi = fields.Selection([
        ('sangat_tinggi', 'Sangat Tinggi'),
        ('tinggi', 'Tinggi'),
        ('cukup', 'Cukup'),
        ('rendah', 'Rendah'),
        ('sangat_rendah', 'Sangat Rendah'),
    ], string='Kemampuan Berkomunikasi')

    kerjasama_tim = fields.Selection([
        ('sangat_tinggi', 'Sangat Tinggi'),
        ('tinggi', 'Tinggi'),
        ('cukup', 'Cukup'),
        ('rendah', 'Rendah'),
        ('sangat_rendah', 'Sangat Rendah'),
    ], string='Kerjasama Tim')

    tingkat_pengembangan_diri = fields.Selection([
        ('sangat_tinggi', 'Sangat Tinggi'),
        ('tinggi', 'Tinggi'),
        ('cukup', 'Cukup'),
        ('rendah', 'Rendah'),
        ('sangat_rendah', 'Sangat Rendah'),
    ], string='Tingkat Pengembangan Diri dalam Pekerjaan Anda')

    saran_kurikulum = fields.Text(string='Apa Saran/Masukan Anda untuk Perbaikan Kurikulum Program Studi?')



    # Onchange logic
    @api.onchange('status')
    def _onchange_status(self):
        if self.status != 'bekerja':
            self._reset_bekerja_fields()
        if self.status != 'wiraswasta':
            self._reset_wiraswasta_fields()
        if self.status != 'lanjut_pendidikan':
            self._reset_lanjut_pendidikan_fields()
        if self.status != 'tidak_bekerja':
            self._reset_tidak_bekerja_fields()

    def _reset_bekerja_fields(self):
        self.kategori_instansi = False
        self.nama_instansi = False
        self.nama_atasan = False
        self.email_atasan = False
        self.no_telp_instansi = False
        self.alamat_instansi = False
        self.bidang_kerja = False
        self.status_usaha = False
        self.waktu_tunggu = False
        self.pendapatan = False
        self.hubungan_prodi = False
        self.pendidikan_sesuai = False
        self.tingkat_etika = False
        self.keahlian_bidang_ilmu = False
        self.penguasaan_bahasa_asing = False
        self.penguasaan_teknologi_informasi = False
        self.kemampuan_berkomunikasi = False
        self.kerjasama_tim = False
        self.tingkat_pengembangan_diri = False
        self.saran_kurikulum = False

    def _reset_wiraswasta_fields(self):
        self.posisi_wiraswasta = False
        self.tingkat_usaha = False
        self.waktu_tunggu_kerja_pertama = False
        self.rata_rata_pendapatan = False
        self.hubungan_bidang_studi_pekerjaan = False
        self.pendidikan_sesuai_pekerjaan = False
        self.tingkat_etika = False
        self.keahlian_bidang_ilmu = False
        self.penguasaan_bahasa_asing = False
        self.penguasaan_teknologi_informasi = False
        self.kemampuan_berkomunikasi = False
        self.kerjasama_tim = False
        self.tingkat_pengembangan_diri = False
        self.saran_kurikulum = False

    def _reset_lanjut_pendidikan_fields(self):
        self.jenjang_pendidikan = False
        self.tingkat_etika = False
        self.keahlian_bidang_ilmu = False
        self.penguasaan_bahasa_asing = False
        self.penguasaan_teknologi_informasi = False
        self.kemampuan_berkomunikasi = False
        self.kerjasama_tim = False
        self.tingkat_pengembangan_diri = False
        self.saran_kurikulum = False
    
    def _reset_tidak_bekerja_fields(self):
        self.tingkat_etika = False
        self.keahlian_bidang_ilmu = False
        self.penguasaan_bahasa_asing = False
        self.penguasaan_teknologi_informasi = False
        self.kemampuan_berkomunikasi = False
        self.kerjasama_tim = False
        self.tingkat_pengembangan_diri = False
        self.saran_kurikulum = False


    # Constraint for Email Validation
    @api.constrains('email')
    def _check_email(self):
        for record in self:
            if record.email and '@' not in record.email:
                raise ValidationError('Alamat email tidak valid: %s' % record.email)
