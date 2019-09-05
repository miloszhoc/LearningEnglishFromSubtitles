Lefs (LearningEnglishFromSubtitles)
---
####Program translates words from subtitles or whole .srt file. 

(Based on Microsoft's Translator API)   
To learn more click [here](https://docs.microsoft.com/en-us/azure/cognitive-services/translator/)
####Features:
* **lang (l)** - command shows supported languages


* **words (w)** - translates words from .srt file without repetitions and saves all words to file.
* **wordsfreq (f)** - translates words from .srt file without repetitions and shows how many times each word occurs.    


* **all (a)** - translates whole .srt file and saves it to new file.
* **part (p)** - translates part of subtitles file specified by user. User can translate  
text passing group number or time in [HH MM SS] format as separated numbers. This command  
only shows translated part without saving it to file. You can still redirect output to file using '>'.
* **double (d)** - command generates subtitles file in both languages (original language and language specified by user).


####Installation:

To see all commands - type `lefs -h`

####Usage:
1.    First check if language which you want to use is supported by API. In order to do that type `lefs lang -w` if you want to translate words,   
or `lefs lang -t` if you want to translate text from subtitles.

2.    If you want to translate eg. words with frequency counter, type:  
`lefs words [path to .srt file] [source language of subtitles] [destination language] [minimal length of each word] [minimal occurs number] [sort] [output file name]`   
Program should create new file in your current directory.  
**Note:** You can pass either readable form of language or just language's code.  

Commands like _all_, _part_ and _double_ does not require specifying source language.
####Arguments:
* **lang (l)**   
_optional arguments:_  
`-h, --help` show this help message and exit   
`-w` shows all supported languages and codes for subtitles translation (for 'words', and 'wordsfreq' command)  
`-t` shows all supported languages and codes for subtitles translation (for 'all', 'part' and 'double' command)

* **words (w)**   
_positional arguments:_   
`srt_file`    file in .srt format   
`src_lang `   source language   
`dest_lang`   destination language   
`out_file`    output file name (without extension)   
_optional arguments:_   
`-h --help` help message

* **wordsfreq (f)**  
_positional arguments:_   
`srt_file`    File in .srt format  
`src_lang`    source language  
`dest_lang`   destination language  
`min_len`     minimal word length  
`min_occurs`  how many times should word occurs   
`sort`  sorting (by frequency) [asc/desc]  
`out_file`    output file name (without extension)  
_optional arguments:_  
` -h, --help` help message

* **all (a)**
_positional arguments:_  
`srt_file`    file in .srt format  
`dest_lang`   destination language  
`out_file`    output file name (without extension)  
_optional arguments:_  
`-h, --help`  help message

* **part (p)**
_positional arguments:_   
`srt_file` file in .srt format  
`dest_lang`destination language  
`out_file` output file name (without extension)   
_optional arguments:_  
`-h, --help` help message  
`-t HH MM SS, --time HH MM SS` show by time  
`-g GROUP, --group GROUP` show by group number  

* **double (d)**  
_positional arguments:_  
`srt_file` file in .srt format   
`dest_lang` destination language  
`out_file` output file name (without extension)  
_optional arguments:_  
`-h, --help`  help message
