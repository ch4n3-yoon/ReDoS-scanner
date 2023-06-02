import re
import time

# Django CVE-2023-23969 ReDoS vulnerability
re.compile(r"([A-Za-z]{1,8}(?:-[A-Za-z0-9]{1,8})*|\*)(?:\s*;\s*q=(0(?:\.[0-9]{,3})?|1(?:\.0{,3})?))?(?:\s*,\s*|$)")

# https://regexlib.com/REDetails.aspx?regexp_id=1757&AspxAutoDetectCookieSupport=1
re.compile(r"^([a-zA-Z0-9])(([\-.]|[_]+)?([a-zA-Z0-9]+))*(@){1}[a-z0-9]+[.]{1}(([a-z]{2,3})|([a-z]{2,3}[.]{1}[a-z]{2,3}))$")
for n in range(100):
    start_time = time.time()
    re.match("(bb|b.)*a", "b" * n)
    print(n, time.time() - start_time)