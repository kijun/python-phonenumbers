"""Auto-generated file, do not edit by hand. FK metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_FK = PhoneMetadata(id='FK', country_code=500, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[2-7]\d{4}', possible_number_pattern=u'\d{5}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'[2-47]\d{4}', possible_number_pattern=u'\d{5}', example_number=u'31234'),
    mobile=PhoneNumberDesc(national_number_pattern=u'[56]\d{4}', possible_number_pattern=u'\d{5}', example_number=u'51234'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'))
