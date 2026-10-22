# ব্যাখ্যাসহ উদাহরণ

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

[ইনপুট মডেল](model.md) · [স্থাপত্য](architecture.md)

এখানকার সব হার্ডওয়্যার ও ভূমিকা কৃত্রিম। `python3 tools/generate_examples.py` দিয়ে হুবহু একই ইনপুট আবার তৈরি করুন। কোনো নির্দেশ Home Assistant-এর সঙ্গে সংযোগ করে না।

## নতুন কাজে ব্যবহৃত প্লাগ ছেড়ে বাতির ভূমিকা সরে যায়

`examples/role-swap`-এর README নির্দেশ চালান। শুরুতে `plug-a/1`-এর কাছে `light.workbench` এবং `plug-b/1`-এর কাছে `switch.spare` থাকে। ম্যানিফেস্ট প্লাগ A-কে পাম্পের ভূমিকা ও B-কে কাজের টেবিলের ভূমিকা দেয়। আলোর অটোমেশন `follows_role` ব্যবহার করে এবং শুধু `workbench` অনুমোদন করে। লক্ষ্য হার্ডওয়্যার বদলালেও রেফারেন্স `light.workbench` থাকে। লেখায় সম্পাদনা না থাকা কাঙ্ক্ষিত ফল, বাদ পড়া মাইগ্রেশন নয়। প্রতিবেদনের `assignments` মানব পর্যালোচনার জন্য হার্ডওয়্যার পরিবর্তন রাখে।

পুরোনো অতিরিক্ত ভোক্তা `/1`-এ, অর্থাৎ পুরো দ্বিতীয় অটোমেশন অবজেক্ট হিসেবে সরানো হয়। ফলে খালি অ্যাকশন-ক্রম থাকে না। প্রতিবেদন পরামর্শমাত্র; প্রোগ্রাম JSON অ্যারের উপাদান মুছে দেয় না। একাধিক প্রস্তাবিত অ্যারে-মোছা হাতে প্রয়োগ করলে সূচক সরে যাওয়া বিবেচনা করুন এবং নতুন স্ন্যাপশট থেকে আবার চালান।

অনুমোদিত ভূমিকা `workbench` রেখে প্রথম নীতি `follows_hardware` করুন: পরিকল্পনা `role_not_allowed` দিয়ে আটকে যায়। অনুমোদিত তালিকায় পাম্প যোগ করা স্পষ্ট ও বিপজ্জনক উদ্দেশ্য-পরিবর্তন, ত্রুটি দূর করার সাধারণ উপায় নয়। সঠিক নীতি ফিরিয়ে আনুন।

## রিলে light থেকে switch হয়

```sh
ha-entity-migrations plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change
```

দুটি প্রস্তাবিত সম্পাদনা লক্ষ্য ও তার `light.turn_off` সার্ভিস বদলায়। উৎস অ্যাকশনে উজ্জ্বলতার ডেটা যোগ করুন, অনুমোদিত উৎসের ফিঙ্গারপ্রিন্ট হালনাগাদ করে আবার চালান: `service_data_review` স্বয়ংক্রিয় রূপান্তর আটকায়। শুধু পরীক্ষায় উত্তীর্ণ হতে উজ্জ্বলতার সেটিং সরাবেন না; কাঙ্ক্ষিত আচরণ পর্যালোচনা করুন।

## অমীমাংসিত টেমপ্লেট

একই নির্দেশ `examples/blocked-template` দিয়ে চালান। লক্ষ্য গতিশীল Jinja। টুল তা মূল্যায়ন করে না এবং কোড 3 ফেরত দেয়। সম্পূর্ণ সমর্থিত পরিকল্পনার জন্য প্রমাণযোগ্য আক্ষরিক লক্ষ্যসহ স্পষ্ট কনফিগারেশন দরকার; নইলে এটি প্রস্তুত পরিসরের বাইরে নথিভুক্ত হাতে করা মাইগ্রেশন হিসেবে রাখুন। প্রস্থান কোড উপেক্ষা করলে টেমপ্লেট সমাধান হয় না।

## বিচ্যুতি ও পুনরাবৃত্তি

ম্যানিফেস্টের হ্যাশ না বদলে উৎস সম্পাদনা করলে `stale_source` হয়। স্ন্যাপশট বদলালে `stale_snapshot` হয়। এই পুরোনো মডেলের জন্য সম্ভাব্য রেফারেন্স-সম্পাদনা বের হয় না। ফাইল অপরিবর্তিত থাকলে বেছে নেওয়া ভাষা ছাড়া JSON ফল নির্ধারিত থাকে। উৎস ফাইল বাইটে বাইটে অপরিবর্তিত থাকে।

বাস্তব প্রকল্পে ফরম্যাট ব্যক্তিগত ফোল্ডারে কপি করুন, শারীরিক পরিচয় যাচাই করুন, ভোক্তা তালিকাভুক্ত করুন এবং পরিকল্পক চালান। সব বরাদ্দ ও সম্পাদনা দেখুন, প্রচলিত স্থাপন-পদ্ধতিতে HA-এর নিজস্ব পরীক্ষা করুন, তারপর ফল যাচাইয়ের জন্য নতুন শুধু-পড়ার স্ন্যাপশট নিন। এই প্রকল্প সেই স্থাপন বা রোলব্যাক চালানোর ব্যবস্থা বাস্তবায়ন করে না।
