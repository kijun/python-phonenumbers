"""Auto-generated file, do not edit by hand. DE metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_DE = PhoneMetadata(id='DE', country_code=49, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'\d{4,14}', possible_number_pattern=u'\d{2,14}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:[24-6]\d{2}|3[03-9]\d|[789](?:[1-9]\d|0[2-9]))\d{3,8}', possible_number_pattern=u'\d{2,14}', example_number=u'30123456'),
    mobile=PhoneNumberDesc(national_number_pattern=u'1(5\d{9}|7\d{8}|6[02]\d{8}|63\d{7})', possible_number_pattern=u'\d{10,11}'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'800\d{7}', possible_number_pattern=u'\d{10}'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'900([135]\d{6}|9\d{7})', possible_number_pattern=u'\d{10,11}'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='(\d{3})(\d{3,8})', format=u'\\1 \\2', leading_digits_pattern=['2|3[3-9]|906|[4-9][1-9]1'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\d{2})(\d{4,9})', format=u'\\1/\\2', leading_digits_pattern=['[34]0|[68]9'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([4-9]\d)(\d{2})', format=u'\\1 \\2', leading_digits_pattern=['[4-9]', '[4-6]|[7-9](?:\d[1-9]|[1-9]\d)'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([4-9]\d{3})(\d{2,7})', format=u'\\1 \\2', leading_digits_pattern=['[4-9]', '[4-6]|[7-9](?:\d[1-9]|[1-9]\d)'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\d{3})(\d{1})(\d{6})', format=u'\\1 \\2 \\3', leading_digits_pattern=['800'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\d{3})(\d{3,4})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['900'], national_prefix_formatting_rule=u'0\\1')])
