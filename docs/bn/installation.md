# ইনস্টলেশন ও CLI

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

[ডকুমেন্টেশনের সূচি](../../README.md#documentation)

Python 3.11 বা নতুন সংস্করণ ব্যবহার করুন। আলাদা ভার্চুয়াল পরিবেশ তৈরি ও সক্রিয় করে চেকআউট থেকে `python3 -m pip install -e .` চালান। প্যাকেজের রানটাইম নির্ভরতা নেই; pip বিল্ড ব্যাকএন্ড আনতে পারে। অফলাইন যন্ত্রের জন্য wheel ও বিল্ড নির্ভরতা আগে প্রস্তুত করুন। `ha-entity-migrations --version` দিয়ে নির্বাচিত ইনস্টলেশন যাচাই করুন; এটি ইনস্টল করা প্যাকেজের সংস্করণ দেখায়।

CLI-তে দুটি নির্দেশ আছে; সাধারণ ভাষার বিকল্প নির্দেশের আগে বসে:

```sh
ha-entity-migrations --lang ru fingerprint examples/domain-change/snapshot.json
ha-entity-migrations --lang en plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change --format text
```

`fingerprint` ফাইলের সঠিক বাইটের SHA-256 ছোট হাতের অক্ষরে ছাপে। এটি ফাইলকে JSON হিসেবে যাচাই করে না। ম্যানিফেস্টে স্ন্যাপশট ও উৎসের ফিঙ্গারপ্রিন্ট ফাঁকসহ হুবহু ফাইলগুলোর সঙ্গে মিলতে হবে। শুধু অপ্রত্যাশিত বিচ্যুতি চাপা দিতে ফিঙ্গারপ্রিন্ট হালনাগাদ করবেন না; আগে নতুন ইনপুট তুলনা ও অনুমোদন করুন।

`plan` একটি JSON ম্যানিফেস্ট, স্বাভাবিকীকৃত JSON স্ন্যাপশট এবং শুধু `manifest.sources`-এ স্পষ্ট নামযুক্ত ফাইল `--root`-এর সাপেক্ষে পড়ে। ডিরেক্টরি পুনরাবৃত্তভাবে খোঁজে না বা আপনার হোম ফোল্ডার অনুসন্ধান করে না। ডিফল্ট আউটপুট JSON। `--lang en|ru|de|es`-এ শুধু মানুষের জন্য বার্তা বদলায়; ফিল্ডের নাম ও ডায়াগনস্টিক কোড স্থির থাকে। `--help` মূল স্তর ও প্রতিটি নির্দেশে আছে। প্রয়োগ, আপলোড, আবিষ্কার বা প্রমাণীকরণের নির্দেশ নেই।

প্রস্থান অবস্থা:

- **0:** সমর্থিত ইনপুটের পরিসর অভ্যন্তরীণভাবে সামঞ্জস্যপূর্ণ এবং পর্যালোচনার জন্য প্রস্তুত।
- **2:** অবৈধ আর্গুমেন্ট/ইনপুট, অপাঠ্য ফাইল বা স্কিমা/সীমা লঙ্ঘন।
- **3:** গঠনগতভাবে সঠিক ইনপুট বিরোধ বা অমীমাংসিত পরিসরের কারণে অবরুদ্ধ পরিকল্পনা তৈরি করেছে।

আর্গুমেন্ট পার্সের পর ইনপুট ব্যর্থতা stdout-এ `status: invalid`-সহ JSON আবরণ দেয়। আর্গুমেন্ট ত্রুটি stderr-এ স্থানীয় ভাষায় ব্যবহারবিধি ছাপে। সফল ফিঙ্গারপ্রিন্ট গণনা শুধু হ্যাশ ছাপে। টেক্সট মোডে প্রস্তাবিত সম্পাদনার রেকর্ডে মেশিনের ফিল্ডের নাম থাকে, ব্যাখ্যা অনূদিত হয়।

চালনার ফাইল ব্যক্তিগত ডিরেক্টরিতে রাখুন। stdout অন্যত্র পাঠালে নিজস্ব প্রতিবেদন তৈরি হয়, যাতে পরিচয়বাহী সত্তার নাম ও ফাইলের পথ থাকতে পারে। টুল নিজে কিছু লেখে না। `python3 -m pip uninstall ha-entity-migrations` দিয়ে সরান। ডেভেলপার পরীক্ষার জন্য [CONTRIBUTING](../../CONTRIBUTING.md) দেখুন।
