"""Auto-generated file, do not edit by hand. ZM metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_ZM = PhoneMetadata(id='ZM', country_code=260, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[289]\d{8}', possible_number_pattern=u'\d{9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'21[1-8]\d{6}', possible_number_pattern=u'\d{9}', example_number=u'211234567'),
    mobile=PhoneNumberDesc(national_number_pattern=u'9(?:55|6[4-9]|7[4-9])\d{6}', possible_number_pattern=u'\d{9}', example_number=u'955123456'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'800\d{6}', possible_number_pattern=u'\d{9}', example_number=u'800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='([29]\d)(\d{7})', format=u'\\1 \\2', leading_digits_pattern=['[29]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(800)(\d{3})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['8'], national_prefix_formatting_rule=u'0\\1')])
