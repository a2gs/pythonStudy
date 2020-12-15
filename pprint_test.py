import pprint

stuff = {1:'abc', 2:'def', 3:['ghi', 'xyz'], 4:'jlm', 5:'nop', 6:["a","b","c","d", {"asd":"123", "cvb":345, "ert":[1,2,3,4,5], "rty":"abcdef"}], 7: "rst", 8:{1:1, 2:2, 3:3, 4:4}}

pp = pprint.PrettyPrinter(indent = 2, compact = False, depth = None)

pp.pprint(stuff)