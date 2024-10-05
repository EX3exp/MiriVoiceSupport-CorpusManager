### MiriVoice - CorpusManager 
### - How can I add my Corpus in Official supported list?
[<img src="Misc\title.png" height="57"/>](https://github.com/EX3exp/MiriVoice)

📜🧐 :
[English](contribute-corpus.md) | [한국어](readme/contribute-corpus-ko.md)
#### [EN]

## 📚1. Before Contribution...
- **Make sure that your corpus has no legal problems, e.g. copyright.**
- The multiple-styled corpus would be great, but you can add single-styled corpus will be welcomed.

## 📚2. Things to Prepare
1. `README.md`, which contains `Rules for using this Corpus` Section.
2. Recording list for [Recstar](https://github.com/sdercolin/recstar) - `reclist_<style>.txt`
    - Each recorded sample's name should be:

        ```MV-<language>-<corpus_identifier>-<style>_<speaker_id>-<file number>```

        (e.g) `MV-KOR-AA-ANGRY_3-000`

3. Recording comment list for [Recstar](https://github.com/sdercolin/recstar) - `reclist_<style>-comment.txt`
    - Each lines should be:

        ```<recorded sample's name> <sentence to record>```

        (e.g) `MV-KOR-AA-NORMAL_0-350 아리스토텔레스의 철자 알고 있는 사람?`

4. ipa transcriptions - `ipa_<style>.txt`
    - Transcription Rule (if your language is supported in `MiriVoice`, it's highly recommended to use `Tools` -> `Transcription IPA Converter`, it will handle these stuffs for you.) : <br>

        > ⚠️To use `Tools` -> `Transcription IPA Converter`, file's Each line should be: <br>
        > ```<recorded sample's name>|<speaker id>|<sentence before transcription>.```

        > ⚠️For Korean Corpus, `MiriVoice`'s current g2p is kinda incomplete, It's highly recommended to use `g2pk` or `g2pk2` or `g2pk3` first before using  `Tools` -> `Transcription IPA Converter`. 
        - You can use [ipa phonemes which contained in this list](https://github.com/AdamSteffanick/ipa-data/blob/master/guid-o-matic/ipa-data/ipa-data.csv), `<space>`, `<bos>`, `<eos>`, `<pad>`, `;`, `:`, `,`, `.`, `!`, `?`, `¡`, `¿`, `—`, `…`, `\`, `"`, `«`, `»`, `“`, `”`,` `only.
        
            (You can use '` `', **but Note that `MiriVoice`'s phonemizer system uses `<space>` instead of '` `'.**)
        - Every phonemes should be separated with `\t`(tab).
        - Each line should be wrapped with one pair of `<pad>`.
        - Put `<bos>` when sentence starts.
        - Put `<eos>` when sentence ends.
        - Please replace '` `' with `<space>`.


            (e.g) `<pad>	<bos>	h	a	n	j	ʌ	h	a	n	t	ʰ	ɛ	<space>	i	ɭ	<space>	s	i	k	ʰ	i	d	ɯ	t	̚	<space>	s	͈	o	m	a	ŋ	i	ɛ	g	ɛ	<space>	i	ɭ	<space>	s	i	k	ʰ	i	d	ʑ	i	<space>	m	a	!	<eos>	<pad>`
    - Each lines should be:

        ```<recorded sample's name>|<speaker id>|<transcription>```

        (e.g) Korean Corpus

        Original:

        ```MV-KOR-AA-NORMAL_0-012|0|의약분업 이후 총요양급여비용을 구십 팔 년에는 의원급이 삼조 오천 사백 십 육억 원으로 더 썼잖아.```


        After `g2pk3`:

        ```MV-KOR-AA-NORMAL_0-012|0|의약뿌넙 이후 총요양그벼비용을 구십 팔 려네는 의원그비 삼조 오천 사백 씹 유걱 워느로 더 썯짜나.```

        After `Tools` -> `Transcription IPA Converter`:

        ```MV-KOR-AA-NORMAL_0-012|0|<pad>	<bos>	ɰ	i	j	a	k	̚	p	͈	u	n	ʌ	p	̚	<space>	b	i	h	u	<space>	t	ɕ	h	o	ŋ	j	o	j	a	ŋ	g	ɯ	b	j	ʌ	b	i	j	o	ŋ	ɯ	ɭ	<space>	g	u	s	i	p	̚	<space>	p	ʰ	a	ɭ	<space>	ɾ	j	ʌ	n	ɛ	n	ɯ	n	<space>	n	ɰ	i	w	ʌ	ŋ	g	ɯ	b	i	<space>	s	a	m	d	ʑ	o	<space>	o	t	ɕ	h	ʌ	n	<space>	s	a	b	ɛ	k	̚	<space>	s	͈	i	p	̚	<space>	b	j	u	g	ʌ	k	̚	<space>	g	w	ʌ	n	ɯ	ɾ	o	<space>	d	ʌ	<space>	s	͈	ʌ	t	̚	t	s	͈	a	n	a	.	<eos>	<pad>```

5. `<language>-<corpus_identifier>.json`
    - `<language>`: Three-Lettered Language code **which corresponds with `CultureInfo.ThreeLetterWindowsLanguageName` in C#**, (e.g) KOR(ko-KR), ENU(en-US). 
    - `<corpus_identifier>`: Please pick your own Two or Three-Lettered Code, it will be used as **unique identifier** in [dataset genaration code](utils/pack_dataset.py).
    - Content of json should be:
    ```
    {
    "title_displayed": "<Your corpus name, into human-readable format>",
    "language": "<language>", 
    "corpus_identifier": "<corpus_identifier>",
    "styles": [
        {
            "style": "<your official style name. Users can change this when making their Voicer.>",
            "speaker_id": <0 or positive integer, should start from 0, should be smaller than *the number of this corpus's styles*>,
            "reclist_filename" : "reclist_<style>.txt",
            "comments_filename" : "reclist_<style>-comment.txt",
            "ipa_filename" : "ipa_<style>.txt"
        },
        ...
    ] 
    }
    ```
## 📚3. Examples
1. *aihub Animation Corpus (KOR-AA)*.
- [Documentation Example](docs/ko-KR/aihub%20Animation%20Corpus/README.md)
     
- [`<language>-<corpus_identifier>.json` Example](https://github.com/EX3exp/MiriVoiceSupport-CorpusManager/blob/main/datas/KOR-AA.json)
     

- [ipa transcriptions, Recstar reclist & comments Example](https://github.com/EX3exp/MiriVoiceSupport-CorpusManager/blob/main/datas/KOR-AA)
    - Folder's name should be `<language>-<corpus_identifier>`.
    
