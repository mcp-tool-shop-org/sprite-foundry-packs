<p align="center">
  <a href="README.ja.md">日本語</a> | <a href="README.zh.md">中文</a> | <a href="README.es.md">Español</a> | <a href="README.fr.md">Français</a> | <a href="README.md">English</a> | <a href="README.it.md">Italiano</a> | <a href="README.pt-BR.md">Português (BR)</a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/goblin-sprite-pack/readme.png" width="400" alt="Goblin Warband — Pixel Art Pack" />
</p>

<p align="center">
  <a href="https://github.com/mcp-tool-shop-org/goblin-sprite-pack/actions/workflows/ci.yml"><img src="https://github.com/mcp-tool-shop-org/goblin-sprite-pack/actions/workflows/ci.yml/badge.svg" alt="CI" /></a>
  <a href="https://www.npmjs.com/package/@sprite-foundry/goblin-warband-48"><img src="https://img.shields.io/npm/v/@sprite-foundry/goblin-warband-48" alt="npm" /></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT" /></a>
  <a href="https://mcp-tool-shop-org.github.io/goblin-sprite-pack/"><img src="https://img.shields.io/badge/Landing_Page-live-brightgreen" alt="Landing Page" /></a>
</p>

**8 गोब्लिन प्रकार | 8 दिशाएँ | 3 परतें (एल्बेडो + सामान्य + गहराई) | 48px पिक्सेल आर्ट**

आरपीजी, रणनीति गेम और डंगऑन क्रॉलर्स के लिए दुश्मनों का एक संग्रह। प्रत्येक प्रकार का एक अलग आकार होता है - मुद्रा, सिर का आकार, उपकरण, खतरे का संकेत और शरीर का वजन सभी अलग-अलग होते हैं ताकि खिलाड़ी दुश्मनों को एक नज़र में पहचान सकें।

## प्रकार

| # | प्रकार | भूमिका | आकार |
|---|---------|------|------------|
| 1 | **Grunt** | हाथापाई में इस्तेमाल होने वाला सैनिक | छोटा, झुका हुआ शरीर, साधारण क्लब |
| 2 | **Archer** | दूर से हमला करने वाला सैनिक | पतला, बड़ा धनुष, तीर का थैला |
| 3 | **Shaman** | जादुई शक्ति वाला/चिकित्सक | सींग वाला मुकुट, टोटेम वाला छड़ी, वस्त्र |
| 4 | **Brute** | भारी हाथापाई करने वाला योद्धा | चौड़े कंधे, बड़ा जबड़ा, नुकीला कुल्हाड़ा |
| 5 | **Scout** | तेज गति वाला सैनिक | झुका हुआ, दो छुरी, हुडेड |
| 6 | **Bomber** | क्षेत्रीय प्रभाव (एओई) वाला खतरा | बड़ा थैला, जला हुआ बम, चश्मा |
| 7 | **Warchief** | अभिजात नेता | सींग वाला हेलमेट, झंडे का डंडा, भारी कवच |
| 8 | **Wolf-Rider** | घुड़सवार सैनिक | गोब्लिन जो भेड़िया की सवारी कर रहा है, अद्वितीय शरीर संरचना |

## इंस्टॉल करें

```bash
npm install @sprite-foundry/goblin-warband-48
```

## उपयोग

```js
const pack = require('@sprite-foundry/goblin-warband-48/pack.json');

// Load a specific variant
const grunt = require('@sprite-foundry/goblin-warband-48/assets/grunt/manifest.json');

// Resolve a sprite path
const albedoPath = grunt.layers.albedo.replace('{direction}', 'front');
// → "albedo/front.png"
```

## फ़ोल्डर संरचना

```
assets/
  grunt/           # Melee fodder — baseline goblin
  archer/          # Ranged skirmisher with shortbow
  shaman/          # Caster with horned headdress + staff
  brute/           # Heavy tank with spiked maul
  scout/           # Fast flanker, crouched + hooded
  bomber/          # AoE threat with bomb + satchel
  warchief/        # Elite leader with banner + armor
  wolf-rider/      # Mounted unit — goblin on dire wolf
    albedo/        # Color sprites (8 directions)
    normal/        # Normal maps (8 directions)
    depth/         # Depth maps (8 directions)
    preview/       # Contact sheet
    manifest.json  # Variant metadata
pack.json          # Pack-level index
```

## मैनिफेस्ट प्रारूप

प्रत्येक प्रकार के लिए एक `manifest.json` फ़ाइल होती है:

```json
{
  "slug": "grunt",
  "name": "Grunt",
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

## इंजन अनुकूलता

ये मानक PNG फ़ाइलें हैं जिनमें JSON मेटाडेटा है - कोई रनटाइम निर्भरता नहीं।

| इंजन | एकीकरण |
|--------|------------|
| **Godot 4** | PNG फ़ाइलों को `Texture2D` के रूप में लोड करें, `CanvasTextureMaterial` पर सामान्य मानचित्र का उपयोग करें। |
| **Unity** | स्प्राइट के रूप में आयात करें, स्प्राइट सामग्री को सामान्य मानचित्र असाइन करें। |
| **Phaser** | एसेट लोडर के माध्यम से लोड करें, पथ द्वारा संदर्भ लें। |
| **LÖVE** | प्रत्येक PNG के लिए `love.graphics.newImage()` का उपयोग करें। |
| **Raw Canvas** | निकटतम पड़ोसी स्केलिंग के साथ `drawImage()` का उपयोग करें। |

पिक्सेल आर्ट की स्पष्टता को बनाए रखने के लिए **निकटतम पड़ोसी इंटरपोलेशन** के साथ स्केल करें।

## पैक का विस्तार

यह पैक [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) के साथ बनाया गया था। नए गोब्लिन प्रकार बनाने के लिए:

1. `pipeline/chars/` में एक विषय कॉन्फ़िगरेशन बनाएं, जो फाउंड्री के विषय स्कीमा का पालन करता हो।
2. 5 शरीर आयामों को लॉक करें: **मुद्रा, सिर का आकार, उपकरण का आकार, खतरे का संकेत, शरीर का वजन**।
3. मौजूदा प्रकारों के साथ विलय को रोकने के लिए स्पष्ट `reject_conditions` जोड़ें।
4. चलाएं: `subject-add` → `foundry_gen` → `batch-accept` → `produce` → `export`

पूरी पाइपलाइन दस्तावेज़ों के लिए [Sprite Foundry README](https://github.com/mcp-tool-shop-org/sprite-foundry) देखें।

## सत्यापित करें

```bash
npm run verify
```

यह जांच करता है कि `pack.json` और प्रकार के मैनिफेस्ट में संदर्भित प्रत्येक एसेट डिस्क पर मौजूद है या नहीं।

## सुरक्षा और खतरा मॉडल

इस पैकेज में **केवल स्थिर PNG चित्र और JSON मेटाडेटा** हैं। इसमें:

- कोई निष्पादन योग्य कोड, स्क्रिप्ट या बाइनरी नहीं
- कोई इंस्टॉलेशन हुक या पोस्टइंस्टॉल स्क्रिप्ट नहीं
- कोई नेटवर्क एक्सेस या टेलीमेट्री नहीं
- कोई फ़ाइल सिस्टम लेखन नहीं

पूरे सुरक्षा नीति के लिए [SECURITY.md](./SECURITY.md) देखें।

## लाइसेंस

[MIT](./LICENSE)

---

<a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a> द्वारा बनाया गया।
