"""Auto-generated file, do not edit by hand. SI metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SI = PhoneMetadata(id='SI', country_code=386, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[1-7]\d{6,7}|[89]\d{4,7}', possible_number_pattern=u'\d{5,8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:1\d|2[2-8]|3[4-8]|4[24-8]|[57][3-8])\d{6}', possible_number_pattern=u'\d{7,8}', example_number=u'11234567'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:[37][01]|4[019]|51|64)\d{6}', possible_number_pattern=u'\d{8}', example_number=u'31234567'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'80\d{4,6}', possible_number_pattern=u'\d{6,8}', example_number=u'80123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'90\d{4,6}|89[1-3]\d{2,5}', possible_number_pattern=u'\d{5,8}', example_number=u'90123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'(?:59|8[1-3])\d{6}', possible_number_pattern=u'\d{8}', example_number=u'59012345'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='(\d)(\d{3})(\d{2})(\d{2})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['[12]|3[4-8]|4[24-8]|5[3-8]|7[3-8]'], national_prefix_formatting_rule=u'(0\\1)'),
        NumberFormat(pattern='([3-7]\d)(\d{3})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[37][01]|4[019]|51|64'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([89][09])(\d{3,6})', format=u'\\1 \\2', leading_digits_pattern=['[89][09]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([58]\d{2})(\d{5})', format=u'\\1 \\2', leading_digits_pattern=['59|8[1-3]'], national_prefix_formatting_rule=u'0\\1')])
