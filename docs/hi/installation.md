# स्थापना और CLI

<!-- language-navigation:start -->
<p dir="ltr">
<a href="../en/installation.md" lang="en" dir="ltr">English</a> ·
<a href="../ar/installation.md" lang="ar" dir="rtl">العربية</a> ·
<a href="../bn/installation.md" lang="bn" dir="ltr">বাংলা</a> ·
<a href="../cs/installation.md" lang="cs" dir="ltr">Čeština</a> ·
<a href="../de/installation.md" lang="de" dir="ltr">Deutsch</a> ·
<a href="../es/installation.md" lang="es" dir="ltr">Español</a> ·
<a href="../fa/installation.md" lang="fa" dir="rtl">فارسی</a> ·
<a href="../fr/installation.md" lang="fr" dir="ltr">Français</a> ·
<a href="../he/installation.md" lang="he" dir="rtl">עברית</a> ·
<a href="../hi/installation.md" lang="hi" dir="ltr">हिन्दी</a> ·
<a href="../id/installation.md" lang="id" dir="ltr">Bahasa Indonesia</a> ·
<a href="../it/installation.md" lang="it" dir="ltr">Italiano</a> ·
<a href="../ja/installation.md" lang="ja" dir="ltr">日本語</a> ·
<a href="../ko/installation.md" lang="ko" dir="ltr">한국어</a> ·
<a href="../nl/installation.md" lang="nl" dir="ltr">Nederlands</a> ·
<a href="../pl/installation.md" lang="pl" dir="ltr">Polski</a> ·
<a href="../pt/installation.md" lang="pt" dir="ltr">Português</a> ·
<a href="../ru/installation.md" lang="ru" dir="ltr">Русский</a> ·
<a href="../th/installation.md" lang="th" dir="ltr">ไทย</a> ·
<a href="../tr/installation.md" lang="tr" dir="ltr">Türkçe</a> ·
<a href="../uk/installation.md" lang="uk" dir="ltr">Українська</a> ·
<a href="../vi/installation.md" lang="vi" dir="ltr">Tiếng Việt</a> ·
<a href="../zh-Hans/installation.md" lang="zh-Hans" dir="ltr">简体中文</a> ·
<a href="../zh-Hant/installation.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

[दस्तावेज़ सूचकांक](../../README.md#documentation)

Python 3.11 या नया इस्तेमाल करें। अलग वर्चुअल वातावरण बनाकर सक्रिय करें, फिर चेकआउट से `python3 -m pip install -e .` चलाएँ। पैकेज की रनटाइम निर्भरताएँ नहीं हैं; pip उसका बिल्ड बैकएंड डाउनलोड कर सकता है। ऑफ़लाइन मशीन के लिए wheel और बिल्ड निर्भरताएँ पहले तैयार करें। चुनी स्थापना `ha-entity-migrations --version` से जाँचें; यह स्थापित पैकेज संस्करण दिखाता है।

CLI में दो आदेश हैं, और वैश्विक भाषा विकल्प आदेश से पहले आता है:

```sh
ha-entity-migrations --lang ru fingerprint examples/domain-change/snapshot.json
ha-entity-migrations --lang en plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change --format text
```

`fingerprint` फ़ाइल के सटीक बाइटों का SHA-256 छोटे अक्षरों में छापता है। वह फ़ाइल को JSON के रूप में सत्यापित नहीं करता। मैनिफ़ेस्ट के स्नैपशॉट और स्रोत फ़िंगरप्रिंट, खाली जगहों सहित, उन्हीं सटीक फ़ाइलों से मिलने चाहिए। केवल अप्रत्याशित विचलन दबाने के लिए फ़िंगरप्रिंट न बदलें; पहले नए इनपुट की तुलना करके स्वीकृति दें।

`plan` JSON मैनिफ़ेस्ट, सामान्यीकृत JSON स्नैपशॉट और सिर्फ़ `manifest.sources` में स्पष्ट नामित फ़ाइलें `--root` के सापेक्ष पढ़ता है। वह निर्देशिका में पुनरावर्ती खोज या आपके होम फ़ोल्डर में खोज नहीं करता। डिफ़ॉल्ट आउटपुट JSON है। `--lang en|ru|de|es` पर केवल मानवीय संदेश बदलते हैं; फ़ील्ड नाम और निदान कोड स्थिर रहते हैं। `--help` शीर्ष स्तर और हर आदेश पर उपलब्ध है। लागू करने, अपलोड, खोज या प्रमाणीकरण का आदेश नहीं है।

निकास स्थिति:

- **0:** समर्थित इनपुट दायरा आंतरिक रूप से संगत और समीक्षा के लिए तैयार है।
- **2:** अमान्य तर्क/इनपुट, अपठनीय फ़ाइल या स्कीमा/सीमा उल्लंघन।
- **3:** संरचनात्मक रूप से सही इनपुट ने विरोध या अनसुलझे दायरे के कारण अवरुद्ध योजना बनाई।

तर्क पार्स होने के बाद इनपुट विफलता stdout पर `status: invalid` वाला JSON आवरण देती है। तर्क त्रुटियाँ stderr पर स्थानीयकृत उपयोग-सहायता छापती हैं। सफल फ़िंगरप्रिंट गणना केवल हैश छापती है। पाठ मोड में प्रस्तावित संपादन के मशीन फ़ील्ड नाम रहते हैं, व्याख्याएँ अनूदित होती हैं।

परिचालन फ़ाइलें निजी निर्देशिका में रखें। stdout पुनर्निर्देशन आपकी रिपोर्ट बनाता है, जिसमें पहचान बताने वाले एंटिटी नाम और फ़ाइल पथ हो सकते हैं। साधन खुद कुछ नहीं लिखता। `python3 -m pip uninstall ha-entity-migrations` से हटाएँ। डेवलपर जाँचों के लिए [CONTRIBUTING](../../CONTRIBUTING.md) देखें।
