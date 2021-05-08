## Natas20

Hint:
The input for name form param can be delimited by new line (Arbitrary SESSION data).

## Natas21

Hint:
The colocated sites can store arbitrary data in their SESSION data.

## Natas22
Hint: 
https://www.gremwell.com/firefox-xss-302
Does firefox/chrome execute/show response body on a 302 respone code? What about burp/curl's default behaviour?

## Natas23
Hint:
https://www.php.net/manual/en/language.types.numeric-strings.php
'==' / + / > / < are loose type operators in php, implicit type conversions take place.

## Natas24
Hint:
strcmp might return NULL on an error
Ans: 
```
$ curl "http://natas24.natas.labs.overthewire.org/index.php" --data-urlencode "passwd[0]={asd}" -H "Authorization: Basic bmF0YXMyNDpPc1JtWEZndW96S3BUWlo1WDE0ek5PNDMzNzlMWnZlZw=="

```

## Natas26
Hint:
Directory traversal still works.

