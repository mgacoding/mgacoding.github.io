#!/usr/bin/env bash
# Point the site at a custom domain. Run ONLY after the DNS records below
# are saved at the registrar, otherwise the site goes dark until they are.
#
#   ./set-domain.sh mairagupta.me
set -euo pipefail
DOMAIN="${1:?usage: ./set-domain.sh <domain>}"
cd "$(dirname "$0")"

echo "Checking DNS for $DOMAIN ..."
# Query a public resolver: the local one may hold a cached NXDOMAIN
GOT=$(dig +short @8.8.8.8 "$DOMAIN" A | sort | tr '\n' ' ')
if [ -z "$GOT" ]; then
  echo "  $DOMAIN does not resolve yet. Add the A records first and wait for propagation."
  exit 1
fi
echo "  A records: $GOT"

echo "$DOMAIN" > CNAME
sed -i '' "s|^URL   = .*|URL   = \"https://$DOMAIN\"|" build.py
python3 build.py

git add -A
git commit -q -m "Point site at $DOMAIN"
git push -q origin main
echo "Pushed. Now enable HTTPS: repo Settings > Pages > tick 'Enforce HTTPS'"
echo "(the certificate takes a few minutes to issue)"
