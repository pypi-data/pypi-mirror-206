from setuptools import setup


def readfile(filename):
    with open(filename, 'r+') as f:
        return f.read()


setup(
    name="whisper-cli-tool",
    version="1.0.1",
    description="Do transcriptions of audiofiles using the whisper-1 model from OpenAI.",
    long_description=readfile('README.md'),
    author="João Nogueira",
    author_email="joaopcnogueira@gmail.com",
    url="",
    py_modules=['whisper_cli'],
    license=readfile('LICENSE'),
    install_requires=['openai'],
    entry_points={
        'console_scripts': [
            'whisper = whisper_cli_tool:main'
        ]
    },
)