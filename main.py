import openai

KEY = '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'

file = open('rot.m4a', 'rb')
file1 = open('rot.m4a', 'rb')

result = openai.Audio.transcribe(
    api_key=KEY,
    model='whisper-1',
    file=file,
    response_format='text'
)

result1 = openai.Audio.translate(
    api_key=KEY,
    model='whisper-1',
    file=file1,
    response_format='text'
)

print(result, result1)
