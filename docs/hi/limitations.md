# सीमाएँ और समीक्षा का दायरा

<!-- language-navigation:start -->
<p dir="ltr">
<a href="../en/limitations.md" lang="en" dir="ltr">English</a> ·
<a href="../ar/limitations.md" lang="ar" dir="rtl">العربية</a> ·
<a href="../bn/limitations.md" lang="bn" dir="ltr">বাংলা</a> ·
<a href="../cs/limitations.md" lang="cs" dir="ltr">Čeština</a> ·
<a href="../de/limitations.md" lang="de" dir="ltr">Deutsch</a> ·
<a href="../es/limitations.md" lang="es" dir="ltr">Español</a> ·
<a href="../fa/limitations.md" lang="fa" dir="rtl">فارسی</a> ·
<a href="../fr/limitations.md" lang="fr" dir="ltr">Français</a> ·
<a href="../he/limitations.md" lang="he" dir="rtl">עברית</a> ·
<a href="../hi/limitations.md" lang="hi" dir="ltr">हिन्दी</a> ·
<a href="../id/limitations.md" lang="id" dir="ltr">Bahasa Indonesia</a> ·
<a href="../it/limitations.md" lang="it" dir="ltr">Italiano</a> ·
<a href="../ja/limitations.md" lang="ja" dir="ltr">日本語</a> ·
<a href="../ko/limitations.md" lang="ko" dir="ltr">한국어</a> ·
<a href="../nl/limitations.md" lang="nl" dir="ltr">Nederlands</a> ·
<a href="../pl/limitations.md" lang="pl" dir="ltr">Polski</a> ·
<a href="../pt/limitations.md" lang="pt" dir="ltr">Português</a> ·
<a href="../ru/limitations.md" lang="ru" dir="ltr">Русский</a> ·
<a href="../th/limitations.md" lang="th" dir="ltr">ไทย</a> ·
<a href="../tr/limitations.md" lang="tr" dir="ltr">Türkçe</a> ·
<a href="../uk/limitations.md" lang="uk" dir="ltr">Українська</a> ·
<a href="../vi/limitations.md" lang="vi" dir="ltr">Tiếng Việt</a> ·
<a href="../zh-Hans/limitations.md" lang="zh-Hans" dir="ltr">简体中文</a> ·
<a href="../zh-Hant/limitations.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

[संरचना](architecture.md) · [सुरक्षा](../../SECURITY.md)

योजना की सटीकता भौतिक/चैनल/भूमिका घोषणाओं और दी गई फ़ाइलों तक सीमित है। साधन छोड़े गए डैशबोर्ड, डिवाइस ट्रिगर, दृश्य, ब्लूप्रिंट, अन्यत्र संग्रहीत स्वचालन, Matter फ़िल्टर, बाहरी क्लाइंट या छिपी एकीकरण स्थिति नहीं खोजता। तैयार रिपोर्ट को पूर्ण Home Assistant ऑडिट न कहें। इस संस्करण में भूमिका अद्वितीय है; कई-से-कई अर्थगत भूमिकाओं और समूहों को हाथ से अलग करना पड़ता है।

JSON कॉन्फ़िगरेशन स्रोत समर्थित हैं। YAML, include, उपनाम, ऐंकर, चलने योग्य टैग, कस्टम घटक और रनटाइम पर बने टेम्पलेट नहीं समझे जाते। सामान्यीकरण इस संस्करण के बाहर है और अर्थ खो सकता है; मूल रखें और समकक्षता जाँचें। समर्थित JSON भी HA के पूरे कॉन्फ़िगरेशन स्कीमा से नहीं जाँचा जाता। स्पष्ट उपभोक्ता ऑब्जेक्ट हटाने पर अमान्य पैरेंट बच सकता है; पैरेंट देखें और सामान्य स्टेजिंग प्रक्रिया में HA कॉन्फ़िगरेशन चेकर चलाएँ।

क्षमताएँ और अनुमत भूमिकाएँ स्पष्ट प्रतिबंध हैं, अनुमानित सुरक्षा नहीं। साधन नहीं जान सकता कि पहले निरापद सॉकेट में पंप या गैराज ड्राइव लगा दिया गया है। रिले की बताई स्थिति संपर्क/लोड का व्यवहार सिद्ध नहीं करती। केवल नाम सत्यापित करने के लिए पूरे घर की स्क्रिप्ट न चलाएँ या सक्रिय उपकरण की बिजली बंद-चालू न करें। भौतिक कमीशनिंग अलग नियंत्रित प्रक्रिया है।

यह संस्करण योजना लागू नहीं करता, रजिस्ट्री एंटिटी का नाम या अद्वितीय ID नहीं बदलता, HA पुनः लोड नहीं करता, नियंत्रक पुनः आरंभ नहीं करता, एकीकरण नहीं हटाता और बदलाव वापस नहीं करता। लौटाए ऑपरेशन सलाह हैं, चलने योग्य JSON Patch नहीं। इन्हें हाथ से लागू करने पर नया स्नैपशॉट लें और हर समीक्षित बदलाव के बाद सत्यापित करें; इंडेक्स और संस्करण बदल सकते हैं। हैश हस्ताक्षर या पहुँच नियंत्रण नहीं देते।

रिपोर्ट में निजी नाम और पहचान हो सकती हैं। उन्हें सार्वजनिक Git, इश्यू ट्रैकर और CI आर्टिफ़ैक्ट से बाहर रखें। सार्वजनिक उदाहरण कृत्रिम डिवाइस इस्तेमाल करते हैं और वास्तविक क्षेत्र-परीक्षण का दावा नहीं करते। निदान जानबूझकर योजना रोकते हैं; कोई force फ़्लैग, ignore सूची या छिपा उदार मोड नहीं है।
