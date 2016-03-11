#Loremimg [![Build Status](https://travis-ci.org/silvanadrian/loremimg.svg?branch=master)](https://travis-ci.org/silvanadrian/loremimg) [![Coverage Status](https://coveralls.io/repos/github/silvanadrian/loremimg/badge.svg?branch=master)](https://coveralls.io/github/silvanadrian/loremimg?branch=master)

##Homepage
```
http://example.com/
```
Returns Random full Image
##Full Image
```
http://example.com/<name>/
```
Returns full Image from the name (unique)
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
##Category
```
http://example.com/category/<category>/
```
Returns Random full Image from Category
##Category Square
```
http://example.com/category/<category>/<width>/
```
Returns Random square Image from Category
##Category Rectangle
```
http://example.com/category/<category>/<width>/<height>/
```
Returns Random rectangle Image from Category

##ToDo
* More functions rotate, Grayscale, Sepia etc.
* Change DB to Postgres (still SQLite at the moment)
