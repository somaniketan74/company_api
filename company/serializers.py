from company.models import Company, Funding, Social
from rest_framework import serializers


class FundingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funding
        fields = ('id','amount', 'date', 'stages', 'investors')


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ('id','email', 'phone_number', 'linkedin', 'twitter', 'facebook')


class CompanySerializer(serializers.ModelSerializer):
    fundings = FundingSerializer(many=True,required=False)
    social = SocialSerializer(required=False)

    class Meta:
        model = Company
        fields = ('id', 'name', 'profile_id', 'logo', 'markets', 'founded_date', 'website', 'fundings', 'social')

    def create(self, validated_data):
        print('Creating Company Record')
        fundings = validated_data.pop('fundings')
        socials = validated_data.pop('social')
        company = Company.objects.create(**validated_data)
        print ('Entered')
        for funding in fundings:
            funding['company_id'] = company
            fundingCreated = Funding.objects.create(**funding)
            company.fundings.add(fundingCreated)

        socials['company_id'] = company
        socialsCreated = Social.objects.create(**socials)
        company.social = socialsCreated

        company.save()
        return company
