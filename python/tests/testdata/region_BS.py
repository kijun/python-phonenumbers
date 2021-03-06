"""Auto-generated file, do not edit by hand. BS metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BS = PhoneMetadata(id='BS', country_code=1, international_prefix='011',
    general_desc=PhoneNumberDesc(national_number_pattern=u'(242|8(00|66|77|88)|900)\d{7}', possible_number_pattern=u'\d{7,10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'242(?:3(?:02|[236][1-9]|4[0-24-9]|5[0-68]|7[3-57]|9[2-5])|4(?:2[237]|51|64|77)|502|636|702)\d{4}', possible_number_pattern=u'\d{7,10}'),
    mobile=PhoneNumberDesc(national_number_pattern=u'242(357|359|457|557)\d{4}', possible_number_pattern=u'\d{10}'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'8(00|66|77|88)\d{7}', possible_number_pattern=u'\d{10}'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'900\d{7}', possible_number_pattern=u'\d{10}'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'1',
    national_prefix_for_parsing=u'1')
