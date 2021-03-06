"""Auto-generated file, do not edit by hand. LB metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_LB = PhoneMetadata(id='LB', country_code=961, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[13-9]\d{6,7}', possible_number_pattern=u'\d{7,8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:[14-6]\d{2}|7(?:[2-57-9]\d|62)|[89][2-9]\d)\d{4}', possible_number_pattern=u'\d{7}', example_number=u'1123456'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:3\d|7(?:[01]\d|6[67]))\d{5}', possible_number_pattern=u'\d{7,8}', example_number=u'71123456'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'9[01]\d{6}', possible_number_pattern=u'\d{8}', example_number=u'90123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'8[01]\d{6}', possible_number_pattern=u'\d{8}', example_number=u'80123456'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='(\d)(\d{3})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[13-6]|7(?:[2-57-9]|62)|[89][2-9]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([7-9]\d)(\d{3})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[89][01]|7(?:[01]|6[67])'], national_prefix_formatting_rule=u'0\\1')])
