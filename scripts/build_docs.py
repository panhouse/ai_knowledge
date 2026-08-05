#!/usr/bin/env python3
"""GitHub Pages 用のビルド元(.site_src/)と mkdocs.gen.yml を組み立てる。

リポジトリ側の構成(`_index.md` という命名、ページ間の `.md` 相対リンク)を
一切変えずにサイト化するため、ビルド時にコピーしながら次の変換をかける。

- `_index.md` → `index.md` にリネーム(MkDocs にディレクトリの目次として扱わせる)
- 本文中の `..._index.md)` 参照を `...index.md)` に書き換え
- nav は各パートの `_index.md` の「## 収録ページ」の並び順から生成する
  (章見出しがあれば章ごとの入れ子にする。未掲載のページは末尾にまとめる)

使い方:
    python3 scripts/build_docs.py && mkdocs build -f mkdocs.gen.yml
"""
from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / 'topics'
OUT = ROOT / '.site_src'
BASE_CONFIG = ROOT / 'mkdocs.base.yml'
GEN_CONFIG = ROOT / 'mkdocs.gen.yml'

# トップレベルの md をサイトに含める(タイトル, 元ファイル, 出力名)
TOP_PAGES = [
    ('ホーム', 'README.md', 'index.md'),
    ('更新ログ', 'UPDATES.md', 'updates.md'),
    ('執筆・運用ルール', 'CLAUDE.md', 'editorial-policy.md'),
]

warnings: list[str] = []


def read(path: Path) -> str:
    return path.read_text(encoding='utf-8')


def frontmatter_value(text: str, key: str) -> str | None:
    m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not m:
        return None
    m2 = re.search(rf'^{key}:\s*(.+)$', m.group(1), re.M)
    if not m2:
        return None
    return m2.group(1).strip().strip('"\'')


def rewrite_links(text: str, out_name_by_src: dict[str, str]) -> str:
    """`_index.md` 参照を `index.md` に、トップレベル md 参照を出力名に書き換える"""
    text = re.sub(r'(?<=\]\()([^)]*?)_index\.md(?=[)#])', r'\1index.md', text)
    for src, out in out_name_by_src.items():
        if src == out:
            continue
        text = re.sub(rf'(?<=\]\()((?:\.\./)*(?:topics/)?){re.escape(src)}(?=[)#])',
                      lambda m, o=out: m.group(1) + o, text)
    return text


def parse_toc(index_text: str) -> list[tuple[str | None, list[tuple[str, str]]]]:
    """`## 収録ページ` を [(章名 or None, [(タイトル, ファイル名), ...]), ...] に分解する"""
    m = re.search(r'^## 収録ページ\s*$(.*?)(?=^## |\Z)', index_text, re.S | re.M)
    if not m:
        return []
    groups: list[tuple[str | None, list[tuple[str, str]]]] = []
    current: str | None = None
    items: list[tuple[str, str]] = []
    for line in m.group(1).split('\n'):
        if line.startswith('### '):
            if items:
                groups.append((current, items))
                items = []
            current = line[4:].strip()
            continue
        link = re.match(r'-\s*\[(.+?)\]\(([a-z0-9\-]+\.md)\)\s*$', line.strip())
        if link:
            items.append((link.group(1), link.group(2)))
    if items:
        groups.append((current, items))
    return groups


def build() -> int:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()

    out_name_by_src = {src: out for _, src, out in TOP_PAGES}

    nav_lines: list[str] = ['nav:']

    # --- トップレベルのページ ---
    for title, src, out in TOP_PAGES:
        path = ROOT / src
        if not path.exists():
            warnings.append(f'{src} が見つからないためスキップ')
            continue
        (OUT / out).write_text(rewrite_links(read(path), out_name_by_src), encoding='utf-8')
        nav_lines.append(f'  - {title}: {out}')

    # --- パートごと ---
    for part_dir in sorted(SRC.glob('part*')):
        index_src = part_dir / '_index.md'
        if not index_src.exists():
            warnings.append(f'{part_dir.name}: _index.md が無いためスキップ')
            continue

        dst_dir = OUT / 'topics' / part_dir.name
        dst_dir.mkdir(parents=True)

        pages: dict[str, str] = {}  # ファイル名 -> ページタイトル
        for md in sorted(part_dir.glob('*.md')):
            text = read(md)
            out_name = 'index.md' if md.name == '_index.md' else md.name
            (dst_dir / out_name).write_text(rewrite_links(text, out_name_by_src), encoding='utf-8')
            if md.name != '_index.md':
                pages[md.name] = frontmatter_value(text, 'title') or md.stem

        part_title = frontmatter_value(read(index_src), 'title') or part_dir.name
        rel = f'topics/{part_dir.name}'
        nav_lines.append(f'  - {yaml_str(part_title)}:')
        nav_lines.append(f'    - 目次: {rel}/index.md')

        listed: set[str] = set()
        for chapter, items in parse_toc(read(index_src)):
            entries = [(t, f) for t, f in items if f in pages]
            for _, f in entries:
                listed.add(f)
            if not entries:
                continue
            if chapter:
                nav_lines.append(f'    - {yaml_str(chapter)}:')
                indent = '      '
            else:
                indent = '    '
            for title, fname in entries:
                nav_lines.append(f'{indent}- {yaml_str(pages[fname] or title)}: {rel}/{fname}')

        unlisted = sorted(set(pages) - listed)
        if unlisted:
            warnings.append(
                f'{part_dir.name}: _index.md の「収録ページ」に未掲載のページ {len(unlisted)}件 '
                f'({", ".join(unlisted)}) を nav 末尾に追加した'
            )
            nav_lines.append('    - (目次未掲載):')
            for fname in unlisted:
                nav_lines.append(f'      - {yaml_str(pages[fname])}: {rel}/{fname}')

    GEN_CONFIG.write_text(
        f'# 自動生成ファイル。編集しないこと(元: mkdocs.base.yml + scripts/build_docs.py)\n'
        f'{read(BASE_CONFIG).rstrip()}\n\n' + '\n'.join(nav_lines) + '\n',
        encoding='utf-8',
    )

    n_pages = len(list(OUT.rglob('*.md')))
    print(f'.site_src/ に {n_pages}ページを展開 / {GEN_CONFIG.name} を生成')
    for w in warnings:
        print(f'  警告: {w}')
    return 0


def yaml_str(s: str) -> str:
    """nav の値として安全な形にする(コロン等を含むタイトルは引用する)"""
    if re.search(r'[:#\[\]{}&*!|>%@`"\']', s) or s.strip() != s:
        return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
    return s


if __name__ == '__main__':
    sys.exit(build())
