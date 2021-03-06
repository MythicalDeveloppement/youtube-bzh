import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="youtube_bzh",
    version="0.2.2",
    author="Flowrey",
    description="YoutubeBrainz allow you to find Youtube Videos associated to an Album on MusicBrainZ. ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/flowrey/ytbz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    python_requires='>=3.6',
    install_requires=['requests', 'pytube', 'moviepy'],
    entry_points = {
        'console_scripts': [
            'youtube-bzh = youtube_bzh:main',
         ],
    },
    scripts=['bin/youtube-bzh'],
)
