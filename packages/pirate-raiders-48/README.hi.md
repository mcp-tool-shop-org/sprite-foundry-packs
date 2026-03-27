<p align="center">
  <a href="README.ja.md">日本語</a> | <a href="README.zh.md">中文</a> | <a href="README.es.md">Español</a> | <a href="README.fr.md">Français</a> | <a href="README.md">English</a> | <a href="README.it.md">Italiano</a> | <a href="README.pt-BR.md">Português (BR)</a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/pirate-raiders-sprite-pack/readme.png" width="400" alt="Pirate Raiders" />
</p>

<p align="center">
  <a href="https://github.com/mcp-tool-shop-org/pirate-raiders-sprite-pack/actions"><img src="https://github.com/mcp-tool-shop-org/pirate-raiders-sprite-pack/actions/workflows/ci.yml/badge.svg" alt="CI" /></a>
  <a href="https://www.npmjs.com/package/@sprite-foundry/pirate-raiders-48"><img src="https://img.shields.io/npm/v/@sprite-foundry/pirate-raiders-48" alt="npm version" /></a>
  <a href="https://github.com/mcp-tool-shop-org/pirate-raiders-sprite-pack/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License" /></a>
  <a href="https://mcp-tool-shop-org.github.io/pirate-raiders-sprite-pack/"><img src="https://img.shields.io/badge/Landing_Page-live-blue" alt="Landing Page" /></a>
</p>

48 पिक्सेल आकार का, 8 दिशाओं वाला समुद्री पात्रों का एक संग्रह, जिसमें एल्बिडो, नॉर्मल और डेप्थ मैप शामिल हैं, जिनका उपयोग किसी भी गेम इंजन के साथ किया जा सकता है। यह [स्प्राइट फाउंड्री](https://github.com/mcp-tool-shop-org/sprite-foundry) कैटलॉग में **पैक 05** है।

## इसमें क्या शामिल है?

समुद्री दुनिया से जुड़े आठ प्रकार के समुद्री डाकू, जिन्हें तीन अलग-अलग शैलियों में दर्शाया गया है:

| विविधता | भूमिका | शिल्पाकृति/आकृति। |
|---------|------|------------|
| कप्तान। | कमांडर | तीन कोणों वाला टोपी, सुनहरे रंग की झालर वाली नौसेना की जैकेट, और कमर पर एक सुंदर कटार। |
| क्वाटरमास्टर। | लॉजिस्टिक्स / अनुशासन | चौड़ी किनारी वाला चमड़े का टोपी, मजबूत कद-काठी, हाथ बांधे हुए, बेल्ट पर चाबी की अंगूठी। |
| अत्यंत प्रतिस्पर्धी सीमावर्ती क्षेत्र। | हाथापाई हमला | लाल रंग का रुमाल, बिना आस्तीन का जैकेट, और दो घुमावदार ब्लेड वाले तलवारें। |
| पिस्तौल चलाने में माहिर व्यक्ति। | दूर की विशेषज्ञ | गहरा लाल रंग का लंबा कोट, फ़्लिंटलॉक पिस्तौल, और गोला-बारूद रखने वाला बेल्ट। |
| नौसेना सैनिक। | सैन्य प्राधिकरण | नीले-सफ़ेद रंग की वर्दी, दो कोणों वाला टोपी, क्रॉस-बेल्ट, और एक साफ-सुथरी सैन्य मुद्रा। |
| हार्बर का गवर्नर। | नागरिक प्राधिकरण | गहरे रंग का औपचारिक कोट, पाउडर से सजी हुई विक (बालों का गुच्छा), गोल-मटोल शरीर, और एक चलने की छड़ी। |
| डूबे हुए रक्षक। | अमर समुद्री | पानी में डूबा हुआ, हरा रंग का त्वचा, फटा हुआ कोट, जंग लगा हुआ लोहे का कवच, समुद्री शैवाल। |
| समुद्री पुजारी। | रहस्यमय / सहायक | कोरल (प्रवाल) शाखाओं से बना मुकुट, गहरे नीले रंग का बहुस्तरीय वस्त्र, और एक श्रृंखला से जुड़ा हुआ, समुद्री जीवों (barnacle) से सजा हुआ धूपदानी। |

प्रत्येक संस्करण में तीन मानचित्र परतें शामिल होती हैं:

- **एल्बिडो:** आधार रंग की छवियां (पारदर्शी पीएनजी प्रारूप में)
- **नॉर्मल:** गतिशील प्रकाश व्यवस्था के लिए नॉर्मल मैप
- **डेप्थ:** पैरलैक्स और ऊंचाई प्रभाव के लिए डेप्थ मैप

## इंस्टॉल करें

```bash
npm install @sprite-foundry/pirate-raiders-48
```

## फ़ोल्डर संरचना।

```
assets/
  captain/
    albedo/    8 directional PNGs (front, front_left, left, back_left, back, back_right, right, front_right)
    normal/    8 matching normal maps
    depth/     8 matching depth maps
    preview/   contact sheet
    manifest.json
  quartermaster/
  cutthroat/
  pistoleer/
  navy-sailor/
  governor/
  drowned/
  sea-priest/
pack.json          pack-level index
previews/          contact sheets per variant
```

## मैनिफेस्ट फ़ॉर्मेट।

प्रत्येक संस्करण में एक `manifest.json` फ़ाइल होती है, जिसमें इसकी उत्पत्ति (provenance) और SHA-256 चेकसम की पूरी जानकारी दी गई है:

```json
{
  "schema_version": "1.0.0",
  "identity": { "subject_slug": "pirate_captain", "display_name": "Captain" },
  "render_contract": {
    "width": 48, "height": 48,
    "direction_order": ["front", "front_left", "left", "back_left", "back", "back_right", "right", "front_right"],
    "pivot": "center_bottom",
    "transparency": true
  },
  "files": { "albedo/front.png": "<sha256>", "normal/front.png": "<sha256>", "..." : "..." }
}
```

"पैक" स्तर पर स्थित `pack.json` फ़ाइल, सभी प्रकारों (variants) को सूचीबद्ध करती है और प्रत्येक "मैनिफेस्ट" फ़ाइल का पथ प्रदान करती है।

## इंजन की अनुकूलता।

ये साधारण पीएनजी (PNG) फाइलें हैं जिनमें जेएसओएन (JSON) मेटाडेटा शामिल है। ये किसी भी ऐसे इंजन या फ्रेमवर्क के साथ काम करती हैं जो छवियों को लोड कर सकते हैं:

- फेज़र
- पिक्सिजेएस
- गॉडोट
- आरपीजी मेकर
- यूनिटी (2डी)
- अनुकूलित इंजन (कस्टम इंजन)

यह किसी विशेष इंजन के लिए डिज़ाइन नहीं किया गया है और न ही इसके लिए किसी विशेष रनटाइम निर्भरता की आवश्यकता है।

## विशेषताएं।

- **टाइल्स का आकार:** 48 x 48 पिक्सेल
- **दिशाएं:** 8 (सामने, सामने-बाएं, बाएं, पीछे-बाएं, पीछे, पीछे-दाएं, दाएं, सामने-दाएं)
- **प्रारूप:** पारदर्शी पीएनजी (PNG)
- **मैप्स:** एल्बिडो (albedo) + सामान्य (normal) + गहराई (depth)
- **एनीमेशन:** स्थिर मुद्राएं (संस्करण 1)
- **दृष्टिकोण:** ऊपर से (टॉप-डाउन)

## पैकेज का विस्तार करना।

क्या आप ऐसे अतिरिक्त "पायरेट" (समुद्री डाकू) संस्करण बनाना चाहते हैं जो इस पैकेज की कला शैली और निर्यात अनुबंध से मेल खाते हों?

यह पैकेज [स्प्राइट फाउंड्री](https://github.com/mcp-tool-shop-org/sprite-foundry) का उपयोग करके बनाया गया है, जो एक ओपन-सोर्स कॉमफीयूआई + एसडीएक्सएल पिक्सेल आर्ट जनरेशन सिस्टम है। इस "फाउंड्री" रिपॉजिटरी में वह सब कुछ है जिसकी आपको आवश्यकता है:

- **जेनरेशन पाइपलाइन:** `pipeline/foundry_gen.py` फ़ाइल, कॉमफ़ीयूआई को प्रत्येक विषय के लिए अलग-अलग कॉन्फ़िगरेशन के साथ चलाती है।
- **विषय कॉन्फ़िगरेशन:** `pipeline/chars/pirate_*.json` फ़ाइलें, इस पैकेज में मौजूद प्रत्येक भिन्नता के लिए सटीक प्रॉम्प्ट, सीड और सिल्हूट नियमों को परिभाषित करती हैं।
- **एक्सपोर्ट कमांड-लाइन इंटरफ़ेस (CLI):** `foundry export <रन_आईडी>` कमांड, चेकसम के साथ स्थिर पैकेज बनाता है।

एक नया विकल्प जोड़ने के लिए:

1. `pipeline/chars/` फ़ोल्डर में, मौजूदा "पायरेट" कॉन्फ़िगरेशन का पालन करते हुए, एक नया विषय कॉन्फ़िगरेशन बनाएं।
2. रजिस्टर करें: `python -m foundry.cli subject-add <id> --name "नाम"`
3. उत्पन्न करें: `python -m pipeline.foundry_gen --config pipeline/chars/<कॉन्फ़िगरेशन>.json`
4. समीक्षा करें, स्वीकार करें, मानचित्र बनाएं, अंतिम स्वीकृति दें, और निर्यात करें।
5. निर्यात किए गए फ़ाइल संग्रह को संबंधित `assets/<स्लग्>/` फ़ोल्डर में कॉपी करें।

"[स्प्राइट फाउंड्री" के लिए दिए गए निर्देशों (रीडमी) में (https://github.com/mcp-tool-shop-org/sprite-foundry#readme), आपको पूरी प्रक्रिया का विस्तृत विवरण मिलेगा।

## सुरक्षा।

इस पैकेज में केवल स्थिर पीएनजी (PNG) चित्र और जेएसओएन (JSON) मेटाडेटा शामिल हैं। इसमें कोई निष्पादन योग्य कोड, कोई इंस्टॉलेशन प्रक्रिया, कोई नेटवर्क एक्सेस और कोई टेलीमेट्री (डेटा संग्रह) नहीं है। डिज़ाइन के अनुसार, इन फ़ाइलों को केवल पढ़ने के लिए ही इस्तेमाल किया जा सकता है।

सुरक्षा नीति के बारे में पूरी जानकारी के लिए, [SECURITY.md](SECURITY.md) देखें।

## लाइसेंस

एमआईटी — वाणिज्यिक और गैर-वाणिज्यिक दोनों परियोजनाओं में उपयोग किया जा सकता है।

## क्रेडिट

[Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) का उपयोग करके, ComfyUI + SDXL पिक्सेल-आर्ट पाइपलाइन के साथ बनाया गया।

यह <a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a> द्वारा बनाया गया है।
