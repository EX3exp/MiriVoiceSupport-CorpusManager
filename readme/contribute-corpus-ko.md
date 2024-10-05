### MiriVoice - CorpusManager 
### - 공식 말뭉치 목록에 제 말뭉치를 추가하고 싶어요
[<img src="..\Misc\title.png" height="57"/>](https://github.com/EX3exp/MiriVoice)

📜🧐 :
[English](..\contribute-corpus.md) | [한국어](contribute-corpus-ko.md)
#### [KO]

## 📚1. 기여하기 전에...
- **말뭉치에 법적 문제가 없는지 꼭 확인하세요. (예: 저작권 등)**
- 여러 스타일을 보유한 말뭉치라면 더 좋겠지만, 단일 스타일의 말뭉치도 환영합니다.

## 📚2. 준비물
1. `README.md` - `녹음 리스트 이용 규칙` 을 반드시 포함해 주세요.
2. [Recstar](https://github.com/sdercolin/recstar)용 녹음 리스트 - `reclist_<스타일>.txt`
    - 녹음되는 파일명은 다음과 같아야 해요 :

        ```MV-<언어>-<말뭉치 식별자>-<스타일>_<발화자 id>-<순번>```

        (예) `MV-KOR-AA-ANGRY_3-000`

3. [Recstar](https://github.com/sdercolin/recstar)용 코멘트 리스트- `reclist_<스타일>-comment.txt`
    - 파일의 각 줄은 다음과 같아야 해요 :

        ```<녹음되는 파일명> <녹음할 문장 내용>```

        (예) `MV-KOR-AA-NORMAL_0-350 아리스토텔레스의 철자 알고 있는 사람?`

4. ipa 전사본 - `ipa_<스타일>.txt`
    - 전사 규칙 (대상 언어가 `MiriVoice`에서 지원되고 있다면, `도구` -> `전사 파일 IPA 변환기`를 사용하세요. 굳이 하단의 사항을 신경쓰지 않아도 됩니다.) : <br>

        > ⚠️`도구` -> `전사 파일 IPA 변환기`를 사용하려면, 파일의 각 줄을 다음과 같게 해주세요: <br>
        > ```<녹음되는 파일명>|<발화자 id>|<전사할 문장 내용>.```

        > ⚠️한국어 말뭉치의 경우, `도구` -> `전사 파일 IPA 변환기`를 사용하기 전 `g2pk`, `g2pk2`, `g2pk3` 중 하나를 거치는 것을 추천해요. `MiriVoice`의 한국어 g2p는 아직 완전하지 않답니다.
        - 사용할 수 있는 음소는 다음으로 제한됩니다: <br>[이 리스트에 포함된 ipa 음소들](https://github.com/AdamSteffanick/ipa-data/blob/master/guid-o-matic/ipa-data/ipa-data.csv), `<space>`, `<bos>`, `<eos>`, `<pad>`, `;`, `:`, `,`, `.`, `!`, `?`, `¡`, `¿`, `—`, `…`, `\`, `"`, `«`, `»`, `“`, `”`,` `.
        
            ('` `'를 쓸 수 있긴 하지만, **`MiriVoice`의 음소화기 시스템은 '` `' 대신 `<space>`를 쓴다는 사실을 유념하세요.**)
        - 각 음소들은 모두 `\t`(탭)으로 구분되어야 합니다.
        - 각 줄은 한 쌍의 `<pad>`로 감싸여 있어야 합니다.
        - 문장의 시작 지점에는 `<bos>`를 두세요.
        - 문장의 끝 지점에는 `<eos>` 를 두세요.
        - '` `'는 `<space>`로 대체해 주세요.


            (예) `<pad>	<bos>	h	a	n	j	ʌ	h	a	n	t	ʰ	ɛ	<space>	i	ɭ	<space>	s	i	k	ʰ	i	d	ɯ	t	̚	<space>	s	͈	o	m	a	ŋ	i	ɛ	g	ɛ	<space>	i	ɭ	<space>	s	i	k	ʰ	i	d	ʑ	i	<space>	m	a	!	<eos>	<pad>`
    - 파일의 각 줄은 다음과 같아야 해요:

        ```<녹음되는 파일명>|<발화자 id>|<전사된 내용>```

        (예) 한국어 말뭉치의 경우

        원본:

        ```MV-KOR-AA-NORMAL_0-012|0|의약분업 이후 총요양급여비용을 구십 팔 년에는 의원급이 삼조 오천 사백 십 육억 원으로 더 썼잖아.```


        `g2pk3`를 거친 후:

        ```MV-KOR-AA-NORMAL_0-012|0|의약뿌넙 이후 총요양그벼비용을 구십 팔 려네는 의원그비 삼조 오천 사백 씹 유걱 워느로 더 썯짜나.```

        `도구` -> `전사 파일 IPA 변환기`를 거친 후:

        ```MV-KOR-AA-NORMAL_0-012|0|<pad>	<bos>	ɰ	i	j	a	k	̚	p	͈	u	n	ʌ	p	̚	<space>	b	i	h	u	<space>	t	ɕ	h	o	ŋ	j	o	j	a	ŋ	g	ɯ	b	j	ʌ	b	i	j	o	ŋ	ɯ	ɭ	<space>	g	u	s	i	p	̚	<space>	p	ʰ	a	ɭ	<space>	ɾ	j	ʌ	n	ɛ	n	ɯ	n	<space>	n	ɰ	i	w	ʌ	ŋ	g	ɯ	b	i	<space>	s	a	m	d	ʑ	o	<space>	o	t	ɕ	h	ʌ	n	<space>	s	a	b	ɛ	k	̚	<space>	s	͈	i	p	̚	<space>	b	j	u	g	ʌ	k	̚	<space>	g	w	ʌ	n	ɯ	ɾ	o	<space>	d	ʌ	<space>	s	͈	ʌ	t	̚	t	s	͈	a	n	a	.	<eos>	<pad>```

5. `<언어>-<말뭉치 식별자>.json`
    - `<언어>`: 세 글자짜리 언어 코드. **C#의 `CultureInfo.ThreeLetterWindowsLanguageName`와 일치해야 해요.** (예) KOR(ko-KR), ENU(en-US). 
    - `<말뭉치 식별자>`: 두 글자나 세 글자짜리 코드를 정해 주세요. [데이터셋 생성 코드](../utils/pack_dataset.py)에서 **고유 식별자**로 사용됩니다.
    - json의 내용은 다음과 같아야 해요:
    ```
    {
    "title_displayed": "<말뭉치의 이름. 사람이 읽을 수 있는(human-readable) 언어여야 합니다.>",
    "language": "<언어>", 
    "corpus_identifier": "<말뭉치 식별자>",
    "styles": [
        {
            "style": "<스타일의 공식 명칭. 사용자들의 의향에 따라 변경되어 사용될 수 있어요.>",
            "speaker_id": <음이 아닌 정수. 0부터 시작해야 하며, *말뭉치의 스타일 수* 미만인 값이어야 해요.>,
            "reclist_filename" : "reclist_<스타일>.txt",
            "comments_filename" : "reclist_<스타일>-comment.txt",
            "ipa_filename" : "ipa_<스타일>.txt"
        },
        ...
    ] 
    }
    ```
## 📚3. 예시
1. *aihub 애니체 말뭉치 (KOR-AA)*.
- [문서 작성 예](docs/ko-KR/aihub%20Animation%20Corpus/README.md)
     
- [`<언어>-<말뭉치 식별자>.json` 예](https://github.com/EX3exp/MiriVoiceSupport-CorpusManager/blob/main/datas/KOR-AA.json)
     

- [ipa 전사본, Recstar 녹음 리스트 & 코멘트 리스트 예](https://github.com/EX3exp/MiriVoiceSupport-CorpusManager/blob/main/datas/KOR-AA)
    - 폴더명은 반드시 `<언어>-<말뭉치 식별자>` 여야만 해요.
    
