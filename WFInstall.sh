#!/usr/bin/env bash

# WiFisploit Installer
# GitHub: https://github.com/CybroZeus
# Telegram: https://t.me/CybroZeus
# Developer: CybroZeus

set -euo pipefail

BOLD=$'\033[1m'
RESET=$'\033[0m'
RED=$'\033[1;31m'
BLUE=$'\033[1;34m'
GREEN=$'\033[1;32m'
YELLOW=$'\033[1;33m'

clear

if [[ $EUID -ne 0 ]]; then
  echo -e "${RED}${BOLD}[-]${RESET} Please run as root."
  exit 1
fi

if grep -qi arch /etc/os-release 2>/dev/null; then
  PM_INSTALL="pacman -S --noconfirm"
  PM_UPDATE="pacman -Sy"
elif grep -qiE 'fedora|rhel|centos' /etc/os-release 2>/dev/null; then
  PM_INSTALL="dnf install -y"
  PM_UPDATE="dnf makecache"
else
  PM_INSTALL="apt-get install -y"
  PM_UPDATE="apt-get update -y"
fi

echo -e "${RED}${BOLD}"
cat << "WFInstall"
 __      _____________ ___                 __          __   __
/  \    /  \_   _____/|   | ____   _______/  |______  |  | |  |
\   \/\/   /|    __)  |   |/    \ /  ___/\   __\__  \ |  | |  |
 \        / |     \   |   |   |  \\___ \  |  |  / __ \|  |_|  |__
  \__/\  /  \___  /   |___|___|  /____  > |__| (____  /____/____/
       \/       \/             \/     \/            \/

                      WiFisploit Installer
WFInstall
echo -e "${RESET}"

echo -e "${BLUE}${BOLD}[*]${RESET} ${RED}${BOLD}WiFisploit${RESET} installer started..."

SCRIPT_PATH="${BASH_SOURCE[0]:-$0}"

[ -f "$SCRIPT_PATH" ] && chmod +x "$SCRIPT_PATH" 2>/dev/null || true

find . -maxdepth 1 -type f -name "*.sh" -exec chmod +x {} \; 2>/dev/null || true

for p in "wsf.py" "./wsf.py" "WiFisploit/wsf/wsf.py" "./WiFisploit/wsf/wsf.py"; do
  [ -f "$p" ] && chmod +x "$p" 2>/dev/null || true
done

echo -e "${BLUE}${BOLD}[*]${RESET} Updating package lists..."

if ! $PM_UPDATE >/dev/null 2>&1; then
  echo -e "${YELLOW}${BOLD}[!]${RESET} update failed — retrying..."
  $PM_UPDATE || { echo -e "${RED}${BOLD}[-]${RESET} update failed."; exit 1; }
fi

echo -e "${BLUE}${BOLD}[*]${RESET} Installing required packages..."

if [[ "$PM_INSTALL" == apt-get* ]]; then
  BASE_PKGS=(python3 python3-venv python3-pip build-essential wget git)
elif [[ "$PM_INSTALL" == pacman* ]]; then
  BASE_PKGS=(python python-virtualenv python-pip base-devel wget git)
else
  BASE_PKGS=(python3 python3-virtualenv python3-pip gcc wget git)
fi

$PM_INSTALL "${BASE_PKGS[@]}" >/dev/null 2>&1 || {
  echo -e "${YELLOW}${BOLD}[!]${RESET} Some packages failed, retrying..."
  $PM_INSTALL "${BASE_PKGS[@]}" || {
    echo -e "${RED}${BOLD}[-]${RESET} Package installation failed."
    exit 1
  }
}

declare -A PKGS
PKGS[metasploit-framework]=msfconsole
PKGS[mingw-w64]=x86_64-w64-mingw32-gcc

check_and_install_pkg() {
  local pkg="$1"
  local cmd="$2"

  if command -v "$cmd" >/dev/null 2>&1; then
    echo -e "${GREEN}${BOLD}[+]${RESET} $pkg already installed."
    return 0
  fi

  echo -e "${YELLOW}${BOLD}[!]${RESET} $pkg not found — installing..."

  if ! $PM_INSTALL "$pkg" >/dev/null 2>&1; then
    echo -e "${YELLOW}${BOLD}[!]${RESET} $pkg installation failed or not available (skipping)."
    return 1
  fi

  if command -v "$cmd" >/dev/null 2>&1; then
    echo -e "${GREEN}${BOLD}[+]${RESET} $pkg installed successfully."
  else
    echo -e "${YELLOW}${BOLD}[!]${RESET} $pkg installed but command missing."
  fi
}

echo -e "${BLUE}${BOLD}[*]${RESET} Checking & installing packages..."

for pkg in "${!PKGS[@]}"; do
  check_and_install_pkg "$pkg" "${PKGS[$pkg]}" || true
done

VENV_DIR="venv"

if [ -d "$VENV_DIR" ]; then
  echo -e "${BLUE}${BOLD}[*]${RESET} Virtualenv exists, reusing..."
else
  echo -e "${BLUE}${BOLD}[*]${RESET} Creating Python virtual environment..."
  python3 -m venv "$VENV_DIR" 2>/dev/null || python -m venv "$VENV_DIR" || {
    echo -e "${RED}${BOLD}[-]${RESET} Failed to create virtualenv."
    exit 1
  }
fi

source "$VENV_DIR/bin/activate"

echo -e "${BLUE}${BOLD}[*]${RESET} Upgrading pip..."

python3 -m pip install --upgrade pip >/dev/null 2>&1 || python -m pip install --upgrade pip

PY_PKGS=(pycryptodome colorama pystyle)

echo -e "${BLUE}${BOLD}[*]${RESET} Installing Python packages..."

python3 -m pip install "${PY_PKGS[@]}" >/dev/null 2>&1 || python -m pip install "${PY_PKGS[@]}"

echo -e "${BLUE}${BOLD}[*]${RESET} Tools status:"

for pkg in "${!PKGS[@]}"; do
  cmd="${PKGS[$pkg]}"
  path=$(command -v "$cmd" 2>/dev/null || true)

  if [[ -n "$path" ]]; then
    echo -e "    ${GREEN}${BOLD}[>]${RESET} $pkg -> $path"
  else
    echo -e "    ${YELLOW}${BOLD}[!]${RESET} $pkg missing."
  fi
done

echo -e "${BLUE}${BOLD}[*]${RESET} Verifying key tools..."

echo -e "${BLUE}${BOLD}[>]${RESET} Python: $(python3 --version 2>/dev/null || python --version)"
echo -e "${BLUE}${BOLD}[>]${RESET} Pip: $(python3 -m pip --version 2>/dev/null || python -m pip --version)"

MINGW_VER=$(x86_64-w64-mingw32-gcc --version 2>/dev/null | head -n1 || echo "mingw-w64 not found.")
echo -e "${GREEN}${BOLD}[+]${RESET} ${MINGW_VER}"

if command -v msfvenom >/dev/null 2>&1; then
  echo -e "${GREEN}${BOLD}[+]${RESET} ${BLUE}Msfvenom${RESET} $(command -v msfvenom)"
else
  echo -e "${YELLOW}${BOLD}[!]${RESET} ${BLUE}Msfvenom${RESET} not found."
fi

echo -e "${GREEN}${BOLD}[+]${RESET} Installation completed."

read -p "$(echo -e "${BLUE}${BOLD}[*]${RESET} Add '${RED}wsf${RESET}' command to system (Y/N) > ")" INSTALL_CMD

if [[ "$INSTALL_CMD" =~ ^[Yy]$ ]]; then

  SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
  TOOL_PATH="$SCRIPT_DIR/wsf.py"
  CMD_PATH="/usr/local/bin/wsf"

  echo -e "${BLUE}${BOLD}[*]${RESET} Creating launcher..."

  cat << EOF > "$CMD_PATH"
#!/usr/bin/env bash
python3 "$TOOL_PATH" "\$@"
EOF

  chmod +x "$CMD_PATH"

  echo -e "${GREEN}${BOLD}[+]${RESET} Command installed to system!"
  echo -e "${BLUE}${BOLD}[*]${RESET} To run > ${RED}${BOLD}wsf${RESET}"

else
  echo -e "${YELLOW}${BOLD}[!]${RESET} Command installation skipped."
fi

echo -e "${GREEN}${BOLD}[+]${RESET} Virtual environment ready."

echo -e "${BLUE}${BOLD}[*]${RESET} To activate the virtual environment run:"
echo -e "    ${YELLOW}${BOLD}source venv/bin/activate${RESET}"

echo -e "${BLUE}${BOLD}[*]${RESET} Then start the tool with:"
echo -e "    ${RED}${BOLD}python3 wsf.py${RESET} ${BLUE}or${RESET} ${RED}${BOLD}wsf${RESET}"

echo -e "${BLUE}${BOLD}[*]${RESET} To deactivate the environment run:"
echo -e "    ${BLUE}${BOLD}deactivate${RESET}"

exit 0
