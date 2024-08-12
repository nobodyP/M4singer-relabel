# M4singer-relabel
relabel of [M4Singer](https://github.com/M4Singer/M4Singer/tree/master)


only tenor 1 for now cause I like his voice. if you want to contribute yourself, do another singer just to make it easier to organize. also make sure you label in the same style as mine, outlined below


Base labels were generated using Labelmakr, and use the Suco_zh Sofa model. Transcription were also made via labelmakr so some phonemes might be off in some areas. I did my best to correct them if they were significantly off but as I don't speak mandarin I cannot say for sure. If you run into any mistakes be sure to let me know or make a pull request fixing any errors you might find.

any english in the model was labeled using SynthV style arpabet + [q] and [vf] and then were appended with the suffix "_en". this was done to remove any overlap between the 2 languages phonemes. any .wav file containing only english was labeled and moved to a seperate folder without the sufix.


 These labels are licensed under CC BY-SA 4.0, though M4singer itself it filed under CC BY-NC-SA 4.0, meaning any commercial use is prohibited. If you somehow get an okay from the team behind m4singer, Commercial use is allowed, but only under those conditions.


i also realised, when i labeled these, i used a script to add the folder name as a prefix all .wav files, as other wise they would clash and fail. i never actualy included that so this repo has been useless until now dhjflsdjkh.

its now included. to use it run "python rename_files.py (path to m4singer folder)" and all files will be renamed.
