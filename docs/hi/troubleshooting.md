# समस्या निवारण

<!-- language-navigation:start -->
<p dir="ltr">
<a href="../en/troubleshooting.md" lang="en" dir="ltr">English</a> ·
<a href="../ar/troubleshooting.md" lang="ar" dir="rtl">العربية</a> ·
<a href="../bn/troubleshooting.md" lang="bn" dir="ltr">বাংলা</a> ·
<a href="../cs/troubleshooting.md" lang="cs" dir="ltr">Čeština</a> ·
<a href="../de/troubleshooting.md" lang="de" dir="ltr">Deutsch</a> ·
<a href="../es/troubleshooting.md" lang="es" dir="ltr">Español</a> ·
<a href="../fa/troubleshooting.md" lang="fa" dir="rtl">فارسی</a> ·
<a href="../fr/troubleshooting.md" lang="fr" dir="ltr">Français</a> ·
<a href="../he/troubleshooting.md" lang="he" dir="rtl">עברית</a> ·
<a href="../hi/troubleshooting.md" lang="hi" dir="ltr">हिन्दी</a> ·
<a href="../id/troubleshooting.md" lang="id" dir="ltr">Bahasa Indonesia</a> ·
<a href="../it/troubleshooting.md" lang="it" dir="ltr">Italiano</a> ·
<a href="../ja/troubleshooting.md" lang="ja" dir="ltr">日本語</a> ·
<a href="../ko/troubleshooting.md" lang="ko" dir="ltr">한국어</a> ·
<a href="../nl/troubleshooting.md" lang="nl" dir="ltr">Nederlands</a> ·
<a href="../pl/troubleshooting.md" lang="pl" dir="ltr">Polski</a> ·
<a href="../pt/troubleshooting.md" lang="pt" dir="ltr">Português</a> ·
<a href="../ru/troubleshooting.md" lang="ru" dir="ltr">Русский</a> ·
<a href="../th/troubleshooting.md" lang="th" dir="ltr">ไทย</a> ·
<a href="../tr/troubleshooting.md" lang="tr" dir="ltr">Türkçe</a> ·
<a href="../uk/troubleshooting.md" lang="uk" dir="ltr">Українська</a> ·
<a href="../vi/troubleshooting.md" lang="vi" dir="ltr">Tiếng Việt</a> ·
<a href="../zh-Hans/troubleshooting.md" lang="zh-Hans" dir="ltr">简体中文</a> ·
<a href="../zh-Hant/troubleshooting.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

[स्थापना](installation.md) · [सीमाएँ](limitations.md)

**आदेश नहीं मिला:** स्थापना वाला ही वर्चुअल वातावरण सक्रिय करें। `python3 -m ha_entity_migrations --version` आज़माएँ; केवल गलत पथ से बचने के लिए सिस्टम Python में स्थापना न करें।

**निकास 2, schema_invalid:** कुंजियों को चलने योग्य उदाहरण और [इनपुट मॉडल](model.md) से मिलाएँ। अज्ञात फ़ील्ड त्रुटि हैं। संस्करण पूर्णांक 1 हैं; चैनल पहचानकर्ता स्ट्रिंग हैं। हर क्रिया नीति को सेवा पॉइंटर चाहिए। स्नैपशॉट में एंटिटी हैं; मैनिफ़ेस्ट में असाइनमेंट और उपभोक्ता। ये परस्पर बदलने योग्य फ़ाइलें नहीं हैं।

**निकास 2, duplicate_source:** दो स्रोत नाम एक भौतिक फ़ाइल पहचानते हैं। `sources` में एक canonical नाम रखें और सभी उपभोक्ता `file` फ़ील्ड बदलें। दोहरे विभाजक या हार्ड-लिंक/केस उपनाम हटाएँ; उपनाम को दूसरी नीति न दें। समान सामग्री वाली अलग फ़ाइलें समर्थित रहती हैं।

**stale_snapshot / stale_source:** वास्तविक बदलावों को स्वीकृत स्रोत से मिलाएँ। समीक्षा के बाद ही fingerprint चलाएँ। खाली जगह बदलने से हैश बदलता है। केवल पुराने हैश को पास कराने के लिए पुरानी प्रति न चुनें।

**source_collision / destination_collision:** भौतिक चैनल, भूमिका या एंटिटी ID दोहराया गया है। भूमिका बदलने के दोनों पक्ष स्पष्ट करें और जाँचें कि अपरिवर्तित एंडपॉइंट इच्छित लक्ष्य ID तो नहीं रखे हुए है।

**role_not_allowed / capability_missing:** उपभोक्ता अनुचित लोड तक पहुँचेगा या क्षमता खोएगा। पुष्टि करें कि उसे भूमिका या हार्डवेयर का अनुसरण करना चाहिए। allowed_roles अपने-आप न बढ़ाएँ या हार्डवेयर में न होने वाली क्षमताएँ न घोषित करें। ऑन/ऑफ़ रिले से बदला प्रकाश डिमिंग नहीं दे सकता।

**missing_policy / unmodeled_reference:** संदर्भित एंडपॉइंट की सूची बनाएँ और उसका उद्देश्य सुनिश्चित होने पर ही स्पष्ट उपभोक्ता घोषणा जोड़ें। पुराना इतिहास-स्ट्रिंग सक्रिय दायरे से बाहर हो सकता है; फ़ाइल सोच-समझकर बाहर करें, बहिष्करण लिखें और स्रोत अनुबंध फिर बनाएँ।

**dynamic_reference / embedded_reference / indirect_target:** यह संस्करण मानचित्र सिद्ध नहीं कर सकता। Jinja या समूह/क्षेत्र/लेबल व्यवहार अलग जाँचें, या स्पष्ट सामान्यीकृत शाब्दिक कॉन्फ़िगरेशन दें। प्रोग्राम टेम्पलेट कभी नहीं चलाता।

**display_domain_review / service_data_review / mixed_action_targets:** कार्ड सुविधाएँ, क्रिया पैरामीटर और लक्ष्य समूह जाँचें। बहु-डोमेन क्रिया को अलग समीक्षित स्रोत बदलाव में बाँटें; केवल उसका सेवा डोमेन न बदलें।

**retire_scope_mixed / overlapping_edits:** असंबंधित संदर्भों के बिना सुसंगत पुराना उपभोक्ता ऑब्जेक्ट चुनें। क्रिया से केवल entity_id न हटाएँ: इससे बहुत व्यापक लक्ष्य या अमान्य कॉन्फ़िगरेशन बन सकता है। प्रोग्राम स्वचालित हटाव लागू नहीं करता।

**unsupported_source:** केवल JSON पर योजना बन सकती है। YAML, बाइनरी और अन्य फ़ाइलें चुपचाप नहीं छोड़ी जातीं। स्पष्ट रूप से सामान्यीकृत JSON प्रति विश्लेषण में मदद कर सकती है, पर वास्तविक संपादन से पहले मूल से तुलना जरूरी है।

न्यूनतम कृत्रिम इनपुट, साधन/Python संस्करण, निकास कोड और निदान कोड के साथ बग रिपोर्ट करें। घर का कच्चा निर्यात या API प्रमाण-पत्र कभी संलग्न न करें।
