#!/bin/bash
# deploy.sh — Deploy cv-site to VPS (anvart.ru)
# Usage: bash deploy.sh
#
# Copies deployable files to /home/anvar/5D/cv-site/,
# then syncs to VPS via deploy-vps.sh and rebuilds the container.

set -e

SCRIPT_DIR="$(dirname "$0")"
TARGET_DIR="/home/anvar/5D/cv-site"

# Deployable files (same as what goes into Docker image)
FILES=(
    index.html
    robots.txt
    sitemap.xml
    photo.png
    photo.webp
    og-image.png
    cv-tukhvatullin.pdf
    favicon.png
    favicon-120.png
    favicon.svg
    apple-touch-icon.png
)

DIRS=(
    fonts
)

echo "=== Обновление файлов в $TARGET_DIR ==="

# Copy individual files
for f in "${FILES[@]}"; do
    if [ -f "$SCRIPT_DIR/$f" ]; then
        cp "$SCRIPT_DIR/$f" "$TARGET_DIR/$f"
        echo "  $f"
    else
        echo "  SKIP: $f (not found)"
    fi
done

# Copy directories
for d in "${DIRS[@]}"; do
    if [ -d "$SCRIPT_DIR/$d" ]; then
        cp -r "$SCRIPT_DIR/$d" "$TARGET_DIR/"
        echo "  $d/"
    fi
done

echo ""
echo "=== Файлы скопированы в $TARGET_DIR ==="
echo ""
echo "Следующие шаги:"
echo "  1. cd /home/anvar/5D && bash deploy-vps.sh sync"
echo "  2. SSH на VPS: docker compose -f docker-compose.prod.yml build cv-site"
echo "  3. SSH на VPS: docker compose -f docker-compose.prod.yml up -d --force-recreate caddy cv-site"
echo ""
echo "Или для полного обновления:"
echo "  SSH на VPS: bash deploy-vps.sh update"
