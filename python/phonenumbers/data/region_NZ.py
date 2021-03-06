"""Auto-generated file, do not edit by hand. NZ metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_NZ = PhoneMetadata(id='NZ', country_code=64, international_prefix='0(?:0|161)',
    general_desc=PhoneNumberDesc(national_number_pattern=u'6[235-9]\d{6}|[2-57-9]\d{7,10}', possible_number_pattern=u'\d{7,11}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:3[2-79]|[49][2-689]|6[235-9]|7[2-589])\d{6}|24099\d{3}', possible_number_pattern=u'\d{7,8}', example_number=u'32345678'),
    mobile=PhoneNumberDesc(national_number_pattern=u'2(?:[079]\d{7}|1(?:0\d{5,7}|[12]\d{5,6}|[3-9]\d{5})|[28]\d{7,8}|4[1-9]\d{6})', possible_number_pattern=u'\d{8,10}', example_number=u'211234567'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'508\d{6,7}|80\d{6,8}', possible_number_pattern=u'\d{8,10}', example_number=u'800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'90\d{7,9}', possible_number_pattern=u'\d{9,11}', example_number=u'900123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'[28]6\d{6,7}', possible_number_pattern=u'\d{8,9}', example_number=u'26123456'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    preferred_international_prefix=u'00',
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='([34679])(\d{3})(\d{4})', format=u'\\1-\\2 \\3', leading_digits_pattern=['[3467]|9[1-9]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(21)(\d{4})(\d{3,4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['21'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([2589]\d{2})(\d{3})(\d{3,4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['2[0247-9]|5|[89]00'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\d{2})(\d{3})(\d{3,4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['2[0169]|86'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(24099)(\d{3})', format=u'\\1 \\2', leading_digits_pattern=['240', '2409', '24099'], national_prefix_formatting_rule=u'0\\1')])
