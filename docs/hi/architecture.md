# संरचना और रिपोर्ट अनुबंध

<!-- language-navigation:start -->
<p dir="ltr">
<a href="../en/architecture.md" lang="en" dir="ltr">English</a> ·
<a href="../ar/architecture.md" lang="ar" dir="rtl">العربية</a> ·
<a href="../bn/architecture.md" lang="bn" dir="ltr">বাংলা</a> ·
<a href="../cs/architecture.md" lang="cs" dir="ltr">Čeština</a> ·
<a href="../de/architecture.md" lang="de" dir="ltr">Deutsch</a> ·
<a href="../es/architecture.md" lang="es" dir="ltr">Español</a> ·
<a href="../fa/architecture.md" lang="fa" dir="rtl">فارسی</a> ·
<a href="../fr/architecture.md" lang="fr" dir="ltr">Français</a> ·
<a href="../he/architecture.md" lang="he" dir="rtl">עברית</a> ·
<a href="../hi/architecture.md" lang="hi" dir="ltr">हिन्दी</a> ·
<a href="../id/architecture.md" lang="id" dir="ltr">Bahasa Indonesia</a> ·
<a href="../it/architecture.md" lang="it" dir="ltr">Italiano</a> ·
<a href="../ja/architecture.md" lang="ja" dir="ltr">日本語</a> ·
<a href="../ko/architecture.md" lang="ko" dir="ltr">한국어</a> ·
<a href="../nl/architecture.md" lang="nl" dir="ltr">Nederlands</a> ·
<a href="../pl/architecture.md" lang="pl" dir="ltr">Polski</a> ·
<a href="../pt/architecture.md" lang="pt" dir="ltr">Português</a> ·
<a href="../ru/architecture.md" lang="ru" dir="ltr">Русский</a> ·
<a href="../th/architecture.md" lang="th" dir="ltr">ไทย</a> ·
<a href="../tr/architecture.md" lang="tr" dir="ltr">Türkçe</a> ·
<a href="../uk/architecture.md" lang="uk" dir="ltr">Українська</a> ·
<a href="../vi/architecture.md" lang="vi" dir="ltr">Tiếng Việt</a> ·
<a href="../zh-Hans/architecture.md" lang="zh-Hans" dir="ltr">简体中文</a> ·
<a href="../zh-Hant/architecture.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

[मॉडल](model.md) · [सीमाएँ](limitations.md)

![केवल पढ़ने वाला डेटा प्रवाह](../diagrams/pipeline.svg)

`io.py` फ़ाइल, पथ और JSON की सीमाएँ तथा सटीक पॉइंटर लागू करता है। `planner.py` घोषणाएँ जाँचता है, बदलाव से पहले/बाद के मानचित्र बनाता है, स्रोत मानों को स्कैन करता है, स्पष्ट नीतियाँ हल करता है और निदान रिकॉर्ड इकट्ठे करता है। `cli.py` अनूदित संदेश जोड़कर रिपोर्ट छापता है। `i18n.py` में चार पूर्ण संदेश-सूचियाँ हैं। इस प्रक्रिया की नेटवर्क या Home Assistant पर निर्भरता नहीं है।

स्कैनर जानबूझकर सावधानी बरतता है। एंटिटी संदर्भ जैसे सटीक स्ट्रिंग स्नैपशॉट से जाँचे जाते हैं। भीतर समाहित संदर्भ वाले स्ट्रिंग अनसुलझे रहते हैं। कुंजियों या मानों में टेम्पलेट तथा डिवाइस/क्षेत्र/लेबल की लक्ष्य-कुंजियाँ अनसुलझी रहती हैं, भले उनका अर्थ अनुमान लगाना आसान लगे। सामान्य सेवा फ़ील्ड एंटिटी ID नहीं माने जाते; गतिशील सेवाएँ फिर भी अनसुलझी रहती हैं। गैर-JSON फ़ाइलें असमर्थित स्रोत के रूप में दर्ज होकर योजना रोकती हैं। यह सामान्य HA पार्सर नहीं है।

![नीति निर्णय प्रवाह](../diagrams/policy.svg)

## स्थिर JSON आवरण, स्कीमा संस्करण 1

`schema_version`, `tool_version`, `status`, `read_only`, `scope`, `snapshot_sha256`, `source_sha256`, `assignments`, `edits`, `diagnostics`, `language`, `summary`। वैध इनपुट पर `status` ready या blocked होता है। `scope` हमेशा `supplied_files_only` और `read_only` हमेशा true है। इनपुट त्रुटियाँ स्थापना में वर्णित छोटा invalid आवरण इस्तेमाल करती हैं।

संपादनों में ऑपरेशन, फ़ाइल और पॉइंटर होते हैं। `replace_reference` में before/after/policy भी होते हैं; `replace_service` में before/after; `remove_consumer` में हटाया जाने वाला संदर्भ होता है। ये **चलाने योग्य JSON Patch नहीं हैं**। इनमें ट्रांज़ैक्शन, इंडेक्स खिसकने और HA जीवनचक्र की कार्यविधि नहीं है। इन्हें सुझाव मानकर जाँचें; यह संस्करण जानबूझकर पैच लागू करने वाला साधन नहीं देता।

निदान में स्थिर `code`, `location`, `severity` और अनूदित `message` होते हैं। `error` और `unresolved` दोनों योजना रोकते हैं। `blocked` रिपोर्ट में अप्रभावित संदर्भों के संभावित संपादन हो सकते हैं, पर उनमें से कोई तैयार ट्रांज़ैक्शन नहीं है। पुराने या विरोधाभासी प्रारंभिक मॉडल सभी संभावित संदर्भ-संपादन रोक देते हैं। असाइनमेंट हमेशा उपयोगकर्ता का माँगा मॉडल दिखाते हैं, पूरे हो चुके बदलाव नहीं।

पुनरुत्पादन के लिए रिपोर्ट स्रोत, असाइनमेंट, संपादन और निदान क्रमबद्ध करती है। मौजूदा टाइमस्टैम्प या मनगढ़ंत विश्वास-अंक नहीं होते। बाइट हैश बताते हैं कि इनपुट के किस संस्करण का विश्लेषण हुआ, यह नहीं कि वह सत्य था या डिवाइस आदेश मानेगा।
