"""Auto-generated file, do not edit by hand. SK metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SK = PhoneMetadata(id='SK', country_code=421, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[2-689]\d{8}', possible_number_pattern=u'\d{9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'[2-5]\d{8}', possible_number_pattern=u'\d{9}', example_number=u'212345678'),
    mobile=PhoneNumberDesc(national_number_pattern=u'9(?:0[1-8]|1[0-24-9]|4[0489])\d{6}', possible_number_pattern=u'\d{9}', example_number=u'912123456'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'800\d{6}', possible_number_pattern=u'\d{9}', example_number=u'800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'9(?:[78]\d{7}|00\d{6})', possible_number_pattern=u'\d{9}', example_number=u'900123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'8[5-9]\d{7}', possible_number_pattern=u'\d{9}', example_number=u'850123456'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'6(?:5[0-4]|9[0-6])\d{6}', possible_number_pattern=u'\d{9}', example_number=u'690123456'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='(2)(\d{3})(\d{3})(\d{2})', format=u'\\1/\\2 \\3 \\4', leading_digits_pattern=['2'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([3-5]\d)(\d{3})(\d{2})(\d{2})', format=u'\\1/\\2 \\3 \\4', leading_digits_pattern=['[3-5]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([689]\d{2})(\d{3})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[689]'], national_prefix_formatting_rule=u'0\\1')])
