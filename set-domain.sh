#!/usr/bin/env bash
# Point the site at a custom domain. Run ONLY after the DNS records below
# are saved at the registrar, otherwise the site goes dark until they are.
#
#   ./set-domain.sh mairagupta.me
set -euo pipefail
DOMAIN="${1:?usage: ./set-domain.sh <domain>}"
cd "$(dirname "$0")"

echo "Checking DNS for $DOMAIN ..."
if ! host "$DOMAIN" >/dev/null 2>&1; then
  echo "  $DOMAIN does not resolve yet. Add the A records first and wait for propagation."
  exit 1
fi
host "$DOMAIN" | sed 's/^/  /'

echo "$DOMAIN" > CNAME
sed -i '' "s|^URL   = .*|URL   = \"https://$DOMAIN\"|" build.py
python3 build.py

git add -A
git commit -q -m "Point site at $DOMAIN"
git push -q origin main
echo "Pushed. Now enable HTTPS: repo Settings > Pages > tick 'Enforce HTTPS'"
echo "(the certificate takes a few minutes to issue)"
