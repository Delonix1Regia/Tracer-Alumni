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
    status_usaha = fields.Char(string='Status Usaha')

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
    bidang_usaha = fields.Char(string="Bidang Usaha")

    # Fields for Lanjut Pendidikan
    jenjang_pendidikan = fields.Selection([
        ('magister', 'Magister/Doktor'),
        ('profesi', 'Pendidikan Profesi'),
        ('sama', 'Tingkat Yang Sama'),
        ('lebih_tinggi', 'Setingkat lebih Tinggi')
    ], string='Jenjang Pendidikan')

    # Onchange logic
    @api.onchange('status')
    def _onchange_status(self):
        if self.status != 'bekerja':
            self._reset_bekerja_fields()
        if self.status != 'wiraswasta':
            self._reset_wiraswasta_fields()
        if self.status != 'lanjut_pendidikan':
            self._reset_lanjut_pendidikan_fields()

    def _reset_bekerja_fields(self):
        self.kategori_instansi = False
        self.nama_instansi = False
        self.nama_atasan = False
        self.email_atasan = False
        self.no_telp_instansi = False
        self.alamat_instansi = False
        self.bidang_kerja = False
        self.status_usaha = False

    def _reset_wiraswasta_fields(self):
        self.posisi_wiraswasta = False
        self.tingkat_usaha = False

    def _reset_lanjut_pendidikan_fields(self):
        self.jenjang_pendidikan = False

    # Constraint for Email Validation
    @api.constrains('email')
    def _check_email(self):
        for record in self:
            if record.email and '@' not in record.email:
                raise ValidationError('Alamat email tidak valid: %s' % record.email)
