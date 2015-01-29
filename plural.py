import re

##def plural(noun):
##    if re.search(r"[sxz]$", noun):
##        return re.sub('$', "es", noun)
##    elif re.search(r"[^aeioudgkprt]h$", noun):
##        return re.sub('$', "es", noun)
##    elif re.search(r"[^aeiou]y$", noun):
##        return re.sub('y$', "ies", noun)
##    else:
##        return noun + 's'


##def match_sxz(noun):
##    return re.search(r"[sxz]$", noun)
##
##def apply_sxz(noun):
##    return re.sub('$', "es", noun)
##
##def match_h(noun):
##    return re.search(r"[^aeioudgkprt]h$", noun)
##
##def apply_h(noun):
##    return re.sub('$', "es", noun)
##
##def match_y(noun):
##    return re.search(r"[^aeiou]y$", noun)
##
##def apply_y(noun):
##    return re.sub("y$", "ies", noun)
##
##def match_default(noun):
##    return True
##
##def apply_default(noun):
##    return noun + 's'
##
##rules = ((match_sxz, apply_sxz),
##         (match_h, apply_h),
##         (match_y, apply_y),
##         (match_default, apply_default)
##         )


def plural(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)

def build_match_and_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.search(search, replace, word)
    return (matches_rule, apply_rule)

##patterns = \
##    (
##        (r"[sxz]$",            '$',    "es"),
##        (r"[^aeioudgkprt]h$",  '$',    "es"),
##        (r"(qu|[^aeiou])y$",   "y$",   "ies"),
##        ('$',                  '$',    's')
##    )
##
##rules = [build_match_and_apply_functions(pattern, search, repace)
##         for (pattern, search, replace) in patterns]

rules = []
with open("plural4-rules.txt", encording="utf-8") as pattern_file:
    for line in pattern_file:
        pattern, search, replace = line.split(None, 3)
        rules.append(build_match_and_functions(
            pattern, search, replace))
