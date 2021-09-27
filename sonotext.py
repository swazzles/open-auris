from configuration import *
import audio


def get_sonobyte(byte):
    f = MESSAGE_SPECTRUM_START + (byte * SPECTRAL_INTERVAL)
    
    return f

def get_letter_ordinal(byte):
    return ALLOWED_CHARACTERS[byte.lower()]

def play_control_sound(type, sampleset):
    f = 0
    if type == 'BEGIN_KEY_HANDSHAKE':
        f = BEGIN_KEY_HANDSHAKE_FREQUENCY
    elif type == 'END_KEY_HANDSHAKE':
        f = END_KEY_HANDSHAKE_FREQUENCY
    elif type == 'BEGIN_MESSAGE':
        f = BEGIN_MESSAGE_FREQUENCY
    elif type == 'END_MESSAGE':
        f = END_MESSAGE_FREQUENCY
    for _ in range(0, CONTROL_MESSAGE_FRAMES):
        sampleset.append(audio.sine_tone(f, VOLUME, SAMPLE_RATE, FRAME_SIZE))
    return sampleset
    
def play_message(message, sampleset):
    for letter in message:
        letter = get_letter_ordinal(letter)
        letter = get_sonobyte(letter)
        sampleset.append(audio.sine_tone(letter, VOLUME, SAMPLE_RATE, FRAME_SIZE))
    return sampleset


def message_to_sound(message, encryption_bundle=None):
    sampleset = []
    if encryption_bundle is not None:
        sampleset = play_control_sound('BEGIN_KEY_HANDSHAKE', sampleset)
        sampleset = play_message(encryption_bundle, sampleset)
        sampleset = play_control_sound('END_KEY_HANDSHAKE', sampleset)
    
    sampleset = play_control_sound('BEGIN_MESSAGE', sampleset)
    sampleset = play_message(message, sampleset)
    sampleset = play_control_sound('END_MESSAGE', sampleset)
    audio.play_audio(sampleset, SAMPLE_RATE)