#!/bin/bash

# WiFisploit Installer

set -euo pipefail

RED="\e[1;31m"
YELLOW="\e[1;33m"
GREEN="\e[1;32m"
CYAN="\e[1;36m"
RESET="\e[0m"

info()   { echo -e "${CYAN}[+]${RESET} $1"; }
warn()   { echo -e "${YELLOW}[!]${RESET} $1"; }
error()  { echo -e "${RED}[-] ERROR:${RESET} $1"; }
success(){ echo -e "${GREEN}[+] $1${RESET}"; }

clear

if [[ $EUID -ne 0 ]]; then
  echo -e "${RED}[-] Please run as root.${RESET}"
  return 1 2>/dev/null || exit 1
fi

echo -e "${RED}"
cat << "WiFisploit"
 __      _____________ ___                 __          __   __
/  \    /  \_   _____/|   | ____   _______/  |______  |  | |  |
\   \/\/   /|    __)  |   |/    \ /  ___/\   __\__  \ |  | |  |
 \        / |     \   |   |   |  \\___ \  |  |  / __ \|  |_|  |__
  \__/\  /  \___  /   |___|___|  /____  > |__| (____  /____/____/
       \/       \/             \/     \/            \/
WiFisploit
echo -e "${RESET}"

info "WiFisploit installer started..."

SCRIPT_PATH="${BASH_SOURCE[0]:-$0}"
if [ -f "$SCRIPT_PATH" ]; then
  chmod +x "$SCRIPT_PATH" 2>/dev/null || true
fi
find . -maxdepth 1 -type f -name "*.sh" -exec chmod +x {} \; 2>/dev/null || true

for p in "wsf.py" "./wsf.py" "WiFisploit/wsf/wsf.py" "./WiFisploit/wsf/wsf.py"; do
  [ -f "$p" ] && chmod +x "$p" 2>/dev/null || true
done

export DEBIAN_FRONTEND=noninteractive

info "Updating package lists..."
if ! apt-get update -y >/dev/null 2>&1; then
  warn "apt-get update failed — you may be offline or apt locked. Trying again without -y output..."
  apt-get update || { error "apt-get update failed."; exit 1; }
fi

info "Installing required packages..."
if ! apt-get install -y python3 python3-venv python3-pip build-essential wget git >/dev/null 2>&1; then
  warn "Some packages failed to install via apt. Attempting verbose install to show errors..."
  apt-get install -y python3 python3-venv python3-pip build-essential wget git || { error "Package installation failed."; exit 1; }
fi

PKGS=(fern-wifi-cracker aircrack-ng airgeddon bettercap wireshark arp-scan tcpdump wifite xterm)

check_and_install_pkg() {
  local pkg="$1"
  if command -v "$pkg" >/dev/null 2>&1; then
    info "$pkg is already installed."
    return 0
  fi

  echo -e "${YELLOW}[-] $pkg not found — installing...${RESET}"
  if ! apt-get install -y "$pkg"; then
    warn "Installation of $pkg failed via apt. You may need to install it manually."
    return 1
  fi

  if command -v "$pkg" >/dev/null 2>&1; then
    success "$pkg installed successfully."
    return 0
  else
    warn "$pkg package installed but '$pkg' command still not found — you may need to check package name or path."
    return 1
  fi
}

info "Checking & installing packages..."
for p in "${PKGS[@]}"; do
  check_and_install_pkg "$p" || true
done

VENV_DIR="venv"
if [ -d "$VENV_DIR" ]; then
  info "Virtual environment '$VENV_DIR' already exists. Reusing it..."
else
  info "Creating Python virtual environment ('$VENV_DIR')..."
  python3 -m venv "$VENV_DIR" || { error "Failed to create virtualenv."; exit 1; }
fi

# shellcheck disable=SC1091
source "$VENV_DIR/bin/activate"

info "Upgrading pip inside virtualenv..."
if ! python3 -m pip install --upgrade pip >/dev/null 2>&1; then
  warn "pip upgrade encountered warnings/errors; trying again with verbose output..."
  python3 -m pip install --upgrade pip || { error "pip upgrade failed."; deactivate 2>/dev/null || true; exit 1; }
fi

PY_PKGS=(py-socket pystyle chardet)
info "Installing Python packages..."
if ! python3 -m pip install "${PY_PKGS[@]}" >/dev/null 2>&1; then
  warn "Some pip installs failed; attempting verbose install..."
  if ! python3 -m pip install "${PY_PKGS[@]}"; then
    error "pip install failed for one or more packages. Please check the output above and install missing packages manually."
    deactivate 2>/dev/null || true
    exit 1
  fi
fi

echo ""
info "Tools status:"
for t in "${PKGS[@]}"; do
  path=$(command -v "$t" 2>/dev/null || true)
  if [[ -n "$path" ]]; then
    echo -e "  ${GREEN}[OK]${RESET} $t -> $path"
  else
    echo -e "  ${YELLOW}[MISSING]${RESET} $t"
  fi
done
echo ""

success "Installation completed."

[ -f "$SCRIPT_PATH" ] && chmod +x "$SCRIPT_PATH" 2>/dev/null || true
find . -maxdepth 1 -type f -name "*.sh" -exec chmod +x {} \; 2>/dev/null || true

info "Activating virtual environment..."
# shellcheck disable=SC1091
source "${VENV_DIR}/bin/activate" || true


if [[ "${BASH_SOURCE[0]}" != "$0" ]]; then
  info "Script was sourced — virtualenv should be active in your current shell."
  return 0 2>/dev/null || true
else
  info "Script executed — virtualenv activated in this process only."
  echo -e "To activate the environment in your shell, run:"
  echo -e "   ${YELLOW}source ${VENV_DIR}/bin/activate${RESET}"
  echo -e "${YELLOW}To deactivate, run:${RESET} ${GREEN}deactivate${RESET}"
  exit 0
fi