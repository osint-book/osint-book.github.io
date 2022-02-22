import json

# Opening JSON file
f = open('saida_teste.txt')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list

for i in data:
    # dns_a
    try:
        var_dns_a = i['dns_a']
    except:
        var_dns_a = "DNS Type A - [Not Found]"

    # dns_mx
    try:
        var_dns_mx = i['dns_mx']
    except:
        var_dns_mx = "DNS Type MX - [Not Found]"

    # dns_ns
    try:
        var_dns_ns = i['dns_ns']
    except:
        var_dns_ns = "DNS Type NS - [Not Found]"

    # dns_ns
    try:
        var_domain = i['domain']
    except:
        var_domain = "Domain - [Not Found]"

    # fuzzer
    try:
        var_fuzzer = i['fuzzer']
    except:
        var_fuzzer = "Fuzzer - [Not Found]"

    print(var_dns_a, "|",var_dns_mx, "|",var_dns_ns, "|", var_domain, "|", var_fuzzer)

# Closing file
f.close()
