# redos-scanner
extremely simple scanner for ReDoS vulnerability

## How It works?
1. Parse python code with `ast` module
2. Extract the regex string where the `compile()`, `match()`, `search()`, and `fullmatch()` methods of the `re` module are used
3. Fuzz extracted regex string with atheris
4. Detect ReDoS vulnerability