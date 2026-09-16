"""Subset the locally installed open font to the site's current text."""
from pathlib import Path
from fontTools import subset
from fontTools.ttLib import TTFont

root = Path(__file__).resolve().parents[1]
text = ''.join(chr(i) for i in range(32, 127))
for path in (root / 'src').rglob('*'):
    if path.suffix in {'.astro', '.ts', '.css'}:
        text += path.read_text(encoding='utf-8')
font = TTFont('C:/Windows/Fonts/NotoSansSC-VF.ttf')
options = subset.Options()
options.flavor = 'woff2'
subsetter = subset.Subsetter(options=options)
subsetter.populate(text=text)
subsetter.subset(font)
font.flavor = 'woff2'
font.save(root / 'public/assets/fonts/PortfolioSans.woff2')
