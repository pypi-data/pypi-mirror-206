from setuptools import setup


def readfile(filename):
    with open(filename, 'r+') as f:
        return f.read()


setup(
    name="whisper-cli-tool",
    version="1.0.3",
    description="Do transcriptions of audiofiles using the whisper-1 model from OpenAI.",
    long_description=readfile('README.md'),
    author="João Nogueira",
    author_email="joaopcnogueira@gmail.com",
    url="",
    py_modules=['whisper_cli_tool'],
    license=readfile('LICENSE'),
    install_requires=['openai'],
    long_description_content_type = 'text/markdown',
    entry_points={
        'console_scripts': [
            'whisper = whisper_cli_tool:main'
        ]
    },
)