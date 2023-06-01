# redos-scanner
extremely simple scanner for ReDoS vulnerability

## How It works?
1. Parse python code with `ast` module
2. Extract the regex string where the `compile()`, `match()`, `search()`, and `fullmatch()` methods of the `re` module are used
3. Fuzz extracted regex string with atheris
4. Detect ReDoS vulnerability

## Example

```python
import re
import time


for n in range(100):
    start_time = time.time()
    re.match("(bb|b.)*a", "b" * n)
    print(n, time.time() - start_time)
```

```
$ python3 scan.py
INFO: Using built-in libfuzzer
WARNING: Failed to find function "__sanitizer_acquire_crash_state". Reason dlsym(RTLD_DEFAULT, __sanitizer_acquire_crash_state): symbol not found.
WARNING: Failed to find function "__sanitizer_print_stack_trace". Reason dlsym(RTLD_DEFAULT, __sanitizer_print_stack_trace): symbol not found.
WARNING: Failed to find function "__sanitizer_set_death_callback". Reason dlsym(RTLD_DEFAULT, __sanitizer_set_death_callback): symbol not found.
INFO: Running with entropic power schedule (0xFF, 100).
INFO: Seed: 2780101204
INFO: -max_len is not provided; libFuzzer will not generate inputs larger than 4096 bytes
INFO: A corpus is not provided, starting from an empty corpus
#2	INITED cov: 4 ft: 4 corp: 1/1b exec/s: 0 rss: 38Mb
Suspicious pattern: (bb|b.)*a
#59057	NEW    cov: 5 ft: 5 corp: 2/50b lim: 589 exec/s: 59057 rss: 39Mb L: 49/49 MS: 5 CopyPart-ChangeBit-ChangeByte-ChangeBit-InsertRepeatedBytes-
Suspicious pattern: (bb|b.)*a
```