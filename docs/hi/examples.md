# समझाए गए उदाहरण

<!-- language-navigation:start -->
<p dir="ltr">
<a href="../en/examples.md" lang="en" dir="ltr">English</a> ·
<a href="../ar/examples.md" lang="ar" dir="rtl">العربية</a> ·
<a href="../bn/examples.md" lang="bn" dir="ltr">বাংলা</a> ·
<a href="../cs/examples.md" lang="cs" dir="ltr">Čeština</a> ·
<a href="../de/examples.md" lang="de" dir="ltr">Deutsch</a> ·
<a href="../es/examples.md" lang="es" dir="ltr">Español</a> ·
<a href="../fa/examples.md" lang="fa" dir="rtl">فارسی</a> ·
<a href="../fr/examples.md" lang="fr" dir="ltr">Français</a> ·
<a href="../he/examples.md" lang="he" dir="rtl">עברית</a> ·
<a href="../hi/examples.md" lang="hi" dir="ltr">हिन्दी</a> ·
<a href="../id/examples.md" lang="id" dir="ltr">Bahasa Indonesia</a> ·
<a href="../it/examples.md" lang="it" dir="ltr">Italiano</a> ·
<a href="../ja/examples.md" lang="ja" dir="ltr">日本語</a> ·
<a href="../ko/examples.md" lang="ko" dir="ltr">한국어</a> ·
<a href="../nl/examples.md" lang="nl" dir="ltr">Nederlands</a> ·
<a href="../pl/examples.md" lang="pl" dir="ltr">Polski</a> ·
<a href="../pt/examples.md" lang="pt" dir="ltr">Português</a> ·
<a href="../ru/examples.md" lang="ru" dir="ltr">Русский</a> ·
<a href="../th/examples.md" lang="th" dir="ltr">ไทย</a> ·
<a href="../tr/examples.md" lang="tr" dir="ltr">Türkçe</a> ·
<a href="../uk/examples.md" lang="uk" dir="ltr">Українська</a> ·
<a href="../vi/examples.md" lang="vi" dir="ltr">Tiếng Việt</a> ·
<a href="../zh-Hans/examples.md" lang="zh-Hans" dir="ltr">简体中文</a> ·
<a href="../zh-Hant/examples.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

[इनपुट मॉडल](model.md) · [संरचना](architecture.md)

यहाँ सभी हार्डवेयर और भूमिकाएँ कृत्रिम हैं। समान इनपुट दोबारा बनाने के लिए `python3 tools/generate_examples.py` चलाएँ। कोई आदेश Home Assistant से नहीं जुड़ता।

## नए उपयोग वाले प्लग से लैंप की भूमिका अलग होती है

`examples/role-swap` के लिए README वाला आदेश चलाएँ। शुरुआत में `plug-a/1` के पास `light.workbench` और `plug-b/1` के पास `switch.spare` है। मैनिफ़ेस्ट प्लग A को पंप की भूमिका और B को कार्यमेज़ की भूमिका देता है। प्रकाश स्वचालन `follows_role` इस्तेमाल करता है और केवल `workbench` की अनुमति देता है। लक्ष्य हार्डवेयर बदलता है लेकिन उसका संदर्भ `light.workbench` ही रहता है। पाठ-संपादन न होना अपेक्षित परिणाम है, अधूरा माइग्रेशन नहीं। रिपोर्ट का `assignments` मानव समीक्षा के लिए हार्डवेयर बदलाव रखता है।

पुराना अतिरिक्त उपभोक्ता `/1` पर, अर्थात दूसरे पूरे स्वचालन ऑब्जेक्ट के रूप में हटाया जाता है। इससे खाली क्रिया-क्रम नहीं बचता। रिपोर्ट केवल सलाह है; प्रोग्राम JSON ऐरे का कोई तत्व नहीं हटाता। कई प्रस्तावित ऐरे-हटाव हाथ से लागू करते समय इंडेक्स खिसकने का ध्यान रखें और नए स्नैपशॉट से फिर चलाएँ।

अनुमत भूमिका `workbench` रखते हुए पहली नीति `follows_hardware` करें: योजना `role_not_allowed` से रुकती है। अनुमत सूची में पंप जोड़ना स्पष्ट और खतरनाक इरादा-बदलाव है, त्रुटि हटाने का सामान्य उपाय नहीं। सही नीति बहाल करें।

## रिले light से switch बनता है

```sh
ha-entity-migrations plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change
```

दो प्रस्तावित संपादन लक्ष्य और उसकी `light.turn_off` सेवा बदलते हैं। स्रोत क्रिया में चमक का डेटा जोड़ें, स्वीकृत स्रोत फ़िंगरप्रिंट अपडेट करें और फिर चलाएँ: `service_data_review` स्वचालित रूपांतरण रोकता है। केवल साधन की जाँच पास करने के लिए चमक सेटिंग न हटाएँ; अपेक्षित व्यवहार की समीक्षा करें।

## अनसुलझा टेम्पलेट

वही आदेश `examples/blocked-template` के साथ चलाएँ। लक्ष्य गतिशील Jinja है। साधन उसका मूल्यांकन नहीं करता और कोड 3 देता है। पूर्ण समर्थित योजना के लिए प्रमाणित शाब्दिक लक्ष्यों वाला स्पष्ट कॉन्फ़िगरेशन चाहिए; अन्यथा इसे तैयार दायरे से बाहर दस्तावेज़ित हस्तचालित माइग्रेशन रखें। निकास कोड अनदेखा करने से टेम्पलेट नहीं सुलझता।

## विचलन और दोहराव

मैनिफ़ेस्ट हैश बदले बिना स्रोत संपादित करने पर `stale_source` मिलता है। स्नैपशॉट बदलने पर `stale_snapshot` मिलता है। इन पुराने मॉडलों के लिए संभावित संदर्भ-संपादन नहीं निकलते। फ़ाइलें समान हों तो चुनी भाषा के अलावा JSON परिणाम निश्चित रहता है। स्रोत फ़ाइलें बाइट-दर-बाइट अपरिवर्तित रहती हैं।

वास्तविक प्रोजेक्ट में प्रारूप निजी फ़ोल्डर में कॉपी करें, भौतिक पहचान जाँचें, उपभोक्ता सूचीबद्ध करें और प्लानर चलाएँ। सभी असाइनमेंट और संपादन देखें, स्थापित परिनियोजन प्रक्रिया में HA की अपनी जाँचें करें, फिर परिणाम सत्यापित करने के लिए नया केवल-पठन स्नैपशॉट बनाएँ। प्रोजेक्ट उस परिनियोजन या रोलबैक निष्पादक को लागू नहीं करता।
