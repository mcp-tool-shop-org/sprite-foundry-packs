<p align="center">
  <a href="README.ja.md">日本語</a> | <a href="README.zh.md">中文</a> | <a href="README.es.md">Español</a> | <a href="README.fr.md">Français</a> | <a href="README.md">English</a> | <a href="README.it.md">Italiano</a> | <a href="README.pt-BR.md">Português (BR)</a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/fantasy-heroes-sprite-pack/readme.png" width="400" alt="Fantasy Heroes" />
</p>

<p align="center">
  <a href="https://github.com/mcp-tool-shop-org/fantasy-heroes-sprite-pack/actions"><img src="https://github.com/mcp-tool-shop-org/fantasy-heroes-sprite-pack/actions/workflows/ci.yml/badge.svg" alt="CI" /></a>
  <a href="https://www.npmjs.com/package/@sprite-foundry/fantasy-heroes-48"><img src="https://img.shields.io/npm/v/@sprite-foundry/fantasy-heroes-48" alt="npm version" /></a>
  <a href="https://github.com/mcp-tool-shop-org/fantasy-heroes-sprite-pack/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License" /></a>
  <a href="https://mcp-tool-shop-org.github.io/fantasy-heroes-sprite-pack/"><img src="https://img.shields.io/badge/Landing_Page-live-blue" alt="Landing Page" /></a>
</p>

एक 48px का, 8 दिशाओं वाला पिक्सेल आर्ट हीरो पार्टी पैक, जिसमें इंजन-स्वतंत्र गेम उपयोग के लिए एल्बेडो, नॉर्मल और डेप्थ मैप शामिल हैं।

![फंतासी नायकों का बैनर](previews/banner.png)

## इसमें क्या शामिल है

8 हीरो आर्कटाइप जो एक पूर्ण साहसिक पार्टी बनाते हैं:

![भिन्न लाइनअप](previews/lineup.png)

| भिन्नता | भूमिका | रूपरेखा |
|---------|------|------------|
| योद्धा | सामने से लड़ने वाला, बहुमुखी | तलवार + ढाल, संतुलित कवच |
| रेंजर | दूर से हमला करने वाला | धनुष, लबादा, हल्की रूपरेखा |
| जादूगर | जादुई शक्ति वाला | छड़ी, वस्त्र, उच्च जादुई रूपरेखा |
| धूर्त | चुपके से हमला करने वाला | हुड, हल्का कवच, छुरी, लचीली मुद्रा |
| पुजारी | चिकित्सक/सहायक | धातु की मल्ल, सूर्य चिह्न वाला ढाल, वस्त्र |
| बर्बर | भारी क्षति पहुंचाने वाला | बड़ा हथियार, चौड़ा ऊपरी शरीर, फर/चमड़े का आवरण |
| पलाडिन | अत्याधुनिक रक्षक | पूर्ण कवच, किट ढाल, युद्ध कुल्हाड़ी, लबादा |
| भिक्षु | तेज़ विशेषज्ञ | बिना कवच, लपेटे, बो स्टाफ, अनुशासित रूपरेखा |

प्रत्येक भिन्नता में तीन मैप परतें शामिल हैं:

- **एल्बेडो** — बेस कलर स्प्राइट (पारदर्शी PNG)
- **नॉर्मल** — गतिशील प्रकाश व्यवस्था के लिए नॉर्मल मैप
- **डेप्थ** — पैरलैक्स और ऊंचाई प्रभावों के लिए डेप्थ मैप

## इंस्टॉल करें

```bash
npm install @sprite-foundry/fantasy-heroes-48
```

## फ़ोल्डर संरचना

```
assets/
  fighter/
    albedo/    8 directional PNGs (front, front_left, left, back_left, back, back_right, right, front_right)
    normal/    8 matching normal maps
    depth/     8 matching depth maps
    preview/   contact sheet
    manifest.json
  ranger/
  mage/
  rogue/
  cleric/
  barbarian/
  paladin/
  monk/
pack.json          pack-level index
previews/          banner and lineup sheets
```

## मैनिफेस्ट प्रारूप

प्रत्येक भिन्नता में एक `manifest.json` होता है:

```json
{
  "slug": "fighter",
  "name": "Fighter",
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

पैक-स्तरीय `pack.json` प्रत्येक भिन्नता के लिए पथ के साथ सभी भिन्नताओं को सूचीबद्ध करता है।

## इंजन संगतता

ये सादे PNG फाइलें हैं जिनमें JSON मेटाडेटा है। ये किसी भी इंजन या फ्रेमवर्क के साथ काम करते हैं जो छवियों को लोड कर सकता है:

- Phaser
- PixiJS
- Godot
- RPG Maker
- Unity (2D)
- कस्टम इंजन

कोई भी इंजन-विशिष्ट प्रारूप या रनटाइम निर्भरता नहीं।

## विशेषताएं

- **टाइल का आकार:** 48 x 48 px
- **दिशाएं:** 8 (सामने, सामने-बाएं, बायां, पीछे-बाएं, पीछे, पीछे-दाएं, दाएं, सामने-दाएं)
- **प्रारूप:** पारदर्शी PNG
- **मैप:** एल्बेडो + नॉर्मल + डेप्थ
- **एनीमेशन:** स्थिर मुद्राएं (v1)
- **दृष्टिकोण:** ऊपर से

## पैक का विस्तार करें

क्या आप अतिरिक्त हीरो भिन्नताएं उत्पन्न करना चाहते हैं जो इस पैक की कला शैली और निर्यात अनुबंध से मेल खाती हों?

यह पैक [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) के साथ बनाया गया था, जो एक ओपन-सोर्स ComfyUI + SDXL पिक्सेल-आर्ट जनरेशन पाइपलाइन है। Foundry रिपॉजिटरी में वह सब कुछ है जिसकी आपको आवश्यकता है:

- **जनरेशन पाइपलाइन** — `pipeline/foundry_gen.py` प्रति-विषय कॉन्फ़िगरेशन के साथ ComfyUI को चलाता है
- **विषय कॉन्फ़िगरेशन** — `pipeline/chars/hero_*.json` इस पैक में प्रत्येक भिन्नता के लिए सटीक प्रॉम्प्ट, बीज, रूपरेखा नियम और अस्वीकृति शर्तों को परिभाषित करते हैं
- **बैच मैनिफेस्ट** — `pipeline/manifests/fantasy_heroes_03.json` सभी 8 कॉन्फ़िगरेशन को निर्यात संरचना में मैप करता है
- **एक्सपोर्ट CLI** — `foundry export <run_id>` चेकसम के साथ नियतात्मक पैक बनाता है
- **ControlNet ट्यूनिंग** — ह्यूमनॉइड डेप्थ स्ट्रेंथ 0.60, एंड% 0.85 (मैनिफेस्ट में प्रलेखित)

एक नई भिन्नता जोड़ने के लिए:

1. मौजूदा हीरो कॉन्फ़िगरेशन का पालन करते हुए `pipeline/chars/` में एक विषय कॉन्फ़िगरेशन बनाएं
2. रजिस्टर करें: `python -m foundry.cli subject-add <id> --name "नाम"`
3. उत्पन्न करें: `python -m pipeline.foundry_gen --config pipeline/chars/<config>.json`
4. समीक्षा करें, स्वीकार करें, मैप बनाएं, समाप्त करें, निर्यात करें
5. निर्यात किए गए पैक को संबंधित `assets/<slug>/` निर्देशिका में कॉपी करें

[Sprite Foundry README](https://github.com/mcp-tool-shop-org/sprite-foundry#readme) में पूरी पाइपलाइन का विवरण दिया गया है।

## सुरक्षा

इस पैकेज में **केवल स्थिर पीएनजी (PNG) चित्र और जेएसओएन (JSON) मेटाडेटा** शामिल हैं। इसमें कोई निष्पादन योग्य कोड, कोई इंस्टॉलेशन प्रक्रिया, कोई नेटवर्क एक्सेस और कोई टेलीमेट्री नहीं है। डिज़ाइन के अनुसार, सभी फाइलें केवल पढ़ने के लिए हैं।

पूर्ण सुरक्षा नीति के लिए, [SECURITY.md](SECURITY.md) देखें।

## लाइसेंस

एमआईटी (MIT) — वाणिज्यिक और गैर-वाणिज्यिक दोनों परियोजनाओं में उपयोग किया जा सकता है।

## क्रेडिट

[स्प्राइट फाउंड्री](https://github.com/mcp-tool-shop-org/sprite-foundry) का उपयोग करके, कॉमफीयूआई (ComfyUI) + एसडीएक्सएल (SDXL) पिक्सेल-आर्ट पाइपलाइन के साथ बनाया गया।

द्वारा निर्मित: <a href="https://mcp-tool-shop.github.io/">एमसीपी टूल शॉप</a>
