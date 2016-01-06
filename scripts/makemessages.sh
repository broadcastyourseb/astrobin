#!/bin/bash
apps="astrobin rawdata nested_comments astrobin_apps_users astrobin_apps_images astrobin_apps_platesolving astrobin_apps_donations astrobin_apps_premium"
langs="ar be ca cs de el en es fa fi fr hu it ja nl pl pt-BR pt ro ru sk sq sr tr zh-CN zh-TW"

echo "Processing apps..."
for app in $apps; do
    echo -n " * $app:"
    for lang in $langs; do
        echo -n " $lang"
        (cd $app; ../manage.py makemessages -l $lang -e html,txt,py -i *zinnia* >/dev/null 2>&1)
    done
    echo
done

