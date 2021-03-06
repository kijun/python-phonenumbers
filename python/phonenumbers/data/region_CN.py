"""Auto-generated file, do not edit by hand. CN metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CN = PhoneMetadata(id='CN', country_code=86, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[1-79]\d{7,11}|8[0-357-9]\d{6,9}', possible_number_pattern=u'\d{4,12}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'21\d{8,10}|(?:10|2[02-57-9]|3(?:11|7[159])|4[135]1|5(?:1\d|2[37]|3[12]|7[13-79]|9[15])|7(?:31|5[457]|6[09])|898)\d{8}|(?:3(?:1[02-9]|35|49|5\d|7[02-68]|9[1-68])|4(?:1[02-9]|2[179]|[35][2-9]|6[4789]|7[0-46-9]|8[23])|5(?:3[03-9]|4[36]|5\d|6[1-6]|7[028]|80|9[2-46-9])|6(?:3[1-5]|6[0238]|9[12])|7(?:01|[1579]\d|2[248]|3[04-9]|4[3-6]|6[2368])|8(?:1[236-8]|2[5-7]|[37]\d|5[1-9]|8[3678]|9[1-7])|9(?:0[1-3689]|1[1-79]|[379]\d|4[13]|5[1-5]))\d{7}|80(?:29|6[03578]|7[018]|81)\d{4}', possible_number_pattern=u'\d{4,12}', example_number=u'1012345678'),
    mobile=PhoneNumberDesc(national_number_pattern=u'1(?:3[0-9]|47|5[0135689]|8[05-9])\d{8}', possible_number_pattern=u'\d{11}', example_number=u'13123456789'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'(?:10)?800\d{7}', possible_number_pattern=u'\d{10,12}', example_number=u'8001234567'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'16[08]\d{5}', possible_number_pattern=u'\d{8}', example_number=u'16812345'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'400\d{7}', possible_number_pattern=u'\d{10}', example_number=u'4001234567'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='(80\d{2})(\d{4})', format=u'\\1 \\2', leading_digits_pattern=['80[2678]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([48]00)(\d{3})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[48]00']),
        NumberFormat(pattern='(\d{3,4})(\d{4})', format=u'\\1 \\2', leading_digits_pattern=['[2-9]']),
        NumberFormat(pattern='(21)(\d{4})(\d{4,6})', format=u'\\1 \\2 \\3', leading_digits_pattern=['21'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([12]\d)(\d{4})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['10[1-9]|2[02-9]', '10[1-9]|2[02-9]', '10(?:[1-79]|8(?:[1-9]|0[1-9]))|2[02-9]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\d{3})(\d{4})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['3(?:11|7[159])|4[135]1|5(?:1|2[37]|3[12]|7[13-79]|9[15])|7(?:31|5[457]|6[09])|898'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\d{3})(\d{3})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['3(?:1[02-9]|35|49|5|7[02-68]|9[1-68])|4(?:1[02-9]|2[179]|[35][2-9]|6[4789]|7[0-46-9]|8[23])|5(?:3[03-9]|4[36]|5|6[1-6]|7[028]|80|9[2-46-9])|6(?:3[1-5]|6[0238]|9[12])|7(?:01|[1579]|2[248]|3[04-9]|4[3-6]|6[2368])|8(?:1[236-8]|2[5-7]|[37]|5[1-9]|8[3678]|9[1-7])|9(?:0[1-3689]|1[1-79]|[379]|4[13]|5[1-5])'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(1[3-58]\d)(\d{4})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['1[3-58]']),
        NumberFormat(pattern='(10800)(\d{3})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['108', '1080', '10800'])],
    intl_number_format=[NumberFormat(pattern='(21)(\d{4})(\d{4,6})', format=u'\\1 \\2 \\3', leading_digits_pattern=['21']),
        NumberFormat(pattern='([12]\d)(\d{4})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['10[1-9]|2[02-9]', '10[1-9]|2[02-9]', '10(?:[1-79]|8(?:[1-9]|0[1-9]))|2[02-9]']),
        NumberFormat(pattern='(80\d{2})(\d{4})', format=u'\\1 \\2', leading_digits_pattern=['80[2678]']),
        NumberFormat(pattern='(\d{3})(\d{4})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['3(?:11|7[159])|4[135]1|5(?:1|2[37]|3[12]|7[13-79]|9[15])|7(?:31|5[457]|6[09])|898']),
        NumberFormat(pattern='(\d{3})(\d{3})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['3(?:1[02-9]|35|49|5|7[02-68]|9[1-68])|4(?:1[02-9]|2[179]|[35][2-9]|6[4789]|7[0-46-9]|8[23])|5(?:3[03-9]|4[36]|5|6[1-6]|7[028]|80|9[2-46-9])|6(?:3[1-5]|6[0238]|9[12])|7(?:01|[1579]|2[248]|3[04-9]|4[3-6]|6[2368])|8(?:1[236-8]|2[5-7]|[37]|5[1-9]|8[3678]|9[1-7])|9(?:0[1-3689]|1[1-79]|[379]|4[13]|5[1-5])']),
        NumberFormat(pattern='(1[3-58]\d)(\d{4})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['1[3-58]']),
        NumberFormat(pattern='([48]00)(\d{3})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[48]00']),
        NumberFormat(pattern='(10800)(\d{3})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['108', '1080', '10800'])])
