Story of File in Dropbox
===========

A simple pythons script which simply get all versions of a specified file in Dropbox, compute some statistics (word count) and save statistics to a CSV file with time stamps. [getAllVersions.py]

Script utilizes the Dropbox API, and it can be reached through https://www.dropbox.com/developers/core/setup#python

In order to combine stories of different files in a single CSV file, a script is also included [combine.py]

Main aim of the script was computing some statistics related to my master thesis as explained in a blog post http://www.ozansener.net/2013/04/story-of-thesis-tex/.

Since I used the script to get statistics of Latex files, I also included a perl script which strips out the latex comments [StripLatexComments.pl]. Script is taken from "http://tex.stackexchange.com/questions/83663/utility-to-strip-comments-from-latex-source"

Plots about my thesis that I obtained after fetching data is also included in Plots/ folder with necessary Mathmetica 7 script used to generate XKCD like plots.
