#!/usr/bin/python3
import os

from tts_arranger import TTS_Item, TTS_Simple_Writer

# Simple example using Simple Writer (using a simple list of TTS items), uses tts_models/en/vctk/vits by (default)

tts_items = []

user_dir = os.path.expanduser('~')

preferred_speakers = ['p273', 'p330']

# tts_items.append(TTS_Item('ehy', 0))  # Uses preferred speaker #0
# tts_items.append(TTS_Item(length=1000))  # Insert pause
# tts_items.append(TTS_Item('bee')) # Uses preferred speaker #1 and sets minimum length
# tts_items.append(TTS_Item(length=1000))  # Insert pause
# tts_items.append(TTS_Item('tsee')) # Uses preferred speaker #1 and sets minimum length
# tts_items.append(TTS_Item(length=1000))  # Insert pause
# tts_items.append(TTS_Item('dee')) # Uses preferred speaker #1 and sets minimum length
# tts_items.append(TTS_Item(length=1000))  # Insert pause
# tts_items.append(TTS_Item('ee')) # Uses preferred speaker #1 and sets minimum length
# tts_items.append(TTS_Item(length=1000))  # Insert pause
tts_items.append(TTS_Item('eph')) # Uses preferred speaker #1 and sets minimum length
tts_items.append(TTS_Item(length=1000))  # Insert pause
# tts_items.append(TTS_Item('gee')) # Uses preferred speaker #1 and sets minimum length
# tts_items.append(TTS_Item(length=1000))  # Insert pause
# tts_items.append(TTS_Item('age')) # Uses preferred speaker #1 and sets minimum length
# tts_items.append(TTS_Item(length=1000))  # Insert pause
# tts_items.append(TTS_Item('ay')) # Uses preferred speaker #1 and sets minimum length
# tts_items.append(TTS_Item(length=1000))  # Insert pause
# tts_items.append(TTS_Item('jay')) # Uses preferred speaker #1 and sets minimum length
tts_items.append(TTS_Item(length=1000))  # Insert pause
tts_items.append(TTS_Item('kkay')) # Uses preferred speaker #1 and sets minimum length
tts_items.append(TTS_Item(length=1000))  # Insert pause
# tts_items.append(TTS_Item('elle')) # Uses preferred speaker #1 and sets minimum length
# tts_items.append(TTS_Item(length=1000))  # Insert pause

# Create writer using our item list and prefered speakers and synthesize and save as mp3 audio
simple_writer = TTS_Simple_Writer(tts_items, preferred_speakers)
simple_writer.synthesize_and_write('/tmp/tts_arranger_example_output/test.mp3')
