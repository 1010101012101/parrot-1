#  encoding=utf-8

"""add locale fixtures

Revision ID: d953381ee580
Revises: bbb34ab1bddf
Create Date: 2018-02-15 22:15:04.815835

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd953381ee580'
down_revision = 'bbb34ab1bddf'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
        INSERT INTO locales (code, language, country)
        VALUES
        ('sq_AL', 'Albanian', 'Albania'),
        ('ar_DZ', 'Arabic', 'Algeria'),
        ('ar_BH', 'Arabic', 'Bahrain'),
        ('ar_EG', 'Arabic', 'Egypt'),
        ('ar_IQ', 'Arabic', 'Iraq'),
        ('ar_JO', 'Arabic', 'Jordan'),
        ('ar_KW', 'Arabic', 'Kuwait'),
        ('ar_LB', 'Arabic', 'Lebanon'),
        ('ar_LY', 'Arabic', 'Libya'),
        ('ar_MA', 'Arabic', 'Morocco'),
        ('ar_OM', 'Arabic', 'Oman'),
        ('ar_QA', 'Arabic', 'Qatar'),
        ('ar_SA', 'Arabic', 'Saudi Arabia'),
        ('ar_SD', 'Arabic', 'Sudan'),
        ('ar_SY', 'Arabic', 'Syria'),
        ('ar_TN', 'Arabic', 'Tunisia'),
        ('ar_AE', 'Arabic', 'United Arab Emirates'),
        ('ar_YE', 'Arabic', 'Yemen'),
        ('be_BY', 'Belarusian', 'Belarus'),
        ('bg_BG', 'Bulgarian', 'Bulgaria'),
        ('ca_ES', 'Catalan', 'Spain'),
        ('zh_CN', 'Chinese (Simplified)', 'China'),
        ('zh_SG', 'Chinese (Simplified)', 'Singapore'),
        ('zh_HK', 'Chinese (Traditional)', 'Hong Kong'),
        ('zh_TW', 'Chinese (Traditional)', 'Taiwan'),
        ('hr_HR', 'Croatian', 'Croatia'),
        ('cs_CZ', 'Czech', 'Czech Republic'),
        ('da_DK', 'Danish', 'Denmark'),
        ('nl_BE', 'Dutch', 'Belgium'),
        ('nl_NL', 'Dutch', 'Netherlands'),
        ('en_AU', 'English', 'Australia'),
        ('en_CA', 'English', 'Canada'),
        ('en_IN', 'English', 'India'),
        ('en_IE', 'English', 'Ireland'),
        ('en_MT', 'English', 'Malta'),
        ('en_NZ', 'English', 'New Zealand'),
        ('en_PH', 'English', 'Philippines'),
        ('en_SG', 'English', 'Singapore'),
        ('en_ZA', 'English', 'South Africa'),
        ('en_GB', 'English', 'United Kingdom'),
        ('en_US', 'English', 'United States'),
        ('et_EE', 'Estonian', 'Estonia'),
        ('fi_FI', 'Finnish', 'Finland'),
        ('fr_BE', 'French', 'Belgium'),
        ('fr_CA', 'French', 'Canada'),
        ('fr_FR', 'French', 'France'),
        ('fr_LU', 'French', 'Luxembourg'),
        ('fr_CH', 'French', 'Switzerland'),
        ('de_AT', 'German', 'Austria'),
        ('de_DE', 'German', 'Germany'),
        ('de_LU', 'German', 'Luxembourg'),
        ('de_CH', 'German', 'Switzerland'),
        ('el_CY', 'Greek', 'Cyprus'),
        ('el_GR', 'Greek', 'Greece'),
        ('iw_IL', 'Hebrew', 'Israel'),
        ('hi_IN', 'Hindi', 'India'),
        ('hu_HU', 'Hungarian', 'Hungary'),
        ('is_IS', 'Icelandic', 'Iceland'),
        ('in_ID', 'Indonesian', 'Indonesia'),
        ('ga_IE', 'Irish', 'Ireland'),
        ('it_IT', 'Italian', 'Italy'),
        ('it_CH', 'Italian', 'Switzerland'),
        ('ja_JP', 'Japanese', 'Japan'),
        ('ko_KR', 'Korean', 'South Korea'),
        ('lv_LV', 'Latvian', 'Latvia'),
        ('lt_LT', 'Lithuanian', 'Lithuania'),
        ('mk_MK', 'Macedonian', 'Macedonia'),
        ('ms_MY', 'Malay', 'Malaysia'),
        ('mt_MT', 'Maltese', 'Malta'),
        ('no_NO', 'Norwegian (Bokmål)', 'Norway'),
        ('no_NO_NY', 'Norwegian (Nynorsk)', 'Norway'),
        ('pl_PL', 'Polish', 'Poland'),
        ('pt_BR', 'Portuguese', 'Brazil'),
        ('pt_PT', 'Portuguese', 'Portugal'),
        ('ro_RO', 'Romanian', 'Romania'),
        ('ru_RU', 'Russian', 'Russia'),
        ('sr_BA', 'Serbian (Cyrillic)', 'Bosnia and Herzegovina'),
        ('sr_ME', 'Serbian (Cyrillic)', 'Montenegro'),
        ('sr_RS', 'Serbian (Cyrillic)', 'Serbia'),
        ('sr_La_tn_BA', 'Serbian (Latin)', 'Bosnia and Herzegovina'),
        ('sr_La_tn_ME', 'Serbian (Latin)', 'Montenegro'),
        ('sr_La_tn_RS', 'Serbian (Latin)', 'Serbia'),
        ('sk_SK', 'Slovak', 'Slovakia'),
        ('sl_SI', 'Slovenian', 'Slovenia'),
        ('es_AR', 'Spanish', 'Argentina'),
        ('es_BO', 'Spanish', 'Bolivia'),
        ('es_CL', 'Spanish', 'Chile'),
        ('es_CO', 'Spanish', 'Colombia'),
        ('es_CR', 'Spanish', 'Costa Rica'),
        ('es_DO', 'Spanish', 'Dominican Republic'),
        ('es_EC', 'Spanish', 'Ecuador'),
        ('es_SV', 'Spanish', 'El Salvador'),
        ('es_GT', 'Spanish', 'Guatemala'),
        ('es_HN', 'Spanish', 'Honduras'),
        ('es_MX', 'Spanish', 'Mexico'),
        ('es_NI', 'Spanish', 'Nicaragua'),
        ('es_PA', 'Spanish', 'Panama'),
        ('es_PY', 'Spanish', 'Paraguay'),
        ('es_PE', 'Spanish', 'Peru'),
        ('es_PR', 'Spanish', 'Puerto Rico'),
        ('es_ES', 'Spanish', 'Spain'),
        ('es_US', 'Spanish', 'United States'),
        ('es_UY', 'Spanish', 'Uruguay'),
        ('es_VE', 'Spanish', 'Venezuela'),
        ('sv_SE', 'Swedish', 'Sweden'),
        ('th_TH', 'Thai (Western digits)', 'Thailand'),
        ('th_TH_TH', 'Thai (Thai digits)', 'Thailand'),
        ('tr_TR', 'Turkish', 'Turkey'),
        ('uk_UA', 'Ukrainian', 'Ukraine'),
        ('vi_VN', 'Vietnamese', 'Vietnam');
    """.decode('utf8'))


def downgrade():
    op.execute("DELETE FROM locales;")