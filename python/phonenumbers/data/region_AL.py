"""Auto-generated file, do not edit by hand. AL metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_AL = PhoneMetadata(id='AL', country_code=355, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[2-57]\d{7}|6\d{8}|8\d{5,7}|9\d{5}', possible_number_pattern=u'\d{5,9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:2(?:[168][1-9]|[247]\d|9[1-7])|3(?:1[1-3]|[2-6]\d|[79][1-8]|8[1-9])|4\d{2}|5(?:1[1-4]|[2-578]\d|6[1-5]|9[1-7])|8(?:[19][1-5]|[2-6]\d|[78][1-7]))\d{5}', possible_number_pattern=u'\d{5,8}', example_number=u'22345678'),
    mobile=PhoneNumberDesc(national_number_pattern=u'6[6-9]\d{7}', possible_number_pattern=u'\d{9}', example_number=u'661234567'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'800\d{4}', possible_number_pattern=u'\d{7}', example_number=u'8001234'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'900\d{3}', possible_number_pattern=u'\d{6}', example_number=u'900123'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'808\d{3}', possible_number_pattern=u'\d{6}', example_number=u'808123'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'700\d{5}', possible_number_pattern=u'\d{8}', example_number=u'70012345'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='(4)(\d{3})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['4[0-6]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(6[6-9])(\d{3})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['6'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\d{2})(\d{3})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[2358][2-5]|4[7-9]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\d{3})(\d{3,5})', format=u'\\1 \\2', leading_digits_pattern=['[235][16-9]|8[016-9]|[79]'], national_prefix_formatting_rule=u'0\\1')])
