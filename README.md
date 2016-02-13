#Loremimg [![Build Status](https://travis-ci.org/silvanadrian/loremimg.svg?branch=master)](https://travis-ci.org/silvanadrian/loremimg) [![Coverage Status](https://coveralls.io/repos/github/silvanadrian/loremimg/badge.svg?branch=master)](https://coveralls.io/github/silvanadrian/loremimg?branch=master)


##Full Image
```
http://example.com/<name>/
```
Returns full image from the name (unique)

##Square Image
```
http://example.com/<width>/
```
Returns one of the uploaded Images as a Square Image (random)
##Square Image Specific
```
http://example.com/<width>/<name>/
```
Returns specific Image as Square Image
##Rectangle Image
```
http://example.com/<width>/<height>/
```
Returns one of the uploaded Images as a Rectangle Image (random)
##Rectangle Image Specific
```
http://example.com/<width>/<height>/<name>
```
Returns Specific Image as Rectangle Image

##ToDo
* Use Category to get Images of a specific Category
* Better Error handling etc.
* More functions rotate, Grayscale, Sepia etc.
* Change DB to Postgres (still SQLite at the moment)
