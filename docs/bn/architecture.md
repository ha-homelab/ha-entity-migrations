# স্থাপত্য ও প্রতিবেদনের চুক্তি

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

[মডেল](model.md) · [সীমাবদ্ধতা](limitations.md)

![শুধু পড়ার ডেটাপ্রবাহ](../diagrams/pipeline.svg)

`io.py` ফাইল, পথ ও JSON-এর সীমা এবং নির্ভুল পয়েন্টার প্রয়োগ করে। `planner.py` ঘোষণা যাচাই করে, আগে/পরের মানচিত্র তৈরি করে, উৎসের মান স্ক্যান করে, স্পষ্ট নীতি সমাধান করে এবং ডায়াগনস্টিক রেকর্ড সংগ্রহ করে। `cli.py` অনূদিত বার্তা যোগ করে প্রতিবেদন ছাপে। `i18n.py`-তে চারটি পূর্ণাঙ্গ বার্তার ক্যাটালগ আছে। এই পথে নেটওয়ার্ক বা Home Assistant-এর ওপর নির্ভরতা নেই।

স্ক্যানার ইচ্ছাকৃতভাবে সতর্ক। হুবহু সত্তার রেফারেন্সের মতো স্ট্রিং স্ন্যাপশটের সঙ্গে যাচাই করা হয়। ভেতরে বসানো রেফারেন্সসহ স্ট্রিং অমীমাংসিত থাকে। কী বা মানের টেমপ্লেট এবং ডিভাইস/এলাকা/লেবেলের লক্ষ্য-কী অমীমাংসিত থাকে, অর্থ সহজে অনুমানযোগ্য মনে হলেও। সাধারণ সার্ভিস ফিল্ডকে সত্তার ID ধরা হয় না; গতিশীল সার্ভিস তবু অমীমাংসিত থাকে। JSON নয় এমন ফাইল অসমর্থিত উৎস হিসেবে নথিভুক্ত হয়ে পরিকল্পনা আটকে দেয়। এটি সাধারণ HA পার্সার নয়।

![নীতির সিদ্ধান্তপ্রবাহ](../diagrams/policy.svg)

## স্থিতিশীল JSON আবরণ, স্কিমার সংস্করণ 1

`schema_version`, `tool_version`, `status`, `read_only`, `scope`, `snapshot_sha256`, `source_sha256`, `assignments`, `edits`, `diagnostics`, `language`, `summary`। বৈধ ইনপুটে `status` হয় ready বা blocked। `scope` সব সময় `supplied_files_only`; `read_only` সব সময় true। ইনপুট ত্রুটি ইনস্টলেশনে বর্ণিত ছোট invalid আবরণ ব্যবহার করে।

সম্পাদনায় অপারেশন, ফাইল ও পয়েন্টার থাকে। `replace_reference`-এ before/after/policy-ও থাকে; `replace_service`-এ before/after; `remove_consumer`-এ অবসান করা রেফারেন্স থাকে। এগুলো **চালানো যায় এমন JSON Patch নয়**। লেনদেন, সূচক সরে যাওয়া ও HA-এর জীবনচক্রের অর্থ এখানে অনুপস্থিত। প্রস্তাব হিসেবে পর্যালোচনা করুন; এই সংস্করণ ইচ্ছাকৃতভাবে প্যাচ প্রয়োগকারী দেয় না।

ডায়াগনস্টিকে স্থিতিশীল `code`, `location`, `severity` এবং অনূদিত `message` থাকে। `error` ও `unresolved` দুটোই পরিকল্পনা আটকায়। `blocked` প্রতিবেদনে অপ্রভাবিত রেফারেন্সের প্রস্তাবিত সম্পাদনা থাকতে পারে, কিন্তু কোনোটি প্রস্তুত লেনদেন নয়। পুরোনো বা বিরোধপূর্ণ প্রাথমিক মডেল সব সম্ভাব্য রেফারেন্স-সম্পাদনা বন্ধ করে দেয়। বরাদ্দ সব সময় ব্যবহারকারীর চাওয়া মডেল দেখায়, সম্পন্ন পরিবর্তন নয়।

পুনরুৎপাদনের জন্য প্রতিবেদন উৎস, বরাদ্দ, সম্পাদনা ও ডায়াগনস্টিক সাজায়। বর্তমান সময়ের ছাপ বা বানানো আস্থার স্কোর নেই। বাইটের হ্যাশ কোন ইনপুট সংস্করণ বিশ্লেষিত হয়েছে তা প্রমাণ করে; ইনপুট সত্য বা ডিভাইস নির্দেশ মানবে কি না তা নয়।
