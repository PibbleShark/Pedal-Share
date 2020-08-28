from django import forms

from . import models

PEDAL_TYPES = [
    'Overdrive',
    'Distortion',
    'Reverb',
    'Delay',
    'Wah/Envelope',
    'Boost',
    'Fuzz',
    'Phaser',
    'Flanger',
    'Chorus',
    'Ring Modulator',
    'Tremolo',
    "Metal Zone (in a class of it's own)",
    'EQ',
    'Looper',
    'Multi-effects',
    'Compressor',
    'Vibrato',
    'Talk Box',
    'Noise Gate',
    'Octaver'
    'Pitch Shifter',
    'Synth',
    'Volume',
    'Univibe',
    'Rotary',
    'Tuner',
    'Other',
]


def must_be_empty(value):
    if value:
        raise forms.ValidationError('is not empty')


class EquipmentForm(forms.ModelForm):
    type = forms.CharField(widget=forms.Select(choices=PEDAL_TYPES))
    secondary_type = forms.CharField(widget=forms.Select(choices=PEDAL_TYPES))
    honeypot = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        label="leave empty",
        validators=[must_be_empty]
    )

    class Meta:
        model = models.Equipment
        fields = [
            'device_name',
            'description',
            'weekly_cost',
            'replacement_cost',
            'image',
        ]

    field_order = [
        'device_name',
        'type',
        'secondary_type',
        'description',
        'weekly_cost',
        'replacement_cost',
        'image',
    ]
