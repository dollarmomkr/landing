# -*- coding: utf-8 -*-
import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# We need to remove the remaining old sections.
# They are between <!-- ═══════ SOLUTIONS SECTION ═══════ --> and <!-- ═══════ FOOTER ═══════ -->
content = re.sub(r'<!-- ═══════ SOLUTIONS SECTION ═══════ -->.*?<!-- ═══════ FOOTER ═══════ -->', '    <!-- ═══════ FOOTER ═══════ -->', content, flags=re.DOTALL)

# And remove the first CTA section if it was duplicated or still there. Let's see if the old CTA Section is before the Solutions?
# Looking at the original index, the order was:
# COURSES SECTION
# SOLUTIONS SECTION
# COMPARISON / FEATURES
# CTA SECTION
# FOOTER

# Because I replaced from COURSES to first </section>, COURSES is gone, replaced by Briefing, Product101, CaseStudy, Life, CTA.
# Then SOLUTIONS SECTION, FEATURES, CTA SECTION are still there.
# Let's remove from SOLUTIONS SECTION to FOOTER.
# Wait, I already wrote the script to do this.

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
