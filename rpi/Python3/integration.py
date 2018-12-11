#!/usr/bin/python

from pushtotalk import main
import click
import audio_helpers
import os

api_endpoint='embeddedassistant.googleapis.com'
credentials=os.path.join(click.get_app_dir('google-oauthlib-tool'),
                                   'credentials.json')
project_id='handassist-581d5'
device_model_id='handassist-581d5-handassist-jkbpdx'
device_config=os.path.join(click.get_app_dir('googlesamples-assistant'),
                  'device_config.json')
lang='en-US'
display=False
verbose=False

audio_sample_rate=audio_helpers.DEFAULT_AUDIO_SAMPLE_RATE
audio_sample_width=audio_helpers.DEFAULT_AUDIO_SAMPLE_WIDTH
audio_iter_size=audio_helpers.DEFAULT_AUDIO_ITER_SIZE
audio_block_size=audio_helpers.DEFAULT_AUDIO_DEVICE_BLOCK_SIZE
audio_flush_size=audio_helpers.DEFAULT_AUDIO_DEVICE_FLUSH_SIZE
grpc_deadline=60 * 3 + 5
once=False





main(api_endpoint, credentials, project_id,
         device_model_id, device_config,
         lang, display, verbose,
         audio_sample_rate, audio_sample_width,
         audio_iter_size, audio_block_size, audio_flush_size,
         grpc_deadline, once)
