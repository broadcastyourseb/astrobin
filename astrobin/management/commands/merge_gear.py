from django.core.management.base import BaseCommand
from django.db.models import Q

from astrobin.models import Gear

class Command(BaseCommand):
    help = "Merges gear items with the same make/name."

    def handle(self, *args, **options):
        def unique_items(l):
            found = []
            for i in l:
                if i not in found:
                    found.append(i)
            return found

        queryset = Gear.objects.all().order_by('id')
        current = 0
        count = queryset.count()
        total_merges = 0
        seen = []

        for item in queryset:
            if item in seen:
                continue

            seen.append(item)

            twins = Gear.objects\
                .filter(Q(make = item.make) & Q(name = item.name))\
                .exclude(id = item.id)

            if twins:
                print "Examining item %d/%d: [%d] %s" % (current, count, item.id, item),
                print "... found %d twins." % twins.count()

            for twin in twins:
                if twin in seen:
                    continue

                print "\tMerging [%d]..." % twin.id
                item.hard_merge(twin)
                total_merges += 1
                if twin not in seen:
                    seen.append(twin)

            current += 1

        print "Performed %d merges." % total_merges
