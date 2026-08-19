from rest_framework import serializers


class JobDescriptionAnalysisSerializer(
    serializers.Serializer
):

    job_description = serializers.CharField(
        required=True,
        allow_blank=False
    )