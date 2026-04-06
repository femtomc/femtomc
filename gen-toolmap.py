#!/usr/bin/env python3
"""Generate a radial tool-ecosystem SVG from the snacks dotfiles.

Nodes with a sponsor URL get a heart (♥) suffix and link to the sponsor page.
Nodes without link to the project repo.
"""

import subprocess, sys, textwrap

# (label, repo_url, sponsor_url_or_None)
TOOLS = {
    "editors": [
        ("Neovim",    "https://github.com/neovim/neovim",           "https://github.com/sponsors/neovim"),
        ("Zed",       "https://github.com/zed-industries/zed",      None),
        ("LazyVim",   "https://github.com/LazyVim/LazyVim",         None),
    ],
    "shell": [
        ("zsh",       "https://www.zsh.org",                         None),
        ("oh-my-zsh", "https://github.com/ohmyzsh/ohmyzsh",         "https://github.com/sponsors/ohmyzsh"),
        ("starship",  "https://github.com/starship/starship",        "https://github.com/sponsors/starship"),
        ("tmux",      "https://github.com/tmux/tmux",                "https://github.com/sponsors/nicm"),
        ("kitty",     "https://github.com/kovidgoyal/kitty",         "https://github.com/sponsors/kovidgoyal"),
    ],
    "cli": [
        ("ripgrep",   "https://github.com/BurntSushi/ripgrep",      "https://github.com/sponsors/BurntSushi"),
        ("fzf",       "https://github.com/junegunn/fzf",            "https://github.com/sponsors/junegunn"),
        ("bat",       "https://github.com/sharkdp/bat",             "https://github.com/sponsors/sharkdp"),
        ("fd",        "https://github.com/sharkdp/fd",              "https://github.com/sponsors/sharkdp"),
        ("eza",       "https://github.com/eza-community/eza",       "https://github.com/sponsors/cafkafk"),
        ("delta",     "https://github.com/dandavison/delta",         "https://github.com/sponsors/dandavison"),
        ("zoxide",    "https://github.com/ajeetdsouza/zoxide",       "https://github.com/sponsors/ajeetdsouza"),
        ("lazygit",   "https://github.com/jesseduffield/lazygit",    "https://github.com/sponsors/jesseduffield"),
    ],
    "dev": [
        ("mise",      "https://github.com/jdx/mise",                "https://github.com/sponsors/jdx"),
        ("uv",        "https://github.com/astral-sh/uv",            None),
        ("ruff",      "https://github.com/astral-sh/ruff",          None),
        ("Rust",      "https://www.rust-lang.org",                   None),
        ("Lean 4",    "https://github.com/leanprover/lean4",         None),
    ],
    "system": [
        ("keyd",      "https://github.com/rvaiya/keyd",             None),
        ("yadm",      "https://github.com/yadm-dev/yadm",           None),
    ],
    "nvim_plugins": [
        ("folke/*",   "https://github.com/folke",                   None),
        ("gitsigns",  "https://github.com/lewis6991/gitsigns.nvim", "https://github.com/sponsors/lewis6991"),
        ("oil.nvim",  "https://github.com/stevearc/oil.nvim",       None),
        ("mini.nvim",  "https://github.com/echasnovski/mini.nvim",  None),
        ("treesitter", "https://github.com/nvim-treesitter/nvim-treesitter", None),
    ],
}

CATEGORY_COLORS = {
    "editors":      "#0d419d",
    "shell":        "#1a7f37",
    "cli":          "#9a6700",
    "dev":          "#6e40c9",
    "system":       "#8b2c2c",
    "nvim_plugins": "#1b6d68",
}

CATEGORY_LABELS = {
    "editors":      "editors",
    "shell":        "shell",
    "cli":          "CLI tools",
    "dev":          "dev infra",
    "system":       "system",
    "nvim_plugins": "nvim plugins",
}

def node_id(label: str) -> str:
    return label.replace(" ", "_").replace(".", "_").replace("/", "_").replace("*", "x").replace("-", "_")

def make_label(name: str, sponsor: str | None) -> str:
    if sponsor:
        return f"{name}  ♥"
    return name

lines = [textwrap.dedent(r"""
digraph toolmap {
    bgcolor="transparent"
    pad=0.5
    ratio=compress
    size="10,10"
    layout=neato
    overlap=scalexy
    splines=curved
    sep="+8"

    node [
        style="filled,rounded"
        shape=box
        fontname="Helvetica,Arial,sans-serif"
        fontsize=10
        fontcolor="#c9d1d9"
        color="#30363d"
        penwidth=0.8
        height=0.32
        margin="0.11,0.055"
    ]
    edge [
        color="#21262d"
        penwidth=0.5
        arrowsize=0.0
    ]

    snacks [
        label=<<B>snacks</B><BR/><FONT POINT-SIZE="8" COLOR="#8b949e">dotfiles</FONT>>
        shape=circle
        width=1.1
        fixedsize=true
        fillcolor="#161b22"
        fontsize=13
        fontcolor="#e6edf3"
        color="#58a6ff"
        penwidth=1.6
        URL="https://github.com/femtomc/snacks"
        target="_blank"
    ]
""")]

# Category hub nodes
for cat, color in CATEGORY_COLORS.items():
    cid = f"cat_{cat}"
    lines.append(f'    {cid} [label=<<FONT POINT-SIZE="9" COLOR="#8b949e">{CATEGORY_LABELS[cat]}</FONT>> shape=plaintext fillcolor="transparent" color="transparent"]')
    lines.append(f'    snacks -> {cid} [penwidth=0.8 color="#30363d"]')

# Tool nodes
for cat, tools in TOOLS.items():
    color = CATEGORY_COLORS[cat]
    cid = f"cat_{cat}"
    for name, repo, sponsor in tools:
        nid = node_id(name)
        url = sponsor if sponsor else repo
        label = make_label(name, sponsor)
        # Heart gets a pink color
        if sponsor:
            html_label = f'<{name}  <FONT COLOR="#db61a2">♥</FONT>>'
            lines.append(f'    {nid} [label={html_label} fillcolor="{color}" URL="{url}" target="_blank" tooltip="Sponsor {name}"]')
        else:
            lines.append(f'    {nid} [label="{label}" fillcolor="{color}" URL="{url}" target="_blank" tooltip="{name}"]')
        lines.append(f'    {cid} -> {nid}')

lines.append("}")

dot_src = "\n".join(lines)

result = subprocess.run(
    ["dot", "-Tsvg"],
    input=dot_src, capture_output=True, text=True,
)
if result.returncode != 0:
    print(result.stderr, file=sys.stderr)
    sys.exit(1)

with open("/tmp/femtomc-profile/toolmap.svg", "w") as f:
    f.write(result.stdout)

print("wrote toolmap.svg")
