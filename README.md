<h1 align="center">
  YouTubeBrainz
</h1>

<p align="center">
  YoutubeBrainz allow you to find Youtube Videos associated to an Album on MusicBrainz.
</p>

<p align="center">
<img src="https://img.shields.io/badge/python-3-blue"></a>
<img src="https://img.shields.io/badge/pypi-0.1.0-brightgreen"></a>
<img src="https://img.shields.io/badge/license-GPT-blue.svg"></a>
</p>

<p align="center"><img src="/img/demo.gif?raw=true"/></p>

## Installation
```
$ sudo pip install youtube-bz
```

## Usage
Display help
```
$ youtube-bz -h
```

You can search for an album with his MBID (see https://musicbrainz.org/doc/MusicBrainz_Identifier)
```
$  youtube-bz -m MBID
```
or you can search directly with the artist's name and the album title
```
$  youtube-bz -s 'artist' 'album'
```

There is two methods available, you can either search for music video auto-generated by Youtube
```
$ youtube-bz -g -m MBID
```
or you can search in all Youtube
```
$ youtube-bz -a -m MBID
```

If you don't want to download the album you can pass the --no-download argument
```
$ youtube-bz --no-download -m MBID
```
