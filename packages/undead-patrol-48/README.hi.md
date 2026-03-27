<p align="center">
  <a href="README.ja.md">日本語</a> | <a href="README.zh.md">中文</a> | <a href="README.es.md">Español</a> | <a href="README.fr.md">Français</a> | <a href="README.md">English</a> | <a href="README.it.md">Italiano</a> | <a href="README.pt-BR.md">Português (BR)</a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/zombie-sprite-pack/readme.png" width="400" alt="Undead Patrol">
</p>

<p align="center">
  <a href="https://github.com/mcp-tool-shop-org/zombie-sprite-pack/actions"><img src="https://github.com/mcp-tool-shop-org/zombie-sprite-pack/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://www.npmjs.com/package/@sprite-foundry/undead-patrol-48"><img src="https://img.shields.io/npm/v/@sprite-foundry/undead-patrol-48" alt="npm version"></a>
  <a href="https://github.com/mcp-tool-shop-org/zombie-sprite-pack/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License"></a>
  <a href="https://mcp-tool-shop-org.github.io/zombie-sprite-pack/"><img src="https://img.shields.io/badge/Landing_Page-live-blue" alt="Landing Page"></a>
</p>

एक 48px का, 8 दिशाओं वाला पिक्सेल आर्ट ज़ॉम्बी दुश्मन पैक, जिसमें इंजन-स्वतंत्र गेम उपयोग के लिए एल्बिडो, नॉर्मल और डेप्थ मैप शामिल हैं।

![अंडरडेड पेट्रोल बैनर](previews/banner.png)

## इसमें क्या शामिल है

8 ज़ॉम्बी वेरिएंट, प्रत्येक में 8 दिशात्मक दृश्य:

![वेरिएंट लाइनअप](previews/lineup.png)

| वेरिएंट | भूमिका | रूपरेखा |
|---------|------|------------|
| शंबलर | बेसिक अंडरडेड | झुका हुआ, धीमा, टूटा हुआ आसन |
| रनर | तेज़ खतरा | झुका हुआ, आगे की ओर, आक्रामक चाल |
| रॉयट ज़ॉम्बी | बख़्तरबंद टैंक | भारी कंधे, ढाल/बख्तरबंद |
| हेज़मेट ज़ॉम्बी | संदूषित विशेषज्ञ | सूट का द्रव्यमान, गोल हुड प्रोफाइल |
| ब्लॉटर | क्षेत्रीय खतरा | चौड़ा धड़, सूजा हुआ असंतुलन |
| स्केलेटल ज़ॉम्बी | नाजुक/प्राचीन | पतली भुजाएं, कोणीय रूप |
| वर्कर ज़ॉम्बी | औद्योगिक/नागरिक | समान, टूल-बेल्ट, पहचानने योग्य गियर |
| एलिट ज़ॉम्बी | कमांडर/बर्बर | ऊंचा, प्रभावशाली, उन्नत द्रव्यमान |

प्रत्येक वेरिएंट में तीन मैप लेयर शामिल हैं:

- **एल्बिडो** — बेस कलर स्प्राइट (पारदर्शी PNG)
- **नॉर्मल** — गतिशील लाइटिंग के लिए नॉर्मल मैप
- **डेप्थ** — पैरलैक्स और ऊंचाई प्रभावों के लिए डेप्थ मैप

## इंस्टॉल करें

```bash
npm install @sprite-foundry/undead-patrol-48
```

## फ़ोल्डर संरचना

```
assets/
  shambler/
    albedo/    8 directional PNGs (front, front_left, left, back_left, back, back_right, right, front_right)
    normal/    8 matching normal maps
    depth/     8 matching depth maps
    preview/   contact sheet
    manifest.json
  runner/
  riot-zombie/
  hazmat-zombie/
  bloater/
  skeletal-zombie/
  worker-zombie/
  elite-zombie/
pack.json          pack-level index
previews/          banner and lineup sheets
```

## मैनिफेस्ट फॉर्मेट

प्रत्येक वेरिएंट में एक `manifest.json` होता है:

```json
{
  "slug": "shambler",
  "name": "Shambler",
  "version": "1.0.0",
  "tileSize": 48,
  "directions": ["front", "front_left", "left", "back_left", "back", "back_right", "right", "front_right"],
  "layers": {
    "albedo": "albedo/{direction}.png",
    "normal": "normal/{direction}.png",
    "depth": "depth/{direction}.png"
  },
  "preview": "preview/contact_sheet.png"
}
```

पैक-लेवल `pack.json` में सभी वेरिएंट के पथ और प्रत्येक मैनिफेस्ट के पथ शामिल हैं।

## इंजन संगतता

ये सादे PNG फाइलें हैं जिनमें JSON मेटाडेटा है। ये किसी भी इंजन या फ्रेमवर्क के साथ काम करते हैं जो छवियों को लोड कर सकता है:

- Phaser
- PixiJS
- Godot
- RPG Maker
- Unity (2D)
- कस्टम इंजन

कोई इंजन-विशिष्ट फॉर्मेट या रनटाइम निर्भरता नहीं।

## विशेषताएं

- **टाइल का आकार:** 48 x 48 px
- **दिशाएं:** 8 (सामने, सामने-बाएं, बाएं, पीछे-बाएं, पीछे, पीछे-दाएं, दाएं, सामने-दाएं)
- **फॉर्मेट:** पारदर्शी PNG
- **मैप:** एल्बिडो + नॉर्मल + डेप्थ
- **एनीमेशन:** स्थिर मुद्राएं (v1)
- **परिप्रेक्ष्य:** टॉप-डाउन

## पैक को विस्तारित करना

क्या आप अतिरिक्त ज़ॉम्बी वेरिएंट बनाना चाहते हैं जो इस पैक की कला शैली और निर्यात अनुबंध से मेल खाते हों?

यह पैक [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) के साथ बनाया गया था, जो एक ओपन-सोर्स ComfyUI + SDXL पिक्सेल-आर्ट जनरेशन पाइपलाइन है। फाउंड्री रिपॉजिटरी में वह सब कुछ है जिसकी आपको आवश्यकता है:

- **जनरेशन पाइपलाइन** — `pipeline/foundry_gen.py` प्रति-विषय कॉन्फ़िगरेशन के साथ ComfyUI को चलाता है
- **विषय कॉन्फ़िगरेशन** — `pipeline/chars/zombie_*.json` इस पैक में प्रत्येक वेरिएंट के लिए सटीक प्रॉम्प्ट, बीज, रूपरेखा नियम और अस्वीकृति शर्तों को परिभाषित करते हैं
- **बैच मैनिफेस्ट** — `pipeline/manifests/undead_patrol_01.json` सभी 8 कॉन्फ़िगरेशन को निर्यात संरचना में मैप करता है
- **एक्सपोर्ट CLI** — `foundry export <run_id>` चेकसम के साथ नियतात्मक पैक बनाता है
- **कंट्रोलनेट ट्यूनिंग** — ह्यूमनॉइड डेप्थ स्ट्रेंथ 0.60, एंड% 0.85 (मैनिफेस्ट में प्रलेखित)

एक नया वेरिएंट जोड़ने के लिए:

1. `pipeline/chars/` में मौजूदा ज़ॉम्बी कॉन्फ़िगरेशन का पालन करते हुए एक विषय कॉन्फ़िगरेशन बनाएं
2. रजिस्टर करें: `python -m foundry.cli subject-add <id> --name "नाम"`
3. उत्पन्न करें: `python -m pipeline.foundry_gen --config pipeline/chars/<config>.json`
4. समीक्षा करें, स्वीकार करें, मैप बनाएं, समाप्त करें, निर्यात करें
5. निर्यात किए गए पैक को संबंधित `assets/<slug>/` निर्देशिका में कॉपी करें

[Sprite Foundry README](https://github.com/mcp-tool-shop-org/sprite-foundry#readme) में पूरी पाइपलाइन का विवरण दिया गया है।

## सुरक्षा

यह पैकेज केवल स्थिर पीएनजी (PNG) छवियों और जेएसओएन (JSON) मेटाडेटा को ही शामिल करता है। इसमें कोई निष्पादन योग्य कोड, कोई इंस्टॉलेशन प्रक्रिया, कोई नेटवर्क एक्सेस और कोई टेलीमेट्री (डेटा संग्रह) नहीं है। डिज़ाइन के अनुसार, सभी फाइलें केवल पढ़ने के लिए हैं।

सुरक्षा नीति के बारे में पूरी जानकारी के लिए, [SECURITY.md](SECURITY.md) देखें।

## लाइसेंस

एमआईटी (MIT) — इसका उपयोग व्यावसायिक और गैर-व्यावसायिक दोनों परियोजनाओं में किया जा सकता है।

## कृतज्ञता

यह [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) का उपयोग करके, ComfyUI + SDXL पिक्सेल-आर्ट पाइपलाइन के साथ बनाया गया है।

यह <a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a> द्वारा बनाया गया है।
